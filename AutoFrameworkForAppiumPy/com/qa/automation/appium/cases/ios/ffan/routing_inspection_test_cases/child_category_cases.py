# -*- coding:utf-8 -*-

import os
import time
import HTMLTestRunner

from unittest import TestCase
from unittest import TestLoader

from com.qa.automation.appium.cases.ios.ffan.common.test_prepare import TestPrepare
from com.qa.automation.appium.cases.ios.ffan.common.clear_app_data import ClearAppData
from com.qa.automation.appium.configs.ios_driver_configs import IosDriverConfigs as IDC
from com.qa.automation.appium.driver.appium_driver import AppiumDriver
from com.qa.automation.appium.pages.ios.ffan.dashboard_page import DashboardPage
from com.qa.automation.appium.pages.ios.ffan.child_category_page import ChildCategoryPage
from com.qa.automation.appium.utility.logger import Logger


class ChildCatergoryCases(TestCase):
    '''
    作者 刘涛
    巡检checklist No.: 9
    自动化测试case No.: 9
    首页进入亲子模块，显示该城市下所有亲子门店，点击可以进入门店详情页
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
        testPrepare.prepare(False)

    def test_case(self):
        dashboardPage = DashboardPage(self , self.driver , self.logger)
        childPage = ChildCategoryPage(self , self.driver , self.logger)

        # 首页进入亲子模块并截图
        dashboardPage.validSelf()
        dashboardPage.clickOnChildCategory()
        childPage.validSelf()
        #childPage.screen_shot("child_category_cases")

        # 检查亲子入口
        clickChildList = (childPage.clickOnChildPlay,
                          childPage.clickOnChildEducation,
                          childPage.clickOnChildShopping,
                          childPage.clickOnOtherStore)

        for clickChild in clickChildList:
            clickChild()
            #childPage.waitBySeconds(20)
            tempText = childPage.clickListFirstItem()
            #childPage.waitBySeconds(20)
            itemName = childPage.getItemName()
            childPage.validKeywords(tempText, itemName)
            childPage.clickBackKey()
            childPage.clickBackKey()
            childPage.clickBackKey()

if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(ChildCatergoryCases)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = os.path.join(reportpath, 'Feifan_automation_test_report_' + now + '.html')
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='food-test',
                                           description='Result for test')
    runner.run(suite)