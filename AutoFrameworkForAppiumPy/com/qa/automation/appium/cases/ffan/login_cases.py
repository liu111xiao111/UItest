# -*- coding: utf-8 -*-

import sys,os
# reload(sys)
# sys.setdefaultencoding('utf8')

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from pages.ffan.dashboard_page import *
from configs.driver_configs import *
from driver.appium_driver import *

import unittest

class LoginCases(unittest.TestCase):

    def tearDown(self):
        self.driver.quit()

    def setUp(self):
        self.logger = Logger()
        self.driver = AppiumDriver(app_package=appPackage_ffan, app_activity=appActivity_ffan,
                                   platform_name=platformName_andr, platform_version=platformVersion,
                                   device_name=deviceName_andr, driver_url=driver_url
                                   ).getDriver()

    def test_case(self):
        dashboardPage = DashboardPage(testcase = self , driver = self.driver , logger = self.logger);
        dashboardPage.validSelf();
        dashboardPage.clickOnMy();
        dashboardPage.waitBySeconds(seconds=10);


if __name__ == "__main__":
    # suite = unittest.TestLoader().loadTestsFromTestCase(LoginCases)
    # print("testcase number is "+suite.countTestCases());
    # unittest.TextTestRunner(verbosity=2).run(suite)
    pass;