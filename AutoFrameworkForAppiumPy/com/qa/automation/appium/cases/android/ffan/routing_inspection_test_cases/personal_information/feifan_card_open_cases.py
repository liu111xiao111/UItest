# -*- coding: utf-8 -*-

import os
import time
import HTMLTestRunner

from unittest import TestCase
from unittest import TestLoader

from com.qa.automation.appium.pages.android.ffan.feifan_card_page import FeiFanCardPage
from com.qa.automation.appium.pages.android.ffan.dashboard_page import DashboardPage
from com.qa.automation.appium.pages.android.ffan.open_card_page import OpenCardPage
from com.qa.automation.appium.configs.driver_configs import platformName_andr
from com.qa.automation.appium.configs.driver_configs import appActivity_ffan
from com.qa.automation.appium.configs.driver_configs import appPackage_ffan
from com.qa.automation.appium.configs.driver_configs import deviceName_andr
from com.qa.automation.appium.configs.driver_configs import driver_url
from com.qa.automation.appium.driver.appium_driver import AppiumDriver
from com.qa.automation.appium.utility.logger import Logger
from com.qa.automation.appium.utility.device_info_util import DeviceInfoUtil
from com.qa.automation.appium.cases.android.ffan.common.clear_app_data import ClearAppData
from com.qa.automation.appium.cases.android.ffan.common.test_prepare import TestPrepare


class FeiFanCardOpenCases(TestCase):
    '''
    作者 刘涛
    巡检checklist No.: 44
    自动化测试case No.: 44
    首页飞凡卡界面，点击市民/公交卡，验证飞凡标准卡及一卡通飞凡联名卡
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

    def test_case(self):
        dashboardPage = DashboardPage(self, self.driver, self.logger)
        feifanCardPage = FeiFanCardPage(self, self.driver, self.logger)
        openCardPage = OpenCardPage(self, self.driver, self.logger)

        # Verify Home Page
        dashboardPage.validSelf()

        # Launch Child Category Page and verify
        dashboardPage.clickOnFeiFanCard()
        feifanCardPage.validSelf()

        feifanCardPage.clickOnOpenCard()
        openCardPage.validSelf()

        openCardPage.validFeifanCard()
        openCardPage.validJointCard()

if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(FeiFanCardOpenCases)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = reportpath + 'food-test_' + now + '.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='feifan-card-test',
                                           description='Result for test')
    runner.run(suite)
