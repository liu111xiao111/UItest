# -*- coding: utf-8 -*-

import os
import time
import HTMLTestRunner

from unittest import TestCase
from unittest import TestLoader

from pages.android.ffan.dashboard_page import DashboardPage
from pages.android.ffan.feifan_card_page import FeiFanCardPage
from pages.android.ffan.feifan_card_integral_page import FeiFanCardIntegralPage
from configs.driver_configs import appActivity_ffan
from configs.driver_configs import appPackage_ffan
from configs.driver_configs import deviceName_andr
from configs.driver_configs import driver_url
from configs.driver_configs import platformName_andr
from driver.appium_driver import AppiumDriver
from utility.logger import Logger
from utility.device_info_util import DeviceInfoUtil
from cases.android.ffan.common.test_prepare import TestPrepare
from cases.android.ffan.common.clear_app_data import ClearAppData


class FeiFanTongQiTaKuaiJieRuKouTestCase(TestCase):
    '''
    作者 刘涛
    巡检checklist #45
    自动化测试 #45
    首页-飞凡卡点击积分，确认显示积分主页页面
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

    def testFeiFanTongQiTaKuaiJieRuKou(self):
        dashboardPage = DashboardPage(testcase=self, driver=self.driver, logger=self.logger)
        ffanCardPage = FeiFanCardPage(testcase=self, driver=self.driver, logger=self.logger)
        ffanCardIntegralPage = FeiFanCardIntegralPage(testcase=self, driver=self.driver, logger=self.logger)

        # Click "飞凡卡", load Feifan card page.
        dashboardPage.validSelf();
        dashboardPage.clickOnFeiFanCard();
        ffanCardPage.validSelf();

        # Click "积分", load "积分主页"
        ffanCardPage.clickOnIntegral();
        ffanCardIntegralPage.validSelf();


if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(FeiFanTongQiTaKuaiJieRuKouTestCase)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = os.path.join(reportpath, 'Feifan_automation_test_report_' + now + '.html')
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Feifan_automation_test_report',
                                           description='Result for test')
    runner.run(suite)