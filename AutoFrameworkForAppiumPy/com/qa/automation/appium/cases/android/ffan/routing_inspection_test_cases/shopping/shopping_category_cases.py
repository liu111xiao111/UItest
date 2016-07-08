# -*- coding: utf-8 -*-

from __init__ import *
import time
import HTMLTestRunner

from unittest import TestCase
from unittest import TestLoader

from com.qa.automation.appium.cases.android.ffan.common.test_prepare import TestPrepare
from com.qa.automation.appium.cases.android.ffan.common.clear_app_data import ClearAppData
from com.qa.automation.appium.pages.android.ffan.dashboard_page import DashboardPage;
from com.qa.automation.appium.pages.android.ffan.shopping_category_page import ShoppingCategoryPage;
from com.qa.automation.appium.pages.android.ffan.shopping_details_category_page import ShoppingDetailsCategoryPage;
from com.qa.automation.appium.configs.driver_configs import appActivity_ffan
from com.qa.automation.appium.configs.driver_configs import appPackage_ffan
from com.qa.automation.appium.configs.driver_configs import deviceName_andr
from com.qa.automation.appium.configs.driver_configs import driver_url
from com.qa.automation.appium.configs.driver_configs import platformName_andr
from com.qa.automation.appium.configs.driver_configs import platformVersion
from com.qa.automation.appium.driver.appium_driver import AppiumDriver
from com.qa.automation.appium.utility.logger import Logger;


class ShoppingCatergoryCases(TestCase):
    '''
        巡检checklist #12
        自动化测试 #12
        首页进入购物模块，数据显示正常，点击进入详情页可以激活商品的提醒
    '''

    def tearDown(self):
        self.driver.quit()
        
        clearAppData = ClearAppData()
        clearAppData.clearData()

    def setUp(self):
        clearAppData = ClearAppData()
        clearAppData.clearData()

        self.logger = Logger()
        self.driver = AppiumDriver(appPackage_ffan,
                                   appActivity_ffan,
                                   platformName_andr,
                                   platformVersion,
                                   deviceName_andr,
                                   driver_url).getDriver()

        #Login & update version
        TestPrepare(self, self.driver, self.logger).prepare(False)

    def test_case(self):
        dashboardPage = DashboardPage(self, self.driver, self.logger)
        shoppingPage = ShoppingCategoryPage(self, self.driver, self.logger)
        shoppingDetailsPage = ShoppingDetailsCategoryPage(self, self.driver, self.logger)

        # Load goods page
        dashboardPage.validSelf();
        dashboardPage.clickOnShoppingCategory()
        shoppingPage.validSelf();

        # Click goods details， load detail pay page.
        shoppingPage.clickOnGoodsDetails();
        shoppingDetailsPage.validSelf();


if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(ShoppingCatergoryCases)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = reportpath + 'Feifan_automation_test_report_' + now + '.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Feifan_automation_test_report',
                                           description='Result for test')
    runner.run(suite)