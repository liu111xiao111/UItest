# -*- coding: utf-8 -*-

import os
import time
import HTMLTestRunner

from unittest import TestCase
from unittest import TestLoader

from com.qa.automation.appium.cases.android.ffan.common.clear_app_data import ClearAppData
from com.qa.automation.appium.cases.android.ffan.common.test_prepare import TestPrepare
from com.qa.automation.appium.configs.driver_configs import appActivity_ffan
from com.qa.automation.appium.configs.driver_configs import appPackage_ffan
from com.qa.automation.appium.configs.driver_configs import deviceName_andr
from com.qa.automation.appium.configs.driver_configs import driver_url
from com.qa.automation.appium.configs.driver_configs import platformName_andr
from com.qa.automation.appium.driver.appium_driver import AppiumDriver
from com.qa.automation.appium.pages.android.ffan.dashboard_page import DashboardPage
from com.qa.automation.appium.pages.android.ffan.feifan_card_bill_page import FeiFanCardBillPage
from com.qa.automation.appium.pages.android.ffan.feifan_card_page import FeiFanCardPage
from com.qa.automation.appium.utility.logger import Logger
from com.qa.automation.appium.utility.device_info_util import DeviceInfoUtil


class FeiFanCardBillCases(TestCase):
    '''
    巡检checklist No.: 43
    自动化测试case No.: 43
    首页-飞凡卡查看账单，确认显示零花钱账单页面
    '''

    def tearDown(self):
        self.reset.clearData()
        self.driver.quit()

    def setUp(self):
        self.logger = Logger()
        self.driver = AppiumDriver(appPackage_ffan,
                                   appActivity_ffan,
                                   platformName_andr,
                                   DeviceInfoUtil().getBuildVersion(),
                                   deviceName_andr,
                                   driver_url).getDriver()

        self.reset = ClearAppData(self.driver)
        self.reset.clearData()

        TestPrepare(self, self.driver, self.logger).prepare()

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
