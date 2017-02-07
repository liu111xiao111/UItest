# -*- coding:utf-8 -*-

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
from pages.android.ffan.message_centre_page import MessageCentrePage
from pages.android.ffan.message_settings_page import MessageSettingsPage
from pages.android.ffan.my_fei_fan_page import MyFeiFanPage
from utility.logger import Logger
from utility.device_info_util import DeviceInfoUtil
from cases.logger import logger


class WoDeXiaoXiZhongXinTestCase(TestCase):
    '''
    回归用例： No.29
    用例名: 我的排队
    在我的飞凡页面点击进入消息中心，查看各类消息数据显示正确，并可以在设置中进行开关设置，可成功设置
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

    def testWoDeXiaoXiZhongXin(self):
        # 验证首页
        dashboardPage = DashboardPage(self, self.driver, self.logger)
        dashboardPage.validSelf()
        dashboardPage.screenShot("aiGuangJie")

        # 点击我的，进入消息中心
        dashboardPage.clickOnMy()
        myFeiFanPage = MyFeiFanPage(self, self.driver, self.logger)
        myFeiFanPage.screenShot("woDe")
        myFeiFanPage.validSelf()
        myFeiFanPage.clickOnMessageCentre()
        messageCentrePage = MessageCentrePage(self, self.driver, self.logger)
        messageCentrePage.validSelf()
        messageCentrePage.screenShot("xiaoXiZhongXin")

        # 设置开关操作
        messageCentrePage.clickOnSettings()
        messageSettingsPage = MessageSettingsPage(self, self.driver, self.logger)
        messageSettingsPage.validSelf()
        messageSettingsPage.clickOnActivityPush()
        messageSettingsPage.validSelf()
        messageSettingsPage.screenShot("xiaoXiZhongXinSheZhi")


if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(WoDeXiaoXiZhongXinTestCase)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = os.path.join(reportpath, 'Feifan_automation_test_report_' + now + '.html')
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Feifan_automation_test_report', description='Result for test')
    runner.run(suite)
