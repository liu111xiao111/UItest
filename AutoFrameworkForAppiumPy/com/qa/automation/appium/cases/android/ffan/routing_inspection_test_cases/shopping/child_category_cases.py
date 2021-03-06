# -*- coding: utf-8 -*-

import os
import time
import HTMLTestRunner

from unittest import TestCase
from unittest import TestLoader

from com.qa.automation.appium.pages.android.ffan.child_category_page import ChildCategoryPage
from com.qa.automation.appium.pages.android.ffan.dashboard_page import DashboardPage
from com.qa.automation.appium.configs.driver_configs import platformName_andr
from com.qa.automation.appium.configs.driver_configs import appActivity_ffan
from com.qa.automation.appium.configs.driver_configs import appPackage_ffan
from com.qa.automation.appium.configs.driver_configs import deviceName_andr
from com.qa.automation.appium.configs.driver_configs import driver_url
from com.qa.automation.appium.driver.appium_driver import AppiumDriver
from com.qa.automation.appium.utility.logger import Logger
from com.qa.automation.appium.cases.android.ffan.common.clear_app_data import ClearAppData
from com.qa.automation.appium.cases.android.ffan.common.test_prepare import TestPrepare
from com.qa.automation.appium.utility.device_info_util import DeviceInfoUtil


class ChildCatergoryCases(TestCase):
    '''
    作者 乔佳溪
    巡检checklist No.: 9
    自动化测试case No.: 9
    首页进入亲子模块，显示该城市下所有亲子门店，点击可以进入门店详情页
    '''

    def tearDown(self):
        self.reset.clearData()
        self.driver.quit()

    def setUp(self):
        self.logger = Logger()
        self.platVersion = DeviceInfoUtil().getBuildVersion()
        self.driver = AppiumDriver(appPackage_ffan,
                                   appActivity_ffan,
                                   platformName_andr,
                                   self.platVersion, 
                                   deviceName_andr,
                                   driver_url).getDriver()

        self.reset = ClearAppData(self.driver)
        self.reset.clearData()

        TestPrepare(self, self.driver, self.logger).prepare(False)

    def test_case(self):
        dashboardPage = DashboardPage(self , self.driver , self.logger)
        childPage = ChildCategoryPage(self , self.driver , self.logger)

        # Verify Home Page
        dashboardPage.validSelf()

        # Launch Child Category Page and verify
        dashboardPage.clickOnChildCategory()
        childPage.validSelf()

        childPage.screenShot("child_category_cases")

        # Launch Child Play, Child Education, Child Shopping and
        clickChildList = (childPage.clickOnChildPlay,
                          childPage.clickOnChildEducation,
                          childPage.clickOnChildShopping,
                          childPage.clickOnOtherStore)

        for clickChild in clickChildList:
            clickChild()
            tempText = childPage.clickListFirstItem()
            tempTextLink = tempText + " Link"
            if int(self.platVersion.split(".")[0]) >= 5:
                childPage.validKeywords(tempText)
            else:
                childPage.validKeywords(tempTextLink)
            childPage.clickBackKey()
            childPage.clickBackKey()

if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(ChildCatergoryCases)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = os.path.join(reportpath, 'Feifan_automation_test_report_' + now + '.html')
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Feifan_automation_test_report',
                                           description='Result for test')
    runner.run(suite)