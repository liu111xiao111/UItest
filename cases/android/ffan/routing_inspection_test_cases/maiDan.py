# -*- coding: utf-8 -*-

import os
import time
import HTMLTestRunner

from unittest import TestCase
from unittest import TestLoader

from cases.android.ffan.common.test_prepare import TestPrepare
from pages.android.ffan.dashboard_page import DashboardPage
from pages.android.ffan.square_lefu_pay_page import SquareLefuPayPage
from pages.android.ffan.lefu_pay_detail_page import LefuPayDetailPage
from pages.android.ffan.lefu_pay_way_page import LefuPayWayPage
from configs.driver_configs import appActivity_ffan
from configs.driver_configs import appPackage_ffan
from configs.driver_configs import deviceName_andr
from configs.driver_configs import driver_url
from configs.driver_configs import platformName_andr
from driver.appium_driver import AppiumDriver
from utility.logger import Logger
from utility.device_info_util import DeviceInfoUtil
from cases.logger import logger


class MaiDanTestCase(TestCase):
    '''
    回归用例： No.8
    用例名: 买单
    首页进入买单（城市维度），验证乐付列表，按距离排序，并下单，取消订单，支付（虚拟城市，
    iOS执行此条请使用蒲公英版本切换到测试城市，使用零花钱支付，使用商户APP进行退款），
    并查看相应订单状态
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

    def testMaiDan(self):
        # 验证首页
        dashboardPage = DashboardPage(self, self.driver, self.logger)
        dashboardPage.validSelf();
        dashboardPage.screenShot("aiGuangJie")

        # 首页(爱逛街页面)点击买单，验证买单列表，按距离排序
        dashboardPage.clickOnLefuCategory()
        lefuPage = SquareLefuPayPage(self, self.driver, self.logger)
        lefuPage.validSelf();
        lefuPage.screenShot("maiDan")

        # 下单
        lefuPage.clickOnLefuPay();
        lefuPayDetailPage = LefuPayDetailPage(self, self.driver, self.logger)
        lefuPayDetailPage.validSelf();
        lefuPayDetailPage.screenShot("maiDanFuKuan")
        lefuPayDetailPage.inputMoney();
        lefuPayDetailPage.screenShot("maiDanFuKuan")
        lefuPayDetailPage.waitBySeconds(seconds=5)
        lefuPayDetailPage.clickOnPay();
        lefuPayWayPage = LefuPayWayPage(self, self.driver, self.logger)
        lefuPayWayPage.validSelf();
        lefuPayWayPage.screenShot("maiDanFuKuanFangShi")

        # 取消订单
        lefuPayWayPage.clickOnBackFromPay()
        lefuPayWayPage.validSelfCanclePopup()
        lefuPayWayPage.screenShot("quXiaoDingDanPopUp")
        lefuPayWayPage.clickOnConfirmFromCancel()
        lefuPayWayPage.validSelfAllOrders()
        lefuPayWayPage.screenShot("quXiaoDingDan")


if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(MaiDanTestCase)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = os.path.join(reportpath, 'Feifan_automation_test_report_' + now + '.html')
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Feifan_automation_test_report',
                                           description='Result for test')
    runner.run(suite)