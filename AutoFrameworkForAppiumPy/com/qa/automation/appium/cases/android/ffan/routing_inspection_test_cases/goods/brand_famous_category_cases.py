# -*- coding: utf-8 -*-

import sys,os
import time

sys.path.append(os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))))

from com.qa.automation.appium.cases.android.ffan.common.test_prepare import TestPrepare
from com.qa.automation.appium.cases.android.ffan.common.clear_app_data import ClearAppData
from com.qa.automation.appium.pages.android.ffan.dashboard_page import DashboardPage;
from com.qa.automation.appium.pages.android.ffan.brand_category_page import BrandCategoryPage;
from com.qa.automation.appium.pages.android.ffan.famous_details_category_page import FamousDetailsCategoryPage;
from com.qa.automation.appium.configs.driver_configs import appActivity_ffan
from com.qa.automation.appium.configs.driver_configs import appPackage_ffan
from com.qa.automation.appium.configs.driver_configs import deviceName_andr
from com.qa.automation.appium.configs.driver_configs import driver_url
from com.qa.automation.appium.configs.driver_configs import platformName_andr
from com.qa.automation.appium.configs.driver_configs import platformVersion
from com.qa.automation.appium.driver.appium_driver import AppiumDriver
from com.qa.automation.appium.utility.logger import Logger;

import unittest
import HTMLTestRunner


class BrandFamousCatergoryCases(unittest.TestCase):
    '''
        巡检checklist #8
        自动化测试 #8-2
        首页进入品牌简单浏览品牌中推荐和大牌的内容，点击验证是否可以进入详情页，显示是否正常，能否喜欢订阅
    '''

    def tearDown(self):
        self.driver.quit()
        
        clearAppData = ClearAppData()
        clearAppData.clearData()

    def setUp(self):
        clearAppData = ClearAppData()
        clearAppData.clearData()

        self.logger = Logger()
        self.driver = AppiumDriver(app_package=appPackage_ffan, app_activity=appActivity_ffan,
                                   platform_name=platformName_andr, platform_version=platformVersion,
                                   device_name=deviceName_andr, driver_url=driver_url
                                   ).getDriver()

        #Login & update version
        testPrepare = TestPrepare(testcase = self , driver = self.driver , logger = self.logger)
        testPrepare.prepare(False)

    def test_case(self):
        dashboardPage = DashboardPage(testcase = self , driver = self.driver , logger = self.logger)
        brandPage = BrandCategoryPage(testcase = self, driver = self.driver, logger = self.logger)
        famousDetailsPage = FamousDetailsCategoryPage(testcase = self, driver = self.driver, logger = self.logger)

        # Load "推荐" page
        dashboardPage.validSelf();
        dashboardPage.clickOnBrandCategory()
        brandPage.validSelf();

        # Click "大牌"
        brandPage.clickOnBrand();
        brandPage.clickOnBrandDetails();
        famousDetailsPage.validSelf();
        
        # Check "男装“、”餐饮“、”生活“、”运动“及”精品“ tab
        famousDetailsPage.clickBackKey();
        brandPage.clickOnMenFasion();
        brandPage.validSelfMenFasion();
        brandPage.clickOnCatering();
        brandPage.validSelfCertering();
        brandPage.clickOnLife();
        brandPage.validSelfLife();
        brandPage.clickOnSports();
        brandPage.validSelfSports();
        brandPage.scrollAsScreenPercent(0.5, 0.1166, 0.1666, 0.1166)
        brandPage.clickOnCompetitiveProducts();
        brandPage.validSelfCompetitiveProducts();


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(BrandFamousCatergoryCases)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = reportpath + 'Feifan_automation_test_report_' + now + '.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Feifan_automation_test_report',
                                           description='Result for test')
    runner.run(suite)