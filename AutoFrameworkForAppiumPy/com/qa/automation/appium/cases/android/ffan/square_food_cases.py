# -*- coding: utf-8 -*-

import sys,os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))))

from com.qa.automation.appium.pages.android.ffan.dashboard_page import *;
from com.qa.automation.appium.pages.android.ffan.square_module_page import *;
from com.qa.automation.appium.pages.android.ffan.square_food_category_page import *;
from com.qa.automation.appium.pages.android.ffan.member_category_page import *;
from com.qa.automation.appium.pages.android.ffan.my_ffan_page import *;
from com.qa.automation.appium.configs.driver_configs import *;
from com.qa.automation.appium.driver.appium_driver import *;
from com.qa.automation.appium.utility.logger import Logger;

from com.qa.automation.appium.cases.android.ffan.common.test_prepare import TestPrepare
from com.qa.automation.appium.cases.android.ffan.common.clear_app_data import ClearAppData

import HTMLTestRunner

class SquareFoodCases(unittest.TestCase):
    '''
       usage: No.31 广场详情页点击美食汇正常进入餐饮模块，数据显示正常可点击进入
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
        dashboardPage = DashboardPage(testcase = self , driver = self.driver , logger = self.logger);
        squarePage = SquareModulePage(testcase = self , driver = self.driver , logger = self.logger);
        squareFoodPage = SquareFoodPage(testcase = self , driver = self.driver , logger = self.logger);
        
        dashboardPage.validSelf();
        squarePage.waitBySeconds(seconds=2);
        
        dashboardPage.clickOnSquareModule();
        squarePage.validSelf();
        
        squarePage.scrollAsScreenPercent(0.5,0.5,0.5,0.3);
        #squarePage.scrollToFood()
        squarePage.waitBySeconds(seconds=2);
        
        squarePage.clickOnFood();
        
        squareFoodPage.validSelf();
        
if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(SquareFoodCases)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = reportpath + 'food-test_' + now + '.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='food-test',
                                           description='Result for test')
    runner.run(suite)