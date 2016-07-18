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


class FeiFanCardBillCases(TestCase):
    '''
    巡检checklist No.: 43
    自动化测试case No.: 43
    首页-飞凡卡查看账单，确认显示零花钱账单页面
    '''

    def tearDown(self):
        self.driver.quit()
        ClearAppData().clearData()

    def setUp(self):
        ClearAppData().clearData()
        self.logger = Logger()
        self.driver = AppiumDriver(None, None, IDC.platformName, IDC.platformVersion,
                                   IDC.deviceName, IDC.driverUrl, IDC.bundleId, IDC.udid).getDriver()
        TestPrepare(self , self.driver , self.logger).prepare()

    def test_case(self):
        dashboardPage = DashboardPage(self , self.driver , self.logger)
        dashboardPage.validSelf()
        dashboardPage.clickOnFeiFanCard()

        feifanCardPage = FeiFanCardPage(self , self.driver , self.logger)
        feifanCardPage.validSelf()
        feifanCardPage.clickOnBill()

        feifanCardBillPage = FeiFanCardBillPage(self , self.driver , self.logger)
        feifanCardBillPage.validSelf()
        for tempText in (u"全部", u"购物金赚取", u"购物金清零", u"现金充值", u"现金提现", u"消费", u"退款"):
            feifanCardBillPage.clickOnFilter()
            feifanCardBillPage.clickOnSubFilterByText(tempText)
            feifanCardBillPage.validSubFilterByText(tempText)
        feifanCardBillPage.clickBackKey()

        feifanCardPage.validSelf()

if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(FeiFanCardBillCases)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = reportpath + 'food-test_' + now + '.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(fp, 'food-test', 'Result for test')
    runner.run(suite)
