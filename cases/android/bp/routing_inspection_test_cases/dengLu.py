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
from pages.android.shanghu.denglu_page import DengLuPage
from pages.android.shanghu.xuanzemendian_page import XuanZeMenDianPage
from pages.android.shanghu.shouye_page import ShouYePage
from pages.android.shanghu.dengluxinxi_page import DengLuXinXiPage
from cases.logger import logger


class DengLuTestCase(TestCase):
    '''
    巡检 No.1
    用例名 登录
    登录验证
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

    def testDengLu(self):
        # 检查是否登录，如果没有登录，进行登录操作
        shouYePage = ShouYePage(self , self.driver , self.logger)
        login = shouYePage.validLogin()

        if not login:
            dengLuPage = DengLuPage(self , self.driver , self.logger)
            dengLuPage.validSelf()
            dengLuPage.screenShot("dengLu")

            dengLuPage.inputUserName()
            dengLuPage.screenShot("yongHuMing")
            dengLuPage.inputPassWord()
            dengLuPage.screenShot("miMa")
            dengLuPage.clickOnLoginBtn()

            xuanZeMenDianPage = XuanZeMenDianPage(self , self.driver , self.logger)
            xuanZeMenDianPage.waitBySeconds(2)
            xuanZeMenDianPage.validSelf()
            xuanZeMenDianPage.waitBySeconds(2)
            xuanZeMenDianPage.screenShot("xuanZeMenDian")
            xuanZeMenDianPage.clickOnStore()
            xuanZeMenDianPage.screenShot("xuanZeMenDian")
            xuanZeMenDianPage.clickOnConfirmBtn()

        # 进入【登录信息】页面后， 验证【姓名】、【手机号】、【登录身份】、【所属商户】信息
        shouYePage.validSelf()
        shouYePage.screenShot("shouYe")
        shouYePage.clickOnUser()

        dengLuXinXiPage = DengLuXinXiPage(self , self.driver , self.logger)
        dengLuXinXiPage.validSelf()
        dengLuXinXiPage.screenShot("dengLuXinXi")


if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(DengLuTestCase)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = os.path.join(reportpath, 'Shanghu_automation_test_report_' + now + '.html')
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Shanghu_automation_test_report',
                                           description='Result for test')
    runner.run(suite)