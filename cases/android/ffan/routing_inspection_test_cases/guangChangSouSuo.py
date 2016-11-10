# -*- coding: utf-8 -*-

import os
import time
import HTMLTestRunner

from unittest import TestCase
from unittest import TestLoader

from cases.android.ffan.common.clear_app_data import ClearAppData
from cases.android.ffan.common.test_prepare import TestPrepare
from pages.android.ffan.dashboard_page import DashboardPage
from pages.android.ffan.square_module_page import SquareModulePage
from pages.android.ffan.search_page import SearchPage
from pages.android.ffan.search_result_store_page import SearchResultStorePage
from configs.driver_configs import platformName_andr
from configs.driver_configs import appActivity_ffan
from configs.driver_configs import appPackage_ffan
from configs.driver_configs import deviceName_andr
from configs.driver_configs import driver_url
from driver.appium_driver import AppiumDriver
from utility.logger import Logger
from utility.device_info_util import DeviceInfoUtil
from cases.logger import logger


class GuangChangSouSuoTestCase(TestCase):
    '''
    巡检 No.22
    用例名 广场搜索
    首页进入广场详情页， 广场详情页点击搜索进入搜索，搜索服务和门店，有正常结果显示（广场维度）
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

        TestPrepare(self, self.driver, self.logger).prepare(False)

    def testGuangChangSouSuo(self):
        dashboardPage = DashboardPage(self, self.driver, self.logger)
        squareModulePage = SquareModulePage(self, self.driver, self.logger)
        searchPage = SearchPage(self, self.driver, self.logger)

        dashboardPage.validSelf()
        dashboardPage.screenShot("aiGuangJie")
        dashboardPage.clickOnSearchView()
        searchPage.validSelf()
        searchPage.screenShot("souSuo")
        searchPage.inputText("北京通州万达广场")
        searchPage.screenShot("souSuo")
        searchPage.waitBySeconds(10)
        searchPage.clickOnSearch()
        searchPage.waitBySeconds(10)
        searchPage.screenShot("souSuoJieGuo")
        searchPage.clickOnSearchResultFirstItem()
        squareModulePage.waitBySeconds(5)
        squareModulePage.validSelf()
        squareModulePage.screenShot("guangChang")
        squareModulePage.clickOnSearch()

        searchPage.validSelf()
        searchPage.screenShot("souSuo")
        searchPage.inputStoreName()
        searchPage.screenShot("shuRuMenDian")
        searchPage.clickOnSearch()
        searchPage.validSearchResult(u"通州", "//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/com.wanda.sliding.SlidingLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.FrameLayout[1]/android.widget.ListView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.TextView[1]")
        #tempText = searchPage.clickOnSearchResultFirstItem()
        searchPage.screenShot("souSuoJieGuo")
        searchPage.clickOnSearchResultFirstItem()

        searchResultStorePage = SearchResultStorePage(self, self.driver, self.logger)
        #searchResultStorePage.validKeywords(tempText)
        searchResultStorePage.validSelf()
        searchResultStorePage.screenShot("souSuoJieGuoXiangXi")
        searchResultStorePage.clickBackKey()
        searchResultStorePage.screenShot("guangChang")

        searchPage.clickBackKey()
        searchPage.screenShot("aiGuangJie")

if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(GuangChangSouSuoTestCase)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = os.path.join(reportpath, 'food-test_' + now + '.html')
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='food-test',
                                           description='Result for test')
    runner.run(suite)
