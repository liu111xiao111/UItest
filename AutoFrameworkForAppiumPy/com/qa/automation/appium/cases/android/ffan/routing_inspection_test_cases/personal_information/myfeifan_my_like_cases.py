# -*- coding: utf-8 -*-

import os
import time
import HTMLTestRunner

from unittest import TestCase
from unittest import TestLoader

from com.qa.automation.appium.pages.android.ffan.dashboard_page import DashboardPage
from com.qa.automation.appium.pages.android.ffan.my_ffan_page import MyFfanPage
from com.qa.automation.appium.pages.android.ffan.my_ffan_my_like_page import MyFfanMyLikePage

from com.qa.automation.appium.configs.driver_configs import platformName_andr
from com.qa.automation.appium.configs.driver_configs import appActivity_ffan
from com.qa.automation.appium.configs.driver_configs import appPackage_ffan
from com.qa.automation.appium.configs.driver_configs import platformVersion
from com.qa.automation.appium.configs.driver_configs import deviceName_andr
from com.qa.automation.appium.configs.driver_configs import driver_url

from com.qa.automation.appium.driver.appium_driver import AppiumDriver
from com.qa.automation.appium.utility.logger import Logger;

from com.qa.automation.appium.cases.android.ffan.common.test_prepare import TestPrepare
from com.qa.automation.appium.cases.android.ffan.common.clear_app_data import ClearAppData


class MyfeifanMyLikeCases(TestCase):
    '''
    	巡检checklist: No.54
    	自动化测试: No.54
    	查看我的喜欢信息及状态是否正确
    '''

    def tearDown(self):
        self.driver.quit()
        ClearAppData().clearData()

    def setUp(self):
        ClearAppData().clearData()

        self.logger = Logger()
        self.driver = AppiumDriver(appPackage_ffan,
                                   appActivity_ffan,
                                   platformName_andr,
                                   platformVersion,
                                   deviceName_andr,
                                   driver_url).getDriver()

        # Login & update version
        testPrepare = TestPrepare(self, self.driver, self.logger)
        testPrepare.prepare()

    def test_case(self):
        dashboardPage = DashboardPage(self, self.driver, self.logger)
        myFfanPage = MyFfanPage(self, self.driver, self.logger)
        myLikePage = MyFfanMyLikePage(self, self.driver, self.logger)

        # Click "我的喜欢"， load "我的喜欢" page.
        dashboardPage.validSelf()
        dashboardPage.clickOnMy()
        myFfanPage.validSelf()
        myFfanPage.clickOnMyLike()
        myLikePage.validSelf()
        myLikePage.clickOnLikeGoods()
        myLikePage.validSelfGoods()
        myLikePage.clickOnLikeDissertation()
        myLikePage.validSelfDissertation()
        myLikePage.clickOnLikeBrand()
        myLikePage.validSelfBrand()


if __name__ == "__main__":
    log = Logger()
    caseName = 'myfeifan_my_lick_cases'
    suite = TestLoader().loadTestsFromTestCase(MyfeifanMyLikeCases)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = reportpath + caseName + now + '.html'
    log.d("report file name ==== %s", filename)
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=caseName,
                                           description='Result for test')
    runner.run(suite)