
from typing import Optional, Tuple
import subprocess

import requests
import logging
cache = {}

# Configuration settings
RETRY_COUNT = 1
FFMPEG_TIMEOUT = 25
NUM_THREADS = 4  # Change to the required number of threads
def check_stream(url: str, channel_name: str, headers: Optional[dict] = None, ffmpeg_timeout: int = FFMPEG_TIMEOUT) -> Tuple[bool, Optional[str]]:
    """Validate stream against URL using ffmpeg and HTTP request. Returns a tuple (success, error) for logging."""
    if url in cache:
        return cache[url]

    for attempt in range(RETRY_COUNT + 1):
        try:
            logging.debug(f"Checking stream: {channel_name} ({url}) with headers: {headers}) - Attempt {attempt + 1}")

            if url.startswith('http://') or url.startswith('https://'):
                response = requests.head(url, headers=headers, timeout=15, verify=False)
                if response.status_code != 200:
                    cache[url] = (False, f"Invalid status code: {response.status_code}")
                    return False, f"Invalid status code: {response.status_code}"

            ffmpeg_command = ['ffmpeg', '-i', url, '-t', '5', '-f', 'null', '-']
            result = subprocess.run(ffmpeg_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=ffmpeg_timeout)
            if result.returncode == 0:
                cache[url] = (True, None)
                return True, None
            else:
                cache[url] = (False, "Stream does not work")
                return False, "Stream does not work"

        except subprocess.TimeoutExpired:
            logging.error(f"ffmpeg timeout for {channel_name} (attempt {attempt + 1})")
            if attempt == RETRY_COUNT:
                cache[url] = (False, "ffmpeg timeout")
                return False, "ffmpeg timeout"

        except requests.exceptions.RequestException as e:
            logging.error(f"Request error for {channel_name} (attempt {attempt + 1}): {e}", exc_info=True)
            simplified_error = simplify_error(str(e))
            if attempt == RETRY_COUNT:
                cache[url] = (False, simplified_error)
                return False, simplified_error

        except Exception as e:
            logging.error(f"General error for {channel_name}: {e}", exc_info=True)
            if attempt == RETRY_COUNT:
                cache[url] = (False, "General error")
                return False, "General error"

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
    stream = check_stream('http://112.234.23.81:9901/tsfile/live/0013_1.m3u8', 'channel_name', {}, 25)
    print(stream)
