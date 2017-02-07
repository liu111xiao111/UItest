# -*- coding:utf-8 -*-

import os
import time
from unittest import TestCase
from unittest import TestLoader

import HTMLTestRunner

from cases.android.ffan.common.test_prepare import TestPrepare
from configs.driver_configs import appActivity_ffan
from configs.driver_configs import appPackage_ffan
from configs.driver_configs import deviceName_andr
from configs.driver_configs import driver_url
from configs.driver_configs import platformName_andr
from driver.appium_driver import AppiumDriver
from pages.android.ffan.dashboard_page import DashboardPage
from pages.android.ffan.hui_life_page import HuiLifePage
from utility.device_info_util import DeviceInfoUtil
from utility.logger import Logger
from cases.logger import logger


class HuiShengHuoJingXuanTestCase(TestCase):
    '''
    回归用例： No.18
    用例名: 慧生活精选/荐店
    首页-慧生活查看精选/荐店，点击可进入详情页，可以点赞
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

    def testHuiShengHuoJingXuan(self):
        # 验证首页
        dashboardPage = DashboardPage(self, self.driver, self.logger)
        dashboardPage.validSelf()
        dashboardPage.screenShot("aiGuangJie")

        # 点击慧生活
        dashboardPage.clickOnSmartLife()
        huiLifePage = HuiLifePage(self, self.driver, self.logger)
        huiLifePage.validSelf()
        huiLifePage.screenShot("huiShengHuo")

        # 精选
        huiLifePage.clickOnSelect()
        huiLifePage.validSelfSelect()
        huiLifePage.clickOnSelectDetails()
        huiLifePage.validSelfSelectDetails()
        huiLifePage.screenShot("jingXuanXiangXi")
        huiLifePage.clickBackKey()
        huiLifePage.validSelf()
        huiLifePage.screenShot("jingXuan")

        # 荐店
        huiLifePage.clickOnShop()
        huiLifePage.validSelfShop()
        huiLifePage.screenShot("jianDian")
        huiLifePage.clickOnShopDetails()
        huiLifePage.validSelfShopDetails()
        huiLifePage.screenShot("jianDianXiangXi")


if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(HuiShengHuoJingXuanTestCase)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = os.path.join(reportpath, 'Feifan_automation_test_report_' + now + '.html')
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Feifan_automation_test_report',
                                           description='Result for test')
    runner.run(suite)