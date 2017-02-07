# -*- coding: utf-8 -*-

import os
import time
import HTMLTestRunner

from unittest import TestCase
from unittest import TestLoader

from cases.android.ffan.common.test_prepare import TestPrepare
from configs.driver_configs import appActivity_ffan
from configs.driver_configs import appPackage_ffan
from configs.driver_configs import deviceName_andr
from configs.driver_configs import driver_url
from configs.driver_configs import platformName_andr
from driver.appium_driver import AppiumDriver
from pages.android.ffan.dashboard_page import DashboardPage
from pages.android.ffan.search_page import SearchPage
from pages.android.ffan.search_result_store_page import SearchResultStorePage
from utility.logger import Logger
from utility.device_info_util import DeviceInfoUtil
from cases.logger import logger


class ReCiSouSuoTestCase(TestCase):
    '''
    回归用例： No.3
    用例名: 热词搜索
    查看搜索中的热词并点击，热词显示正常点击进入内容无误
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

    def testReCiSouSuo(self):
        # 验证首页
        dashboardPage = DashboardPage(self, self.driver, self.logger)
        dashboardPage.validSelf()
        dashboardPage.screenShot("aiGuangJie")

        # 首页(爱逛街页面)点击搜索，并验证搜索页面
        dashboardPage.clickOnSearchAll()
        searchPage = SearchPage(self, self.driver, self.logger)
        searchPage.waitBySeconds(5)
        searchPage.validSelf()
        searchPage.screenShot("souSuo")

        # 点击热词“百货”，并验证搜索结果
        searchPage.clickOnShoppingMall()
        searchResultStorePage = SearchResultStorePage(self, self.driver, self.logger)
        searchResultStorePage.waitBySeconds(5)
        length = searchPage.getHotWordListLength()
        searchResultStorePage.validHotWords(length)
        searchResultStorePage.screenShot("reChiJianSuoJieGuo")


if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(ReCiSouSuoTestCase)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = os.path.join(reportpath, 'Feifan_automation_test_report_' + now + '.html')
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Feifan_automation_test_report', description='Result for test')
    runner.run(suite)
