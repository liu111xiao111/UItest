# -*- coding: utf-8 -*-

import os
import time
import HTMLTestRunner

from unittest import TestCase
from unittest import TestLoader

from com.qa.automation.appium.pages.android.ffan.dashboard_page import DashboardPage
from com.qa.automation.appium.pages.android.ffan.love_shopping_page import LoveShoppingPage
from com.qa.automation.appium.pages.android.ffan.shopping_center_page import ShoppingCenterPage
from com.qa.automation.appium.driver.appium_driver import AppiumDriver
from com.qa.automation.appium.utility.logger import Logger
from com.qa.automation.appium.configs.driver_configs import platformName_andr
from com.qa.automation.appium.configs.driver_configs import appActivity_ffan
from com.qa.automation.appium.configs.driver_configs import appPackage_ffan
from com.qa.automation.appium.configs.driver_configs import platformVersion
from com.qa.automation.appium.configs.driver_configs import deviceName_andr
from com.qa.automation.appium.configs.driver_configs import driver_url


class LoveShoppingCases(TestCase):
    '''
        备注：原始版本的case
    '''

    def tearDown(self):
        self.driver.quit()

    def setUp(self):
        self.logger = Logger()
        self.driver = AppiumDriver(appPackage_ffan,
                                   appActivity_ffan,
                                   platformName_andr,
                                   platformVersion,
                                   deviceName_andr,
                                   driver_url).getDriver()

    def test_shopping_mall(self):
        dashboardPage = DashboardPage(self, self.driver, self.logger);
        dashboardPage.validSelf();
        loveShoppingPage = LoveShoppingPage(self, self.driver, self.logger);
        loveShoppingPage.clickOnShoppingMall();
        shoppingCenterPage = ShoppingCenterPage(self, self.driver, self.logger);
        shoppingCenterPage.validSelf();

    def test_film(self):
        dashboardPage = DashboardPage(self, self.driver, self.logger);
        dashboardPage.validSelf();
        loveShoppingPage = LoveShoppingPage(self, self.driver, self.logger);
        loveShoppingPage.clickOnFilm();

    def test_food(self):
        dashboardPage = DashboardPage(self, self.driver, self.logger);
        dashboardPage.validSelf();
        loveShoppingPage = LoveShoppingPage(self, self.driver, self.logger);
        loveShoppingPage.clickOnFood();

    def test_brand(self):
        dashboardPage = DashboardPage(self, self.driver, self.logger);
        dashboardPage.validSelf();
        loveShoppingPage = LoveShoppingPage(self, self.driver, self.logger);
        loveShoppingPage.clickOnBrand();

    def test_children(self):
        dashboardPage = DashboardPage(self, self.driver, self.logger);
        dashboardPage.validSelf();
        loveShoppingPage = LoveShoppingPage(self, self.driver, self.logger);
        loveShoppingPage.clickOnChlidren();

    def test_preferential(self):
        dashboardPage = DashboardPage(self, self.driver, self.logger);
        dashboardPage.validSelf();
        loveShoppingPage = LoveShoppingPage(self, self.driver, self.logger);
        loveShoppingPage.clickOnPreferential();

    def test_shopping(self):
        dashboardPage = DashboardPage(self, self.driver, self.logger);
        dashboardPage.validSelf();
        loveShoppingPage = LoveShoppingPage(self, self.driver, self.logger);
        loveShoppingPage.clickOnShopping();

    def test_flash_sale(self):
        dashboardPage = DashboardPage(self, self.driver, self.logger);
        dashboardPage.validSelf();
        loveShoppingPage = LoveShoppingPage(self, self.driver, self.logger);
        loveShoppingPage.clickOnFlashSale();

    def test_parking(self):
        dashboardPage = DashboardPage(self, self.driver, self.logger);
        dashboardPage.validSelf();
        loveShoppingPage = LoveShoppingPage(self, self.driver, self.logger);
        loveShoppingPage.clickOnParking();

    def test_le_pay(self):
        dashboardPage = DashboardPage(self, self.driver, self.logger);
        dashboardPage.validSelf();
        loveShoppingPage = LoveShoppingPage(self, self.driver, self.logger);
        loveShoppingPage.clickOnLePays();


if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(LoveShoppingCases)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = reportpath + 'Feifan_automation_test_report_' + now + '.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Feifan_automation_test_report',
                                           description='Result for test')
    runner.run(suite)
