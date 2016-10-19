# -*- coding: utf-8 -*-

import os
import time
import HTMLTestRunner

from unittest import TestCase
from unittest import TestLoader

from cases.android.ffan.common.clear_app_data import ClearAppData
from cases.android.ffan.common.test_prepare import TestPrepare
from configs.driver_configs import appActivity_ffan
from configs.driver_configs import appPackage_ffan
from configs.driver_configs import deviceName_andr
from configs.driver_configs import driver_url
from configs.driver_configs import platformName_andr
from driver.appium_driver import AppiumDriver
from pages.android.ffan.dashboard_page import DashboardPage
from pages.android.ffan.feifan_card_charge_page import FeiFanCardChargePage
from pages.android.ffan.feifan_card_page import FeiFanCardPage
from pages.android.ffan.feifan_card_bill_page import FeiFanCardBillPage
from utility.logger import Logger
from utility.device_info_util import DeviceInfoUtil


class FeiFanTongLingHuaQianTestCase(TestCase):
    '''
    作者 乔佳溪
    巡检checklist No.: 44
    自动化测试case No.: 44
    首页-飞凡通查看零花钱，确认零花钱页面显示正确，进行充值和提现，确认功能正常
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

        TestPrepare(self, self.driver, self.logger).prepare()

    def testFeiFanTongLingHuaQian(self):
        dashboardPage = DashboardPage(self , self.driver , self.logger)
        dashboardPage.validSelf()
        dashboardPage.clickOnFeiFanCard()

        feifanCardPage = FeiFanCardPage(self , self.driver , self.logger)
        feifanCardPage.validSelf()
        feifanCardPage.clickOnCharge()
        feifanCardChargePage = FeiFanCardChargePage(self , self.driver , self.logger)
        feifanCardChargePage.validSelf()
        feifanCardChargePage.clickOnBill()
        feifanCardBillPage = FeiFanCardBillPage(self , self.driver , self.logger)
        feifanCardBillPage.validSelf()

if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(FeiFanTongLingHuaQianTestCase)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = os.path.join(reportpath, 'Feifan_automation_test_report_' + now + '.html')
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Feifan_automation_test_report',
                                           description='Result for test')
    runner.run(suite)
