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