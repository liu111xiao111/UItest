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
from cases.android.bp.common.test_prepare import TestPrepare
from pages.android.shanghu.shouye_page import ShouYePage
from pages.android.shanghu.yuangongguanli_page import YuanGongGuanLiPage
from cases.logger import logger


class JieDongYuanGongTestCase(TestCase):
    '''
    巡检 No.7
    用例名 解冻员工检查
    解冻员工检查
    '''
    @classmethod
    def setUpClass(cls):
        '''
        初始化Appium driver
        '''
        cls.driver = AppiumDriver(appPackage_bp,
                                  appActivity_bp,
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

    def testJieDongYuanGong(self):
        # 验证首页
        shouYePage = ShouYePage(self , self.driver , self.logger)
        shouYePage.validSelf()
        shouYePage.screenShot("shouYe")

        # 员工管理，解冻员工
        shouYePage.clickOnMemberManager()
        yuanGongGuanLiPage = YuanGongGuanLiPage(self , self.driver , self.logger)
        yuanGongGuanLiPage.validNormalStatus()
        yuanGongGuanLiPage.screenShot("yuanGongGuanLi")
        yuanGongGuanLiPage.clickOnFreezeStatus()
        yuanGongGuanLiPage.screenShot("yuanGongGuanLi")
        freezeData = yuanGongGuanLiPage.validFreezeData()
        if freezeData:
            memberInfo = yuanGongGuanLiPage.getFreezeMemberInfo()
            yuanGongGuanLiPage.clickOnUnfreeze()
            yuanGongGuanLiPage.waitBySeconds(2)
            yuanGongGuanLiPage.screenShot("jieDong")
            yuanGongGuanLiPage.clickOnNormalStatus()
            yuanGongGuanLiPage.waitBySeconds(5)
            yuanGongGuanLiPage.validNormalMemberInfo(memberInfo)
            yuanGongGuanLiPage.screenShot("yuanGongGuanLi")


if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(JieDongYuanGongTestCase)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = os.path.join(reportpath, 'Shanghu_automation_test_report_' + now + '.html')
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Shanghu_automation_test_report',
                                           description='Result for test')
    runner.run(suite)