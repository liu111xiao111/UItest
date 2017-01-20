# -*- coding:utf-8 -*-

import subprocess
import threading
import time
import sys, os
import time
from unittest import TestCase
from unittest import TestLoader
from unittest.suite import TestSuite
import unittest

import HTMLTestRunner

#from cases.ios.ffan.common.reportProcess import ReportHandle
from cases.ios.ffan.stability_test.guangChangMaiDan import GuangChangMaiDanTestCase
from cases.ios.ffan.stability_test.guangChangMeiShiHui import GuangChangMeiShiHuiTestCase
from cases.ios.ffan.stability_test.guangChangSouSuo import GuangChangSouSuoTestCase
from cases.ios.ffan.stability_test.guangChangTingChe import GuangChangTingCheTestCase
from cases.ios.ffan.stability_test.guangChangZhaoDian import GuangChangZhaoDianTestCase
from cases.ios.ffan.stability_test.paiDuiQuHao import PaiDuiQuHaoTestCase
from cases.ios.ffan.stability_test.quanChengSouSuoMenDian import QuanChengSouSuoMenDianTestCase
from cases.ios.ffan.stability_test.quanChengSouSuoPinPai import QuanChengSouSuoPinPaiTestCase
from cases.ios.ffan.stability_test.quanChengSouSuoShangPin import QuanChengSouSuoShangPinTestCase
from cases.ios.ffan.stability_test.woDeDengLu import WoDeDengLuTestCase
from cases.ios.ffan.stability_test.gouWuZhongXin import GouWuZhongXinTestCase
from cases.ios.ffan.stability_test.woDeTuiChu import WoDeTuiChuTestCase

from utility.mailProcess import sendTestResultMail

class Stability(object):
    pidList = []

    #总循环次数
    EXTERNAL_LOOP_TIMES = 3;
    #每个case循环次数
    INTERNAL_LOOP_TIMES = 3;

    COMMAND = "idevicesyslog"

    def __init__(self):
        pass


    def _saveLog(self,logpath, case_name, external_case_count, internal_case_count):
        print('BEGIN get iOS log')
        '''
        保存log到回归测试目录
        :return:
        '''
        #logpath = "/Users/auto/Desktop/testlog.txt"
        command = "%s > %s" % (self.COMMAND, "%s/%s_%s_%s.%s" % (logpath, case_name, external_case_count, internal_case_count,'log'))
        print("Save log : " + command)
        os.system(command)
        #print('DEBUG GET LOE END!')


    def _execCmd(self,cmd):
        r = os.popen(cmd)
        line = r.readlines()
        r.close()
        return line

    def _getIdevicelogPid(self):
        '''
        获取 IdevicelogPid
        :return:
        '''

        list = self._execCmd("ps -A | grep idevicesyslog")
        for item in list:
            print("idevicesyslog pid : " + item.split(' ')[0])
            pid = item.split(' ')[0]
            if(pid==" "):
                pid = item.split(' ')[1]
            self.pidList.append(pid)


    def _killIdevicelogPid(self):
        '''
        kill IdevicelogPid
        :return:
        '''
        self._getIdevicelogPid()
        for pid in self.pidList:
            if(pid != " "):
                self._execCmd('kill %s' % pid)
            #print("kill idevicelog pid %s" % pid)
        self.pidList = []

    def _startGetLog(self, logpath , case_name, external_case_count, internal_case_count):
        '''
        Thread for get log
        :param logpath:
        :return:
        '''
        t = threading.Thread(target=Stability()._saveLog, args=(logpath, case_name, external_case_count, internal_case_count))
        t.start()

    def _createPath(self,reportpath=""):
        '''
        Create path
        :param reportpath:
        :return:
        '''
        if not os.path.exists(reportpath):
            print("create path %s " % reportpath)
            os.makedirs(reportpath)


    def _launchCase(self, case_name, class_name, external_case_count, internal_case_count,reportpath):
        '''

        :param reportpath:
        :return:
        '''
        print("external %s loop 执行 %s 次 " % (case_name, external_case_count))
        print("internal %s loop 执行 %s 次 " % (case_name,internal_case_count))
        suite = unittest.TestSuite()
        runner = unittest.TextTestRunner()
        reportpath = "%s/%s/%s" % (reportpath, case_name,'log')
        # 创建路径
        print("reportpath : " + reportpath)
        stability._createPath(reportpath)
        # 开始获取LOG
        stability._startGetLog(reportpath, case_name, external_case_count, internal_case_count)

        print("开始执行case...")
        suite.addTest(class_name("test_case"))
        runner.run(suite)

        # case执行完成后,kill idevicesyslog 进程
        time.sleep(5)
        stability._killIdevicelogPid()


    def _writeCharInToSpecificFile(self, file ,context):
        '''
        Write char into specific file
        :param file:
        :param context:
        :return:
        '''
        f = open(file, "a")
        f.write(context + '\n')
        f.close()


if __name__ == "__main__":
    stability = Stability()
    #Kill idevice log pi process before test
    stability._killIdevicelogPid()
    #stability._saveLog()

    #
    # t = threading.Thread(target=Stability()._saveLog)
    # t.start()
    #
    # time.sleep(10)
    #
    # Stability()._killIdevicelogPid()

    build_num = sys.argv[1]

    reportpath = "%s/stability/%s/%s" % ("/Users/auto/workspace_pycharm/autotest/report", time.strftime("%Y%m%d"), build_num)

    #Cache file for saving data
    cacheFile = "%s/%s" % (reportpath,'cache')

    #开始时候时间
    startTime = time.strftime('%H:%M:%S')

    #循环次数计数
    external_case_count = 0
    #内层case循环次数
    internal_case_count = 0

    for external_case_count in range(1,stability.EXTERNAL_LOOP_TIMES):
        reportpath = "%s/stability/%s/%s" % ("/Users/auto/workspace_pycharm/autotest/report", time.strftime("%Y%m%d"), build_num)
        print("external loop 执行 %s 次 " % external_case_count)
        reportpath = "%s/%s" % (reportpath,external_case_count)
        print("debug reportpath %s " % reportpath)
        for internal_case_count in range(1, stability.INTERNAL_LOOP_TIMES):
            #开始运行case
            # # 全城搜索品牌
            # stability._launchCase("QuanChengSouSuoPinPaiTestCase", QuanChengSouSuoPinPaiTestCase, external_case_count,
            #                       internal_case_count, reportpath)
            # #全城搜索商品
            # stability._launchCase("QuanChengSouSuoShangPinTestCase", QuanChengSouSuoShangPinTestCase, external_case_count,
            #                       internal_case_count, reportpath)
            #全城搜索门店
            stability._launchCase("quanchengsousuo", QuanChengSouSuoMenDianTestCase, external_case_count,
                                  internal_case_count, reportpath)
            #广场搜索
            stability._launchCase("guangchangsousuo", GuangChangSouSuoTestCase, external_case_count,
                                  internal_case_count, reportpath)
            #购物中心
            stability._launchCase("gouwuzhongxin", GouWuZhongXinTestCase, external_case_count,
                                  internal_case_count, reportpath)

            #广场找店
            stability._launchCase("guangchangzhaodian", GuangChangZhaoDianTestCase, external_case_count,
                                  internal_case_count,reportpath)
            #广场排队取号
            stability._launchCase("guangchangpaidui", PaiDuiQuHaoTestCase, external_case_count,
                                  internal_case_count, reportpath)
            #广场停车
            stability._launchCase("guangchangtingche", GuangChangTingCheTestCase, external_case_count,
                                  internal_case_count, reportpath)
            #广场买单
            stability._launchCase("guangchangmaidan", GuangChangMaiDanTestCase, external_case_count,
                                  internal_case_count, reportpath)
            #美食汇
            stability._launchCase("meishihui", GuangChangMeiShiHuiTestCase, external_case_count,
                                  internal_case_count, reportpath)
            #我的登录
            stability._launchCase("wodedenglu", WoDeDengLuTestCase, external_case_count,
                                  internal_case_count, reportpath)
            #我的退出
            stability._launchCase("wodetuichu", WoDeTuiChuTestCase, external_case_count,
                                  internal_case_count, reportpath)

    #结束时间
    endTime = time.strftime('%H:%M:%S')
    stability._writeCharInToSpecificFile(cacheFile, startTime)
    stability._writeCharInToSpecificFile(cacheFile, endTime)


