# -*- coding: utf-8 -*-

import os
import time
import HTMLTestRunner

from unittest import TestCase
from unittest import TestLoader

from com.qa.automation.appium.cases.android.ffan.common.clear_app_data import ClearAppData
from com.qa.automation.appium.cases.android.ffan.common.test_prepare import TestPrepare
from com.qa.automation.appium.configs.driver_configs import appActivity_ffan
from com.qa.automation.appium.configs.driver_configs import appPackage_ffan
from com.qa.automation.appium.configs.driver_configs import deviceName_andr
from com.qa.automation.appium.configs.driver_configs import driver_url
from com.qa.automation.appium.configs.driver_configs import platformName_andr
from com.qa.automation.appium.driver.appium_driver import AppiumDriver
from com.qa.automation.appium.pages.android.ffan.dashboard_page import DashboardPage
from com.qa.automation.appium.pages.android.ffan.search_page import SearchPage
from com.qa.automation.appium.pages.android.ffan.store_info_page import StoreInfoPage
from com.qa.automation.appium.pages.android.ffan.search_result_store_page import SearchResultStorePage
from com.qa.automation.appium.utility.logger import Logger
from com.qa.automation.appium.utility.device_info_util import DeviceInfoUtil


class HotWordSearchCases(TestCase):
    '''
    巡检checklist No.: 04
    自动化测试case No.: 04
    查看搜索中的热词并点击，热词显示正常点击进入内容无误
    '''

    def tearDown(self):
        self.reset.clearData()
        self.driver.quit()

    def setUp(self):
        self.logger = Logger()
        self.platVersion = DeviceInfoUtil().getBuildVersion()
        self.driver = AppiumDriver(appPackage_ffan,
                                   appActivity_ffan,
                                   platformName_andr,
                                   self.platVersion, 
                                   deviceName_andr,
                                   driver_url).getDriver()

        self.reset = ClearAppData(self.driver)
        self.reset.clearData()

        TestPrepare(self, self.driver, self.logger).prepare(False)

    def test_case(self):
        dashboardPage = DashboardPage(self, self.driver, self.logger)
        searchResultStorePage = SearchResultStorePage(self, self.driver, self.logger)
        storeInfoPage = StoreInfoPage(self, self.driver, self.logger)
        dashboardPage.validSelf()
        dashboardPage.clickOnSearchAll()

        searchPage = SearchPage(self, self.driver, self.logger)
        searchPage.waitBySeconds(10)
        searchPage.validSelf()
        '''searchPage.clickOnMovie()
        searchPage.validSearchResult(u"电影", "//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/com.wanda.sliding.SlidingLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.FrameLayout[1]/android.widget.ListView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.TextView[1]")
        searchPage.clickOnSpecificMovie()

        storeInfoPage = StoreInfoPage(self, self.driver, self.logger)
        storeInfoPage.waitBySeconds(10)
        storeInfoPage.validSelf()
        storeInfoPage.clickBackKey()

        searchPage.clickBackKey()'''

        # 点击热词“百货”
        searchPage.clickOnShoppingMall()
        searchResultStorePage.waitBySeconds(10)
        # 获取检索热词的结果列表长度
        length = searchPage.getHotWordListLength()
        searchResultStorePage.validHotWords(length)
        # 获取检索热词的结果列表第一项条目标题
        '''item = searchResultStorePage.getShoppingMallListItemTitle()
        if int(self.platVersion.split(".")[0]) < 5:
            item = item + " Link"
        searchResultStorePage.clickOnShoppingMallItem()
        storeInfoPage.waitBySeconds(30)
        storeInfoPage.validHotWordTitle(item)'''


if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(HotWordSearchCases)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = os.path.join(reportpath, 'Feifan_automation_test_report_' + now + '.html')
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Feifan_automation_test_report', description='Result for test')
    runner.run(suite)
