import concurrent.futures
import subprocess

import requests
import logging
import warnings

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(threadName)s - %(message)s', handlers=[logging.FileHandler("invalid_urls.log", "w", encoding="utf-8"), logging.StreamHandler()])

if __name__ == "__main__":
    with open("invalid_urls", 'r', encoding='utf-8') as f:
        future_to_url = {}
        warnings.filterwarnings('ignore')
        with concurrent.futures.ThreadPoolExecutor(max_workers = 512) as executor:
            for url in f:
                    try:
                        if url.startswith('http://') or url.startswith('https://'):
                            future = executor.submit(requests.get, url, headers={}, timeout=15, verify=False)
                            future_to_url[future] = url
                    except subprocess.TimeoutExpired as e:
                        logging.error(f"check invalid_urls {url} code {e}")

                    except requests.exceptions.RequestException as e:
                        logging.error(f"check invalid_urls {url} code {e}")

                    except Exception as e:
                        logging.error(f"check invalid_urls {url} code {e}")

            try:
                for future in concurrent.futures.as_completed(future_to_url):
                    try:
                        url = future_to_url[future]
                        response = future.result(600)
                        if response.status_code != 200 and response.status_code != 403:
                            logging.error(f"Invalid status code {url} code {response.status_code}")

                    except Exception as e:
                        logging.info(f"url: {url} Processing took too long")
            except Exception as e:
                logging.info(f"url: {url} Processing took too long {e}")
