# -*- coding:utf-8 -*-

import os
import time
import HTMLTestRunner

from unittest import TestCase
from unittest import TestLoader


from com.qa.automation.appium.cases.android.ffan.common.clear_app_data import ClearAppData
from com.qa.automation.appium.cases.android.ffan.common.test_prepare import TestPrepare

from com.qa.automation.appium.configs.driver_configs import appActivity_ffan
from com.qa.automation.appium.configs.driver_configs import appPackage_ffan
from com.qa.automation.appium.configs.driver_configs import deviceName_andr
from com.qa.automation.appium.configs.driver_configs import driver_url
from com.qa.automation.appium.configs.driver_configs import platformName_andr
from com.qa.automation.appium.driver.appium_driver import AppiumDriver

from com.qa.automation.appium.pages.android.ffan.dashboard_page import DashboardPage
from com.qa.automation.appium.pages.android.ffan.hui_life_page import HuiLifePage
from com.qa.automation.appium.utility.logger import Logger
from com.qa.automation.appium.utility.device_info_util import DeviceInfoUtil


class HuiLifeResourceNicheCases(TestCase):
    '''
    巡检checklist No.: 39
    自动化测试case No.: 39
    首页-慧生活，惠生活截图，基本入口检查
    '''

    def tearDown(self):
        self.reset.clearData()
        self.driver.quit()

    def setUp(self):
        self.logger = Logger()
        self.driver = AppiumDriver(appPackage_ffan,
                                   appActivity_ffan,
                                   platformName_andr,
                                   DeviceInfoUtil().getBuildVersion(),
                                   deviceName_andr,
                                   driver_url).getDriver()

        self.reset = ClearAppData(self.driver)
        self.reset.clearData()

        TestPrepare(self, self.driver, self.logger).prepare()

    def testHuiLifeScreenShot(self):
        dashboardPage = DashboardPage(self, self.driver, self.logger)
        huiLifePage = HuiLifePage(self, self.driver, self.logger)
        dashboardPage.validSelf()
        # 惠生活界面截图
        dashboardPage.clickOnSmartLife()
        huiLifePage.validSelf()
        huiLifePage.screen_shot("hui_life_resource_niche")

        # 验证打车入口
        huiLifePage.clickOnTaxi()
        huiLifePage.validDiDiTravel()
        huiLifePage.clickBackKey()

        # 验证代驾入口
        huiLifePage.clickOnDesignatedDriving()
        huiLifePage.validDiDiTravel()
        huiLifePage.clickBackKey()

        # 验证公交查询入口
        huiLifePage.clickOnBus()
        huiLifePage.validDiDiTravel()
        huiLifePage.clickBackKey()

        # 验证股票资讯入口
        huiLifePage.clickOnStockInformation()
        huiLifePage.validStockInformation()
        huiLifePage.clickBackKey()

        # 验证飞凡阅读入口
        huiLifePage.clickOnFeifanRead()
        huiLifePage.validFeifanRead()
        huiLifePage.clickBackKey()

        # 验证话费充值入口
        huiLifePage.clickOnPrepaidRecharge()
        huiLifePage.validPrepaidRecharge()
        huiLifePage.clickBackKey()

        # 验证流量充值入口
        huiLifePage.clickOnTrafficRecharge()
        huiLifePage.validTrafficRecharge()
        huiLifePage.clickBackKey()

        # 验证QQ充值入口
        huiLifePage.clickOnQQRecharge()
        huiLifePage.validQQRecharge()
        huiLifePage.clickBackKey()

        # 验证网游充值入口
        huiLifePage.clickOnOnlineGameRecharge()
        huiLifePage.validOnlineGameRecharge()
        huiLifePage.clickBackKey()

        # 验证飞悦入口
        huiLifePage.clickOnFlyYue()
        huiLifePage.validFlyYue()
        huiLifePage.clickBackKey()

        # 验证加油入口
        huiLifePage.clickOnRefuel()
        huiLifePage.validRefuel()
        huiLifePage.clickBackKey()

        # 验证演唱会入口
        huiLifePage.clickOnConcert()
        huiLifePage.validConcert()
        huiLifePage.clickBackKey()

        # 验证话剧入口
        huiLifePage.clickOnDrama()
        huiLifePage.validDrama()
        huiLifePage.clickBackKey()
        
        # 验证音乐会入口
        huiLifePage.clickOnPhilharmonic()
        huiLifePage.validPhilharmonic()
        huiLifePage.clickBackKey()
        
        # 验证违章查询入口
        huiLifePage.clickOnIllegalInquiry()
        huiLifePage.validIllegalInquiry()
        huiLifePage.clickBackKey()

if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(HuiLifeResourceNicheCases)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = reportpath + '/'+ 'Hui_life_resource_niche_' + now + '.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Feifan_automation_test_report', description='Result for test')
    runner.run(suite)
