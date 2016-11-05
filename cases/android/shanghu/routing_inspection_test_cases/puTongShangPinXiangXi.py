# -*- coding: utf-8 -*-

import os
import time
import HTMLTestRunner

from unittest import TestCase
from unittest import TestLoader
from cases.android.shanghu.common.test_prepare import TestPrepare

from configs.driver_configs import platformName_andr
from configs.driver_configs import appPackage_bp
from configs.driver_configs import appActivity_bp
from configs.driver_configs import deviceName_andr
from configs.driver_configs import driver_url
from driver.appium_driver import AppiumDriver
from utility.logger import Logger
from utility.device_info_util import DeviceInfoUtil
from cases.android.shanghu.common.clear_app_data import ClearAppData
from pages.android.shanghu.shouye_page import ShouYePage
from pages.android.shanghu.shangpinguanli_page import ShangPinGuanLiPage


class PuTongShangPinTestCase(TestCase):
    '''
    巡检 No.15
    用例名 普通商品
    普通商品快速检查
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

        self.reset = ClearAppData(self.driver)
        self.reset.clearData()

        TestPrepare(self, self.driver, self.logger).prepare()

    def testPuTongShangPin(self):
        shouYePage = ShouYePage(self , self.driver , self.logger)
        shouYePage.validSelf()
        shouYePage.clickOnShangPinGuanLi()

        shangPinGuanLiPage = ShangPinGuanLiPage(self , self.driver , self.logger)
        shangPinGuanLiPage.clickOnGoods()
        itemNum = shangPinGuanLiPage.getGoodsNumber()
        if itemNum[0] != '0':
            shangPinGuanLiPage.validTempSave()
            tempSave = shangPinGuanLiPage.getTempSaveDetails()
            shangPinGuanLiPage.clickOnTempSaveDetails()
            shangPinGuanLiPage.validDetails(title = tempSave)
            shangPinGuanLiPage.clickBackKey()
            shangPinGuanLiPage.clickBackKey()
        if itemNum[1] != '0':
            shangPinGuanLiPage.validToBeExamined()
            toBeExamined = shangPinGuanLiPage.getToBeExaminedDetails()
            shangPinGuanLiPage.clickOnToBeExaminedDetails()
            shangPinGuanLiPage.validDetails(title = toBeExamined)
            shangPinGuanLiPage.clickBackKey()
            shangPinGuanLiPage.clickBackKey()
        if itemNum[2] != '0':
            shangPinGuanLiPage.validPassed()
            passedDetails = shangPinGuanLiPage.getPassedDetails()
            shangPinGuanLiPage.clickOnPassedDetails()
            shangPinGuanLiPage.validDetails(title = passedDetails)
            shangPinGuanLiPage.clickBackKey()
            shangPinGuanLiPage.clickBackKey()
        if itemNum[3] != '0':
            shangPinGuanLiPage.validReject()
            rejectDetails = shangPinGuanLiPage.getRejectDetails()
            shangPinGuanLiPage.clickOnRejectDetails()
            shangPinGuanLiPage.validDetails(title = rejectDetails)


if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(PuTongShangPinTestCase)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = os.path.join(reportpath, 'Shanghu_automation_test_report_' + now + '.html')
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Shanghu_automation_test_report',
                                           description='Result for test')
    runner.run(suite)