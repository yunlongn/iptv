
from typing import Optional, Tuple
import subprocess
from urllib.parse import urlsplit

import requests
import logging
import time

import config.config
from main import is_ipv6

cache = {}

# Configuration settings
RETRY_COUNT = 0
FFMPEG_TIMEOUT = 25
def check_stream(url: str, channel_name: str, headers: Optional[dict] = None, invalid_urls=None, ffmpeg_timeout: int = FFMPEG_TIMEOUT) -> Tuple[bool, Optional[str], Optional[float]]:
    """Validate stream against URL using ffmpeg and HTTP request. Returns a tuple (success, error) for logging."""
    start_time = time.time()
    if invalid_urls is None:
        invalid_urls = set()
    if url in cache:
        return cache[url]
    if config.config.notCheck == 1:
        cache[url] = (True, None)
        return True, None, 999999
    if is_ipv6(url):
        cache[url] = (True, None)
        return True, None, 999999

    for attempt in range(RETRY_COUNT + 1):
        try:
            logging.debug(f"Checking stream: {channel_name} ({url}) with headers: {headers}) - Attempt {attempt + 1}")

            if url.startswith('http://') or url.startswith('https://'):
                response = requests.head(url, headers=headers, timeout=15, verify=False)
                end_time = time.time()
                if response.status_code == 200:
                    cache[url] = (True, None)
                    return True, None, end_time - start_time
                if response.status_code == 403 or response.status_code == 400:
                    cache[url] = (True, None)
                    return True, None, end_time - start_time
                if response.status_code != 200:
                    cache[url] = (False, f"Invalid status code: {response.status_code}")
                    invalid_urls.add(urlsplit(url).hostname)
                    return False, f"Invalid status code: {response.status_code}", 99999

            end_time = time.time()
            ffmpeg_command = ['ffmpeg', '-i', url, '-t', '5', '-f', 'null', '-']
            result = subprocess.run(ffmpeg_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=ffmpeg_timeout)
            if result.returncode == 0:
                cache[url] = (True, None)
                return True, None, end_time - start_time
            else:
                cache[url] = (False, "Stream does not work")
                return False, "Stream does not work", 99999

        except subprocess.TimeoutExpired:
            logging.error(f"ffmpeg timeout for {channel_name} {url} (attempt {attempt + 1})")
            if attempt == RETRY_COUNT:
                cache[url] = (False, "ffmpeg timeout")
                invalid_urls.add(urlsplit(url).hostname)
                return False, "ffmpeg timeout", 99999

        except requests.exceptions.RequestException as e:
            logging.error(f"Request error for {channel_name}  {url}  (attempt {attempt + 1})")
            simplified_error = simplify_error(str(e))
            if attempt == RETRY_COUNT:
                cache[url] = (False, simplified_error)
                invalid_urls.add(urlsplit(url).hostname)
                return False, simplified_error, 99999

        except Exception as e:
            logging.error(f"General error for {channel_name}: {e}", exc_info=True)
            if attempt == RETRY_COUNT:
                cache[url] = (False, "General error")
                invalid_urls.add(urlsplit(url).hostname)
                return False, "General error", 99999

def simplify_error(error_message: str) -> str:
    error_map = {
        "No connection adapters": "No connection!",
        "Timeout": "Request timeout",
        "403 Forbidden": "Access forbidden (403)"
    }
    for error, message in error_map.items():
        if error in error_message:
            return message
    return "Request error"


if __name__ == "__main__":
    stream = check_stream('http://112.234.23.81:9901/tsfile/live/0013_1.m3u8', 'channel_name', {}, set(), 25)
    print(stream)
