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
from pages.android.shanghu.yuangongguanli_page import YuanGongGuanLiPage
from cases.logger import logger


class DongJieYuanGongTestCase(TestCase):
    '''
    巡检 No.6
    用例名 冻结员工
    冻结员工检查
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
        logger.info("Appium client init completed")

        self.reset = ClearAppData(self.driver)
        self.reset.clearData()
        logger.info("Clear data completed")

        TestPrepare(self, self.driver, self.logger).prepare()

    def testDongJieYuanGong(self):
        shouYePage = ShouYePage(self , self.driver , self.logger)

        shouYePage.validSelf()
        shouYePage.screenShot("shouYe")
        shouYePage.clickOnMemberManager()

        yuanGongGuanLiPage = YuanGongGuanLiPage(self , self.driver , self.logger)
        yuanGongGuanLiPage.validNormalStatus()
        yuanGongGuanLiPage.screenShot("yuanGongGuanLi")
        memberInfo = yuanGongGuanLiPage.getMemberInfo(1)
        yuanGongGuanLiPage.clickOnFreeze()
        yuanGongGuanLiPage.waitBySeconds(2)
        yuanGongGuanLiPage.screenShot("dongJie")
        yuanGongGuanLiPage.clickOnFreezeStatus()
        yuanGongGuanLiPage.waitBySeconds(2)
        yuanGongGuanLiPage.validFreezeMemberInfo(memberInfo)
        yuanGongGuanLiPage.screenShot("yuanGongGuanLi")


if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(DongJieYuanGongTestCase)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = os.path.join(reportpath, 'Shanghu_automation_test_report_' + now + '.html')
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Shanghu_automation_test_report',
                                           description='Result for test')
    runner.run(suite)