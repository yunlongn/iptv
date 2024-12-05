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
    "https://raw.githubusercontent.com/Guovin/iptv-api/gd/output/result.txt",
    "https://raw.githubusercontent.com/YanG-1989/m3u/main/Gather.m3u",
    "https://raw.githubusercontent.com/YueChan/Live/main/IPTV.m3u",
    "https://raw.githubusercontent.com/yuanzl77/IPTV/main/直播/央视频道.txt",
    "https://raw.githubusercontent.com/yuanzl77/IPTV/main/live.txt",
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
    "https://raw.githubusercontent.com/xzw832/cmys/refs/heads/main/Z_12_cctv.txt",
    "https://raw.githubusercontent.com/xzw832/cmys/refs/heads/main/Z_12_weishi.txt",
    "https://raw.githubusercontent.com/xzw832/cmys/refs/heads/main/Z_15_cctv.txt",
    "https://raw.githubusercontent.com/xzw832/cmys/refs/heads/main/Z_15_weishi.txt",
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
    "119.62.36.174",
    "218.76.32.193",
    "115.171.216.195",
    "118.249.23.16",
    "117.27.190.42",
    "123.122.162.250",
    "101.43.66.162",
    "60.208.104.234",
    "223.159.8.12",
    "49.67.96.109",
    "121.24.98.226",
    "113.120.46.204",
    "183.185.105.197",
    "112.234.20.171",
    "123.163.55.234:9901",
    "219.159.147.195:9901",
    "124.231.215.102:9999",
    "221.213.108.11:9901",
    "171.213.196.134:8088",
    "zmjwy168.duckdns.org:35455",
    "dbiptv.sn.chinamobile.com",
    "xxxxxxxxx",
    "116.226.15.172",
    "183.185.129.160",
    "114.228.152.34",
    "180.119.183.89",
    "58.144.154.93",
    "121.227.243.195",
    "124.165.251.82",
    "171.8.244.248",
    "39.134.65.164",
    "38.64.72.148",
    "223.112.219.174",
    "239.3.1.122",
    "175.8.213.198",
    "115.48.62.69",
    "60.164.229.63",
    "39.134.65.162",
    "113.15.185.31",

    "116.21.121.116",
    "123.120.212.233",
    "112.123.155.153",
    "www.dsmcloud.top",
    "171.214.224.243",
    "221.222.162.206",
    "39.134.66.66",
    "123.138.216.44",
    "61.144.103.154",
    "cg0.hunancatv.cn",
    "221.221.162.225",
    "58.248.112.230",
    "123.189.36.39",
    "mail.petzhu.top",
    "27.222.3.214",
    "120.238.84.44",
    "yujukoo.gicp.net",
    "www.91dos.cn",
    "124.79.25.97",
    "123.113.189.90",
    "27.11.254.67",
    "124.230.56.27",
    "z.b.bkpcp.top",
    "163.177.122.125",
    "171.8.244.248",
    "110.52.99.109",
    "60.164.229.63",
    "123.113.187.204",
    "116.162.6.191",
    "39.134.136.161",
    "27.17.252.56",
    "114.243.98.12",
    "58.248.112.205",
    "iptviptv.site",
    "8.138.7.223",
    "222.128.86.76",
    "182.92.109.190",
    "123.112.19.67",
    "221.4.143.70",
    "p.ytelc.com",
    "119.125.134.201",
    "gouwu.pthv.gitv.tv",
    "gslbservzqhsw.itv.cmvideo.cn",
    "115.48.62.253",
    "125.227.210.55",
    "api.olelive.com",
    "115.234.196.165",
    "123.114.19.80",
    "117.72.68.25",
    "114.244.233.134",
    "60.164.128.167",
    "171.108.239.80",
    "221.221.167.14",
    "23.224.49.18",
    "111.20.40.171",
    "114.252.229.26",
    "103.95.24.37",
    "115.171.216.246",
    "223.151.49.74",
    "litv.zapi.us.kg",
    "223.166.234.215",
    "120.234.5.28",
    "pi.0472.org",
    "gslbserv.itv.cmvideo.cn",
    "222.240.82.92",
    "120.234.49.38",
    "nz171l122.bb60246.ctm.net",
    "115.48.62.61",
    "175.146.122.104",
    "cqshushu.us.kg",
    "115.60.241.249",
    "stream.qhbtv.com",
    "120.6.2.161",
    "124.228.160.197",
    "60.255.240.247",
    "ik6.iptv8.net",
    "114.254.82.176",
    "120.234.5.29",
    "171.108.239.79",
    "cg14.hunancatv.cn",
    "60.246.171.122",
    "114.252.235.176",
    "live.nctv.top",
    "live.v1.mk",
    "171.213.128.110",
    "imzbpfrp.zzmd.fun",
    "116.23.96.160",
    "171.8.247.154",
    "113.15.185.31",
    "cdn.iptv8k.top",
    "211.101.247.19",
    "58.53.152.234",
    "ku9.fr.to",
    "beishan008.asuscomm.com",
    "hms2844nc1972666628.live.aikan.miguvideo.com",
    "tvlive.ynradio.com",
    "60.2.190.206",
    "fash2043.cloudycdn.services",
    "115.48.61.209",
    "111.20.40.170",
    "180.141.28.176",
    "iptv.cdn.ha.chinamobile.com",
    "www.unraidd.top",
    "14.112.86.101",
    "117.161.12.124",
    "175.173.198.22",
    "nas.hssvm.com",
    "39.134.115.163",
    "14.117.234.37",
    "111.199.234.10",
    "webmail.axxe.top",
    "38.64.72.148",
    "60.7.56.33",
    "125.94.180.231",
    "171.108.239.98",
    "120.77.28.4",
    "114.254.81.231",
    "gouwu.pthvcdn.gitv.tv",
    "hw-m-l.cztv.com",
    "123.189.36.4",
    "203.205.220.174",
    "huanqiuzhibo.cn",
    "223.166.234.114",
    "hlsbkmgsplive.miguvideo.com",
    "58.248.112.229",
    "ttkx.live",
    "121.18.43.254",
    "123.113.237.160",
    "1.24.39.180",
    "116.18.37.213",
    "118.183.212.36",
    "58.250.155.2",
    "111.196.12.108",
    "113.240.177.80",
    "stream1.freetv.fun",
    "116.162.6.192",
    "113.119.39.206",
    "223.12.13.231",
    "114.254.83.83",
    "61.52.158.169",
    "www.zzlag.top",
    "14.29.76.30",
    "171.116.59.153",
    "hms2924nc1972666636.live.aikan.miguvideo.com",
    "zteres.sn.chinamobile.com",
    "119.122.214.182",
    "dd.ddzb.fun",
    "175.8.213.198",
    "tianhewan.top",
    "171.108.239.99",
    "198.16.100.90",
    "183.130.30.174",
    "cdn.jdshipin.com",
    "223.151.51.27",
    "115.48.61.177",
    "43.138.11.122",
    "121.238.98.120",
    "211.72.65.236",
    "118.113.146.174",
    "hms184nc1972679574.live.aikan.miguvideo.com",
    "hikvision.city",
    "php.jdshipin.com",
    "111.196.129.152",
    "36.40.237.20",
    "114.243.102.150",
    "111.225.115.176",
    "115.48.62.69",
    "1.203.184.45",
    "180.141.201.208",
    "106.112.254.54",
    "114.254.93.146",
    "2409",
    "grandprix2023.asuscomm.com",
    "cg11.hunancatv.cn",
    "wouu.net",
    "bjuni.iptv.im2k.com",
    "120.6.209.42",
    "wo.xiang.lai.ge.bi.jiao.chang.de.yu.ming.wan.wan.jie.xi.bu.zhi.dao.ke.bu.ke.xing.hk3.345888.xyz.cdn.cloudflare.net",
    "59.127.17.227",
    "ngtv.sjpt.ylrb.com",
    "119.98.143.13",
    "121.29.91.210",
    "124.231.213.16",
    "114.252.114.248",
    "223.112.219.174",
    "diyp.zxxoo.work",
    "api.livednow.org",
    "liveop.cctv.cn",
    "114.252.238.87",
    "115.48.60.30",
    "xeace.cn",
    "liveshowbak2.kan0512.com",
    "146.56.153.245",
    "115.48.60.156",
    "14.145.224.50",
    "222.129.139.91",
    "coolcat.synology.me",
    "www.furymax.top",
    "114.244.237.230",
    "gslbservstudent.itv.cmvideo.cn",
    "ottrrs.hl.chinamobile.com",
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
