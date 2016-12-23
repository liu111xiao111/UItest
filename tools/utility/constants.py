'''
Created on Nov 17, 2016

@author: songbo
'''
# 性能数据类型
TYPE_CPU         = 'cpu'
TYPE_MEMORY      = 'memory'
TYPE_TX          = 'tx'
TYPE_RX          = 'rx'
TYPE_COLD_BOOT   = 'cold'
TYPE_WARM_BOOT   = 'warm'
TYPE_FPS         = 'fps'
TYPE_DRAW        = 'draw'
TYPE_TRAFFIC     = 'traffic'
TYPE_TEMPERATURE = 'temperature'

# 测试app目录及测试用例目录
FFAN    = 'ffan'
MTUAN   = 'mtuan'

FFAN_APP = u'飞凡'
MTUAN_APP = u'美团'

CASE_LOGIN     = u'我的登录'
CASE_ORDERS    = u'我的订单'
CASE_MOVIE     = u'电影'
CASE_FOOD      = u'美食汇'
CASE_COLD_BOOT = u'冷启动'
CASE_WARM_BOOT = u'热启动'
CASE_FPS       = u'FPS'

# 测试数据文件
PERF_FILE         = 'performance.xml'
TRAFFIC_FILE      = 'traffic.txt'
BOOTTIME_FILE     = 'boottime.txt'
FPS_FILE          = 'fps.txt'
EXCEL_REPORT_FILE = '%s_performance_result.xlsx'

# 测试用例List
CASE_LIST = [
    CASE_LOGIN,
    CASE_ORDERS,
    CASE_MOVIE,
    CASE_FOOD,
    CASE_COLD_BOOT,
    CASE_WARM_BOOT,
    CASE_FPS
]

CASE_FOLDER_LIST = {
    CASE_LOGIN     : 'wodedenglu',
    CASE_ORDERS    : 'wodedingdan',
    CASE_MOVIE     : 'dianying',
    CASE_FOOD      : 'meishihui',
    CASE_COLD_BOOT : 'coldboot',
    CASE_WARM_BOOT : 'warmboot',
    CASE_FPS       : 'fps',
}

# # 性能测试图表图片信息
# IMAGE_DICT = {
#     TYPE_CPU       : 'cpuPerf.png',
#     TYPE_COLD_BOOT : 'coldBootPerf.png',
#     TYPE_WARM_BOOT : 'warmBootPerf.png',
#     TYPE_TRAFFIC   : 'trafficUsagePerf.png',
#     TYPE_DRAW      : 'overDrawPerf.png',
#     TYPE_FPS       : 'fpsPerf.png',
#     TYPE_MEMORY    : 'memoryUsagePerf.png',
#     TYPE_RX        : 'rxRatePerf.png',
#     TYPE_TX        : 'txRatePerf.png'
# }
#
# TITLE_DICT = {
#     TYPE_CPU       : u'CPU Performance(%)',
#     TYPE_COLD_BOOT : u'Cold Boot Performance(ms)',
#     TYPE_WARM_BOOT : u'Warm Boot Performance(ms)',
#     TYPE_TRAFFIC   : u'Traffic Performance(Mb)',
#     TYPE_DRAW      : u'Draw Performance',
#     TYPE_FPS       : u'Fps Performance',
#     TYPE_MEMORY    : u'Memory Performance(Mb)',
#     TYPE_RX        : u'Upstream Rate(KBps)',
#     TYPE_TX        : u'Downstream Rate(KBps)'
# }

# 邮件地址
MAIL_LIST = ['lichunyan19@wanda.cn', 'sunkai31@wanda.cn', 'renyang5@wanda.cn', 'renhaitao@wanda.cn',
             'mulihui@wanda.cn', 'yindq@neusoft.com', 'chencheng@neusoft.com', 'tl@neusoft.com',
             'song_b@neusoft.com', 'qiaojx@neusoft.com', 'zhiyuchao@wanda.cn', 'xukai36@wanda.cn']


OUTLOOPNUM = 2
INSIDELOOPNUM = 2

# 重点功能稳定性测试用例Name
CASE_CESHI_HUANJING = u'测试环境'
CASE_QUANCHENG_SOUSUO = u'全城搜索'
CASE_GOUWU_ZHONGXIN = u'购物中心'
CASE_MEISHUIHUI = u'美食汇'
CASE_GUANGCHANG_SOUSUO = u'广场搜索'
CASE_GUANGCHANG_ZHAODIAN = u'广场找店'
CASE_GUANGCHANG_PAIDUI = u'广场排队'
CASE_GUANGCHANG_TINGCHE = u'广场停车'
CASE_GUANGCHANG_MAIDAN = u'广场买单'
CASE_WODE_DENGLU = u'我的登录'
CASE_WODE_TUICHU = u'我的退出'

# 重点功能稳定性测试用例文件夹名
STABILITY_CASE_FOLDER_LIST = {
    CASE_QUANCHENG_SOUSUO     : 'quanchengsousuo',
    CASE_GOUWU_ZHONGXIN       : 'gouwuzhongxin',
    CASE_MEISHUIHUI           : 'meishihui',
    CASE_GUANGCHANG_SOUSUO    : 'guangchangsousuo',
    CASE_GUANGCHANG_ZHAODIAN  : 'guangchangzhaodian',
    CASE_GUANGCHANG_PAIDUI    : 'guangchangpaidui',
    CASE_GUANGCHANG_TINGCHE   : 'guangchangtingche',
    CASE_GUANGCHANG_MAIDAN    : 'guangchangmaidan',
    CASE_WODE_DENGLU          : 'wodedenglu',
    CASE_WODE_TUICHU          : 'wodetuichu'
}

# 重点功能稳定性测试用例List
STABILITY_REPORT_SHEET = [
    CASE_CESHI_HUANJING,
    CASE_QUANCHENG_SOUSUO,
    CASE_GOUWU_ZHONGXIN,
    CASE_MEISHUIHUI,
    CASE_GUANGCHANG_SOUSUO,
    CASE_GUANGCHANG_ZHAODIAN,
    CASE_GUANGCHANG_PAIDUI,
    CASE_GUANGCHANG_TINGCHE,
    CASE_GUANGCHANG_MAIDAN,
    CASE_WODE_DENGLU,
    CASE_WODE_TUICHU
]
