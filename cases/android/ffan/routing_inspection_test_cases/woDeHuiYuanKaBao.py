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
from pages.android.ffan.fei_fan_membership_page import FeiFanMembershipPage
from pages.android.ffan.my_fei_fan_page import MyFeiFanPage
from pages.android.ffan.my_membership_card_package_page import MyMembershipCardPackagePage
from utility.logger import Logger
from utility.device_info_util import DeviceInfoUtil
from cases.logger import logger


class WoDeHuiYuanKaBaoTestCase(TestCase):
    '''
    回归用例： No.25
    用例名: 我的会员卡包
    点击进入我的会员卡包，查看数据是否显示正常并可进入会员页 
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

    def testWoDeHuiYuanKaBao(self):
        # 验证首页
        dashboardPage = DashboardPage(self, self.driver, self.logger)
        dashboardPage.validSelf()
        dashboardPage.screenShot("aiGuangJie")

        # 点击我的，验证会员卡包
        dashboardPage.clickOnMy()
        myFeiFanPage = MyFeiFanPage(self, self.driver, self.logger)
        myFeiFanPage.validSelf()
        myFeiFanPage.screenShot("woDe")
        myFeiFanPage.clickOnMembershipCardPackage()
        myMembershipCardPackagePage = MyMembershipCardPackagePage(self, self.driver, self.logger)
        myMembershipCardPackagePage.waitBySeconds(2)
        myMembershipCardPackagePage.validSelf()
        myMembershipCardPackagePage.screenShot("huiYuanKaBao")
        myMembershipCardPackagePage.clickOnLeHuoKa()
        feiFanMembershipPage = FeiFanMembershipPage(self, self.driver, self.logger)
        feiFanMembershipPage.validSelf()
        feiFanMembershipPage.screenShot("leHuoKa")


if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(WoDeHuiYuanKaBaoTestCase)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = os.path.join(reportpath, 'Feifan_automation_test_report_' + now + '.html')
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Feifan_automation_test_report', description='Result for test')
    runner.run(suite)
