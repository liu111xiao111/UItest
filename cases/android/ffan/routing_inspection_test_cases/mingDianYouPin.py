# -*- coding: utf-8 -*-

import os
import time
import HTMLTestRunner

from unittest import TestCase
from unittest import TestLoader

from cases.android.ffan.common.test_prepare import TestPrepare
from cases.android.ffan.common.clear_app_data import ClearAppData
from pages.android.ffan.dashboard_page import DashboardPage
from pages.android.ffan.my_ffan_page import MyFfanPage
from pages.android.ffan.my_ffan_my_like_page import MyFfanMyLikePage
from pages.android.ffan.shopping_category_page import ShoppingCategoryPage
from pages.android.ffan.shopping_details_category_page import ShoppingDetailsCategoryPage
from pages.android.ffan.shopping_trolley_page import ShoppingTrolleyPage
from configs.driver_configs import appActivity_ffan
from configs.driver_configs import appPackage_ffan
from configs.driver_configs import deviceName_andr
from configs.driver_configs import driver_url
from configs.driver_configs import platformName_andr
from driver.appium_driver import AppiumDriver
from utility.logger import Logger
from utility.device_info_util import DeviceInfoUtil


class MingDianYouPinTestCase(TestCase):
    '''
    巡检 No.14
    用例名 名店优品
    首页进入购物模块，数据显示正常，点击进入详情页可以激活商品的提醒
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

    def testMingDianYouPin(self):
        dashboardPage = DashboardPage(self, self.driver, self.logger)
        shoppingPage = ShoppingCategoryPage(self, self.driver, self.logger)
        shoppingDetailsPage = ShoppingDetailsCategoryPage(self, self.driver, self.logger)
        shoppingTrolleyPage = ShoppingTrolleyPage(self, self.driver, self.logger)
        myFfanPage = MyFfanPage(self, self.driver, self.logger)
        myLikePage = MyFfanMyLikePage(self, self.driver, self.logger)

        # Load goods page
        dashboardPage.validSelf();
        dashboardPage.clickOnShoppingCategory()
        shoppingPage.waitBySeconds(10)
        shoppingPage.validSelf();

        # Click goods details， load detail pay page.
        shoppingPage.clickOnGoodsDetails();
        shoppingDetailsPage.waitBySeconds(10);
        shoppingDetailsPage.validSelf();
        shoppingDetailsPage.clickBackKey();
        shoppingPage.clickOnShoppingTrolley();
        shoppingTrolleyPage.waitBySeconds(10);
        shoppingTrolleyPage.validSelf();
        shoppingTrolleyPage.clickBackKey();
        shoppingPage.clickBackKey();
        dashboardPage.clickOnMy();
        myFfanPage.waitBySeconds(10)
        myFfanPage.validSelf();
        myFfanPage.clickOnMyLike();
        myLikePage.validSelf();


if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(MingDianYouPinTestCase)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = os.path.join(reportpath, 'Feifan_automation_test_report_' + now + '.html')
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Feifan_automation_test_report',
                                           description='Result for test')
    runner.run(suite)