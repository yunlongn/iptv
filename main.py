import re

import requests
import logging
import concurrent.futures
from collections import OrderedDict
from datetime import datetime
import tqdm

import ffmpeg_util
from config import config

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', handlers=[logging.FileHandler("logs/fetch.log", "w", encoding="utf-8"), logging.StreamHandler()])

def parse_template(template_file):
    template_channels = OrderedDict()
    current_category = None

    with open(template_file, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#"):
                if "#genre#" in line:
                    current_category = line.split(",")[0].strip()
                    template_channels[current_category] = []
                elif current_category:
                    channel_name = line.split(",")[0].strip()
                    template_channels[current_category].append(channel_name)

    return template_channels

def fetch_channels(url, invalid_url):
    channels = OrderedDict()

    try:
        response = requests.get(url)
        response.raise_for_status()
        response.encoding = 'utf-8'
        lines = response.text.split("\n")
        current_category = None
        channel_name = None
        is_m3u = any("#EXTINF" in line for line in lines[:15])
        source_type = "m3u" if is_m3u else "txt"
        logging.info(f"url: {url} 获取成功，判断为{source_type}格式")

        if is_m3u:
            for line in lines:
                try:
                    line = line.strip()
                    if line.startswith("#EXTINF"):
                        match = re.search(r'group-title="(.*?)"', line)
                        match2 = re.search(r',(.*)', line)
                        if match:
                            current_category = match.group(1).strip()
                            channel_name = match2.group(1).strip()
                            if current_category not in channels:
                                channels[current_category] = []
                    elif line and not line.startswith("#"):
                        channel_url = line.strip()
                        if current_category and channel_name:
                            channels[current_category].append((channel_name, channel_url))
                except Exception as e:
                    logging.error(f"fetch_channels m3u error line {url} {line}", e)
        else:
            for line in lines:
                try:
                    line = line.strip()
                    if "#genre#" in line:
                        current_category = line.split(",")[0].strip()
                        channels[current_category] = []
                    elif current_category:
                        match = re.match(r"^(.*?),(.*?)$", line)
                        if match:
                            channel_name = match.group(1).strip()
                            channel_url = match.group(2).strip()
                            channels[current_category].append((channel_name, channel_url))
                        elif line:
                            channels[current_category].append((line, ''))
                except Exception as e:
                    logging.error(f"fetch_channels txt error line {url} {line}", e)

        if channels:
            categories = ", ".join(channels.keys())
            logging.info(f"url: {url} 读取成功✅，包含频道分类: {categories}")
    except requests.RequestException as e:
        logging.error(f"url: {url} 读取失败❌, Error: {e}")
        invalid_url.write(f"{url}\n")


    return channels

def match_channels(template_channels, all_channels, rename_dic):
    matched_channels = OrderedDict()
    for category, channel_list in template_channels.items():
        matched_channels[category] = OrderedDict()
        for channel_name in channel_list:
            for online_category, online_channel_list in all_channels.items():
                for online_channel_name, online_channel_url in online_channel_list:
                    # 纠错频道名称
                    if online_channel_name in rename_dic and online_channel_name != rename_dic[online_channel_name]:
                        online_channel_name = rename_dic[online_channel_name]
                    if channel_name == online_channel_name:
                        matched_channels[category].setdefault(channel_name, []).append(online_channel_url)

    return matched_channels

def load_modify_name(filename):
    corrections = {}
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            parts = line.strip().split(',')
            correct_name = parts[0]
            for name in parts[1:]:
                corrections[name] = correct_name
    return corrections

def filter_source_urls(template_file):
    #读取修改字典文件
    rename_dic: dict[str, str] = load_modify_name('config/rename.txt')
    template_channels = parse_template(template_file)
    source_urls = config.source_urls
    future_to_url = {}
    pbar = tqdm.tqdm(total=len(source_urls), desc="Checking channels", ncols=100, colour="green")

    with open("config/invalid_url.txt", "w", encoding="utf-8") as invalid_url:
        with concurrent.futures.ThreadPoolExecutor(max_workers = config.threadNum) as executor:
            all_channels = OrderedDict()
            for url in source_urls:
                future = executor.submit(fetch_channels, url, invalid_url)
                future_to_url[future] = url
            try:
                for future in concurrent.futures.as_completed(future_to_url, timeout = config.futureTimout):
                    url = future_to_url[future]
                    try:
                        for category, channel_list in future.result(config.futureTimout).items():
                            if category in all_channels:
                                all_channels[category].extend(channel_list)
                            else:
                                all_channels[category] = channel_list
                    except concurrent.futures.TimeoutError:
                        logging.info(f"url: {url} Processing took too long")
                    pbar.update(1)
                    logging.info(pbar.__str__())
            except concurrent.futures.TimeoutError:
                logging.info(f"url: {url} Processing took too long")

            finally:
                pbar.close()
                logging.info(pbar.__str__())

    matched_channels = match_channels(template_channels, all_channels, rename_dic)

    return matched_channels, template_channels

def is_ipv6(url):
    return re.match(r'^http:\/\/\[[0-9a-fA-F:]+\]', url) is not None

def update_channel_urls_m3u(channels, template_channels):
    written_urls = set()

    current_date = datetime.now().strftime("%Y-%m-%d")
    for group in config.announcements:
        for announcement in group['entries']:
            if announcement['name'] is None:
                announcement['name'] = current_date

    with open("live.m3u", "w", encoding="utf-8") as f_m3u:
        f_m3u.write(f"""#EXTM3U x-tvg-url={",".join(f'"{epg_url}"' for epg_url in config.epg_urls)}\n""")

        with open("live.txt", "w", encoding="utf-8") as f_txt:
            add_author_info(f_m3u, f_txt)

            with concurrent.futures.ThreadPoolExecutor(max_workers=config.ffmpegCheckThreadNum) as executor:
                for category, channel_list in template_channels.items():
                    f_txt.write(f"{category},#genre#\n")
                    # 分类不数据要保存的分类列表则跳过
                    if category not in channels:
                        continue
                    for channel_name in channel_list:
                        # 渠道不数据要操作的渠道列表则跳过
                        if channel_name not in channels[category]:
                            continue
                        # 讲指定的数据排序到最前面 由于 ip_version_priority决定
                        sorted_urls = sorted(channels[category][channel_name], key=lambda url: not is_ipv6(url) if config.ip_version_priority == "ipv6" else is_ipv6(url))
                        filtered_urls = []
                        future_concurrents = {}
                        for url in sorted_urls:
                            if url and url not in written_urls and not any(blacklist in url for blacklist in config.url_blacklist):
                                filtered_urls.append(url)
                                written_urls.add(url)
                        total_urls = len(filtered_urls)
                        if total_urls >= 1:
                            f_m3u.write(f"#EXTINF:-1 tvg-name=\"{channel_name}\" tvg-logo=\"https://live.fanmingming.com/tv/{channel_name}.png\" group-title=\"{category}\",{channel_name}\n")

                        for index, url in enumerate(filtered_urls, start=1):
                            future = executor.submit(ffmpeg_util.check_stream, url, channel_name, {}, 25)
                            future_concurrents[future] = (index, url)

                        try:
                            for future in concurrent.futures.as_completed(future_concurrents,
                                                                          timeout=config.ffmpegCheckThreadTimeout):
                                (index, url) = future_concurrents[future]
                                try:
                                    success, error = future.result(config.ffmpegCheckThreadTimeout)
                                    if success:
                                        if is_ipv6(url):
                                            url_suffix = f"$LR•IPV6" if total_urls == 1 else f"$LR•IPV6『线路{index}』"
                                        else:
                                            url_suffix = f"$LR•IPV4" if total_urls == 1 else f"$LR•IPV4『线路{index}』"
                                        if '$' in url:
                                            base_url = url.split('$', 1)[0]
                                        else:
                                            base_url = url

                                        new_url = f"{base_url}{url_suffix}"
                                        if is_ipv6(url):
                                            f_txt.write(f"{channel_name}(IPV6),{new_url}\n")
                                        else:
                                            f_txt.write(f"{channel_name},{new_url}\n")

                                        f_m3u.write(new_url + "\n")
                                    else:
                                        logging.error(f"Failed to play {url} {error}")

                                except concurrent.futures.TimeoutError:
                                    logging.info(f"url: {url} Processing took too long")
                        except concurrent.futures.TimeoutError:
                            logging.info(f"url: {url} Processing took too long")


                        # for index, url in enumerate(filtered_urls, start=1):
                        #     if is_ipv6(url):
                        #         url_suffix = f"$LR•IPV6" if total_urls == 1 else f"$LR•IPV6『线路{index}』"
                        #     else:
                        #         url_suffix = f"$LR•IPV4" if total_urls == 1 else f"$LR•IPV4『线路{index}』"
                        #     if '$' in url:
                        #         base_url = url.split('$', 1)[0]
                        #     else:
                        #         base_url = url
                        #
                        #     new_url = f"{base_url}{url_suffix}"
                        #     if is_ipv6(url):
                        #         f_txt.write(f"{channel_name}(IPV6),{new_url}\n")
                        #     else:
                        #         f_txt.write(f"{channel_name},{new_url}\n")
                        #
                        #     f_m3u.write(new_url + "\n")


            f_txt.write("\n")


def add_author_info(f_m3u, f_txt):
    for group in config.announcements:
        f_txt.write(f"{group['channel']},#genre#\n")
        for announcement in group['entries']:
            f_m3u.write(
                f"""#EXTINF:-1 tvg-id="1" tvg-name="{announcement['name']}" tvg-logo="{announcement['logo']}" group-title="{group['channel']}",{announcement['name']}\n""")
            f_m3u.write(f"{announcement['url']}\n")
            f_txt.write(f"{announcement['name']},{announcement['url']}\n")


if __name__ == "__main__":
    template_file = "config/tag.txt"
    channels, template_channels = filter_source_urls(template_file)
    update_channel_urls_m3u(channels, template_channels)