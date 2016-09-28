# -*- coding:utf-8 -*-

import os
import time
from unittest import TestCase
from unittest import TestLoader

import HTMLTestRunner

from cases.android.ffan.common.clear_app_data import ClearAppData
from cases.android.ffan.common.test_prepare import TestPrepare
from configs.driver_configs import appActivity_ffan
from configs.driver_configs import appPackage_ffan
from configs.driver_configs import deviceName_andr
from configs.driver_configs import driver_url
from configs.driver_configs import platformName_andr
from driver.appium_driver import AppiumDriver
from pages.android.ffan.dashboard_page import DashboardPage
from pages.android.ffan.hui_life_page import HuiLifePage
from utility.device_info_util import DeviceInfoUtil
from utility.logger import Logger


class HuiShengHuoTestCase(TestCase):
    '''
    巡检 No.38
    用例名: 惠生活
    首页-慧生活，惠生活截图，基本入口检查
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

    def testHuiShenghuo(self):
        dashboardPage = DashboardPage(self, self.driver, self.logger)
        dashboardPage.validSelf()
        dashboardPage.clickOnSmartLife()

        huiLifePage = HuiLifePage(self, self.driver, self.logger)
        huiLifePage.validSelf()
        huiLifePage.screenShot("hui_life_resource_niche")

        tempTuple = (u"火车票", u"滴滴出行", u"滴滴出行", u"加油 Heading", u"数码回收",
                     u"演唱会", u"亲子票务", u"自选股", u"有料", u"违章查询")
        for tempNum in range(10):
            huiLifePage.clickOnAndValidByXpathAndName("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.support.v4.widget.DrawerLayout[1]/android.widget.RelativeLayout[1]/android.support.v4.view.ViewPager[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.View[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.support.v4.view.ViewPager[1]/android.widget.LinearLayout[1]/android.widget.GridView[1]/android.widget.RelativeLayout[%d]" % (tempNum + 1), tempTuple[tempNum])
            huiLifePage.waitBySeconds(10)

if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(HuiShengHuoTestCase)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = os.path.join(reportpath, 'Feifan_automation_test_report_' + now + '.html')
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Feifan_automation_test_report', description='Result for test')
    runner.run(suite)
