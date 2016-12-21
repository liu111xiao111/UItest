# -*- coding: utf-8 -*-

from unittest import TestCase
from configs.iosDriverConfig import IosDriverConfigs as IDC
from driver.appium_driver import AppiumDriver
from utility.logger import Logger
from cases.ios.bp.common.prepare import Prepare
from pages.ios.shanghu.homePage import HomePage
from pages.ios.shanghu.bussinessSchoolPage import BussinessSchoolPage


class ShangXueYuanRuKou(TestCase):
    '''
    商学院入口检查
    '''

    def setUp(self):
        self.logger = Logger()
        self.driver = AppiumDriver(None, None, IDC.platformName, IDC.platformVersion,
                                   IDC.deviceName, IDC.driverUrl, IDC.bundleId_sh, IDC.udid).getDriver()

        prepare = Prepare(self, self.driver, self.logger)
        prepare.login()

    def test_case(self):
        homePage = HomePage(self, self.driver, self.logger)
        bussinessSchoolPage = BussinessSchoolPage(self, self.driver, self.logger)

        homePage.clickOnBusinessSchool()

        #进入常见问题
        bussinessSchoolPage.enterCommonQuestions()
        bussinessSchoolPage.checkCommonQuestionsItems()
        bussinessSchoolPage.back()

        #进入新手指南
        bussinessSchoolPage.enterNewerGuide()
        bussinessSchoolPage.checkNewergudieItems()
        bussinessSchoolPage.back()

        bussinessSchoolPage.enterSellerNotices()
        bussinessSchoolPage.checkSellerNoticesItems()
        bussinessSchoolPage.back()

        homePage.waitBySeconds(10)

    def tearDown(self):
        self.driver.quit()