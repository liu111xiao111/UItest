# -*- coding: utf-8 -*-

import os
import time
import HTMLTestRunner

from unittest import TestCase
from unittest import TestLoader

from pages.android.ffan.my_ffan_my_queue_page import MyFfanMyQueuePage
from pages.android.ffan.dashboard_page import DashboardPage
from pages.android.ffan.food_category_page import FoodCategoryPage
from pages.android.ffan.my_ffan_page import MyFfanPage
from configs.driver_configs import platformName_andr
from configs.driver_configs import appActivity_ffan
from configs.driver_configs import appPackage_ffan
from configs.driver_configs import deviceName_andr
from configs.driver_configs import driver_url
from driver.appium_driver import AppiumDriver
from utility.logger import Logger
from utility.device_info_util import DeviceInfoUtil
from cases.android.ffan.common.test_prepare import TestPrepare
from cases.logger import logger


class WoDePaiDuiTestCase(TestCase):
    '''
    回归用例： No.27
    用例名: 我的排队
    点击我的排队，成功进入并显示正确数据，点击更多餐厅，进入美食汇
    '''
    @classmethod
    def setUpClass(cls):
        '''
        初始化Appium driver
        '''
        cls.driver = AppiumDriver(appPackage_ffan,
                                   appActivity_ffan,
                                   platformName_andr,
                                   DeviceInfoUtil().getBuildVersion(),
                                   deviceName_andr,
                                   driver_url).getDriver()
        logger.info("Appium client init completed")

    def tearDown(self):
        self.driver.quit()

    def setUp(self):
        self.logger = Logger()
        TestPrepare(self, self.driver, self.logger).prepare()

    def testWoDePaiDui(self):
        # 验证首页
        dashboardPage = DashboardPage(self, self.driver, self.logger)
        dashboardPage.validSelf()
        dashboardPage.screenShot("aiGuangJie")

        # 点击我的，进入我的排队
        dashboardPage.clickOnMy()
        myFfanPage = MyFfanPage(self, self.driver, self.logger)
        myFfanPage.validSelf()
        myFfanPage.clickOnMyQueue()
        myQueuePage = MyFfanMyQueuePage(self, self.driver, self.logger)
        myQueuePage.validSelf()
        myQueuePage.clickOnMoreRestaurant()
        foodPage = FoodCategoryPage(self, self.driver, self.logger)
        foodPage.validFoodHomePage()
        foodPage.screenShot("meiShiHui")


if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(WoDePaiDuiTestCase)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = os.path.join(reportpath, 'Feifan_automation_test_report_' + now + '.html')
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Feifan_automation_test_report',
                                           description='Result for test')
    runner.run(suite)