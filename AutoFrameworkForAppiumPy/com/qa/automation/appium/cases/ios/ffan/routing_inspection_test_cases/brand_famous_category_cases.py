# -*- coding:utf-8 -*-

import os
import time
import HTMLTestRunner

from unittest import TestCase
from unittest import TestLoader

from com.qa.automation.appium.cases.ios.ffan.common.clear_app_data import ClearAppData
from com.qa.automation.appium.configs.ios_driver_configs import IosDriverConfigs as IDC
from com.qa.automation.appium.driver.appium_driver import AppiumDriver
from com.qa.automation.appium.pages.ios.ffan.dashboard_page import DashboardPage
from com.qa.automation.appium.pages.ios.ffan.brand_category_page import BrandCategoryPage
from com.qa.automation.appium.pages.ios.ffan.famous_details_category_page import FamousDetailsCategoryPage
from com.qa.automation.appium.utility.logger import Logger


class BrandFamousCatergoryCases(TestCase):
    '''
        巡检checklist #8
        自动化测试 #8-2
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

    def test_case(self):
        dashboardPage = DashboardPage(testcase = self , driver = self.driver , logger = self.logger)
        brandPage = BrandCategoryPage(testcase = self, driver = self.driver, logger = self.logger)
        famousDetailsPage = FamousDetailsCategoryPage(testcase = self, driver = self.driver, logger = self.logger)

        # 首页点击品牌街
        dashboardPage.validSelf();
        dashboardPage.click_brand()
        brandPage.validSelf();

        # 点击 "大牌"
        brandPage.clickOnBrand();
        brandPage.clickOnBrandDetails();
        famousDetailsPage.validSelf();

        # 点击 "男装“、”餐饮“、”生活“、”运动“及”精品“ tab
        famousDetailsPage.clickBackKey();
        brandPage.clickOnMenFasion();
        brandPage.validSelfMenFasion();
        brandPage.clickOnCatering();
        brandPage.validSelfCertering();
        brandPage.clickOnLife();
        brandPage.validSelfLife();
        brandPage.clickOnSports();
        brandPage.validSelfSports();
        '''brandPage.scrollAsScreenPercent(0.5, 0.1166, 0.1666, 0.1166)
        brandPage.waitBySeconds(1);
        brandPage.clickOnCompetitiveProducts();
        brandPage.waitBySeconds(1);
        brandPage.validSelfCompetitiveProducts();'''


if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(BrandFamousCatergoryCases)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = reportpath + 'Feifan_automation_test_report_' + now + '.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Feifan_automation_test_report',
                                           description='Result for test')
    runner.run(suite)