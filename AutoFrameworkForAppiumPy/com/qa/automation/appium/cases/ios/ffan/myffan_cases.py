# -*- coding: utf-8 -*-

import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))))))

from com.qa.automation.appium.configs.driver_configs import *;
from com.qa.automation.appium.driver.appium_driver import *;
from com.qa.automation.appium.utility.logger import Logger;
from com.qa.automation.appium.utility.device_info_util import *;

from com.qa.automation.appium.pages.ios.ffan.dashboard_page import *


import unittest
import HTMLTestRunner


class MyFfanCases(unittest.TestCase):

    """
        备注：原始版本的case，暂没作修改
    """
    def tearDown(self):
        self.driver.quit()

    def setUp(self):
        self.logger = Logger()
        device_info_util = DeviceInfoUtil();
        prod_version = device_info_util.get_product_version();
        udid = device_info_util.getUdid();
        appiumDriver = AppiumDriver(platform_name="iOS", platform_version=prod_version, device_name='iPhone',
                                    bundle_id=bundle_id,
                                    ios_udid=udid)
        self.driver = appiumDriver.getDriver();

    def test_demo(self):
        dashboard = DashboardPage(testcase=self,driver=self.driver,logger=self.logger)
        dashboard.wait_by_seconds(seconds=1)
        dashboard.valid_self()

if __name__ == "__main__":
    print("path is %s." % (sys.path))
