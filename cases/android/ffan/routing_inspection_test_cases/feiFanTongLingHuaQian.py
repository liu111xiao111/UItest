# -*- coding: utf-8 -*-

import os
import time
import HTMLTestRunner

from unittest import TestCase
from unittest import TestLoader

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
from utility.logger import Logger
from utility.device_info_util import DeviceInfoUtil
from cases.logger import logger


class FeiFanTongLingHuaQianTestCase(TestCase):
    '''
    回归用例： No.19
    用例名: 飞凡通零花钱
    首页-飞凡通查看零花钱，确认零花钱页面显示正确，进行充值和提现，确认功能正常
    '''
    @classmethod
    def setUpClass(cls):
        '''
        初始化Appium driver
        '''
        cls.driver = AppiumDriver(appPackage_ffan,
                                   appActivity_ffan,
                                   platformName_andr,
                                   DeviceInfoUtil().getBuildVersion(),
                                   deviceName_andr,
                                   driver_url).getDriver()
        logger.info("Appium client init completed")

    def tearDown(self):
        self.driver.quit()

    def setUp(self):
        self.logger = Logger()
        TestPrepare(self, self.driver, self.logger).prepare()

    def testFeiFanTongLingHuaQian(self):
        # 验证首页
        dashboardPage = DashboardPage(self , self.driver , self.logger)
        dashboardPage.validSelf()
        dashboardPage.screenShot("aiGuangJie")

        # 点击飞凡通
        dashboardPage.clickOnFeiFanCard()
        feifanCardPage = FeiFanCardPage(self , self.driver , self.logger)
        feifanCardPage.validSelf()
        feifanCardPage.screenShot("feiFanTong")
        feifanCardPage.clickOnCharge()
        feifanCardChargePage = FeiFanCardChargePage(self , self.driver , self.logger)
        feifanCardChargePage.validSelf()
        feifanCardChargePage.screenShot("lingHuaQian")


if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(FeiFanTongLingHuaQianTestCase)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = os.path.join(reportpath, 'Feifan_automation_test_report_' + now + '.html')
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Feifan_automation_test_report',
                                           description='Result for test')
    runner.run(suite)
