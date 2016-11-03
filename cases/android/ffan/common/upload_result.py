# coding: utf-8

import requests


def upload():
    log1 = '{"logcat": "http://testplat.intra.sit.ffan.com/static/app/webShow/doc/woDeDengLuLogcat.log", "caselog": "http://testplat.intra.sit.ffan.com/static/app/webShow/doc/woDeDengLu.log"}'
    log2 = '{"logcat": "http://testplat.intra.sit.ffan.com/static/app/webShow/doc/guangChangMeiShiHuiLogcat.log", "caselog": "http://testplat.intra.sit.ffan.com/static/app/webShow/doc/guangChangMeiShiHui.log"}'
    img1 = '["http://testplat.intra.sit.ffan.com/static/app/webShow/img/woDeDengLu1.png","http://testplat.intra.sit.ffan.com/static/app/webShow/img/woDeDengLu2.png","http://testplat.intra.sit.ffan.com/static/app/webShow/img/woDeDengLu3.png","http://testplat.intra.sit.ffan.com/static/app/webShow/img/woDeDengLu4.png","http://testplat.intra.sit.ffan.com/static/app/webShow/img/woDeDengLu5.png","http://testplat.intra.sit.ffan.com/static/app/webShow/img/woDeDengLu6.png","http://testplat.intra.sit.ffan.com/static/app/webShow/img/woDeDengLu7.png"]'
    img2 = '["http://testplat.intra.sit.ffan.com/static/app/webShow/img/guangChangMeiShiHui1.png","http://testplat.intra.sit.ffan.com/static/app/webShow/img/guangChangMeiShiHui2.png","http://testplat.intra.sit.ffan.com/static/app/webShow/img/guangChangMeiShiHui3.png","http://testplat.intra.sit.ffan.com/static/app/webShow/img/guangChangMeiShiHui4.png","http://testplat.intra.sit.ffan.com/static/app/webShow/img/guangChangMeiShiHui5.png","http://testplat.intra.sit.ffan.com/static/app/webShow/img/guangChangMeiShiHui6.png","http://testplat.intra.sit.ffan.com/static/app/webShow/img/guangChangMeiShiHui7.png"]'
    #per = '{"cpu": "http://testplat.intra.sit.ffan.com/static/app/webShow/doc/Cpu_performance.txt","memory": "http://testplat.intra.sit.ffan.com/static/app/webShow/doc/Mem_peformance.txt","upstreamrate": "http://testplat.intra.sit.ffan.com/static/app/webShow/doc/Tx_performance.txt","downstreamrate": "http://testplat.intra.sit.ffan.com/static/app/webShow/doc/Rx_performance.txt","coldboottime": "http://testplat.intra.sit.ffan.com/static/app/webShow/doc/ColdBootTime_performance.txt","warmboottime": "http://testplat.intra.sit.ffan.com/static/app/webShow/doc/WarmBootTime_performance.txt"}'

    # 巡检用例执行成功数据
    patrolData1 = {
        "testcase": "我的登录", #测试用例名称
        "result": "passed", #用例执行结果（1，通过，0，未通过）
        "logpath": log1, #日志存放地址
        "starttime": "2016/10/27 17:18:08", #用例执行开始时间
        "endtime": "2016/10/27 17:20:39", #用例执行结束时间
        "buildnumber": "4.9.0.0", #App Build Number
        "prod": "ffan", #产品id
        "devicetype": "LGE LG-D802", #设备型号
        "osversion": "Android 4.2.2", #系统版本
        "imglist": img1, #截图路径
        "perftable": "", #性能数据路径
        "failtype": "", #失败类型（prod,script,infra）
        "errinfo": "", #错误信息路径
        "stepfroerr": "", #发生错误的步骤
        "errcounts":"", #错误数目统计
        "stacktrace":""
    }

    # 巡检用例执行失败数据
    patrolData2 = {
        "testcase": "广场美食汇", #测试用例名称
        "result": "failed", #用例执行结果（1，通过，0，未通过）
        "logpath": log2, #日志存放地址
        "starttime": "2016/10/27 17:30:57", #用例执行开始时间
        "endtime": "2016/10/27 17:32:56", #用例执行结束时间
        "buildnumber": "4.9.0.0", #App Build Number
        "prod": "ffan", #产品id
        "devicetype": "LGE LG-D802", #设备型号
        "osversion": "Android 4.2.2", #系统版本
        "imglist": img2, #截图路径
        "perftable": "", #性能数据路径
        "failtype": "prod", #失败类型（prod,script,infra）
        "errinfo": "Traceback (most recent call last):\
                    File '/Volumes/Disk/workspace/autotest/cases/android/ffan/routing_inspection_test_cases/guangChangMeiShiHui.py', line 70, in testGuangChangMeiShiHui\
                    squareFoodPage.clickOnFindRestaurant()\
                    File '/Volumes/Disk/workspace/autotest/pages/android/ffan/square_food_category_page.py', line 24, in clickOnFindRestaurant\
                    SFPC.click_child_module_timeout)\
                    File '/Volumes/Disk/workspace/autotest/api/api.py', line 615, in clickElementByResourceId\
                    testCase.assertTrue(False, 'Click element by resource id [%s] timeout' % (resourceId))\
                    AssertionError: False is not true : Click element by resource id [com.wanda.app.wanhui:id/food_circle_item_text] timeout", #错误信息路径
        "stepfroerr": "", #发生错误的步骤
        "errcounts": '{"crashed": 0, "ANR": 0}', #错误数目统计
        "stacktrace":""
    }

    dataList = [patrolData1, patrolData2]
    for i in range(len(dataList)):
        r = requests.post(url="http://testplat.intra.sit.ffan.com/1.0/xunjian_android_20160722/executions/", data=dataList[i])

'''def uploadPatrolData1():
    log =  '{"logcat": "http://testplat.intra.sit.ffan.com/static/app/webShow/img/woDeDengLuLogcat.log", "caselog": "http://testplat.intra.sit.ffan.com/static/app/webShow/img/woDeDengLu.log"}'
    img = '["http://testplat.intra.sit.ffan.com/static/app/webShow/img/woDeDengLu1.png","http://testplat.intra.sit.ffan.com/static/app/webShow/img/woDeDengLu2.png","http://testplat.intra.sit.ffan.com/static/app/webShow/img/woDeDengLu3.png","http://testplat.intra.sit.ffan.com/static/app/webShow/img/woDeDengLu4.png","http://testplat.intra.sit.ffan.com/static/app/webShow/img/woDeDengLu5.png","http://testplat.intra.sit.ffan.com/static/app/webShow/img/woDeDengLu6.png","http://testplat.intra.sit.ffan.com/static/app/webShow/img/woDeDengLu7.png","http://testplat.intra.sit.ffan.com/static/app/webShow/doc/guangChangMeiShiHui1.png","http://testplat.intra.sit.ffan.com/static/app/webShow/doc/guangChangMeiShiHui2.png","http://testplat.intra.sit.ffan.com/static/app/webShow/doc/guangChangMeiShiHui3.png","http://testplat.intra.sit.ffan.com/static/app/webShow/doc/guangChangMeiShiHui4.png","http://testplat.intra.sit.ffan.com/static/app/webShow/doc/guangChangMeiShiHui5.png","http://testplat.intra.sit.ffan.com/static/app/webShow/doc/guangChangMeiShiHui6.png","http://testplat.intra.sit.ffan.com/static/app/webShow/doc/guangChangMeiShiHui7.png"]'
    per = '{"cpu": "http://testplat.intra.sit.ffan.com/static/app/webShow/doc/Cpu_performance.txt","memory": "http://testplat.intra.sit.ffan.com/static/app/webShow/doc/Mem_peformance.txt","upstreamrate": "http://testplat.intra.sit.ffan.com/static/app/webShow/doc/Tx_performance.txt","downstreamrate": "http://testplat.intra.sit.ffan.com/static/app/webShow/doc/Rx_performance.txt","coldboottime": "http://testplat.intra.sit.ffan.com/static/app/webShow/doc/ColdBootTime_performance.txt","warmboottime": "http://testplat.intra.sit.ffan.com/static/app/webShow/doc/WarmBootTime_performance.txt"}'

    # 巡检用例执行成功数据
    patrolData1 = {
        "testcase": "我的登录", #测试用例名称
        "result": "passed", #用例执行结果（1，通过，0，未通过）
        "logpath": log, #日志存放地址
        "starttime": "2016/10/27 17:18:08", #用例执行开始时间
        "endtime": "2016/10/27 17:20:39", #用例执行结束时间
        "buildnumber": "4.9.0.0", #App Build Number
        "prod": "ffan", #产品id
        "devicetype": "LGE LG-D802", #设备型号
        "osversion": "Android 4.2.2", #系统版本
        "imglist": img, #截图路径
        "perftable": "", #性能数据路径
        "failtype": "", #失败类型（prod,script,infra）
        "errinfo": "", #错误信息路径
        "stepfroerr": "", #发生错误的步骤
        "errcounts":"", #错误数目统计
        "stacktrace":""
    }

    r = requests.post(url="http://192.168.1.133:8888/1.0/xunjian_android_20160721/executions/", data=patrolData1)
    # r = requests.get(url="http://192.168.1.133:8888/1.0/ios_20160720/executions/")

def uploadPatrolData2():
    log = '{"logcat": "http://testplat.intra.sit.ffan.com/static/app/webShow/doc/guangChangMeiShiHuiLogcat.log", "caselog": "http://testplat.intra.sit.ffan.com/static/app/webShow/doc/guangChangMeiShiHui.log"}'
    img = '["http://testplat.intra.sit.ffan.com/static/app/webShow/img/woDeDengLu1.png","http://testplat.intra.sit.ffan.com/static/app/webShow/img/woDeDengLu2.png","http://testplat.intra.sit.ffan.com/static/app/webShow/img/woDeDengLu3.png","http://testplat.intra.sit.ffan.com/static/app/webShow/img/woDeDengLu4.png","http://testplat.intra.sit.ffan.com/static/app/webShow/img/woDeDengLu5.png","http://testplat.intra.sit.ffan.com/static/app/webShow/img/woDeDengLu6.png","http://testplat.intra.sit.ffan.com/static/app/webShow/img/woDeDengLu7.png","http://testplat.intra.sit.ffan.com/static/app/webShow/doc/guangChangMeiShiHui1.png","http://testplat.intra.sit.ffan.com/static/app/webShow/doc/guangChangMeiShiHui2.png","http://testplat.intra.sit.ffan.com/static/app/webShow/doc/guangChangMeiShiHui3.png","http://testplat.intra.sit.ffan.com/static/app/webShow/doc/guangChangMeiShiHui4.png","http://testplat.intra.sit.ffan.com/static/app/webShow/doc/guangChangMeiShiHui5.png","http://testplat.intra.sit.ffan.com/static/app/webShow/doc/guangChangMeiShiHui6.png","http://testplat.intra.sit.ffan.com/static/app/webShow/doc/guangChangMeiShiHui7.png"]'
    per = '{"cpu": "http://testplat.intra.sit.ffan.com/static/app/webShow/doc/Cpu_performance.txt","memory": "http://testplat.intra.sit.ffan.com/static/app/webShow/doc/Mem_peformance.txt","upstreamrate": "http://testplat.intra.sit.ffan.com/static/app/webShow/doc/Tx_performance.txt","downstreamrate": "http://testplat.intra.sit.ffan.com/static/app/webShow/doc/Rx_performance.txt","coldboottime": "http://testplat.intra.sit.ffan.com/static/app/webShow/doc/ColdBootTime_performance.txt","warmboottime": "http://testplat.intra.sit.ffan.com/static/app/webShow/doc/WarmBootTime_performance.txt"}'

    # 巡检用例执行失败数据
    patrolData2 = {
        "testcase": "广场美食汇", #测试用例名称
        "result": "failed", #用例执行结果（1，通过，0，未通过）
        "logpath": log, #日志存放地址
        "starttime": "2016/10/27 17:30:57", #用例执行开始时间
        "endtime": "2016/10/27 17:32:56", #用例执行结束时间
        "buildnumber": "4.9.0.0", #App Build Number
        "prod": "ffan", #产品id
        "devicetype": "LGE LG-D802", #设备型号
        "osversion": "Android 4.2.2", #系统版本
        "imglist": img, #截图路径
        "perftable": "", #性能数据路径
        "failtype": "prod", #失败类型（prod,script,infra）
        "errinfo": "", #错误信息路径
        "stepfroerr": "", #发生错误的步骤
        "errcounts":'{"timeout": 1}', #错误数目统计
        "stacktrace":""
    }

    r = requests.post(url="http://192.168.1.133:8888/1.0/xunjian_android_20160721/executions/", data=patrolData2)'''
    # r = requests.get(url="http://192.168.1.133:8888/1.0/ios_20160720/executions/")

'''def uploadPerformanceData():
    #log = '[{"logcat": "http://testplat.intra.sit.ffan.com/static/app/webShow/img/woDeDengLuLogcat.log", "caselog": "http://testplat.intra.sit.ffan.com/static/app/webShow/img/woDeDengLu.log"}, {"logcat": "http://testplat.intra.sit.ffan.com/static/app/webShow/doc/guangChangMeiShiHuiLogcat.log", "caselog": "http://testplat.intra.sit.ffan.com/static/app/webShow/doc/guangChangMeiShiHui.log"}, {"monkey": "http://testplat.intra.sit.ffan.com/static/app/webShow/doc/Android_monkey_logcat.log"}]'
    #img = '["http://testplat.intra.sit.ffan.com/static/app/webShow/img/woDeDengLu1.png","http://testplat.intra.sit.ffan.com/static/app/webShow/img/woDeDengLu2.png","http://testplat.intra.sit.ffan.com/static/app/webShow/img/woDeDengLu3.png","http://testplat.intra.sit.ffan.com/static/app/webShow/img/woDeDengLu4.png","http://testplat.intra.sit.ffan.com/static/app/webShow/img/woDeDengLu5.png","http://testplat.intra.sit.ffan.com/static/app/webShow/img/woDeDengLu6.png","http://testplat.intra.sit.ffan.com/static/app/webShow/img/woDeDengLu7.png","http://testplat.intra.sit.ffan.com/static/app/webShow/doc/guangChangMeiShiHui1.png","http://testplat.intra.sit.ffan.com/static/app/webShow/doc/guangChangMeiShiHui2.png","http://testplat.intra.sit.ffan.com/static/app/webShow/doc/guangChangMeiShiHui3.png","http://testplat.intra.sit.ffan.com/static/app/webShow/doc/guangChangMeiShiHui4.png","http://testplat.intra.sit.ffan.com/static/app/webShow/doc/guangChangMeiShiHui5.png","http://testplat.intra.sit.ffan.com/static/app/webShow/doc/guangChangMeiShiHui6.png","http://testplat.intra.sit.ffan.com/static/app/webShow/doc/guangChangMeiShiHui7.png"]'
    per = '{"cpu": "http://testplat.intra.sit.ffan.com/static/app/webShow/doc/Cpu_performance.txt","memory": "http://testplat.intra.sit.ffan.com/static/app/webShow/doc/Mem_peformance.txt","upstreamrate": "http://testplat.intra.sit.ffan.com/static/app/webShow/doc/Tx_performance.txt","downstreamrate": "http://testplat.intra.sit.ffan.com/static/app/webShow/doc/Rx_performance.txt","coldboottime": "http://testplat.intra.sit.ffan.com/static/app/webShow/doc/ColdBootTime_performance.txt","warmboottime": "http://testplat.intra.sit.ffan.com/static/app/webShow/doc/WarmBootTime_performance.txt"}'

    # 性能测试数据
    performanceData = {
        "testcase": "性能测试", #测试用例名称
        "result": "passed", #用例执行结果（1，通过，0，未通过）
        "logpath":  "", #日志存放地址
        "starttime": "2016/10/27 01:06:05", #用例执行开始时间
        "endtime": "2016/10/27 03:07:45", #用例执行结束时间
        "buildnumber": "4.9.0.0", #App Build Number
        "prod": "ffan", #产品id
        "devicetype": "LGE LG-D802", #设备型号
        "osversion": "Android 4.2.2", #系统版本
        "imglist": "", #截图路径
        "perftable": per, #性能数据路径
        "failtype": "", #失败类型（prod,script,infra）
        "errinfo": "", #错误信息路径
        "stepfroerr": "", #发生错误的步骤
        "errcounts": "", #错误数目统计
        "stacktrace":""
    }

    r = requests.post(url="http://192.168.1.133:8888/1.0/xunjian_android_20160721/executions/", data=uploadPerformanceData)
    # r = requests.get(url="http://192.168.1.133:8888/1.0/ios_20160720/executions/")

def uploadMonkeyData():
    log = '{"monkey": "http://testplat.intra.sit.ffan.com/static/app/webShow/doc/Android_monkey_logcat.log"}'
    #img = '["http://testplat.intra.sit.ffan.com/static/app/webShow/img/woDeDengLu1.png","http://testplat.intra.sit.ffan.com/static/app/webShow/img/woDeDengLu2.png","http://testplat.intra.sit.ffan.com/static/app/webShow/img/woDeDengLu3.png","http://testplat.intra.sit.ffan.com/static/app/webShow/img/woDeDengLu4.png","http://testplat.intra.sit.ffan.com/static/app/webShow/img/woDeDengLu5.png","http://testplat.intra.sit.ffan.com/static/app/webShow/img/woDeDengLu6.png","http://testplat.intra.sit.ffan.com/static/app/webShow/img/woDeDengLu7.png","http://testplat.intra.sit.ffan.com/static/app/webShow/doc/guangChangMeiShiHui1.png","http://testplat.intra.sit.ffan.com/static/app/webShow/doc/guangChangMeiShiHui2.png","http://testplat.intra.sit.ffan.com/static/app/webShow/doc/guangChangMeiShiHui3.png","http://testplat.intra.sit.ffan.com/static/app/webShow/doc/guangChangMeiShiHui4.png","http://testplat.intra.sit.ffan.com/static/app/webShow/doc/guangChangMeiShiHui5.png","http://testplat.intra.sit.ffan.com/static/app/webShow/doc/guangChangMeiShiHui6.png","http://testplat.intra.sit.ffan.com/static/app/webShow/doc/guangChangMeiShiHui7.png"]'
    #per = '{"cpu": "http://testplat.intra.sit.ffan.com/static/app/webShow/doc/Cpu_performance.txt","memory": "http://testplat.intra.sit.ffan.com/static/app/webShow/doc/Mem_peformance.txt","upstreamrate": "http://testplat.intra.sit.ffan.com/static/app/webShow/doc/Tx_performance.txt","downstreamrate": "http://testplat.intra.sit.ffan.com/static/app/webShow/doc/Rx_performance.txt","coldboottime": "http://testplat.intra.sit.ffan.com/static/app/webShow/doc/ColdBootTime_performance.txt","warmboottime": "http://testplat.intra.sit.ffan.com/static/app/webShow/doc/WarmBootTime_performance.txt"}'

    # 稳定性测试数据
    monkeyData = {
        "testcase": "稳定性测试", #测试用例名称
        "result": "passed", #用例执行结果（1，通过，0，未通过）
        "logpath": log, #日志存放地址
        "starttime": "2016/10/27 03:01:00", #用例执行开始时间
        "endtime": "2016/10/27 07:16:08", #用例执行结束时间
        "buildnumber": "4.9.0.0", #App Build Number
        "prod": "ffan", #产品id
        "devicetype": "LGE LG-D802", #设备型号
        "osversion": "Android 4.2.2", #系统版本
        "imglist": "", #截图路径
        "perftable": "", #性能数据路径
        "failtype": "", #失败类型（prod,script,infra）
        "errinfo": "", #错误信息路径
        "stepfroerr": "", #发生错误的步骤
        "errcounts": "", #错误数目统计
        "stacktrace": ""
    }

    r = requests.post(url="http://192.168.1.133:8888/1.0/xunjian_android_20160721/executions/", data=uploadMonkeyData)
    # r = requests.get(url="http://192.168.1.133:8888/1.0/ios_20160720/executions/")'''

'''def upload():
    log = '[{"logcat": "http://testplat.intra.sit.ffan.com/static/app/webShow/img/woDeDengLuLogcat.log", "caselog": "http://testplat.intra.sit.ffan.com/static/app/webShow/img/woDeDengLu.log"}, {"logcat": "http://testplat.intra.sit.ffan.com/static/app/webShow/doc/guangChangMeiShiHuiLogcat.log", "caselog": "http://testplat.intra.sit.ffan.com/static/app/webShow/doc/guangChangMeiShiHui.log"}, {"monkey": "http://testplat.intra.sit.ffan.com/static/app/webShow/doc/Android_monkey_logcat.log"}]'
    img = '["http://testplat.intra.sit.ffan.com/static/app/webShow/img/woDeDengLu1.png","http://testplat.intra.sit.ffan.com/static/app/webShow/img/woDeDengLu2.png","http://testplat.intra.sit.ffan.com/static/app/webShow/img/woDeDengLu3.png","http://testplat.intra.sit.ffan.com/static/app/webShow/img/woDeDengLu4.png","http://testplat.intra.sit.ffan.com/static/app/webShow/img/woDeDengLu5.png","http://testplat.intra.sit.ffan.com/static/app/webShow/img/woDeDengLu6.png","http://testplat.intra.sit.ffan.com/static/app/webShow/img/woDeDengLu7.png","http://testplat.intra.sit.ffan.com/static/app/webShow/doc/guangChangMeiShiHui1.png","http://testplat.intra.sit.ffan.com/static/app/webShow/doc/guangChangMeiShiHui2.png","http://testplat.intra.sit.ffan.com/static/app/webShow/doc/guangChangMeiShiHui3.png","http://testplat.intra.sit.ffan.com/static/app/webShow/doc/guangChangMeiShiHui4.png","http://testplat.intra.sit.ffan.com/static/app/webShow/doc/guangChangMeiShiHui5.png","http://testplat.intra.sit.ffan.com/static/app/webShow/doc/guangChangMeiShiHui6.png","http://testplat.intra.sit.ffan.com/static/app/webShow/doc/guangChangMeiShiHui7.png"]'
    per = '{"cpu": "http://testplat.intra.sit.ffan.com/static/app/webShow/doc/Cpu_performance.txt","memory": "http://testplat.intra.sit.ffan.com/static/app/webShow/doc/Mem_peformance.txt","upstreamrate": "http://testplat.intra.sit.ffan.com/static/app/webShow/doc/Tx_performance.txt","downstreamrate": "http://testplat.intra.sit.ffan.com/static/app/webShow/doc/Rx_performance.txt","coldboottime": "http://testplat.intra.sit.ffan.com/static/app/webShow/doc/ColdBootTime_performance.txt","warmboottime": "http://testplat.intra.sit.ffan.com/static/app/webShow/doc/WarmBootTime_performance.txt"}'

    # 巡检用例执行成功数据
    patrolData1 = {
        "testcase": "我的登录", #测试用例名称
        "result": "passed", #用例执行结果（1，通过，0，未通过）
        "logpath": log, #日志存放地址
        "starttime": "2016/10/27 17:18:08", #用例执行开始时间
        "endtime": "2016/10/27 17:20:39", #用例执行结束时间
        "buildnumber": "4.9.0.0", #App Build Number
        "prod": "ffan", #产品id
        "devicetype": "LGE LG-D802", #设备型号
        "osversion": "Android 4.2.2", #系统版本
        "imglist": img, #截图路径
        "perftable": "", #性能数据路径
        "failtype": "", #失败类型（prod,script,infra）
        "errinfo": "", #错误信息路径
        "stepfroerr": "", #发生错误的步骤
        "errcounts":"", #错误数目统计
        "stacktrace":""
    }

    # 巡检用例执行失败数据
    patrolData2 = {
        "testcase": "广场美食汇", #测试用例名称
        "result": "failed", #用例执行结果（1，通过，0，未通过）
        "logpath": log, #日志存放地址
        "starttime": "2016/10/27 17:30:57", #用例执行开始时间
        "endtime": "2016/10/27 17:32:56", #用例执行结束时间
        "buildnumber": "4.9.0.0", #App Build Number
        "prod": "ffan", #产品id
        "devicetype": "LGE LG-D802", #设备型号
        "osversion": "Android 4.2.2", #系统版本
        "imglist": img, #截图路径
        "perftable": "", #性能数据路径
        "failtype": "prod", #失败类型（prod,script,infra）
        "errinfo": "", #错误信息路径
        "stepfroerr": "", #发生错误的步骤
        "errcounts":'{"timeout": 1}', #错误数目统计
        "stacktrace":""
    }

    # 性能测试数据
    performanceData = {
        "testcase": "性能测试", #测试用例名称
        "result": "passed", #用例执行结果（1，通过，0，未通过）
        "logpath":  "", #日志存放地址
        "starttime": "2016/10/27 01:06:05", #用例执行开始时间
        "endtime": "2016/10/27 03:07:45", #用例执行结束时间
        "buildnumber": "4.9.0.0", #App Build Number
        "prod": "ffan", #产品id
        "devicetype": "LGE LG-D802", #设备型号
        "osversion": "Android 4.2.2", #系统版本
        "imglist": "", #截图路径
        "perftable": per, #性能数据路径
        "failtype": "", #失败类型（prod,script,infra）
        "errinfo": "", #错误信息路径
        "stepfroerr": "", #发生错误的步骤
        "errcounts": "", #错误数目统计
        "stacktrace":""
    }

    # 稳定性测试数据
    monkeyData = {
        "testcase": "稳定性测试", #测试用例名称
        "result": "passed", #用例执行结果（1，通过，0，未通过）
        "logpath": log, #日志存放地址
        "starttime": "2016/10/27 03:01:00", #用例执行开始时间
        "endtime": "2016/10/27 07:16:08", #用例执行结束时间
        "buildnumber": "4.9.0.0", #App Build Number
        "prod": "ffan", #产品id
        "devicetype": "LGE LG-D802", #设备型号
        "osversion": "Android 4.2.2", #系统版本
        "imglist": "", #截图路径
        "perftable": "", #性能数据路径
        "failtype": "", #失败类型（prod,script,infra）
        "errinfo": "", #错误信息路径
        "stepfroerr": "", #发生错误的步骤
        "errcounts": "", #错误数目统计
        "stacktrace": ""
    }

    r = requests.post(url="http://192.168.1.133:8888/1.0/xunjian_android_20160721/executions/", data=patrolData1)'''
    # r = requests.get(url="http://192.168.1.133:8888/1.0/ios_20160720/executions/")


if __name__ == "__main__":
    upload()
    '''uploadPatrolData1()
    uploadPatrolData2()
    uploadPerformanceData()
    uploadMonkeyData()'''