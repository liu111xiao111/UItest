# -*- coding:utf-8 -*-

import os
import time
import HTMLTestRunner

from unittest import TestCase
from unittest import TestLoader

from com.qa.automation.appium.cases.ios.ffan.common.clear_app_data import ClearAppData
from com.qa.automation.appium.cases.ios.ffan.common.test_prepare import TestPrepare
from com.qa.automation.appium.configs.ios_driver_configs import IosDriverConfigs as IDC
from com.qa.automation.appium.driver.appium_driver import AppiumDriver
from com.qa.automation.appium.pages.ios.ffan.dashboard_page import DashboardPage
from com.qa.automation.appium.pages.ios.ffan.fei_fan_membership_page import FeiFanMembershipPage
from com.qa.automation.appium.pages.ios.ffan.my_fei_fan_page import MyFeiFanPage
from com.qa.automation.appium.pages.ios.ffan.my_membership_card_package_page import MyMembershipCardPackagePage
from com.qa.automation.appium.utility.logger import Logger


class MembershipCardPackageCases(TestCase):
    '''
    巡检checklist No.: 52
    自动化测试case No.: 52
    点击进入我的会员卡包，查看数据是否显示正常并可进入会员页
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
