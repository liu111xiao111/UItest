# -*- coding: utf-8 -*-

import os
import time
import HTMLTestRunner

from unittest import TestCase
from unittest import TestLoader

from cases.android.ffan.common.test_prepare import TestPrepare
from cases.android.ffan.common.clear_app_data import ClearAppData
from pages.android.ffan.dashboard_page import DashboardPage
from pages.android.ffan.feifan_card_page import FeiFanCardPage
from pages.android.ffan.feifan_card_payment_page import FeiFanCardPaymentPage
from configs.driver_configs import appActivity_ffan
from configs.driver_configs import appPackage_ffan
from configs.driver_configs import deviceName_andr
from configs.driver_configs import driver_url
from configs.driver_configs import platformName_andr
from driver.appium_driver import AppiumDriver
from utility.logger import Logger
from utility.device_info_util import DeviceInfoUtil


class WoDeFuKuanMaTestCase(TestCase):
    '''
    作者 乔佳溪
    巡检checklist #54
    自动化测试 #54
    我的付款码
    '''

    def tearDown(self):
        self.reset.clearData()
        self.driver.quit()

    def setUp(self):
        self.logger = Logger()
        self.platVersion = DeviceInfoUtil().getBuildVersion()
        self.driver = AppiumDriver(appPackage_ffan, appActivity_ffan, platformName_andr,
                                   self.platVersion, deviceName_andr,
                                   driver_url).getDriver()

        self.reset = ClearAppData(self.driver)
        self.reset.clearData()

        TestPrepare(self, self.driver, self.logger).prepare()

    def testWoDeFuKuanMa(self):
        dashboardPage = DashboardPage(self , self.driver , self.logger)
        dashboardPage.validSelf()
        dashboardPage.clickOnFeiFanCard()

        feifanCardPage = FeiFanCardPage(self , self.driver , self.logger)
        feifanCardPage.validSelf()

        feifanCardPage.clickOnCodeIcon()

        if int(self.platVersion.split(".")[0]) >= 5:
            feifanCardPage.clickOnPaymentCode()
            feifanCardPaymentPage = FeiFanCardPaymentPage(self , self.driver , self.logger)
            feifanCardPaymentPage.validSelf()
            feifanCardPaymentPage.clickBackKey()
        feifanCardPage.validSelf()

if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(WoDeFuKuanMaTestCase)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = os.path.join(reportpath, 'Feifan_automation_test_report_' + now + '.html')
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Feifan_automation_test_report',
                                           description='Result for test')
    runner.run(suite)