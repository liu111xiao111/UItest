# -*- coding: utf-8 -*-

import sys,os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))))

from com.qa.automation.appium.pages.android.ffan.dashboard_page import DashboardPage;
from com.qa.automation.appium.pages.android.ffan.search_page import SearchPage;
from com.qa.automation.appium.pages.android.ffan.search_result_store_page import SearchResultStorePage;
from com.qa.automation.appium.pages.android.ffan.my_ffan_page import *;
from com.qa.automation.appium.configs.driver_configs import *;
from com.qa.automation.appium.driver.appium_driver import AppiumDriver;
from com.qa.automation.appium.utility.logger import Logger;

from com.qa.automation.appium.cases.android.ffan.common.test_prepare import TestPrepare
from com.qa.automation.appium.cases.android.ffan.common.clear_app_data import ClearAppData

import unittest
import HTMLTestRunner

class DashboardSearchBrandCases(unittest.TestCase):
    '''
        巡检checklist No.: 3
        自动化测试case No.: 4
        全城搜索品牌
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
                                   
        #登陆　升级
        testPrepare = TestPrepare(testcase = self , driver = self.driver , logger = self.logger)
        testPrepare.prepare(False)

    def test_case(self):
        dashboardPage = DashboardPage(testcase = self , driver = self.driver , logger = self.logger)
        searchPage = SearchPage(testcase = self , driver = self.driver , logger = self.logger)
        searchResultStorePage = SearchResultStorePage(testcase = self , driver = self.driver , logger = self.logger)
        
        dashboardPage.validSelf()
        dashboardPage.waitBySeconds(3)
        
        dashboardPage.clickOnSearchView()
                
        searchPage.validSelf()
        searchPage.inputBrandName()
        searchPage.clickOnSearch()
        
        searchPage.validSearchResult()
        
        

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(DashboardSearchBrandCases)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = reportpath + 'food-test_' + now + '.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='food-test',
                                           description='Result for test')
    runner.run(suite)