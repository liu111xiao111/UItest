# -*- coding: utf-8 -*-

import sys,os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))))

print("path contains %s" % (sys.path));

from com.qa.automation.appium.pages.ffan.dashboard_page import *;
from com.qa.automation.appium.pages.ffan.my_ffan_page import *;
from com.qa.automation.appium.configs.driver_configs import *;
from com.qa.automation.appium.driver.appium_driver import *;
from com.qa.automation.appium.utility.logger import Logger;

import unittest
import HTMLTestRunner

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
        myFfanPage = MyFfanPage(testcase=self,driver=self.driver,logger=self.logger);
        myFfanPage.validSelf();
        dashboardPage.waitBySeconds(seconds=10);


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(LoginCases)
    #print("testcase number is "+suite.countTestCases());
    unittest.TextTestRunner(verbosity=2).run(suite)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = reportpath + 'Feifan_automation_test_report_' + now + '.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Feifan_automation_test_report',
                                           description='Result for test')
    runner.run(suite)