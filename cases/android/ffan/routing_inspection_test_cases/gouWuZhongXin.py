# -*- coding:utf-8 -*-

import os
import time
import HTMLTestRunner

from unittest import TestCase
from unittest import TestLoader

from cases.android.ffan.common.test_prepare import TestPrepare
from pages.android.ffan.shopping_mall_page import ShoppingMallPage
from pages.android.ffan.dashboard_page import DashboardPage
from configs.driver_configs import platformName_andr
from configs.driver_configs import appActivity_ffan
from configs.driver_configs import appPackage_ffan
from configs.driver_configs import deviceName_andr
from configs.driver_configs import driver_url
from driver.appium_driver import AppiumDriver
from utility.logger import Logger
from utility.device_info_util import DeviceInfoUtil
from cases.logger import logger


class GouWuZhongXinTestCase(TestCase):
    '''
    作者 乔佳溪
    巡检checklist No.: 05
    自动化测试case No.: 05
    爱逛街进入购物中心确认广场距离排序顺序以及广场信息
    '''
    @classmethod
    def setUpClass(cls):
        '''
        初始化Appium driver
        '''
        cls.driver = AppiumDriver(appPackage_ffan,
                                   appActivity_ffan,
                                   platformName_andr,
                                   DeviceInfoUtil().getBuildVersion(),
                                   deviceName_andr,
                                   driver_url).getDriver()
        logger.info("Appium client init completed")

    def tearDown(self):
        self.driver.quit()

    def setUp(self):
        self.logger = Logger()
        TestPrepare(self, self.driver, self.logger).prepare(False)

    def testGouWuZhongXin(self):
        dashboardPage = DashboardPage(self, self.driver, self.logger)
        shoppingMallPage = ShoppingMallPage(self, self.driver, self.logger)

        # Verify Home Page
        dashboardPage.validSelf()
        dashboardPage.screenShot("aiGuangJie")

        # Enter Shopping Mall Page and Verify
        dashboardPage.clickOnShoppingMall()
        shoppingMallPage.validSelf()
        shoppingMallPage.screenShot("gouWuZhongXin")

        tabNumberList = (1,    # Total
                         2,    # Mall
                         3)    # Department
        for tabNumber in tabNumberList:
            shoppingMallPage.clickOnTab(tabNumber)
            shoppingMallPage.validListView()
            shoppingMallPage.validDistance()
            shoppingMallPage.screenShot("gouWuZhongXinXiangXi")

if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(GouWuZhongXinTestCase)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = os.path.join(reportpath, 'Feifan_automation_test_report_' + now + '.html')
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Feifan_automation_test_report',
                                           description='Result for test')
    runner.run(suite)
