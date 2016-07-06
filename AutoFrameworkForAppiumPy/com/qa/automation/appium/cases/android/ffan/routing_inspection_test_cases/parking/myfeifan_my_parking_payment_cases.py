
# -*- coding: utf-8 -*-

import sys,os
import time

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))))

from com.qa.automation.appium.cases.android.ffan.common.test_prepare import TestPrepare
from com.qa.automation.appium.cases.android.ffan.common.clear_app_data import ClearAppData
from com.qa.automation.appium.pages.android.ffan.dashboard_page import DashboardPage;
from com.qa.automation.appium.pages.android.ffan.my_ffan_page import MyFfanPage
from com.qa.automation.appium.pages.android.ffan.my_ffan_my_parking_payment_page import MyFfanMyParkingPaymentPage
from com.qa.automation.appium.pages.android.ffan.my_ffan_my_parking_payment_details_page import MyFfanMyParkingPaymentDetailsPage
from com.qa.automation.appium.pages.android.ffan.my_ffan_my_parking_payment_more_page import MyFfanMyParkingPaymentMorePage
from com.qa.automation.appium.pages.android.ffan.my_ffan_my_parking_payment_unbunding_page import MyFfanMyParkingPaymentUnbundingPage
from com.qa.automation.appium.configs.driver_configs import appActivity_ffan
from com.qa.automation.appium.configs.driver_configs import appPackage_ffan
from com.qa.automation.appium.configs.driver_configs import deviceName_andr
from com.qa.automation.appium.configs.driver_configs import driver_url
from com.qa.automation.appium.configs.driver_configs import platformName_andr
from com.qa.automation.appium.configs.driver_configs import platformVersion
from com.qa.automation.appium.driver.appium_driver import AppiumDriver
from com.qa.automation.appium.utility.logger import Logger;

import unittest
import HTMLTestRunner


class MyfeifanMyQueueCases(unittest.TestCase):
    '''
    	巡检checklist #56
    	自动化测试 #56
    	点击停车缴费，成功进入并显示正确数据
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
        parkingPaymentPage = MyFfanMyParkingPaymentPage(testcase = self,driver = self.driver,logger = self.logger)
        parkingPaymentDetailsPage = MyFfanMyParkingPaymentDetailsPage(testcase = self,driver = self.driver,logger = self.logger)
        parkingPaymentMorePage = MyFfanMyParkingPaymentMorePage(testcase = self,driver = self.driver,logger = self.logger)
        parkingPaymentUnbundingPage = MyFfanMyParkingPaymentUnbundingPage(testcase = self,driver = self.driver,logger = self.logger)


        # Click "我的排队"， load "我的排队" page.
        dashboardPage.validSelf();
        dashboardPage.clickOnMy();
        myFfanPage.validSelf();
        myFfanPage.clickOnParkingPayment();
        parkingPaymentPage.validSelf();

        # Bunding VIN
        parkingPaymentPage.waitBySeconds(2);
        parkingPaymentPage.inputVIN();
        parkingPaymentPage.clickOnNextBtn();
        parkingPaymentDetailsPage.validSelf();

        # Unbunding VIN
        parkingPaymentDetailsPage.clickOnMore();
        parkingPaymentMorePage.waitBySeconds(2);
        parkingPaymentMorePage.clickOnUnbundingBtn();
        parkingPaymentUnbundingPage.clickOnUnbundingBtn();
        parkingPaymentPage.validSelf();

if __name__ == "__main__":
    log = Logger()
    caseName = 'myfeifan_my_queue_cases'
    suite = unittest.TestLoader().loadTestsFromTestCase(MyfeifanMyQueueCases)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = reportpath + caseName + now + '.html'
    log.d("report file name ==== %s" , filename)
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=caseName,
                                           description='Result for test')
    runner.run(suite)