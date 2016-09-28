# -*- coding: utf-8 -*-

import os
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
from com.qa.automation.appium.configs.driver_configs import driver_url
from com.qa.automation.appium.driver.appium_driver import AppiumDriver
from com.qa.automation.appium.utility.logger import Logger
from com.qa.automation.appium.utility.device_info_util import DeviceInfoUtil

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
        self.driver = AppiumDriver(appPackage_ffan,
                                   appActivity_ffan,
                                   platformName_andr,
                                   DeviceInfoUtil().getBuildVersion(),
                                   deviceName_andr,
                                   driver_url).getDriver()

        self.reset = ClearAppData(self.driver)
        self.reset.clearData()

        TestPrepare(self, self.driver, self.logger).prepare()

    def test_case(self):
        recommendDetailsPage = RecommendDetailsCategoryPage(self, self.driver, self.logger)
        dashboardPage = DashboardPage(self , self.driver , self.logger)
        brandPage = BrandCategoryPage(self, self.driver, self.logger)

        # Load "推荐" page
        dashboardPage.validSelf()
        dashboardPage.clickOnBrandCategory()
        brandPage.validSelf()
        brandPage.waitBySeconds(10)
        brandPage.clickOnRecommendDetails()
        recommendDetailsPage.validSelf()
        recommendDetailsPage.waitBySeconds(5)

        # Click “心形”
        '''recommendDetailsPage.clickOnSubsciber()
        recommendDetailsPage.waitBySeconds(3)
        recommendDetailsPage.validSelfSubsciberLike()
        recommendDetailsPage.clickCancelSubsciber()
        recommendDetailsPage.waitBySeconds(3)
        recommendDetailsPage.validSelfSubsciberUnlike()'''


if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(BrandRecommendCatergoryCases)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = os.path.join(reportpath, 'Feifan_automation_test_report_' + now + '.html')
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Feifan_automation_test_report',
                                           description='Result for test')
    runner.run(suite)