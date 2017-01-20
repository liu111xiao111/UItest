# -*- coding:utf-8 -*-

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
from pages.android.ffan.message_centre_page import MessageCentrePage
from pages.android.ffan.message_settings_page import MessageSettingsPage
from pages.android.ffan.my_fei_fan_page import MyFeiFanPage
from utility.logger import Logger
from utility.device_info_util import DeviceInfoUtil
from cases.logger import logger


class WoDeXiaoXiZhongXinTestCase(TestCase):
    '''
    巡检 No.61
    用例名 我的消息中心
    在我的飞凡页面点击进入消息中心，查看各类消息数据显示正确，并可以在设置中设置
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
        dashboardPage = DashboardPage(self, self.driver, self.logger)
        dashboardPage.validSelf()
        dashboardPage.screenShot("aiGuangJie")
        dashboardPage.clickOnMy()

        myFeiFanPage = MyFeiFanPage(self, self.driver, self.logger)
        myFeiFanPage.screenShot("woDe")
        myFeiFanPage.validSelf()
        myFeiFanPage.clickOnMessageCentre()

        messageCentrePage = MessageCentrePage(self, self.driver, self.logger)
        messageCentrePage.validSelf()
        messageCentrePage.screenShot("xiaoXiZhongXin")
        '''
        messageCentrePage.clickOnFeiFanActivity()

        feiFanActivityPage = FeiFanActivityPage(self, self.driver, self.logger)
        feiFanActivityPage.validSelf()
        feiFanActivityPage.clickBackKey()

        messageCentrePage.validSelf()
        messageCentrePage.clickOnSquareDynamic()

        squareDynamicPage = SquareDynamicPage(self, self.driver, self.logger)
        squareDynamicPage.validSelf()
        squareDynamicPage.clickBackKey()

        messageCentrePage.validSelf()
        messageCentrePage.clickOnBrandActivity()

        brandActivityPage = BrandActivityPage(self, self.driver, self.logger)
        brandActivityPage.validSelf()
        brandActivityPage.clickBackKey()

        messageCentrePage.validSelf()
        messageCentrePage.clickOnStoreMessage()

        storeMessagePage = StoreMessagePage(self, self.driver, self.logger)
        storeMessagePage.validSelf()
        storeMessagePage.clickBackKey()

        messageCentrePage.validSelf()
        '''


        messageCentrePage.clickOnSettings()

        messageSettingsPage = MessageSettingsPage(self, self.driver, self.logger)
        messageSettingsPage.validSelf()
        messageSettingsPage.clickOnActivityPush()
        messageSettingsPage.clickBackKey()
        messageCentrePage.clickBackKey()

if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(WoDeXiaoXiZhongXinTestCase)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = os.path.join(reportpath, 'Feifan_automation_test_report_' + now + '.html')
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Feifan_automation_test_report', description='Result for test')
    runner.run(suite)
