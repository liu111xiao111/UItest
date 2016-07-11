# -*- coding:utf-8 -*-

import os
import time
from unittest import TestCase
from unittest import TestLoader

import HTMLTestRunner

from com.qa.automation.appium.cases.android.ffan.common.clear_app_data import ClearAppData
from com.qa.automation.appium.cases.android.ffan.common.test_prepare import TestPrepare
from com.qa.automation.appium.configs.driver_configs import appActivity_ffan
from com.qa.automation.appium.configs.driver_configs import appPackage_ffan
from com.qa.automation.appium.configs.driver_configs import deviceName_andr
from com.qa.automation.appium.configs.driver_configs import driver_url
from com.qa.automation.appium.configs.driver_configs import platformName_andr
from com.qa.automation.appium.configs.driver_configs import platformVersion
from com.qa.automation.appium.driver.appium_driver import AppiumDriver
from com.qa.automation.appium.pages.android.ffan.dashboard_page import DashboardPage
from com.qa.automation.appium.pages.android.ffan.fei_fan_membership_page import FeiFanMembershipPage
from com.qa.automation.appium.pages.android.ffan.my_fei_fan_page import MyFeiFanPage
from com.qa.automation.appium.pages.android.ffan.my_membership_card_package_page import MyMembershipCardPackagePage
from com.qa.automation.appium.utility.logger import Logger


class MembershipCardPackageCases(TestCase):
    '''
    巡检checklist No.: 52
    自动化测试case No.: 52
    点击进入我的会员卡包，查看数据是否显示正常并可进入会员页
    '''

    def tearDown(self):
        self.driver.quit()
        ClearAppData().clearData()

    def setUp(self):
        ClearAppData().clearData()
        self.logger = Logger()
        self.driver = AppiumDriver(appPackage_ffan, appActivity_ffan, platformName_andr, platformVersion,
                                   deviceName_andr, driver_url).getDriver()
        TestPrepare(self, self.driver, self.logger).prepare()

    def test_case(self):
        dashboardPage = DashboardPage(self, self.driver, self.logger)
        dashboardPage.validSelf()
        dashboardPage.clickOnMy()

        myFeiFanPage = MyFeiFanPage(self, self.driver, self.logger)
        myFeiFanPage.validSelf()
        myFeiFanPage.clickOnMembershipCardPackage()

        myMembershipCardPackagePage = MyMembershipCardPackagePage(self, self.driver, self.logger)
        myMembershipCardPackagePage.validSelf()
        myMembershipCardPackagePage.clickOnLeHuoKa()

        feiFanMembershipPage = FeiFanMembershipPage(self, self.driver, self.logger)
        feiFanMembershipPage.validSelf()
        feiFanMembershipPage.clickBackKey()

        myMembershipCardPackagePage.clickBackKey()


if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(MembershipCardPackageCases)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = reportpath + 'Feifan_automation_test_report_' + now + '.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(fp, 'Feifan_automation_test_report', 'Result for test')
    runner.run(suite)
