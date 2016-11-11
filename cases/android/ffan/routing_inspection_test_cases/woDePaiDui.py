# -*- coding: utf-8 -*-

import os
import time
import HTMLTestRunner

from unittest import TestCase
from unittest import TestLoader

from pages.android.ffan.my_ffan_my_queue_page import MyFfanMyQueuePage
from pages.android.ffan.dashboard_page import DashboardPage
from pages.android.ffan.square_queue_page import SquareQueuePage
from pages.android.ffan.square_module_page import SquareModulePage
from pages.android.ffan.search_page import SearchPage
from pages.android.ffan.my_ffan_page import MyFfanPage
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
from cases.logger import logger


class WoDePaiDuiTestCase(TestCase):
    '''
    巡检 No.58
    用例名 我的排队
    点击我的排队，成功进入并显示正确数据
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
        logger.info("Appium client init completed")

        self.reset = ClearAppData(self.driver)
        self.reset.clearData()
        logger.info("Clear data completed")

        TestPrepare(self, self.driver, self.logger).prepare()

    def testWoDePaiDui(self):
        dashboardPage = DashboardPage(self, self.driver, self.logger)
        myFfanPage = MyFfanPage(self, self.driver, self.logger)
        myQueuePage = MyFfanMyQueuePage(self, self.driver, self.logger)
        queuePage = SquareQueuePage(self, self.driver, self.logger)
        squarePage = SquareModulePage(self, self.driver, self.logger)
        searchPage = SearchPage(self, self.driver, self.logger)

        # Load square page
        dashboardPage.validSelf()
        dashboardPage.screenShot("aiGuangJie")
        dashboardPage.clickOnSearchView()
        searchPage.validSelf()
        searchPage.screenShot("souSuo")
        searchPage.inputText("北京通州万达广场")
        searchPage.screenShot("souSuo")
        searchPage.clickOnSearch()
        searchPage.waitBySeconds(5)
        searchPage.screenShot("souSuoJieGuo")
        searchPage.clickOnSearchResultFirstItem()
        squarePage.validSelf()
        squarePage.screenShot("guangChang")

        # Click "排队取号"， load "排队取号" page.
        squarePage.clicOnQueue()
        queuePage.validSelf()
        queuePage.screenShot("paiDuiQuHao")

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
    suite = TestLoader().loadTestsFromTestCase(WoDePaiDuiTestCase)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = os.path.join(reportpath, 'Feifan_automation_test_report_' + now + '.html')
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Feifan_automation_test_report',
                                           description='Result for test')
    runner.run(suite)