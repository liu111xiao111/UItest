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
from cases.android.bp.common.clear_app_data import ClearAppData
from cases.android.bp.common.test_prepare import TestPrepare
from pages.android.shanghu.denglu_page import DengLuPage
from pages.android.shanghu.xuanzemendian_page import XuanZeMenDianPage
from pages.android.shanghu.shouye_page import ShouYePage
from pages.android.shanghu.yuangongguanli_page import YuanGongGuanLiPage
from pages.android.shanghu.xinzengyuangong_page import XinZengYuanGongPage
from pages.android.shanghu.shezhi_page import SheZhiPage
from pages.android.shanghu.dengluxinxi_page import DengLuXinXiPage
from cases.logger import logger


class XinZengYuanGongTestCase(TestCase):
    '''
    巡检 No.4
    用例名 新增员工
    新增员工检查
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

    def testXinZengYuanGong(self):
        shouYePage = ShouYePage(self , self.driver , self.logger)
        dengLuPage = DengLuPage(self , self.driver , self.logger)
        xuanZeMenDianPage = XuanZeMenDianPage(self , self.driver , self.logger)

        shouYePage.validSelf()
        shouYePage.screenShot("shouYe")
        shouYePage.clickOnMemberManager()

        yuanGongGuanLiPage = YuanGongGuanLiPage(self , self.driver , self.logger)
        yuanGongGuanLiPage.screenShot("yuanGongGuanLi")
        yuanGongGuanLiPage.clickOnAddMember()

        xinZengYuanGongPage = XinZengYuanGongPage(self , self.driver , self.logger)
        xinZengYuanGongPage.screenShot("xinZengYuanGong")
        xinZengYuanGongPage.clickOnChooseRole()
        xinZengYuanGongPage.waitBySeconds(2)
        xinZengYuanGongPage.screenShot("xinZengYuanGong")
        xinZengYuanGongPage.inputUserName()
        xinZengYuanGongPage.screenShot("shuRuXingMing")
        xinZengYuanGongPage.inputPhone()
        xinZengYuanGongPage.waitBySeconds(2)
        xinZengYuanGongPage.screenShot("shuRuShouJiHao")
        xinZengYuanGongPage.clickOnSave()

        yuanGongGuanLiPage.waitBySeconds(10)
        yuanGongGuanLiPage.validAddMember()
        yuanGongGuanLiPage.screenShot("renYuanGuanLi")
        yuanGongGuanLiPage.clickBackKey()

        shouYePage.screenShot("shouYe")
        shouYePage.clickOnSetting()

        sheZhiPage = SheZhiPage(self , self.driver , self.logger)
        sheZhiPage.validSelf()
        sheZhiPage.screenShot("sheZhi")
        sheZhiPage.clickOnLogout()
        dengLuPage.screenShot("dengLu")

        dengLuPage.inputMemberPhoneNumber()
        dengLuPage.screenShot("shuRuShouJiHao")
        dengLuPage.inputMemberDefaultPassword()
        dengLuPage.screenShot("shuRuMiMa")
        dengLuPage.clickOnLoginBtn()
        xuanZeMenDianPage.waitBySeconds(2)
        xuanZeMenDianPage.validSelf()
        xuanZeMenDianPage.screenShot("xuanZeMenDian")
        xuanZeMenDianPage.clickOnStore()
        xuanZeMenDianPage.screenShot("xuanZeMenDian")
        xuanZeMenDianPage.clickOnConfirmBtn()

        shouYePage.validSelf()
        shouYePage.screenShot("shouYe")
        shouYePage.clickOnUser()

        dengLuXinXiPage = DengLuXinXiPage(self , self.driver , self.logger)
        dengLuXinXiPage.validSelfNewMember()
        dengLuXinXiPage.screenShot("dengLuXinXi")

        dengLuXinXiPage.clickBackKey()
        shouYePage.screenShot("shouYe")
        shouYePage.clickOnSetting()

        sheZhiPage = SheZhiPage(self , self.driver , self.logger)
        sheZhiPage.validSelf()
        sheZhiPage.screenShot("sheZhi")
        sheZhiPage.clickOnLogout()

        dengLuPage.waitBySeconds(2)
        dengLuPage.validPassword()
        dengLuPage.screenShot("dengLu")


if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(XinZengYuanGongTestCase)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = os.path.join(reportpath, 'Shanghu_automation_test_report_' + now + '.html')
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Shanghu_automation_test_report',
                                           description='Result for test')
    runner.run(suite)