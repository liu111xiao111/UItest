# -*- coding: utf-8 -*-

import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))))))

from com.qa.automation.appium.configs.driver_configs import *;
from com.qa.automation.appium.driver.appium_driver import *;
from com.qa.automation.appium.utility.logger import Logger;
from com.qa.automation.appium.utility.device_info_util import *;

from com.qa.automation.appium.pages.ios.ffan.dashboard_page import *
from com.qa.automation.appium.pages.ios.ffan.love_shopping_page import *
from com.qa.automation.appium.pages.ios.ffan.shopping_center_page import *
from com.qa.automation.appium.pages.ios.ffan.film_selector_page import *
from com.qa.automation.appium.pages.ios.ffan.food_category_page import *
from com.qa.automation.appium.pages.ios.ffan.brand_page import *
from com.qa.automation.appium.pages.ios.ffan.parent_children_page import *
from com.qa.automation.appium.pages.ios.ffan.preferential_page import *
from com.qa.automation.appium.pages.ios.ffan.shopping_page import *
from com.qa.automation.appium.pages.ios.ffan.parking_page import *
from com.qa.automation.appium.pages.ios.ffan.le_pay_page import *

import unittest
import HTMLTestRunner


class MyFfanCases(unittest.TestCase):

    """
        备注：原始版本的case，暂没作修改
    """
    def tearDown(self):
        self.driver.quit()

    def setUp(self):
        self.logger = Logger()
        device_info_util = DeviceInfoUtil();
        prod_version = device_info_util.get_product_version();
        udid = device_info_util.getUdid();
        appiumDriver = AppiumDriver(platform_name="iOS", platform_version=prod_version, device_name='iPhone',
                                    bundle_id=bundle_id,
                                    ios_udid=udid)
        self.driver = appiumDriver.getDriver();

    def test_shopping_mall(self):
        dashboard = DashboardPage(testcase=self,driver=self.driver,logger=self.logger)
        dashboard.wait_by_seconds(seconds=1)
        dashboard.validSelf()
        dashboard.clickOnBornToShop()
        dashboard.wait_by_seconds(seconds=1)
        loveShoppingPage = LoveShoppingPage(test_case=self,driver=self.driver,logger=self.logger)
        loveShoppingPage.validSelf()
        loveShoppingPage.clickOnShoppingMall()
        loveShoppingPage.wait_by_seconds(seconds=2)
        shoppingCenterPage = ShoppingCenterPage(testcase=self,driver=self.driver,logger=self.logger)
        shoppingCenterPage.validSelf()

    def test_film(self):
        dashboard = DashboardPage(testcase=self,driver=self.driver,logger=self.logger)
        dashboard.wait_by_seconds(seconds=1)
        dashboard.validSelf()
        dashboard.clickOnBornToShop()
        dashboard.wait_by_seconds(seconds=1)
        loveShoppingPage = LoveShoppingPage(test_case=self,driver=self.driver,logger=self.logger)
        loveShoppingPage.validSelf()
        loveShoppingPage.clickOnFilm()
        loveShoppingPage.wait_by_seconds(seconds=2)
        filmSelectorPage = FilmSelectorPage(test_case=self,driver=self.driver,logger=self.logger)
        filmSelectorPage.validSelf()


    def test_food(self):
        dashboard = DashboardPage(testcase=self, driver=self.driver, logger=self.logger)
        dashboard.wait_by_seconds(seconds=1)
        dashboard.validSelf()
        dashboard.clickOnBornToShop()
        dashboard.wait_by_seconds(seconds=1)
        loveShoppingPage = LoveShoppingPage(test_case=self, driver=self.driver, logger=self.logger)
        loveShoppingPage.validSelf()
        loveShoppingPage.clickOnFood()
        loveShoppingPage.wait_by_seconds(seconds=2)
        foodCategoryPage = FoodCategoryPage(testcase=self,driver=self.driver,logger=self.logger)
        foodCategoryPage.validSelf()

    def test_brand(self):
        dashboard = DashboardPage(testcase=self, driver=self.driver, logger=self.logger)
        dashboard.wait_by_seconds(seconds=1)
        dashboard.validSelf()
        dashboard.clickOnBornToShop()
        dashboard.wait_by_seconds(seconds=1)
        loveShoppingPage = LoveShoppingPage(test_case=self, driver=self.driver, logger=self.logger)
        loveShoppingPage.validSelf()
        loveShoppingPage.clickOnBrand()
        loveShoppingPage.wait_by_seconds(seconds=2)
        brandPage = BrandPage(test_case=self,driver=self.driver,logger=self.logger)
        brandPage.validSelf()

    """
        首页点击亲子页面
    """
    def test_child(self):
        dashboard = DashboardPage(testcase=self, driver=self.driver, logger=self.logger)
        dashboard.wait_by_seconds(seconds=1)
        dashboard.validSelf()
        dashboard.clickOnBornToShop()
        dashboard.wait_by_seconds(seconds=1)
        loveShoppingPage = LoveShoppingPage(test_case=self, driver=self.driver, logger=self.logger)
        loveShoppingPage.validSelf()
        loveShoppingPage.clickOnChlidren()
        loveShoppingPage.wait_by_seconds(seconds=2)
        parentChildrenPage = ParentChildrenPage(testcase=self,driver=self.driver,logger=self.logger)
        parentChildrenPage.validSelf()

    """
        首页点击优惠页面
    """
    def test_preferential(self):
        dashboard = DashboardPage(testcase=self, driver=self.driver, logger=self.logger)
        dashboard.wait_by_seconds(seconds=1)
        dashboard.validSelf()
        dashboard.clickOnBornToShop()
        dashboard.wait_by_seconds(seconds=1)
        loveShoppingPage = LoveShoppingPage(test_case=self, driver=self.driver, logger=self.logger)
        loveShoppingPage.validSelf()
        loveShoppingPage.clickOnPreferential()
        loveShoppingPage.wait_by_seconds(seconds=2)
        preferentialPage = PreferentialPage(testcase=self,driver=self.driver,logger=self.logger)
        preferentialPage.validSelf()

    def test_shopping(self):
        dashboard = DashboardPage(testcase=self, driver=self.driver, logger=self.logger)
        dashboard.wait_by_seconds(seconds=1)
        dashboard.validSelf()
        dashboard.clickOnBornToShop()
        dashboard.wait_by_seconds(seconds=1)
        loveShoppingPage = LoveShoppingPage(test_case=self, driver=self.driver, logger=self.logger)
        loveShoppingPage.validSelf()
        loveShoppingPage.clickOnShopping()
        loveShoppingPage.wait_by_seconds(seconds=10)
        shoppingPage = ShoppingPage(testcase=self,driver=self.driver,logger=self.logger)
        shoppingPage.validSelf()

    def test_flash_pay(self):
        dashboard = DashboardPage(testcase=self, driver=self.driver, logger=self.logger)
        dashboard.wait_by_seconds(seconds=1)
        dashboard.validSelf()
        dashboard.clickOnBornToShop()
        dashboard.wait_by_seconds(seconds=1)
        loveShoppingPage = LoveShoppingPage(test_case=self, driver=self.driver, logger=self.logger)
        loveShoppingPage.validSelf()
        loveShoppingPage.clickOnFlashSale()
        loveShoppingPage.wait_by_seconds(seconds=2)

    def test_parking(self):
        dashboard = DashboardPage(testcase=self, driver=self.driver, logger=self.logger)
        dashboard.wait_by_seconds(seconds=1)
        dashboard.validSelf()
        dashboard.clickOnBornToShop()
        dashboard.wait_by_seconds(seconds=1)
        loveShoppingPage = LoveShoppingPage(test_case=self, driver=self.driver, logger=self.logger)
        loveShoppingPage.validSelf()
        loveShoppingPage.clickOnParking()
        loveShoppingPage.wait_by_seconds(seconds=2)
        parkingPage = ParkingPage(testcase=self,driver=self.driver,logger=self.logger)
        parkingPage.validSelf()

    def test_le_pay(self):
        dashboard = DashboardPage(testcase=self, driver=self.driver, logger=self.logger)
        dashboard.wait_by_seconds(seconds=1)
        dashboard.validSelf()
        dashboard.clickOnBornToShop()
        dashboard.wait_by_seconds(seconds=1)
        loveShoppingPage = LoveShoppingPage(test_case=self, driver=self.driver, logger=self.logger)
        loveShoppingPage.validSelf()
        loveShoppingPage.clickOnLePays()
        loveShoppingPage.wait_by_seconds(seconds=2)
        lePayPage = LePayPage(testcase=self,driver=self.driver,logger=self.logger)
        lePayPage.validSelf()


if __name__ == "__main__":
    print("path is %s." % (sys.path))
