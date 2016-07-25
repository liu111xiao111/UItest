# -*- coding:utf-8 -*-

import os
import time
import HTMLTestRunner

from unittest import TestCase
from unittest import TestLoader

from com.qa.automation.appium.cases.ios.ffan.common.test_prepare import TestPrepare
from com.qa.automation.appium.cases.ios.ffan.common.clear_app_data import ClearAppData
from com.qa.automation.appium.configs.ios_driver_configs import IosDriverConfigs as IDC
from com.qa.automation.appium.driver.appium_driver import AppiumDriver
from com.qa.automation.appium.pages.ios.ffan.dashboard_page import DashboardPage
from com.qa.automation.appium.pages.ios.ffan.brand_category_page import BrandCategoryPage
from com.qa.automation.appium.pages.ios.ffan.recommend_details_category_page import RecommendDetailsCategoryPage
from com.qa.automation.appium.utility.logger import Logger


class BrandRecommendCatergoryCases(TestCase):
    '''
    作者 刘涛
    巡检checklist #8
    自动化测试 #8-1
    首页进入品牌简单浏览品牌中推荐和大牌的内容，点击验证是否可以进入详情页，显示是否正常，能否喜欢订阅
    '''

    def tearDown(self):
        self.reset.clearData()
        self.driver.quit()

    def setUp(self):
        self.logger = Logger()
        self.driver = AppiumDriver(None,
                                   None,
                                   IDC.platformName,
                                   IDC.platformVersion,
                                   IDC.deviceName,
                                   IDC.driverUrl,
                                   IDC.bundleId,
                                   IDC.udid).getDriver()

        self.reset = ClearAppData(self.driver)
        self.reset.clearData()

        testPrepare = TestPrepare(testcase = self , driver = self.driver , logger = self.logger)
        testPrepare.prepare()

    def test_case(self):
        dashboardPage = DashboardPage(testcase = self , driver = self.driver , logger = self.logger)
        brandPage = BrandCategoryPage(testcase = self, driver = self.driver, logger = self.logger)
        recommendDetailsPage = RecommendDetailsCategoryPage(self, self.driver, self.logger)

        # 首页点击品牌街
        dashboardPage.validSelf();
        dashboardPage.click_brand();
        brandPage.validSelf();

        # 首页点击推荐商品详细页
        brandPage.clickOnRecommendDetails()
        recommendDetailsPage.waitBySeconds(10)
        recommendDetailsPage.validSelf()

        # 点击 “心形”订阅
        recommendDetailsPage.waitBySeconds(10)
        originNumber = recommendDetailsPage.getSubsciberNumber()
        tempNumber = str(int(originNumber)+1)
        recommendDetailsPage.clickOnSubsciber()
        recommendDetailsPage.waitBySeconds(10)
        newNumber = recommendDetailsPage.getSubsciberNumber()
        recommendDetailsPage.validSelfSubsciberNumber(tempNumber, newNumber)

        # 取消订阅
        recommendDetailsPage.waitBySeconds(10)
        recommendDetailsPage.clickOnSubsciber()
        recommendDetailsPage.waitBySeconds(10)
        newCancelNumber = recommendDetailsPage.getSubsciberNumber()
        recommendDetailsPage.validSelfSubsciberNumber(originNumber, newCancelNumber)

if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(BrandRecommendCatergoryCases)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = reportpath + 'Feifan_automation_test_report_' + now + '.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Feifan_automation_test_report',
                                           description='Result for test')
    runner.run(suite)