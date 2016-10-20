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
from pages.android.ffan.account_management_page import AccountManagementPage
from pages.android.ffan.dashboard_page import DashboardPage
from pages.android.ffan.my_fei_fan_page import MyFeiFanPage
from pages.android.ffan.settings_page import SettingsPage
from pages.android.ffan.update_login_password_page import UpdateLoginPasswordPage
from utility.logger import Logger
from utility.device_info_util import DeviceInfoUtil


class WoDeSheZhiXiuGaiDengLuMiMaTestCase(TestCase):
    '''
    巡检checklist No.: 57
    自动化测试case No.: 57
    点击设置，在账号管理中可以成功修改登录密码，支付密码，小额免密设置
    '''

    def tearDown(self):
        self.reset.clearData()
        self.driver.quit()

    def setUp(self):
        self.logger = Logger()
        self.driver = AppiumDriver(appPackage_ffan,
                                   appActivity_ffan,
                                   platformName_andr,
                                   DeviceInfoUtil().getBuildVersion(),
                                   deviceName_andr,
                                   driver_url).getDriver()

        self.reset = ClearAppData(self.driver)
        self.reset.clearData()

        TestPrepare(self, self.driver, self.logger).prepare()

    def testWoDeSheZhiXiuGaiDengLuMiMa(self):
        dashboardPage = DashboardPage(self, self.driver, self.logger)
        dashboardPage.waitBySeconds()
        dashboardPage.validSelf()
        dashboardPage.clickOnMy()

        myFeiFanPage = MyFeiFanPage(self, self.driver, self.logger)
        myFeiFanPage.waitBySeconds()
        myFeiFanPage.validSelf()
        myFeiFanPage.validLoginStatus()
        myFeiFanPage.clickOnSettings()

        settingPage = SettingsPage(self, self.driver, self.logger)
        settingPage.waitBySeconds()
        settingPage.validSelf()
        settingPage.clickOnAccountManagement()

        accountManagementPage = AccountManagementPage(self, self.driver, self.logger)
        accountManagementPage.validSelf()
        accountManagementPage.clickOnUpdatePassword()

        updateLoginPasswordPage = UpdateLoginPasswordPage(self, self.driver, self.logger)
        updateLoginPasswordPage.waitBySeconds()
        updateLoginPasswordPage.validSelf()
        updateLoginPasswordPage.inputOldLoginPassword("Neu1234!")
        updateLoginPasswordPage.inputNewLoginPassword("Neu1234!")
        updateLoginPasswordPage.inputNewLoginPasswordAgain("Neu1234!")
        updateLoginPasswordPage.clickOnConfirm()

        accountManagementPage.waitBySeconds()
        accountManagementPage.clickBackKey()
        settingPage.clickBackKey()


if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(WoDeSheZhiXiuGaiDengLuMiMaTestCase)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = os.path.join(reportpath + 'Feifan_automation_test_report_' + now + '.html')
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Feifan_automation_test_report', description='Result for test')
    runner.run(suite)
