# -*- coding: utf-8 -*-

import os
import time
import HTMLTestRunner

from unittest import TestCase
from unittest import TestLoader

from configs.driver_configs import platformName_andr
from configs.driver_configs import appPackage_bp
from configs.driver_configs import appActivity_bp
from configs.driver_configs import deviceName_andr
from configs.driver_configs import driver_url
from driver.appium_driver import AppiumDriver
from utility.logger import Logger
from utility.device_info_util import DeviceInfoUtil
from cases.android.shanghu.common.clear_app_data import ClearAppData
from cases.android.shanghu.common.test_prepare import TestPrepare
from pages.android.shanghu.shouye_page import ShouYePage
from pages.android.shanghu.dingdanguanli_page import DingDanGuanLiPage


class JiaoYiGuanBiDingDanTestCase(TestCase):
    '''
    巡检 No.12
    用例名 交易关闭订单
    交易关闭订单状态检查
    '''
    def tearDown(self):
        self.reset.clearData()
        self.driver.quit()

    def setUp(self):
        self.logger = Logger()
        self.driver = AppiumDriver(appPackage_bp,
                                   appActivity_bp,
                                   platformName_andr,
                                   DeviceInfoUtil().getBuildVersion(),
                                   deviceName_andr,
                                   driver_url).getDriver()

        self.reset = ClearAppData(self.driver)
        self.reset.clearData()

        TestPrepare(self, self.driver, self.logger).prepare()

    def testJiaoYiGuanBiDingDan(self):
        shouYePage = ShouYePage(self , self.driver , self.logger)
        shouYePage.validSelf()
        shouYePage.clickOnOrderManager()

        dingDanGuanLiPage = DingDanGuanLiPage(self , self.driver , self.logger)
        dingDanGuanLiPage.validSelf()
        dingDanGuanLiPage.clickOnOrderStatus()
        dingDanGuanLiPage.clickOnClosedOrder()


if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(JiaoYiGuanBiDingDanTestCase)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = os.path.join(reportpath, 'Shanghu_automation_test_report_' + now + '.html')
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Shanghu_automation_test_report',
                                           description='Result for test')
    runner.run(suite)