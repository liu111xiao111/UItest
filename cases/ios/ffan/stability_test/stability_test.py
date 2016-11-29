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
from cases.ios.ffan.routing_inspection_test_cases.gouWuZhongXin import GouWuZhongXinTestCase
from cases.ios.ffan.routing_inspection_test_cases.guangChangMaiDan import GuangChangMaiDanTestCase
from cases.ios.ffan.routing_inspection_test_cases.guangChangMeiShiHui import GuangChangMeiShiHuiTestCase
from cases.ios.ffan.routing_inspection_test_cases.guangChangSouSuo import GuangChangSouSuoTestCase
from cases.ios.ffan.routing_inspection_test_cases.guangChangTingChe import GuangChangTingCheTestCase
from cases.ios.ffan.routing_inspection_test_cases.guangChangZhaoDian import GuangChangZhaoDianTestCase
from cases.ios.ffan.routing_inspection_test_cases.paiDuiQuHao import PaiDuiQuHaoTestCase
from cases.ios.ffan.routing_inspection_test_cases.quanChengSouSuoMenDian import QuanChengSouSuoMenDianTestCase
from cases.ios.ffan.routing_inspection_test_cases.quanChengSouSuoPinPai import QuanChengSouSuoPinPaiTestCase
from cases.ios.ffan.routing_inspection_test_cases.quanChengSouSuoShangPin import QuanChengSouSuoShangPinTestCase
from cases.ios.ffan.routing_inspection_test_cases.woDeDengLu import WoDeDengLuTestCase
from cases.ios.ffan.routing_inspection_test_cases.woDeTuiChu import WoDeTuiChuTestCase

from utility.mailProcess import sendTestResultMail

class Stability(object):
    pidList = []

    #总循环次数
    ALLCASE_LOOP_TIMES = 2;
    #每个case循环次数
    CASE_LOOP_TIMES = 10;

    COMMAND = "idevicesyslog"

    def __init__(self):
        pass


    def _saveLog(self,logpath=""):
        print('BEGIN get iOS log')
        '''
        保存log到回归测试目录
        :return:
        '''
        logcatFile = "/Users/auto/Desktop/testlog.txt"
        command = "%s > %s" % (self.COMMAND, logcatFile)
        os.system(command)
        print('DEBUG GET LOE END!')


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
            print(pid)


if __name__ == "__main__":
    stability = Stability()
    # Stability()._saveLog()
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

    reportpath = "%s/stability/%s/%s/" % ("/Users/auto/workspace_pycharm/autotest", time.strftime("%Y%m%d"), build_num)

    if not os.path.exists(reportpath):
        os.makedirs(reportpath)

    suite = unittest.TestSuite()
    runner = suite.TextTestRunner()

    suite.addTest(QuanChengSouSuoPinPaiTestCase("test_case"))
    # suite.addTest(QuanChengSouSuoShangPinTestCase("test_case"))
    # suite.addTest(QuanChengSouSuoMenDianTestCase("test_case"))
    # suite.addTest(GouWuZhongXinTestCase("test_case"))
    # suite.addTest(GuangChangSouSuoTestCase("test_case"))
    # suite.addTest(GuangChangZhaoDianTestCase("test_case"))
    # suite.addTest(PaiDuiQuHaoTestCase("test_case"))
    # suite.addTest(GuangChangTingCheTestCase("test_case"))
    # suite.addTest(GuangChangMaiDanTestCase("test_case"))
    # suite.addTest(GuangChangMeiShiHuiTestCase("test_case"))
    # suite.addTest(WoDeDengLuTestCase("test_case"))
    # suite.addTest(WoDeTuiChuTestCase("test_case"))


    # now = time.strftime('%H_%M_%S')

    # filename = reportpath + 'feifan_automation_test_report_ios.html'
    # fp = open(filename, 'wb')
    # runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Feifan_automation_test_report_ios',
    #                                        description='Result for test')

    #循环次数计数
    all_case_count = 0

    while(all_case_count < stability.ALLCASE_LOOP_TIMES):
        #print("all case 执行 %s 次 " % all_case_count)

        runner.run(suite)

        all_case_count = all_case_count + 1


    # ReportHandle().handle(reportpath)
    #
    # if sentMail:
    #     sendTestResultMail(reportpath, 'ios')


