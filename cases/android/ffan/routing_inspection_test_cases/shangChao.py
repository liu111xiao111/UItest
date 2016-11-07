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
from pages.android.ffan.supermarket_page import SupermarketPage
from utility.device_info_util import DeviceInfoUtil
from utility.logger import Logger

TESTCITY = u"厦门市"
DESCITY = u"北京市"

class ShangChaoTestCase(TestCase):
    '''
    巡检 No.11
    用例名: 商超
    有便利店的城市显示商超,点击进入商超列表
    '''

    def tearDown(self):
        self.reset.clearData()
        self.driver.quit()

    def setUp(self):
        self.logger = Logger()
        self.driver = AppiumDriver(appPackage_ffan,
                                   appActivity_ffan,
                                   platformName_andr,
                                   DeviceInfoUtil().getBuildVersion(),
                                   deviceName_andr,
                                   driver_url).getDriver()

        self.reset = ClearAppData(self.driver)
        self.reset.clearData()

        TestPrepare(self, self.driver, self.logger).prepare(False)

    def testShangChao(self):
        dashboardPage = DashboardPage(self, self.driver, self.logger)
        supermarketPage = SupermarketPage(self, self.driver, self.logger)

        # 切换到测试城市（厦门市）
        dashboardPage.validSelf()
        '''tempCityName = dashboardPage.getCityName()
        if tempCityName != TESTCITY:
            dashboardPage.clickOnSwithCith()
            dashboardPage.switchCity(TESTCITY)'''

        # 点击商超，进入商店超市页面
        dashboardPage.clickOnSupermarket()
        supermarketPage.validSelf()
        '''supermarketPage.clickBackKey()
        dashboardPage.clickOnSwithCith()
        dashboardPage.switchCity(DESCITY)'''


if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(ShangChaoTestCase)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = os.path.join(reportpath, 'Feifan_automation_test_report_' + now + '.html')
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Feifan_automation_test_report',
                                           description='Result for test')
    runner.run(suite)