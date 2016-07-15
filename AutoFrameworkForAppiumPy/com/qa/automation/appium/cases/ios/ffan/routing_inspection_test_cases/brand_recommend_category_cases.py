# -*- coding:utf-8 -*-

import os
import sys
import time

sys.path.append(os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))))

from com.qa.automation.appium.cases.android.ffan.common.clear_app_data import ClearAppData
from com.qa.automation.appium.configs.ios_driver_configs import IosDriverConfigs as IDC
from com.qa.automation.appium.driver.appium_driver import AppiumDriver
from com.qa.automation.appium.pages.ios.ffan.dashboard_page import DashboardPage
from com.qa.automation.appium.pages.ios.ffan.brand_category_page import BrandCategoryPage
from com.qa.automation.appium.pages.ios.ffan.recommend_details_category_page import RecommendDetailsCategoryPage
from com.qa.automation.appium.utility.logger import Logger

from unittest import TestCase
from unittest import TestLoader
import HTMLTestRunner


class BrandRecommendCatergoryCases(TestCase):
    '''
        巡检checklist #8
        自动化测试 #8-1
        首页进入品牌简单浏览品牌中推荐和大牌的内容，点击验证是否可以进入详情页，显示是否正常，能否喜欢订阅
    '''

    def tearDown(self):
        self.driver.quit()
        ClearAppData().clearData()

    def setUp(self):
        ClearAppData().clearData()
        self.logger = Logger()
        self.driver = AppiumDriver(None, None, IDC.platformName, IDC.platformVersion,
                                   IDC.deviceName, IDC.driverUrl, IDC.bundleId, IDC.udid).getDriver()

    def test_case(self):
        dashboardPage = DashboardPage(testcase = self , driver = self.driver , logger = self.logger)
        brandPage = BrandCategoryPage(testcase = self, driver = self.driver, logger = self.logger)
        recommendDetailsPage = RecommendDetailsCategoryPage(self, self.driver, self.logger)

        # 首页点击品牌街
        dashboardPage.validSelf();
        dashboardPage.click_brand()
        brandPage.validSelf();

        # 首页点击推荐商品详细页
        brandPage.clickOnRecommendDetails()
        recommendDetailsPage.waitBySeconds(10)
        recommendDetailsPage.validSelf()

        # 点击 “心形”订阅
        orifinalNumber = recommendDetailsPage.getSubsciberNumber()
        recommendDetailsPage.clickOnSubsciber()
        newNumber = recommendDetailsPage.getSubsciberNumber()
        recommendDetailsPage.validSelfSubsciberNumber(orifinalNumber, newNumber+1)

        # 取消订阅
        '''recommendDetailsPage.clickOnSubsciber()
        newCancelNumber = recommendDetailsPage.getSubsciberNumber()
        recommendDetailsPage.validSelfSubsciberNumber(orifinalNumber, newCancelNumber)'''

if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(BrandRecommendCatergoryCases)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = reportpath + 'Feifan_automation_test_report_' + now + '.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Feifan_automation_test_report',
                                           description='Result for test')
    runner.run(suite)