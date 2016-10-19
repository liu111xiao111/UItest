# -*- coding:utf-8 -*-

import os
import time
import HTMLTestRunner

from unittest import TestCase
from unittest import TestLoader

from cases.ios.ffan.common.testPrepare import TestPrepare
from cases.ios.ffan.common.clearAppData import ClearAppData
from configs.iosDriverConfig import IosDriverConfigs as IDC
from driver.appium_driver import AppiumDriver
from pages.ios.ffan.dashboard_page import DashboardPage
from pages.ios.ffan.brand_category_page import BrandCategoryPage
from pages.ios.ffan.famous_details_category_page import FamousDetailsCategoryPage
from utility.logger import Logger


class PinPaiJieTestCase(TestCase):
    '''
    作者 刘涛
    巡检checklist #8 品牌街
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

        testPrepare = TestPrepare(testcase = self , driver = self.driver , logger = self.logger)
        testPrepare.prepare(True)

    def test_case(self):
        dashboardPage = DashboardPage(testcase = self , driver = self.driver , logger = self.logger)
        brandPage = BrandCategoryPage(testcase = self, driver = self.driver, logger = self.logger)
        famousDetailsPage = FamousDetailsCategoryPage(testcase = self, driver = self.driver, logger = self.logger)

        # 首页点击品牌
        dashboardPage.validSelf();
        dashboardPage.clickOnBrand()
        brandPage.validSelf();

        #点击 "大牌"
        #brandPage.clickOnBrand();
        #brandPage.clickOnBrandDetails();
        #famousDetailsPage.validSelf();

        # 点击 "男装“、”餐饮“、”生活“、”运动“及”精品“ tab
        #famousDetailsPage.clickBackKey();
        brandPage.clickOnWomenFasion();
        brandPage.validSelfWomenFasion();
        brandPage.clickBackKey()
        brandPage.clickOnMenFasion();
        brandPage.validSelfMenFasion();
        brandPage.clickBackKey()
        brandPage.clickOnCatering();
        brandPage.validSelfCertering();
        brandPage.clickBackKey()
        brandPage.clickOnLife();
        brandPage.validSelfLife();
        brandPage.clickBackKey()
        brandPage.clickOnSports();
        brandPage.validSelfSports();
        brandPage.clickBackKey()
        brandPage.clickOnCompetitiveProducts();
        brandPage.validSelfCompetitiveProducts();
        brandPage.clickBackKey()
        
        #点击大牌入驻
        brandPage.clickOnDapairuzhu()
        brandPage.validDapairuzhu()
        


if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(PinPaiJieTestCase)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = os.path.join(reportpath, 'Feifan_automation_test_report_' + now + '.html')
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Feifan_automation_test_report',
                                           description='Result for test')
    runner.run(suite)