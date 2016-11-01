# -*- coding:utf-8 -*-

import os
import time
from unittest import TestCase
from unittest import TestLoader

import HTMLTestRunner

from cases.ios.ffan.common.clearAppData import ClearAppData
from cases.ios.ffan.common.testPrepare import TestPrepare
from configs.iosDriverConfig import IosDriverConfigs as IDC
from driver.appium_driver import AppiumDriver
from pages.ios.ffan.dashboard_page import DashboardPage
from pages.ios.ffan.hui_life_page import HuiLifePage
from utility.logger import Logger


class HuiShengHuoRuKouTestCase(TestCase):
    '''
    巡检checklist No.: 39
    自动化测试case No.: 39
    首页-慧生活，惠生活截图，基本入口检查
    '''

    def tearDown(self):
        self.reset.clearData()
        self.driver.quit()

    def setUp(self):
        self.logger = Logger()
        self.driver = AppiumDriver(None, None, IDC.platformName, IDC.platformVersion,
                                   IDC.deviceName, IDC.driverUrl, IDC.bundleId, IDC.udid).getDriver()
        self.reset = ClearAppData(self.driver)
        self.reset.clearData()
        TestPrepare(self, self.driver, self.logger).prepare(False)

    def test_case(self):
        dashboardPage = DashboardPage(self, self.driver, self.logger)
        dashboardPage.validSelf()
        dashboardPage.clickOnHuiLife()

        huiLifePage = HuiLifePage(self, self.driver, self.logger)
        huiLifePage.validSelf()
        #huiLifePage.screen_shot("hui_life_resource_niche")

        tempTuple = (u"火车票", u"加油", u"演唱会",u"股票资讯", u"违章查询")
        for tempNum in range(15):
            huiLifePage.clickOnAndValidByXpathAndName("//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[1]/UIAStaticText[%d]" % (tempNum + 1), tempTuple[tempNum])




if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(HuiShengHuoRuKouTestCase)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = os.path.join(reportpath, 'Feifan_automation_test_report_' + now + '.html')
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(fp, 'food-test', 'Result for test')
    runner.run(suite)
