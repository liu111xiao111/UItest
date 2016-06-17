# -*- coding: utf-8 -*-

import sys,os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))))

from com.qa.automation.appium.pages.android.ffan.dashboard_page import *;
from com.qa.automation.appium.pages.android.ffan.my_ffan_page import *;
from com.qa.automation.appium.pages.android.ffan.my_ffan_my_ticket_page import *;
from com.qa.automation.appium.configs.driver_configs import *;
from com.qa.automation.appium.driver.appium_driver import *;
from com.qa.automation.appium.utility.logger import Logger;

from com.qa.automation.appium.cases.android.ffan.common.test_prepare import TestPrepare
from com.qa.automation.appium.cases.android.ffan.common.clear_app_data import ClearAppData

import unittest
import HTMLTestRunner

class MyfeifanMyTicketCases(unittest.TestCase):
    '''
    	巡检checklist #50
    	自动化测试 #50
    	查看我的票券里数据显示正常
    '''

    def tearDown(self):
        self.driver.quit()
        
        clearAppData = ClearAppData()
        clearAppData.clearData()

    def setUp(self):
        clearAppData = ClearAppData()
        clearAppData.clearData()

        self.logger = Logger()
        self.driver = AppiumDriver(app_package=appPackage_ffan, app_activity=appActivity_ffan,
                                   platform_name=platformName_andr, platform_version=platformVersion,
                                   device_name=deviceName_andr, driver_url=driver_url
                                   ).getDriver()

        #Login & update version
        testPrepare = TestPrepare(testcase = self , driver = self.driver , logger = self.logger)
        testPrepare.prepare()

    def test_case(self):
        dashboardPage = DashboardPage(testcase = self , driver = self.driver , logger = self.logger)
        myFfanPage = MyFfanPage(testcase = self,driver = self.driver,logger = self.logger)
        myTicketPage = MyFfanMyTicketPage(testcase = self,driver = self.driver,logger = self.logger)

        # Click "我的票券"， load "我的票券" page.
        dashboardPage.validSelf();
        dashboardPage.clickOnMy();
        myFfanPage.validSelf();
        myFfanPage.clickOnMyTicket();
        myTicketPage.validSelf();
        myTicketPage.clickOnTicketUsed();
        myTicketPage.validSelfUsed();
        myTicketPage.clickOnTicketOutOfDate();
        myTicketPage.validSelfOutOfDate();
        myTicketPage.clickOnReturnRefund();
        myTicketPage.validSelfReturnRefund();
        

if __name__ == "__main__":
    log = Logger()
    caseName = 'myfeifan_my_queue_cases'
    suite = unittest.TestLoader().loadTestsFromTestCase(MyfeifanMyTicketCases)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = reportpath + caseName + now + '.html'
    log.d("report file name ==== %s" , filename)
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=caseName,
                                           description='Result for test')
    runner.run(suite)