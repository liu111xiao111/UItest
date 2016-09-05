# -*- coding:utf-8 -*-

import os
import time
import logging
import HTMLTestRunner

from unittest import TestCase
from unittest import TestLoader

from com.qa.automation.appium.cases.android.ffan.common.clear_app_data import ClearAppData
from com.qa.automation.appium.cases.android.ffan.common.test_prepare import TestPrepare
from com.qa.automation.appium.configs.driver_configs import appActivity_ffan
from com.qa.automation.appium.configs.driver_configs import appPackage_ffan
from com.qa.automation.appium.configs.driver_configs import deviceName_andr
from com.qa.automation.appium.configs.driver_configs import driver_url
from com.qa.automation.appium.configs.driver_configs import platformName_andr
from com.qa.automation.appium.driver.appium_driver import AppiumDriver
from com.qa.automation.appium.pages.android.ffan.version_upgrade_page import VersionUpgradePage
from com.qa.automation.appium.utility.logger import Logger
from com.qa.automation.appium.utility.device_info_util import DeviceInfoUtil


class VersionUpgradeCases(TestCase):
    '''
    巡检checklist No.: 60
    自动化测试case No.: 60
    启动APP，判断是否弹出更新对话框
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

        TestPrepare(self, self.driver, self.logger).switchCity()

    def test_case(self):
        versionUpgradePage = VersionUpgradePage(self, self.driver, self.logger)
        for tempTimes in range(5):
            logging.info("ATTEMPTS: %d" % (tempTimes + 1))
            if versionUpgradePage.validSelf(False):
                versionUpgradePage.cancelVersionUpgrade()
                break
            versionUpgradePage.waitBySeconds(2)
        versionUpgradePage.invalidSelf()


if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(VersionUpgradeCases)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = os.path.join(reportpath, 'Feifan_automation_test_report_' + now + '.html')
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Feifan_automation_test_report', description='Result for test')
    runner.run(suite)
