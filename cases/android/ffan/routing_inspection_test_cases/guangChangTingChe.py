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
    巡检 No.29
    用例名: 广场停车
    点击停车缴费，成功进入并显示正确数据
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
        dashboardPage = DashboardPage(self, self.driver, self.logger)
        dashboardPage.validSelf()
        dashboardPage.screenShot("aiGuangJie")
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
        squareModulePage.clickOnParking()

        parkingPage = ParkingCategoryPage(self, self.driver, self.logger)
#         parkingPaymentPage = MyFfanMyParkingPaymentPage(testcase=self, driver=self.driver, logger=self.logger)
        parkingPage.waitBySeconds(5)
        parkingPage.validSelf()
        '''parkingPage.screenShot("tingChe")
        # 检查入口项目
        itemList = (u"停车找车", u"附近停车场", u"停车券", u"停车记录", u"帮助")
        titleList = (u"停车找车", u"停车场列表", u"停车优惠券", u"停车记录", u"停车帮助")
        for i in range(len(titleList)):
            parkingPaymentPage.clickAndValidItems(itemList[i], titleList[i])
            parkingPaymentPage.waitBySeconds(10)'''

if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(GuangChangTingCheTestCase)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = os.path.join(reportpath, 'food-test_' + now + '.html')
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='food-test',
                                           description='Result for test')
    runner.run(suite)
