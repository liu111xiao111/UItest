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
    回归用例： No.4
    用例名: 购物中心
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
        # 验证首页
        dashboardPage = DashboardPage(self, self.driver, self.logger)
        dashboardPage.validSelf()
        dashboardPage.screenShot("aiGuangJie")

        # 首页(爱逛街页面)进入购物中心，查看广场距离排序及广场信息
        dashboardPage.clickOnShoppingMall()
        shoppingMallPage = ShoppingMallPage(self, self.driver, self.logger)
        shoppingMallPage.validSelf()
        shoppingMallPage.screenShot("gouWuZhongXin")
        tabNumberList = (1,    # 全部tab
                         2,    # 购物中心tab
                         3)    # 百货tab
        for tabNumber in tabNumberList:
            shoppingMallPage.clickOnTab(tabNumber)
            shoppingMallPage.validDistance()
            shoppingMallPage.validSquareInfo(tabNumber)
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
