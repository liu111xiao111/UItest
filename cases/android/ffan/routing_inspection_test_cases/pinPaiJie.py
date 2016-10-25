# -*- coding: utf-8 -*-

import os
import time
import HTMLTestRunner

from unittest import TestCase
from unittest import TestLoader

from cases.android.ffan.common.test_prepare import TestPrepare
from cases.android.ffan.common.clear_app_data import ClearAppData
from pages.android.ffan.dashboard_page import DashboardPage;
from pages.android.ffan.brand_category_page import BrandCategoryPage;
from pages.android.ffan.famous_details_category_page import FamousDetailsCategoryPage;
from configs.driver_configs import appActivity_ffan
from configs.driver_configs import appPackage_ffan
from configs.driver_configs import deviceName_andr
from configs.driver_configs import driver_url
from configs.driver_configs import platformName_andr
from driver.appium_driver import AppiumDriver
from utility.logger import Logger
from utility.device_info_util import DeviceInfoUtil


class PinPaiJieTestCase(TestCase):
    '''
    巡检 No.8
    用例名: 品牌街
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

        TestPrepare(self, self.driver, self.logger).prepare(False)

    def testPinPaiJie(self):
        dashboardPage = DashboardPage(testcase = self , driver = self.driver , logger = self.logger)
        brandPage = BrandCategoryPage(testcase = self, driver = self.driver, logger = self.logger)
        #famousDetailsPage = FamousDetailsCategoryPage(testcase = self, driver = self.driver, logger = self.logger)

        # Load "推荐" page
        dashboardPage.validSelf();
        dashboardPage.clickOnBrandCategory()
        brandPage.validSelf();

        # Click "大牌"
        '''brandPage.clickOnBrand();
        brandPage.clickOnBrandDetails();
        famousDetailsPage.validSelf();'''

        # Check "男装“、”餐饮“、”生活“、”运动“及”精品“ tab
        #famousDetailsPage.clickBackKey();
        brandPage.waitBySeconds(2);
        brandPage.clickOnWomenFasion();
        brandPage.validSelfWomenFasion();
        brandPage.clickBackKey();
        brandPage.waitBySeconds(2);
        brandPage.clickOnMenFasion();
        brandPage.validSelfMenFasion();
        brandPage.clickBackKey();
        brandPage.waitBySeconds(2);
        brandPage.clickOnCatering();
        brandPage.validSelfCertering();
        brandPage.clickBackKey();
        brandPage.waitBySeconds(2);
        brandPage.clickOnLife();
        brandPage.validSelfLife();
        brandPage.clickBackKey();
        brandPage.waitBySeconds(2);
        brandPage.clickOnSports();
        brandPage.validSelfSports();
        brandPage.clickBackKey();
        brandPage.waitBySeconds(2);
        brandPage.clickOnCompetitiveProducts();
        brandPage.validSelfCompetitiveProducts();


if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(PinPaiJieTestCase)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = os.path.join(reportpath, 'Feifan_automation_test_report_' + now + '.html')
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Feifan_automation_test_report',
                                           description='Result for test')
    runner.run(suite)