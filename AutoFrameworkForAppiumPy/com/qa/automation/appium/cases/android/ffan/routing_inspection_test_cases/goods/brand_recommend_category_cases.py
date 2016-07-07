# -*- coding: utf-8 -*-

from __init__ import *

import time
import HTMLTestRunner

from unittest import TestCase
from unittest import TestLoader

from com.qa.automation.appium.pages.android.ffan.recommend_details_category_page import RecommendDetailsCategoryPage
from com.qa.automation.appium.pages.android.ffan.brand_category_page import BrandCategoryPage
from com.qa.automation.appium.cases.android.ffan.common.clear_app_data import ClearAppData
from com.qa.automation.appium.cases.android.ffan.common.test_prepare import TestPrepare
from com.qa.automation.appium.pages.android.ffan.dashboard_page import DashboardPage

from com.qa.automation.appium.configs.driver_configs import platformName_andr
from com.qa.automation.appium.configs.driver_configs import appActivity_ffan
from com.qa.automation.appium.configs.driver_configs import appPackage_ffan
from com.qa.automation.appium.configs.driver_configs import deviceName_andr
from com.qa.automation.appium.configs.driver_configs import platformVersion
from com.qa.automation.appium.configs.driver_configs import driver_url

from com.qa.automation.appium.driver.appium_driver import AppiumDriver
from com.qa.automation.appium.utility.logger import Logger


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
        self.driver = AppiumDriver(appPackage_ffan,
                                   appActivity_ffan,
                                   platformName_andr,
                                   platformVersion,
                                   deviceName_andr,
                                   driver_url).getDriver()

        #Login & update version
        TestPrepare(self , self.driver , self.logger).prepare()

    def test_case(self):
        recommendDetailsPage = RecommendDetailsCategoryPage(self, self.driver, self.logger)
        dashboardPage = DashboardPage(self , self.driver , self.logger)
        brandPage = BrandCategoryPage(self, self.driver, self.logger)

        # Load "推荐" page
        dashboardPage.validSelf()
        dashboardPage.clickOnBrandCategory()
        brandPage.validSelf()
        brandPage.clickOnRecommendDetails()
        recommendDetailsPage.validSelf()

        # Click “心形”
        recommendDetailsPage.clickOnSubsciber()
        recommendDetailsPage.clickBackKey()
        brandPage.clickOnRecommendDetails()
        recommendDetailsPage.validSelf()
        recommendDetailsPage.clickCancelSubsciber()
    

if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(BrandRecommendCatergoryCases)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = reportpath + 'Feifan_automation_test_report_' + now + '.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Feifan_automation_test_report',
                                           description='Result for test')
    runner.run(suite)