# -*- coding: utf-8 -*-

import os
import time
from unittest import TestCase
from unittest import TestLoader

import HTMLTestRunner

from com.qa.automation.appium.cases.ios.ffan.common.clear_app_data import ClearAppData
from com.qa.automation.appium.cases.ios.ffan.common.test_prepare import TestPrepare
from com.qa.automation.appium.configs.ios_driver_configs import IosDriverConfigs as IDC
from com.qa.automation.appium.driver.appium_driver import AppiumDriver
from com.qa.automation.appium.pages.ios.ffan.dashboard_page import DashboardPage
from com.qa.automation.appium.pages.ios.ffan.feifan_card_bill_page import FeiFanCardBillPage
from com.qa.automation.appium.pages.ios.ffan.feifan_card_page import FeiFanCardPage
from com.qa.automation.appium.utility.logger import Logger


class FeiOtherEntranceCasess(TestCase):
    '''
    作者 宋波
    巡检checklist #43
    自动化测试 #43
    首页-飞凡卡查看账单，确认显示零花钱账单页面
    '''

    def tearDown(self):
        self.reset.clearData()
        self.driver.quit()

    def setUp(self):
        self.logger = Logger()
        self.driver = AppiumDriver(None, None, IDC.platformName, IDC.platformVersion,
                                   IDC.deviceName, IDC.driverUrl, IDC.bundleId, IDC.udid).getDriver()
        self.reset = ClearAppData(self.driver)
        self.reset.clearData()
        TestPrepare(self, self.driver, self.logger).prepare()

    def test_case(self):
        dashboardPage = DashboardPage(self , self.driver , self.logger)
        dashboardPage.validSelf()
        dashboardPage.clickOnFeiFanCard()

        feifanCardPage = FeiFanCardPage(self , self.driver , self.logger)
        feifanCardPage.validSelf()

        otherEntranceName = (u"零花钱充值", u"零花钱提现", u"积分", u"市民/公交卡", u"飞凡贷",
                     u"快易花", u"快利来", u"预约理财")
        otherEntrancePageName = (u"零花钱现金充值", u"零花钱现金提现", u"我的飞凡积分", u"市民/公交卡", u"飞凡贷",
                             u"快易花", u"快利来", u"预约理财")
        count = 0;
        for tempNum in range(8):
            count = count + 1
            feifanCardPage.validFeiFanTongOtherEntrance(otherEntrancePageName[count], otherEntranceName[count])



if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(FeiOtherEntranceCasess)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = os.path.join(reportpath, 'Feifan_automation_test_report_' + now + '.html')
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(fp, 'food-test', 'Result for test')
    runner.run(suite)
