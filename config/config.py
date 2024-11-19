ip_version_priority = "ipv4" #ipv6
threadNum = 10 # 请求线程数
ffmpegCheckThreadNum = 32 # 请求线程数
futureTimout = 300 # 请求线程等待时间

source_urls = [
    "https://aktv.top/live.m3u",
    # --https://raw.githubusercontent.com/zzj2678/IPTVzb1/refs/heads/main/iptv_list.txt
    # --https://4gtv.mytvsuper.xyz/myiptv.m3u
    # --https://gongdian.top/tv/gongdian.txt
    # --http://wp.wadg.pro/down.php/d7b52d125998d00e2d2339bac6abd2b5.txt
    # --https://raw.githubusercontent.com/zzmaze/iptv/main/iptv.txt
    # --https://tvkj.top/tvlive.txt
    # --https://raw.githubusercontent.com/YueChan/Live/main/IPTV.m3u
    # --https://gitcode.net/MZ011/BHJK/-/raw/master/BHZB1.txt
    # --https://raw.githubusercontent.com/ssili126/tv/main/itvlist.txt
    # --http://117.72.68.25:9230/latest.txt
    # --https://gitlab.com/tvtg/vip/-/raw/main/log.txt
    # --https://cdn05042023.gitlink.org.cn/liliang74120/cmds/raw/branch/master/myDS.txt
    # --https://cdn05042023.gitlink.org.cn/api/v1/repos/xuanbei/ysv/raw/live.txt
    # --http://ttkx.live:55/lib/kx2024.txt
    # --https://2883.kstore.vip/gggg.nzk
    # --http://kxrj.site:35455/tv.m3u
    # --http://ttkx.live:567/gggg.nzk
    # ++http://120.79.4.185/new/mdlive.txt
    # ++http://tv.850930.xyz/kdsb.m3u
    # ++http://tv.850930.xyz/kdsb2.m3u
    # ++http://tv.850930.xyz/gather.m3u
    # ++http://tv.850930.xyz/543.m3u
    # ++http://tv.850930.xyz/histar.m3u
    # ++http://l.gmbbk.com/upload/16401640.txt
    # ++http://122.228.85.203:5988/uploads/tvbox/tv.txt
    # ++https://raw.githubusercontent.com/lystv/short/main/影视/tvb/MTV.txt
    # "https://dingyue.mytvsuper.xyz/myiptv.m3u",
]

url_blacklist = [
    "epg.pw/stream/",
    "103.40.13.71:12390",
    "[2409:8087:1a01:df::4077]/PLTV/",
    "8.210.140.75:68",
    "154.12.50.54",
    "yinhe.live_hls.zte.com",
    "8.137.59.151",
    "[2409:8087:7000:20:1000::22]:6060",
    "histar.zapi.us.kg",
    "www.tfiplaytv.vip",
    "dp.sxtv.top",
    "111.230.30.193",
    "148.135.93.213:81",
    "live.goodiptv.club",
    "iptv.luas.edu.cn",
    "[2409:8087:2001:20:2800:0:df6e:eb22]:80",
    "[2409:8087:2001:20:2800:0:df6e:eb23]:80",
    "[2409:8087:2001:20:2800:0:df6e:eb1d]/ott.mobaibox.com/",
    "[2409:8087:2001:20:2800:0:df6e:eb1d]:80",
    "[2409:8087:2001:20:2800:0:df6e:eb24]",
    "2409:8087:2001:20:2800:0:df6e:eb25]:80",
    "[2409:8087:2001:20:2800:0:df6e:eb27]"
]

announcements = [
    {
        "channel": "公告",
        "entries": [
            {"name": "请阅读", "url": "https://yunlongn.github.io/", "logo": "https://avatars.githubusercontent.com/u/38271111?v=4"},
            {"name": "yunlongn.github.io", "url": "https://yunlongn.github.io/", "logo": "https://avatars.githubusercontent.com/u/38271111?v=4"},
            {"name": "更新日期", "url": "https://yunlongn.github.io/", "logo": "https://avatars.githubusercontent.com/u/38271111?v=4"},
            {"name": None, "url": "https://yunlongn.github.io/", "logo": "https://avatars.githubusercontent.com/u/38271111?v=4"}
        ]
    }
]

epg_urls = [
    "https://live.fanmingming.com/e.xml",
    "http://epg.51zmt.top:8000/e.xml",
    "http://epg.aptvapp.com/xml",
    "https://epg.pw/xmltv/epg_CN.xml",
    "https://epg.pw/xmltv/epg_HK.xml",
    "https://epg.pw/xmltv/epg_TW.xml"
]