# -*- coding: utf-8 -*-

import os
import time
import HTMLTestRunner

from unittest import TestCase
from unittest import TestLoader

from pages.android.ffan.square_module_page import SquareModulePage
from pages.android.ffan.square_queue_page import SquareQueuePage
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
from cases.android.ffan.common.test_prepare import TestPrepare
from cases.logger import logger


class GuangChangPaiDuiTestCase(TestCase):
    '''
    回归用例： No.12
    用例名: 广场排队取号
    广场详情页点击排队取号进入排队取号页面，有取号的情况下点击立即取号，取号成功，可以取消排队
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

    def testGuangChangPaiDui(self):
        # 验证首页
        dashboardPage = DashboardPage(self, self.driver, self.logger)
        dashboardPage.validSelf()
        dashboardPage.screenShot("aiGuangJie")

        # 首页(爱逛街页面)点击搜索,通过搜索进入“北京通州万达广场”
        dashboardPage.clickOnSearchView()
        searchPage = SearchPage(self, self.driver, self.logger)
        searchPage.validSelf()
        searchPage.screenShot("souSuo")
        searchPage.inputText("北京通州万达广场")
        searchPage.screenShot("souSuo")
        searchPage.clickOnSearch()
        searchPage.screenShot("souSuoJieGuo")
        searchPage.clickOnSearchResultFirstItem()
        squarePage = SquareModulePage(self, self.driver, self.logger)
        squarePage.validSelf()
        squarePage.screenShot("guangChang")

        # 点击"排队取号"
        squarePage.clickOnQueue()
        queuePage = SquareQueuePage(self, self.driver, self.logger)
        queuePage.validSelf()
        queuePage.screenShot("paiDuiQuHao")

        # 如果可以取号，点击"取号"
        if (queuePage.validGetQueue()):
            queuePage.clickOnQueueNumber()
            queuePage.waitBySeconds(10)
            queuePage.inputNumberOfMeals()
            queuePage.clickOnGetQueueNumber()
            queuePage.validQueueSuccess()


if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(GuangChangPaiDuiTestCase)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = os.path.join(reportpath, 'Feifan_automation_test_report_' + now + '.html')
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Feifan_automation_test_report',
                                           description='Result for test')
    runner.run(suite)
