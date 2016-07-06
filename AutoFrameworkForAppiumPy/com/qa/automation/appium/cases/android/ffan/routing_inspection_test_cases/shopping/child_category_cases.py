# -*- coding: utf-8 -*-

import os
import time
import HTMLTestRunner

from unittest import TestCase, TestLoader

# Pages function
from com.qa.automation.appium.pages.android.ffan.child_category_page import ChildCategoryPage
from com.qa.automation.appium.pages.android.ffan.dashboard_page import DashboardPage

# Driver parameters
from com.qa.automation.appium.configs.driver_configs import platformName_andr
from com.qa.automation.appium.configs.driver_configs import appActivity_ffan
from com.qa.automation.appium.configs.driver_configs import appPackage_ffan
from com.qa.automation.appium.configs.driver_configs import platformVersion
from com.qa.automation.appium.configs.driver_configs import deviceName_andr
from com.qa.automation.appium.configs.driver_configs import driver_url

# Driver function
from com.qa.automation.appium.driver.appium_driver import AppiumDriver

# Logger
from com.qa.automation.appium.utility.logger import Logger

# Common function
from com.qa.automation.appium.cases.android.ffan.common.clear_app_data import ClearAppData
from com.qa.automation.appium.cases.android.ffan.common.test_prepare import TestPrepare


class ChildCatergoryCases(TestCase):
    '''
    巡检checklist No.: 9
    自动化测试case No.: 9
    首页进入亲子模块，显示该城市下所有亲子门店，点击可以进入门店详情页
    '''

    def tearDown(self):
        self.driver.quit()
        clearAppData = ClearAppData()
        clearAppData.clearData()

    def setUp(self):
        clearAppData = ClearAppData()
        clearAppData.clearData()

        self.logger = Logger()
        self.driver = AppiumDriver(appPackage_ffan, appActivity_ffan,
                                   platformName_andr, platformVersion,
                                   deviceName_andr, driver_url).getDriver()

        # Prepare switch city. update version and login
        TestPrepare(self, self.driver, self.logger).prepare(False)

    def test_case(self):
        dashboardPage = DashboardPage(self , self.driver , self.logger)
        childPage = ChildCategoryPage(self , self.driver , self.logger)

        # Verify Home Page
        dashboardPage.validSelf()

        # Launch Child Category Page and verify
        dashboardPage.clickOnChildCategory()
        childPage.validSelf()

        # Launch Child Play, Child Education, Child Shopping and
        clickChildList = (childPage.clickOnChildPlay,
                          childPage.clickOnChildEducation,
                          childPage.clickOnChildShopping,
                          childPage.clickOnOtherStore)

        for clickChild in clickChildList:
            clickChild()
            tempText = childPage.clickListFirstItem()
            childPage.validKeywords(tempText)
            childPage.clickBackKey()
            childPage.clickBackKey()
            childPage.clickBackKey()

if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(ChildCatergoryCases)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = reportpath + 'food-test_' + now + '.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='food-test',
                                           description='Result for test')
    runner.run(suite)