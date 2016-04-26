#! /Library/Frameworks/Python.framework/Versions/2.7/bin/python
# -*- coding: utf-8 -*-

import sys,os
reload(sys)
sys.setdefaultencoding('utf8')

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from driver.appium_driver import *
from pages.bp.dashboard import *
from configs.driver_configs import *
from pages.bp.msgcenter import *

import unittest
import time


class MessageCases(unittest.TestCase):

    def setUp(self):
        self.driver = AppiumDriver(app_package=appPackage_bp, app_activity=appActivity_bp,
                                   platform_name=platformName_andr, platform_version=platformVersion,
                                   device_name=deviceName_andr,driver_url=driver_url
                                   ).getDriver()

    def tearDown(self):
        self.driver.quit()

    def test_clickOnMsgCenter(self):
        dashboard = Dashboard(self.driver)
        dashboard.validSelf(self)
        dashboard.clickOnMessageTextView()
        mc = MessageCenter(self.driver)
        mc.clickOnMsgNoticeTab()
        dashboard.waitBySeconds(6)
        mc.validMsgNoticeTabSelected()

    # def test_clickOnSettings(self):
    #     dashboard = Dashboard(self.driver)
    #     dashboard.validSelf(self)

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(MessageCases)
    unittest.TextTestRunner(verbosity=2).run(suite)