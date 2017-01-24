# -*- coding:utf-8 -*-

import os
import time
import HTMLTestRunner

from unittest import TestCase
from unittest import TestLoader

from cases.ios.ffan.common.testPrepare import TestPrepare
from configs.iosDriverConfig import IosDriverConfigs as IDC
from driver.appium_driver import AppiumDriver
from pages.ios.ffan.dashboard_page import DashboardPage
from pages.ios.ffan.brand_category_page import BrandCategoryPage
from pages.ios.ffan.famous_details_category_page import FamousDetailsCategoryPage
from cases.logger import logger


class PinPaiJieTestCase(TestCase):
    '''
    作者 刘涛
    巡检checklist #8 品牌街
    自动化测试 #8-2
    首页进入品牌简单浏览品牌中推荐和大牌的内容，点击验证是否可以进入详情页，显示是否正常，能否喜欢订阅
    '''

    @classmethod
    def setUpClass(cls):
        '''
        初始化Appium driver
        '''

        cls.driver = AppiumDriver(None,
                                  None,
                                  IDC.platformName,
                                  IDC.platformVersion,
                                  IDC.deviceName,
                                  IDC.driverUrl,
                                  IDC.bundleId,
                                  IDC.udid).getDriver()
        logger.info("Appium client init completed")

    def setUp(self):
        self.logger = logger

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
        #点击女装
        brandPage.clickOnWomenFasion();
        #验证
        brandPage.validSelfWomenFasion();
        brandPage.clickBackKey()
        #返回验证
        brandPage.validSelf();
        #点击男装
        brandPage.clickOnMenFasion();
        brandPage.validSelfMenFasion();
        brandPage.clickBackKey()
        # 返回验证
        brandPage.validSelf();
        #点击餐饮
        brandPage.clickOnCatering();
        brandPage.clickBackKey()
        # 返回验证
        brandPage.validSelf();

        brandPage.clickOnLife();
        brandPage.clickBackKey()
        # 返回验证
        brandPage.validSelf();

        brandPage.clickOnSports();
        brandPage.clickBackKey()
        # 返回验证
        brandPage.validSelf();

        brandPage.clickOnCompetitiveProducts();


    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(PinPaiJieTestCase)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = os.path.join(reportpath, 'Feifan_automation_test_report_' + now + '.html')
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Feifan_automation_test_report',
                                           description='Result for test')
    runner.run(suite)