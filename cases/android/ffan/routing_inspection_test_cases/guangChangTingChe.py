# -*- coding: utf-8 -*-

import os
import time
import HTMLTestRunner

from unittest import TestCase
from unittest import TestLoader

# from pages.android.ffan.my_ffan_my_parking_payment_page import MyFfanMyParkingPaymentPage
from pages.android.ffan.parking_category_page import ParkingCategoryPage
from pages.android.ffan.square_module_page import SquareModulePage
from cases.android.ffan.common.test_prepare import TestPrepare
from pages.android.ffan.dashboard_page import DashboardPage
from pages.android.ffan.search_page import SearchPage
from configs.driver_configs import platformName_andr
from configs.driver_configs import appActivity_ffan
from configs.driver_configs import appPackage_ffan
from configs.driver_configs import deviceName_andr
from configs.driver_configs import driver_url
from driver.appium_driver import AppiumDriver
from utility.logger import Logger
from utility.device_info_util import DeviceInfoUtil
from cases.logger import logger


class GuangChangTingCheTestCase(TestCase):
    '''
    回归用例： No.14
    用例名: 广场停车
    广场详情页点击停车，正常进入停车模块 
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
        TestPrepare(self, self.driver, self.logger).prepare()

    def testGuangChangTingChe(self):
        # 验证首页
        dashboardPage = DashboardPage(self, self.driver, self.logger)
        dashboardPage.validSelf()
        dashboardPage.screenShot("aiGuangJie")

        # 首页(爱逛街页面)点击搜索,通过搜索进入“北京通州万达广场”
        dashboardPage.clickOnSearchAll()
        searchPage = SearchPage(self, self.driver, self.logger)
        searchPage.validSelf()
        searchPage.screenShot("souSuo")
        searchPage.inputKeywords(u"北京通州万达广场")
        searchPage.screenShot("souSuo")
        searchPage.clickOnSearch()
        searchPage.screenShot("souSuoJieGuo")
        searchPage.clickOnSearchResultFirstItem()
        squareModulePage = SquareModulePage(self, self.driver, self.logger)
        squareModulePage.validSelf()
        squareModulePage.screenShot("guangChang")

        # 点击停车 
        squareModulePage.clickOnParking()
        parkingPage = ParkingCategoryPage(self, self.driver, self.logger)
        parkingPage.waitBySeconds(5)
        parkingPage.validSelf()


if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(GuangChangTingCheTestCase)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = os.path.join(reportpath, 'food-test_' + now + '.html')
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='food-test',
                                           description='Result for test')
    runner.run(suite)
