
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
def check_stream(url: str, channel_name: str, headers: Optional[dict] = None, invalid_hosts=None, invalid_urls=None,  ffmpeg_timeout: int = FFMPEG_TIMEOUT) -> Tuple[bool, Optional[str], Optional[float]]:
    """Validate stream against URL using ffmpeg and HTTP request. Returns a tuple (success, error) for logging."""
    start_time = time.time()
    if invalid_urls is None:
        invalid_urls = set()
    if invalid_hosts is None:
        invalid_hosts = set()
    if url in cache:
        return cache[url]
    if config.config.notCheck == 1:
        return True, None, 999999
    if is_ipv6(url):
        return True, None, 999999

    for attempt in range(RETRY_COUNT + 1):
        try:
            logging.debug(f"Checking stream: {channel_name} ({url}) with headers: {headers}) - Attempt {attempt + 1}")

            if url.startswith('http://') or url.startswith('https://'):
                response = requests.head(url, headers=headers, timeout=15, verify=False)
                end_time = time.time()
                if response.status_code == 200:
                    cache[url] = (True, None, 99999)
                    return True, None, end_time - start_time
                if response.status_code != 200:
                    hostname = urlsplit(url).hostname
                    if hostname not in invalid_hosts:
                        invalid_hosts.add(hostname)
                    invalid_urls.add(url)

                    logging.error(f"Invalid status code {channel_name} {url} code {response.status_code}")
                    # 404 说明内容确实不可达
                    if response.status_code == 404:
                        cache[url] = (False, None, 99999)
                        return False, None, end_time - start_time
                    # 400 403 有可能是要切换一下其他地址再回来才能看
                    if response.status_code == 403 or response.status_code == 400:
                        cache[url] = (True, None, 99999)
                        return True, None, end_time - start_time
                    cache[url] = (False, f"Invalid status code: {response.status_code}")
                    return True, f"Invalid status code: {response.status_code}", end_time - start_time

            end_time = time.time()
            ffmpeg_command = ['ffmpeg', '-i', url, '-t', '5', '-f', 'null', '-']
            result = subprocess.run(ffmpeg_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=ffmpeg_timeout)
            if result.returncode == 0:
                cache[url] = (True, None, 99999)
                return True, None, end_time - start_time
            else:
                cache[url] = (False, "Stream does not work", 99999)
                return True, "Stream does not work", 99999

        except subprocess.TimeoutExpired:
            logging.error(f"ffmpeg timeout for {channel_name}{url}(attempt {attempt + 1})")
            if attempt == RETRY_COUNT:
                cache[url] = (True, "ffmpeg timeout", 99999)
                hostname = urlsplit(url).hostname
                if hostname not in invalid_hosts:
                    invalid_hosts.add(hostname)
                invalid_urls.add(url)
                return True, "ffmpeg timeout", 99999

        except requests.exceptions.RequestException as e:
            logging.error(f"Request error for {channel_name} {url} (attempt {attempt + 1})")
            simplified_error = simplify_error(str(e))
            if attempt == RETRY_COUNT:
                cache[url] = (True, simplified_error, 99999)
                hostname = urlsplit(url).hostname
                if hostname not in invalid_hosts:
                    invalid_hosts.add(hostname)
                invalid_urls.add(url)
                return True, simplified_error, 99999

        except Exception as e:
            logging.error(f"General error for {channel_name}: {e}", exc_info=True)
            if attempt == RETRY_COUNT:
                cache[url] = (True, "General error", 99999)
                hostname = urlsplit(url).hostname
                if hostname not in invalid_hosts:
                    invalid_hosts.add(hostname)
                invalid_urls.add(url)
                return True, "General error", 99999

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
    stream = check_stream('http://112.234.23.81:9901/tsfile/live/0013_1.m3u8', 'channel_name', {}, set(), set(), 25)
    print(stream)
