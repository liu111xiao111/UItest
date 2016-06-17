# -*- coding: utf-8 -*-

import sys,os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))))

from com.qa.automation.appium.pages.android.ffan.dashboard_page import *;
from com.qa.automation.appium.pages.android.ffan.square_module_page import *;
from com.qa.automation.appium.pages.android.ffan.square_food_category_page import *;
from com.qa.automation.appium.pages.android.ffan.store_info_page import *;
from com.qa.automation.appium.pages.android.ffan.member_category_page import *;
from com.qa.automation.appium.pages.android.ffan.my_ffan_page import *;
from com.qa.automation.appium.configs.driver_configs import *;
from com.qa.automation.appium.driver.appium_driver import *;
from com.qa.automation.appium.utility.logger import Logger;

from com.qa.automation.appium.cases.android.ffan.common.test_prepare import TestPrepare
from com.qa.automation.appium.cases.android.ffan.common.clear_app_data import ClearAppData

import unittest
import HTMLTestRunner

class SquareRecommendCases(unittest.TestCase):
    '''
       usage:  No.35 广场详情页点击达人推荐可以进入门店详情页    
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
        squarePage = SquareModulePage(testcase = self , driver = self.driver , logger = self.logger)
        storeInfoPage = StoreInfoPage(testcase = self , driver = self.driver , logger = self.logger)
        
        dashboardPage.validSelf()
        squarePage.waitBySeconds(seconds=2)
        
        dashboardPage.clickOnSquareModule()
        squarePage.validSelf()
        
        for i in range(0,5):
            if i==5:
                break
            else:
                squarePage.scrollAsScreenPercent(xPercent = 20, yPercent = 30, orientation = 'down');
        
        squarePage.clickOnRecommmendStore()
        
        storeInfoPage.validSelf()
        
if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(SquareRecommendCases)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = reportpath + 'food-test_' + now + '.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='food-test',
                                           description='Result for test')
    runner.run(suite)