# -*- coding: utf-8 -*-

import os
import time
import HTMLTestRunner

from unittest import TestCase
from unittest import TestLoader

from pages.android.ffan.my_ffan_my_queue_page import MyFfanMyQueuePage
from pages.android.ffan.square_module_page import SquareModulePage
from pages.android.ffan.square_queue_page import SquareQueuePage
from pages.android.ffan.dashboard_page import DashboardPage
from pages.android.ffan.my_ffan_page import MyFfanPage
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
from cases.android.ffan.common.clear_app_data import ClearAppData


class GuangChangPaiDuiTestCase(TestCase):
    '''
    巡检 No.27
    用例名: 广场排队取号
    广场详情页点击排队取号进入排队取号页面，可以成功排队
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

        TestPrepare(self, self.driver, self.logger).prepare()

    def testGuangChangPaiDui(self):
        myQueuePage = MyFfanMyQueuePage(self, self.driver, self.logger)
        myFfanPage = MyFfanPage(self, self.driver, self.logger)
        dashboardPage = DashboardPage(self, self.driver, self.logger)
        squarePage = SquareModulePage(self, self.driver, self.logger)
        queuePage = SquareQueuePage(self, self.driver, self.logger)
        searchPage = SearchPage(self, self.driver, self.logger)

        # Load square page
        dashboardPage.validSelf()
        dashboardPage.clickOnSearchView()
        searchPage.validSelf()
        searchPage.inputText("北京通州万达广场")
        searchPage.clickOnSearch()
        searchPage.clickOnSearchResultFirstItem()
        squarePage.validSelf()

        # Click "排队取号"， load "排队取号" page.
        squarePage.clicOnQueue()
        queuePage.validSelf()

        # Click "取号"
        if (queuePage.validGetQueue()):
            queuePage.clicOnQueueNumber()
            queuePage.waitBySeconds(10)
            queuePage.inputNumberOfMeals()
            queuePage.clicOnGetQueueNumber()
            queuePage.validQueueSuccess()

            for _ in range(3):
                queuePage.clickBackKey()

            dashboardPage.clickOnMy()
            myFfanPage.validSelf()
            myFfanPage.clickOnMyQueue()
            myQueuePage.validSelf()
            myQueuePage.clickOnCancelQueue()

if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(GuangChangPaiDuiTestCase)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = os.path.join(reportpath, 'Feifan_automation_test_report_' + now + '.html')
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Feifan_automation_test_report',
                                           description='Result for test')
    runner.run(suite)
