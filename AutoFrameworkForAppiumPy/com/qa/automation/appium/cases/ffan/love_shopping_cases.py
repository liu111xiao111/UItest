# -*- coding: utf-8 -*-

import sys, os

sys.path.append(os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))))

from com.qa.automation.appium.pages.ffan.dashboard_page import *;
from com.qa.automation.appium.pages.ffan.love_shopping_page import *;
from com.qa.automation.appium.pages.ffan.shopping_center_page import *;
from com.qa.automation.appium.driver.appium_driver import *;
from com.qa.automation.appium.utility.logger import Logger;

import unittest
import HTMLTestRunner


class LoveShoppingCases(unittest.TestCase):
    def tearDown(self):
        self.driver.quit()

    def setUp(self):
        self.logger = Logger()
        self.driver = AppiumDriver(app_package=appPackage_ffan, app_activity=appActivity_ffan,
                                   platform_name=platformName_andr, platform_version=platformVersion,
                                   device_name=deviceName_andr, driver_url=driver_url
                                   ).getDriver()

    def test_shopping_mall(self):
        dashboardPage = DashboardPage(testcase=self, driver=self.driver, logger=self.logger);
        dashboardPage.waitBySeconds(seconds=20)
        dashboardPage.validSelf();
        loveShoppingPage = LoveShoppingPage(testcase=self, driver=self.driver, logger=self.logger);
        loveShoppingPage.clickOnShoppingMall();
        shoppingCenterPage = ShoppingCenterPage(testcase=self, driver=self.driver, logger=self.logger);
        shoppingCenterPage.validSelf();

    def test_film(self):
        dashboardPage = DashboardPage(testcase=self, driver=self.driver, logger=self.logger);
        dashboardPage.waitBySeconds(seconds=20)
        dashboardPage.validSelf();
        loveShoppingPage = LoveShoppingPage(testcase=self, driver=self.driver, logger=self.logger);
        loveShoppingPage.clickOnFilm();

    def test_food(self):
        dashboardPage = DashboardPage(testcase=self, driver=self.driver, logger=self.logger);
        dashboardPage.waitBySeconds(seconds=20)
        dashboardPage.validSelf();
        loveShoppingPage = LoveShoppingPage(testcase=self, driver=self.driver, logger=self.logger);
        loveShoppingPage.clickOnFood();

    def test_brand(self):
        dashboardPage = DashboardPage(testcase=self, driver=self.driver, logger=self.logger);
        dashboardPage.waitBySeconds(seconds=20)
        dashboardPage.validSelf();
        loveShoppingPage = LoveShoppingPage(testcase=self, driver=self.driver, logger=self.logger);
        loveShoppingPage.clickOnBrand();

    def test_children(self):
        dashboardPage = DashboardPage(testcase=self, driver=self.driver, logger=self.logger);
        dashboardPage.waitBySeconds(seconds=20)
        dashboardPage.validSelf();
        loveShoppingPage = LoveShoppingPage(testcase=self, driver=self.driver, logger=self.logger);
        loveShoppingPage.clickOnChlidren();

    def test_preferential(self):
        dashboardPage = DashboardPage(testcase=self, driver=self.driver, logger=self.logger);
        dashboardPage.waitBySeconds(seconds=20)
        dashboardPage.validSelf();
        loveShoppingPage = LoveShoppingPage(testcase=self, driver=self.driver, logger=self.logger);
        loveShoppingPage.clickOnPreferential();

    def test_shopping(self):
        dashboardPage = DashboardPage(testcase=self, driver=self.driver, logger=self.logger);
        dashboardPage.waitBySeconds(seconds=20)
        dashboardPage.validSelf();
        loveShoppingPage = LoveShoppingPage(testcase=self, driver=self.driver, logger=self.logger);
        loveShoppingPage.clickOnShopping();

    def test_flash_sale(self):
        dashboardPage = DashboardPage(testcase=self, driver=self.driver, logger=self.logger);
        dashboardPage.waitBySeconds(seconds=20)
        dashboardPage.validSelf();
        loveShoppingPage = LoveShoppingPage(testcase=self, driver=self.driver, logger=self.logger);
        loveShoppingPage.clickOnFlashSale();

    def test_parking(self):
        dashboardPage = DashboardPage(testcase=self, driver=self.driver, logger=self.logger);
        dashboardPage.waitBySeconds(seconds=20)
        dashboardPage.validSelf();
        loveShoppingPage = LoveShoppingPage(testcase=self, driver=self.driver, logger=self.logger);
        loveShoppingPage.clickOnParking();

    def test_le_pay(self):
        dashboardPage = DashboardPage(testcase=self, driver=self.driver, logger=self.logger);
        dashboardPage.waitBySeconds(seconds=20)
        dashboardPage.validSelf();
        loveShoppingPage = LoveShoppingPage(testcase=self, driver=self.driver, logger=self.logger);
        loveShoppingPage.clickOnLePays();


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(LoveShoppingCases)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = reportpath + 'Feifan_automation_test_report_' + now + '.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Feifan_automation_test_report',
                                           description='Result for test')
    runner.run(suite)