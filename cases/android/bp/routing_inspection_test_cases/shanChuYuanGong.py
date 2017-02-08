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


class ShanChuYuanGongTestCase(TestCase):
    '''
    巡检 No.8
    用例名 删除员工
    删除员工检查
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

    def testShanChuYuanGong(self):
        # 验证首页
        shouYePage = ShouYePage(self , self.driver , self.logger)
        shouYePage.validSelf()
        shouYePage.screenShot("shouYe")

        # 员工管理 删除员工
        shouYePage.clickOnMemberManager()
        yuanGongGuanLiPage = YuanGongGuanLiPage(self , self.driver , self.logger)
        yuanGongGuanLiPage.validNormalStatus()
        yuanGongGuanLiPage.screenShot("yuanGongGuanLi")
        phoneNum = yuanGongGuanLiPage.getMemberPhone()
        # 如果是指定的自动化测试帐户，可以删除，否则不要删除其他账号
        if phoneNum:
            memberInfo = yuanGongGuanLiPage.getMemberInfo(phoneNum)
            yuanGongGuanLiPage.clickOnDelete(phoneNum)
            yuanGongGuanLiPage.validDeleteMember(memberInfo)
            yuanGongGuanLiPage.screenShot("yuanGongGuanLi")


if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(ShanChuYuanGongTestCase)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = os.path.join(reportpath, 'Shanghu_automation_test_report_' + now + '.html')
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Shanghu_automation_test_report',
                                           description='Result for test')
    runner.run(suite)