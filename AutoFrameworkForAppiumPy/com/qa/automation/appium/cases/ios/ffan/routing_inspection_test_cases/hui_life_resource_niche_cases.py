# -*- coding:utf-8 -*-

import os
import time
from unittest import TestCase
from unittest import TestLoader

import HTMLTestRunner

from com.qa.automation.appium.cases.ios.ffan.common.clear_app_data import ClearAppData
from com.qa.automation.appium.cases.ios.ffan.common.test_prepare import TestPrepare
from com.qa.automation.appium.configs.ios_driver_configs import IosDriverConfigs as IDC
from com.qa.automation.appium.driver.appium_driver import AppiumDriver
from com.qa.automation.appium.pages.ios.ffan.dashboard_page import DashboardPage
from com.qa.automation.appium.pages.ios.ffan.hui_life_page import HuiLifePage
from com.qa.automation.appium.utility.logger import Logger


class HuiLifeResourceNicheCases(TestCase):
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

    def testHuiLifeScreenShot(self):
        dashboardPage = DashboardPage(self, self.driver, self.logger)
        dashboardPage.validSelf()
        dashboardPage.clickOnHuiLife()

        huiLifePage = HuiLifePage(self, self.driver, self.logger)
        huiLifePage.validSelf()
        huiLifePage.screen_shot("hui_life_resource_niche")

        tempTuple = (u"滴滴出行", u"滴滴出行", u"违章查询", u"自选股", u"首页",
                     u"话费充值", u"流量充值", u"QQ充值", u"数码回收", u"有料",
                     u"加油", u"演唱会", u"话剧", u"音乐会", u"亲子票务")
        for tempNum in range(15):
            huiLifePage.clickOnAndValidByXpathAndName("//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[1]/UIAStaticText[%d]" % (tempNum + 1), tempTuple[tempNum])
            huiLifePage.waitBySeconds()

if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(HuiLifeResourceNicheCases)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = reportpath + '/' + 'Hui_life_resource_niche_' + now + '.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Feifan_automation_test_report', description='Result for test')
    runner.run(suite)
