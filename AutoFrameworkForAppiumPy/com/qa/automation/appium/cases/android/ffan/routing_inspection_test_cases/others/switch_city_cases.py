# -*- coding:utf-8 -*-

import os
import time
import logging
from unittest import TestCase
from unittest import TestLoader

import HTMLTestRunner

from com.qa.automation.appium.cases.android.ffan.common.clear_app_data import ClearAppData
from com.qa.automation.appium.configs.driver_configs import appActivity_ffan
from com.qa.automation.appium.configs.driver_configs import appPackage_ffan
from com.qa.automation.appium.configs.driver_configs import deviceName_andr
from com.qa.automation.appium.configs.driver_configs import driver_url
from com.qa.automation.appium.configs.driver_configs import platformName_andr
from com.qa.automation.appium.driver.appium_driver import AppiumDriver
from com.qa.automation.appium.pages.android.ffan.love_shopping_page import LoveShoppingPage
from com.qa.automation.appium.pages.android.ffan.switch_city_page import SwitchCityPage
from com.qa.automation.appium.utility.device_info_util import DeviceInfoUtil
from com.qa.automation.appium.utility.logger import Logger


class SwitchCityCases(TestCase):
    '''
    巡检checklist No.: 02
    自动化测试case No.: 02
    启动APP，城市切换正常
    '''

    def tearDown(self):
        self.reset.clearData()
        self.driver.quit()

    def setUp(self):
        self.logger = Logger()
        self.driver = AppiumDriver(appPackage_ffan, appActivity_ffan, platformName_andr,
                                   DeviceInfoUtil().getBuildVersion(), deviceName_andr,
                                   driver_url).getDriver()
        self.reset = ClearAppData(self.driver)

    def test_case_step_1(self):
        switchCityPage = SwitchCityPage(self, self.driver, self.logger)
        for tempTimes in range(5):
            logging.info("ATTEMPTS: %d" % (tempTimes + 1))
            if switchCityPage.validSelf(False):
                return
            switchCityPage.waitBySeconds(2)

        loveShoppingPage = LoveShoppingPage(self, self.driver, self.logger)
        loveShoppingPage.validSelf()
        tempCityName = loveShoppingPage.getCurrentCityName()
        loveShoppingPage.clickOnCityName()
        loveShoppingPage.waitBySeconds()
        loveShoppingPage.switchCity(tempCityName)
        loveShoppingPage.validSelf()

    def test_case_step_2(self):
        switchCityPage = SwitchCityPage(self, self.driver, self.logger)
        for tempTimes in range(5):
            logging.info("ATTEMPTS: %d" % (tempTimes + 1))
            if switchCityPage.validSelf(False):
                switchCityPage.cancelSwitchCity()
                break
            switchCityPage.waitBySeconds(2)
        switchCityPage.invalidSelf()


if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(SwitchCityCases)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = os.path.join(reportpath, 'Feifan_automation_test_report_' + now + '.html')
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Feifan_automation_test_report', description='Result for test')
    runner.run(suite)
