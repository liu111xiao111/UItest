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
from pages.android.shanghu.jueseguanli_page import JueSeGuanLiPage
from pages.android.shanghu.xinjianjuese_page import XinJianJueSePage
from cases.logger import logger


class XinZengJueSeTestCase(TestCase):
    '''
    巡检 No.10
    用例名 新增角色
    新增角色检查
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

    def testXinZengJueSe(self):
        # 验证首页
        shouYePage = ShouYePage(self , self.driver , self.logger)
        shouYePage.validSelf()
        shouYePage.screenShot("shouYe")

        # 角色管理，新增角色
        shouYePage.clickOnRoleManager()
        jueSeGuanLiPage = JueSeGuanLiPage(self , self.driver , self.logger)
        jueSeGuanLiPage.validSelf()
        jueSeGuanLiPage.screenShot("jueSeGuanLi")
        jueSeGuanLiPage.clickOnAddRole()
        xinJianJueSePage = XinJianJueSePage(self , self.driver , self.logger)
        xinJianJueSePage.waitBySeconds(2)
        xinJianJueSePage.validSelf()
        xinJianJueSePage.screenShot("xinJianJueSe")
        xinJianJueSePage.inputRoleName()
        xinJianJueSePage.screenShot("jueSeMingCheng")
        xinJianJueSePage.clickOnFunctionalAutority()
        xinJianJueSePage.waitBySeconds(2)
        xinJianJueSePage.clickOnSave()
        xinJianJueSePage.validFunctionalAutority()
        xinJianJueSePage.screenShot("xinJianJueSe")
        xinJianJueSePage.inputRoleInstruction()
        xinJianJueSePage.screenShot("xinJianJueSe")
        xinJianJueSePage.clickOnSave()
        jueSeGuanLiPage.screenShot("jueSeGuanLi")


if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(XinZengJueSeTestCase)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = os.path.join(reportpath, 'Shanghu_automation_test_report_' + now + '.html')
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Shanghu_automation_test_report',
                                           description='Result for test')
    runner.run(suite)