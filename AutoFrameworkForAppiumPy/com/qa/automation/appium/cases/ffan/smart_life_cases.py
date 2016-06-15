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


    # 测试点击快车
    def test_ClickQuickCar(self):

        dashboardPage = DashboardPage(testcase = self , driver = self.driver , logger = self.logger);
        dashboardPage.waitBySeconds(seconds=20)
        dashboardPage.validSelf();

        dashboardPage.clickOnSmartLife();
        smartLifePage = SmartLifePage(testcase=self,driver=self.driver,logger=self.logger);

        smartLifePage.validSelf();
        smartLifePage.clickQuickCar();

    # 测试点击出租车
    def test_clickTaxi(self):

        dashboardPage = DashboardPage(testcase=self, driver=self.driver, logger=self.logger);
        dashboardPage.waitBySeconds(seconds=20)
        dashboardPage.validSelf();

        dashboardPage.clickOnSmartLife();
        smartLifePage = SmartLifePage(testcase=self, driver=self.driver, logger=self.logger);
        smartLifePage.validSelf();
        smartLifePage.clickTaxi();

    # 测试点击专车
    def test_clickTailoredCar(self):

        dashboardPage = DashboardPage(testcase=self, driver=self.driver, logger=self.logger);
        dashboardPage.waitBySeconds(seconds=20)
        dashboardPage.validSelf();

        dashboardPage.clickOnSmartLife();
        smartLifePage = SmartLifePage(testcase=self, driver=self.driver, logger=self.logger);
        smartLifePage.validSelf();
        smartLifePage.clickTailoredCar();


    # 测试点击代驾
    def test_clickDrivingService(self):

        dashboardPage = DashboardPage(testcase=self, driver=self.driver, logger=self.logger);
        dashboardPage.waitBySeconds(seconds=20)
        dashboardPage.validSelf();

        dashboardPage.clickOnSmartLife();
        smartLifePage = SmartLifePage(testcase=self, driver=self.driver, logger=self.logger);
        smartLifePage.validSelf();
        smartLifePage.clickDrivingService();

    # 测试点击话费
    def test_clickTelephoneCharge(self):

        dashboardPage = DashboardPage(testcase=self, driver=self.driver, logger=self.logger);
        dashboardPage.waitBySeconds(seconds=20)
        dashboardPage.validSelf();

        dashboardPage.clickOnSmartLife();
        smartLifePage = SmartLifePage(testcase=self, driver=self.driver, logger=self.logger);
        smartLifePage.validSelf();
        smartLifePage.clickTelephoneCharge();


    # 测试点击流量
    def test_clickFlow(self):

        dashboardPage = DashboardPage(testcase=self, driver=self.driver, logger=self.logger);
        dashboardPage.waitBySeconds(seconds=20)
        dashboardPage.validSelf();

        dashboardPage.clickOnSmartLife();
        smartLifePage = SmartLifePage(testcase=self, driver=self.driver, logger=self.logger);
        smartLifePage.validSelf();
        smartLifePage.clickFlow();

    # 测试点击Q币
    def test_clickQCoin(self):

        dashboardPage = DashboardPage(testcase=self, driver=self.driver, logger=self.logger);
        dashboardPage.waitBySeconds(seconds=20)
        dashboardPage.validSelf();

        dashboardPage.clickOnSmartLife();
        smartLifePage = SmartLifePage(testcase=self, driver=self.driver, logger=self.logger);
        smartLifePage.validSelf();
        smartLifePage.clickQCoin();

    # 测试点击游戏充值
    def test_clickGameCharge(self):
        dashboardPage = DashboardPage(testcase=self, driver=self.driver, logger=self.logger);
        dashboardPage.waitBySeconds(seconds=20)
        dashboardPage.validSelf();
        dashboardPage.clickOnSmartLife();
        smartLifePage = SmartLifePage(testcase=self, driver=self.driver, logger=self.logger);
        smartLifePage.validSelf();
        smartLifePage.clickGameCharge();

    # 测试点击股票
    def test_clickStock(self):
        dashboardPage = DashboardPage(testcase=self, driver=self.driver, logger=self.logger);
        dashboardPage.waitBySeconds(seconds=20)
        dashboardPage.validSelf();
        dashboardPage.clickOnSmartLife();
        smartLifePage = SmartLifePage(testcase=self, driver=self.driver, logger=self.logger);
        smartLifePage.validSelf();
        smartLifePage.clickStock();


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(SmartLifeCases)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = reportpath + 'Feifan_automation_test_report_' + now + '.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Feifan_automation_test_report',
                                           description='Result for test')
    runner.run(suite)