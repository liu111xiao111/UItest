# -*- coding:utf-8 -*-

import os
import time
from unittest import TestCase
from unittest import TestLoader

import HTMLTestRunner

from com.qa.automation.appium.cases.android.ffan.common.clear_app_data import ClearAppData
from com.qa.automation.appium.cases.android.ffan.common.test_prepare import TestPrepare
from com.qa.automation.appium.configs.driver_configs import appActivity_ffan
from com.qa.automation.appium.configs.driver_configs import appPackage_ffan
from com.qa.automation.appium.configs.driver_configs import deviceName_andr
from com.qa.automation.appium.configs.driver_configs import driver_url
from com.qa.automation.appium.configs.driver_configs import platformName_andr
from com.qa.automation.appium.driver.appium_driver import AppiumDriver
from com.qa.automation.appium.pages.android.ffan.dashboard_page import DashboardPage
from com.qa.automation.appium.pages.android.ffan.hui_life_page import HuiLifePage
from com.qa.automation.appium.utility.device_info_util import DeviceInfoUtil
from com.qa.automation.appium.utility.logger import Logger


class HuiLifeEntranceCases(TestCase):
    '''
    作者 乔佳溪
    巡检checklist No.: 39
    自动化测试case No.: 39
    首页-慧生活，进入各个功能球入口查看相应功能
    '''

    def tearDown(self):
        self.reset.clearData()
        self.driver.quit()

    def setUp(self):
        self.logger = Logger()
        self.driver = AppiumDriver(appPackage_ffan, appActivity_ffan, platformName_andr,
                                   DeviceInfoUtil().getBuildVersion(), deviceName_andr,
                                   driver_url).getDriver()
        self.reset = ClearAppData(self.driver)
        self.reset.clearData()
        TestPrepare(self, self.driver, self.logger).prepare()

    def test_case(self):
        dashboardPage = DashboardPage(self, self.driver, self.logger)
        dashboardPage.validSelf()
        dashboardPage.clickOnSmartLife()

        huiLifePage = HuiLifePage(self, self.driver, self.logger)
        huiLifePage.validSelf()
        #huiLifePage.screenShot("hui_life_resource_niche")

        tempTuple = (u"火车票", u"滴滴出行", u"滴滴出行", u"加油 Heading", u"数码回收",
                     u"演唱会", u"亲子票务", u"自选股", u"违章查询", u"有料")
        for tempNum in range(10):
            huiLifePage.clickOnAndValidByXpathAndName("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.support.v4.widget.DrawerLayout[1]/android.widget.RelativeLayout[1]/android.support.v4.view.ViewPager[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.View[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.support.v4.view.ViewPager[1]/android.widget.LinearLayout[1]/android.widget.GridView[1]/android.widget.RelativeLayout[%d]" % (tempNum + 1), tempTuple[tempNum])
            huiLifePage.waitBySeconds(10)

if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(HuiLifeEntranceCases)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = os.path.join(reportpath, 'Hui_life_resource_niche_' + now + '.html')
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Feifan_automation_test_report', description='Result for test')
    runner.run(suite)
