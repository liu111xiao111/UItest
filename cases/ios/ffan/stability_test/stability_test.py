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
    EXTERNAL_LOOP_TIMES = 1;
    #每个case循环次数
    INTERNAL_LOOP_TIMES = 1;

    COMMAND = "idevicesyslog"

    def __init__(self):
        pass


    def _saveLog(self,logpath=""):
        print('BEGIN get iOS log')
        '''
        保存log到回归测试目录
        :return:
        '''
        #logpath = "/Users/auto/Desktop/testlog.txt"
        command = "%s > %s" % (self.COMMAND, "%s/log.txt" % logpath)
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
            self.pidList.append(item.split(' ')[0])
            #print(item.split(' '))


    def _killIdevicelogPid(self):
        '''
        kill IdevicelogPid
        :return:
        '''
        self._getIdevicelogPid()
        for pid in self.pidList:
            self._execCmd('kill %s' % pid)
            print("kill idevicelog pid %s" % pid)

    def _startGetLog(self, logpath = ""):
        '''
        Thread for get log
        :param logpath:
        :return:
        '''
        t = threading.Thread(target=Stability()._saveLog(logpath))
        t.start()

    def _createPath(self,reportpath=""):
        '''
        Create path
        :param reportpath:
        :return:
        '''
        print("create path %s " % reportpath)
        if not os.path.exists(reportpath):
            os.makedirs(reportpath)

if __name__ == "__main__":
    stability = Stability()
    #stability._saveLog()

    #
    # t = threading.Thread(target=Stability()._saveLog)
    # t.start()
    #
    # time.sleep(10)
    #
    # Stability()._killIdevicelogPid()

    sentMail = False
    if len(sys.argv) > 2:
        sentMail = True
    build_num = sys.argv[1]

    reportpath = "%s/stability/%s/%s" % ("/Users/auto/workspace_pycharm/autotest/report", time.strftime("%Y%m%d"), build_num)

    suite = unittest.TestSuite()
    runner = unittest.TextTestRunner()


    suite.addTest(QuanChengSouSuoShangPinTestCase("test_case"))
    suite.addTest(QuanChengSouSuoMenDianTestCase("test_case"))
    suite.addTest(GouWuZhongXinTestCase("test_case"))
    suite.addTest(GuangChangSouSuoTestCase("test_case"))
    suite.addTest(GuangChangZhaoDianTestCase("test_case"))
    suite.addTest(PaiDuiQuHaoTestCase("test_case"))
    suite.addTest(GuangChangTingCheTestCase("test_case"))
    suite.addTest(GuangChangMaiDanTestCase("test_case"))
    suite.addTest(GuangChangMeiShiHuiTestCase("test_case"))
    suite.addTest(WoDeDengLuTestCase("test_case"))
    suite.addTest(WoDeTuiChuTestCase("test_case"))


    # now = time.strftime('%H_%M_%S')

    # filename = reportpath + 'feifan_automation_test_report_ios.html'
    # fp = open(filename, 'wb')
    # runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Feifan_automation_test_report_ios',
    #                                        description='Result for test')

    #循环次数计数
    external_case_count = 0
    #内层case循环次数
    internal_case_count = 0

    while(external_case_count < stability.EXTERNAL_LOOP_TIMES):
        print("external loop 执行 %s 次 " % external_case_count)
        while(internal_case_count < stability.INTERNAL_LOOP_TIMES):
            print("internal QuanChengSouSuoPinPaiTestCase loop 执行 %s 次 " % internal_case_count)
            reportpath =  "%s/QuanChengSouSuoPinPaiTestCase" % reportpath
            #创建路径
            stability._createPath(reportpath)
            #开始获取LOG
            stability._startGetLog(reportpath)

            print("开始执行case...")
            suite.addTest(QuanChengSouSuoPinPaiTestCase("test_case"))
            runner.run(suite)

            #case执行完成后,kill idevicesyslog 进程
            stability._killIdevicelogPid()
            internal_case_count = internal_case_count + 1


        external_case_count = external_case_count + 1


    # ReportHandle().handle(reportpath)
    #
    # if sentMail:
    #     sendTestResultMail(reportpath, 'ios')


