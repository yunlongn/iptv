ip_version_priority = "ipv4" #ipv6
threadNum = 128 # 请求线程数
futureTimout = 300 # 请求线程等待时间
ffmpegCheckThreadNum = 128 # 请求线程数
ffmpegCheckThreadTimeout = 60 # 请求线程等待时间
notCheck = 0 # 是否不检查地址

source_urls = [
    "https://aktv.top/live.m3u",
    "http://175.178.251.183:6689/aktvlive.txt",
    "https://live.fanmingming.com/tv/m3u/ipv6.m3u",
    "https://raw.githubusercontent.com/yuanzl77/IPTV/main/直播/央视频道.txt",
    "https://live.zhoujie218.top/tv/iptv6.txt",
    "https://tv.youdu.fan:666/live/",
    "http://ww.weidonglong.com/dsj.txt",
    "http://xhztv.top/zbc.txt",
    "https://raw.githubusercontent.com/qingwen07/awesome-iptv/main/tvbox_live_all.txt",
    "https://raw.githubusercontent.com/Guovin/TV/gd/output/result.txt",
    "http://home.jundie.top:81/Cat/tv/live.txt",
    "https://raw.githubusercontent.com/vbskycn/iptv/master/tv/hd.txt",
    "https://cdn.jsdelivr.net/gh/YueChan/live@main/IPTV.m3u",
    "https://raw.githubusercontent.com/cymz6/AutoIPTV-Hotel/main/lives.txt",
    "https://raw.githubusercontent.com/PizazzGY/TVBox_warehouse/main/live.txt",
    "https://fm1077.serv00.net/SmartTV.m3u",
    "https://raw.githubusercontent.com/ssili126/tv/main/itvlist.txt",
    "https://raw.githubusercontent.com/kimwang1978/collect-tv-txt/main/merged_output.txt",
    "https://www.mytvsuper.xyz/m3u/Live.m3u",
    "http://wx.thego.cn/ak.m3u",
    "https://raw.githubusercontent.com/BurningC4/Chinese-IPTV/master/TV-IPV4.m3u",
    "https://raw.githubusercontent.com/xzw832/cmys/refs/heads/main/S_CCTV.txt",
    "https://raw.githubusercontent.com/xzw832/cmys/refs/heads/main/S_weishi.txt",
    "https://raw.githubusercontent.com/YueChan/Live/main/APTV.m3u",
    "http://aktv.top/live.m3u",
    "https://live.zhoujie218.top/tv/iptv6.txt",
    "https://raw.githubusercontent.com/mlzlzj/hnyuan/refs/heads/main/iptv_list.txt",
    "http://kxrj.site:567/gggg.nzk",
    "http://rihou.cc:555/gggg.nzk",
    "http://rihou.cc:567/gggg.nzk",
    "http://ttkx.cc:55/lib/kx2024.txt",
    "http://xn--ur0a.xn--dkw.xn--6qq986b3xl/down.php/a7c9d038627e11f037adcad788da129e.txt",
    "http://kxrj.site:55/lib/kx2024.txt",
    "https://raw.githubusercontent.com/altn2025/iptv/main/iptv.m3u",
    "https://2912.kstore.space/520.txt",
    "http://home.jundie.top:81/Cat/tv/live.txt",
    "https://raw.githubusercontent.com/YanG-1989/m3u/refs/heads/main/Gather.m3u",
    "https://raw.githubusercontent.com/BP3388/BP001.github.io/main/tivi.list",
    "https://raw.githubusercontent.com/iptv-org/iptv/master/streams/cn.m3u",
    "https://raw.githubusercontent.com/joevess/IPTV/main/iptv.m3u8",
    "https://raw.githubusercontent.com/Supprise0901/TVBox_live/main/live.txt",
    "https://raw.githubusercontent.com/Guovin/TV/gd/output/result.txt",
    "https://10085.kstore.space/%E8%93%9D%E5%A4%A9%E7%99%BD%E4%BA%91.txt",
    "https://m3u.ibert.me/txt/fmml_ipv6.txt",
    "https://m3u.ibert.me/txt/ycl_iptv.txt",
    "https://m3u.ibert.me/txt/y_g.txt",
    "https://m3u.ibert.me/txt/j_home.txt",
    "https://raw.githubusercontent.com/gaotianliuyun/gao/master/list.txt",
    "https://gitee.com/xxy002/zhiboyuan/raw/master/zby.txt",
    "https://raw.githubusercontent.com/fenxp/iptv/main/live/tvlive.txt",
    "https://raw.githubusercontent.com/zwc456baby/iptv_alive/master/live.txt",
    "https://gitlab.com/p2v5/wangtv/-/raw/main/lunbo.txt",
    "https://raw.githubusercontent.com/PizazzGY/TVBox/main/live.txt",
    "https://raw.githubusercontent.com/wwb521/live/main/tv.m3u",
    "http://47.99.102.252/live.txt",
    "https://raw.githubusercontent.com/vbskycn/iptv/master/tv/iptv4.txt",
    "http://xhztv.top/v6.txt",
    "https://raw.githubusercontent.com/junge3333/juds6/main/yszb1.txt",
    "https://raw.githubusercontent.com/zzmaze/iptv/main/itvlist.txt",
    "https://raw.githubusercontent.com/maitel2020/iptv-self-use/main/iptv.txt",
    "https://raw.githubusercontent.com/kimwang1978/TV/master/output/result.txt",
    "https://raw.githubusercontent.com/kimwang1978/collect-tv-txt/refs/heads/main/assets/freetv/freetv_output_other.txt",
    "http://1805842a.123nat.com:66/agent/2.txt",
    "https://gitea.moe/Fathers/EkfkgH/raw/branch/main/yyfug.txt",
    "https://raw.gitcode.com/hjf520/00/raw/main/sirenzb.txt",
    "http://154.9.252.167:190/tvlive.txt",
    "https://gitee.com/tushaoyong/live/raw/master/%E6%8E%A5%E5%8F%A3/IPV6.txt",
    "https://raw.githubusercontent.com/fanmingming/live/refs/heads/main/tv/m3u/ipv6.m3u",
    # "https://raw.githubusercontent.com/frxz751113/IPTVzb1/refs/heads/main/{MMdd}%E7%BB%BC%E5%90%88%E6%BA%90.txt",
    # "https://raw.githubusercontent.com/frxz751113/IPTVzb1/refs/heads/main/{MMdd-1}%E7%BB%BC%E5%90%88%E6%BA%90.txt",
    # "https://d.kstore.space/download/7395/xiaohei.txt",
    # "http://vip.vip0531.com/viptv/live202405.txt",
    # "http://120.79.4.185/new/mdlive.txt",
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
    "[2409:8087:2001:20:2800:0:df6e:eb27]",
    "123.112.208.22",
    "zb.688768.xyz",
    "221.213.108.130",
    "111.167.176.61",
    "59.62.8.250",
    "223.105.252.8",
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
