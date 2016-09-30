# -*- coding: utf-8 -*-

import os
import time
import HTMLTestRunner

from unittest import TestCase
from unittest import TestLoader

from pages.android.ffan.recommend_details_category_page import RecommendDetailsCategoryPage
from pages.android.ffan.brand_category_page import BrandCategoryPage
from cases.android.ffan.common.clear_app_data import ClearAppData
from cases.android.ffan.common.test_prepare import TestPrepare
from pages.android.ffan.dashboard_page import DashboardPage
from configs.driver_configs import platformName_andr
from configs.driver_configs import appActivity_ffan
from configs.driver_configs import appPackage_ffan
from configs.driver_configs import deviceName_andr
from configs.driver_configs import driver_url
from driver.appium_driver import AppiumDriver
from utility.logger import Logger
from utility.device_info_util import DeviceInfoUtil


class PinPaiJieTuiJianTestCase(TestCase):
    '''
    作者 刘涛
    巡检 No.8-1
    用例名: 品牌街推荐
    首页进入品牌简单浏览品牌中推荐内容，点击验证是否可以进入详情页，显示是否正常
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

    def testPinPaiJieTuiJian(self):
        recommendDetailsPage = RecommendDetailsCategoryPage(self, self.driver, self.logger)
        dashboardPage = DashboardPage(self , self.driver , self.logger)
        brandPage = BrandCategoryPage(self, self.driver, self.logger)

        # Load "推荐" page
        dashboardPage.validSelf()
        dashboardPage.clickOnBrandCategory()
        brandPage.validSelf()
        brandPage.waitBySeconds(10)
        brandPage.clickOnRecommendDetails()
        recommendDetailsPage.validSelf()
        recommendDetailsPage.waitBySeconds(5)

        # Click “心形”
        '''recommendDetailsPage.clickOnSubsciber()
        recommendDetailsPage.waitBySeconds(3)
        recommendDetailsPage.validSelfSubsciberLike()
        recommendDetailsPage.clickCancelSubsciber()
        recommendDetailsPage.waitBySeconds(3)
        recommendDetailsPage.validSelfSubsciberUnlike()'''


if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(PinPaiJieTuiJianTestCase)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = os.path.join(reportpath, 'Feifan_automation_test_report_' + now + '.html')
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Feifan_automation_test_report',
                                           description='Result for test')
    runner.run(suite)