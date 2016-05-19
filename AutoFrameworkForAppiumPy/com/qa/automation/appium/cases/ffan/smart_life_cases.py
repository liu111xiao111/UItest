# -*- coding: utf-8 -*-

import sys,os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))))

from com.qa.automation.appium.pages.ffan.dashboard_page import *;
from com.qa.automation.appium.pages.ffan.smart_life_page import *;
from com.qa.automation.appium.driver.appium_driver import *;
from com.qa.automation.appium.utility.logger import Logger;

import unittest
import HTMLTestRunner

class SmartLifeCases(unittest.TestCase):

    def tearDown(self):
        self.driver.quit()

    def setUp(self):
        self.logger = Logger()
        self.driver = AppiumDriver(app_package=appPackage_ffan, app_activity=appActivity_ffan,
                                   platform_name=platformName_andr, platform_version=platformVersion,
                                   device_name=deviceName_andr, driver_url=driver_url
                                   ).getDriver()



    # 测试慧生活页面
    def test_self(self):
        dashboardPage = DashboardPage(testcase = self , driver = self.driver , logger = self.logger);
        dashboardPage.validSelf();
        dashboardPage.clickOnSmartLife();
        smartLifePage = SmartLifePage(testcase=self,driver=self.driver,logger=self.logger);
        smartLifePage.validSelf();



    # # 测试点击全城找店图标
    # def test_ClickFindStore(self):
    #     dashboardPage = DashboardPage(testcase = self , driver = self.driver , logger = self.logger);
    #     dashboardPage.validSelf();
    #     dashboardPage.clickOnSmartLife();
    #     smartLifePage = SmartLifePage(testcase=self,driver=self.driver,logger=self.logger);
    #     smartLifePage.clickFindStore();
    #
    # # 测试点击全城找店图标
    # def test_ClickQueue(self):
    #     dashboardPage = DashboardPage(testcase = self , driver = self.driver , logger = self.logger);
    #     dashboardPage.validSelf();`
    #     dashboardPage.clickOnSmartLife();
    #     smartLifePage = SmartLifePage(testcase=self,driver=self.driver,logger=self.logger);
    #     smartLifePage.clickQueue();
    #
    # # 测试点击全城找店图标
    # def test_ClickFly(self):
    #     dashboardPage = DashboardPage(testcase = self , driver = self.driver , logger = self.logger);
    #     dashboardPage.validSelf();
    #     dashboardPage.clickOnSmartLife();
    #     smartLifePage = SmartLifePage(testcase=self,driver=self.driver,logger=self.logger);
    #     smartLifePage.clickFly();
    #
    # # 测试点击优惠券图标
    # def test_ClickCoupon(self):
    #     dashboardPage = DashboardPage(testcase = self , driver = self.driver , logger = self.logger);
    #     dashboardPage.validSelf();
    #     dashboardPage.clickOnSmartLife();
    #     smartLifePage = SmartLifePage(testcase=self,driver=self.driver,logger=self.logger);
    #     smartLifePage.clickCoupon();
    #
    # # 测试点击活动图标
    # def test_ClickActivity(self):
    #     dashboardPage = DashboardPage(testcase = self , driver = self.driver , logger = self.logger);
    #     dashboardPage.validSelf();
    #     dashboardPage.clickOnSmartLife();
    #     smartLifePage = SmartLifePage(testcase=self,driver=self.driver,logger=self.logger);
    #     smartLifePage.clickActivity();
    #
    #
    # # 测试点击活动页签
    # def test_ClickActivityTag(self):
    #     dashboardPage = DashboardPage(testcase = self , driver = self.driver , logger = self.logger);
    #     dashboardPage.validSelf();
    #     dashboardPage.clickOnSmartLife();
    #     smartLifePage = SmartLifePage(testcase=self,driver=self.driver,logger=self.logger);
    #     smartLifePage.clickActivityTag();
    #
    # # 测试点击优惠页签
    # def test_ClickCouponTag(self):
    #     dashboardPage = DashboardPage(testcase = self , driver = self.driver , logger = self.logger);
    #     dashboardPage.validSelf();
    #     dashboardPage.clickOnSmartLife();
    #     smartLifePage = SmartLifePage(testcase=self,driver=self.driver,logger=self.logger);
    #     smartLifePage.clickCouponTag();



if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(SmartLifeCases)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = reportpath + 'Feifan_automation_test_report_' + now + '.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Feifan_automation_test_report',
                                           description='Result for test')
    runner.run(suite)