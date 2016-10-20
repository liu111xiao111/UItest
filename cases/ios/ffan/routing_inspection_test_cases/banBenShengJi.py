# -*- coding:utf-8 -*-

import os
import time
import logging
from unittest import TestCase
from unittest import TestLoader

import HTMLTestRunner

from cases.ios.ffan.common.clearAppData import ClearAppData
from cases.ios.ffan.common.testPrepare import TestPrepare
from configs.iosDriverConfig import IosDriverConfigs as IDC
from driver.appium_driver import AppiumDriver
from pages.ios.ffan.version_upgrade_page import VersionUpgradePage
from utility.logger import Logger


class BanBenShengJiTestCase(TestCase):
    '''
    作者 宋波
    巡检checklist #60
    自动化测试 #60
    版本升级
    '''

    def tearDown(self):
        self.reset.clearData()
        self.driver.quit()

    def setUp(self):
        self.logger = Logger()
        self.driver = AppiumDriver(None, None, IDC.platformName, IDC.platformVersion,
                                   IDC.deviceName, IDC.driverUrl, IDC.bundleId, IDC.udid).getDriver()
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
    suite = TestLoader().loadTestsFromTestCase(BanBenShengJiTestCase)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = reportpath + 'Feifan_automation_test_report_' + now + '.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(fp, 'Feifan_automation_test_report', 'Result for test')
    runner.run(suite)
