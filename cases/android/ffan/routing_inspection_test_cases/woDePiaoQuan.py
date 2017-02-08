# -*- coding: utf-8 -*-

import os
import time
import HTMLTestRunner

from unittest import TestCase
from unittest import TestLoader

from cases.android.ffan.common.test_prepare import TestPrepare
from pages.android.ffan.dashboard_page import DashboardPage
from pages.android.ffan.my_ffan_page import MyFfanPage
from pages.android.ffan.my_ffan_my_ticket_page import MyFfanMyTicketPage
from configs.driver_configs import appActivity_ffan
from configs.driver_configs import appPackage_ffan
from configs.driver_configs import deviceName_andr
from configs.driver_configs import driver_url
from configs.driver_configs import platformName_andr
from driver.appium_driver import AppiumDriver
from utility.logger import Logger
from utility.device_info_util import DeviceInfoUtil
from cases.logger import logger


class WoDePiaoQuanTestCase(TestCase):
    '''
    回归用例： No.23
    用例名: 我的票券
    查看我的票券里数据显示正常 
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

    def testWoDePiaoQuan(self):
        # 验证首页
        dashboardPage = DashboardPage(self, self.driver, self.logger)
        dashboardPage.validSelf()
        dashboardPage.screenShot("aiGuangJie")

        # 点击我的，查看票券
        dashboardPage.clickOnMy()
        myFfanPage = MyFfanPage(self, self.driver, self.logger)
        myFfanPage.validSelf()
        myFfanPage.screenShot("woDe")
        ticketNumber = myFfanPage.getTicketNumber()
        myFfanPage.clickOnMyTicket()
        myTicketPage = MyFfanMyTicketPage(self, self.driver, self.logger)
        myTicketPage.validSelf()
        myTicketPage.validTicketNumber(ticketNumber)
        myTicketPage.screenShot("woDePiaoQuan")


if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(WoDePiaoQuanTestCase)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = os.path.join(reportpath, 'Feifan_automation_test_report_' + now + '.html')
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Feifan_automation_test_report',
                                           description='Result for test')
    runner.run(suite)
