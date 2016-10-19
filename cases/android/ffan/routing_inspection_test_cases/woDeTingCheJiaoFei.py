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
from pages.android.ffan.my_ffan_my_parking_payment_page import MyFfanMyParkingPaymentPage
# from pages.android.ffan.my_ffan_my_parking_payment_details_page import MyFfanMyParkingPaymentDetailsPage
# from pages.android.ffan.my_ffan_my_parking_payment_more_page import MyFfanMyParkingPaymentMorePage
# from pages.android.ffan.my_ffan_my_parking_payment_unbunding_page import MyFfanMyParkingPaymentUnbundingPage
from configs.driver_configs import appActivity_ffan
from configs.driver_configs import appPackage_ffan
from configs.driver_configs import deviceName_andr
from configs.driver_configs import driver_url
from configs.driver_configs import platformName_andr
from driver.appium_driver import AppiumDriver
from utility.logger import Logger
from utility.device_info_util import DeviceInfoUtil


class WoDeTingCheJiaoFeiTestCase(TestCase):
    '''
    巡检 No.59
    用例名: 我的停车缴费
    点击停车缴费，成功进入并显示正确数据
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

    def testWoDeTingCheJiaoFei(self):
        dashboardPage = DashboardPage(self, self.driver, self.logger)
        myFfanPage = MyFfanPage(self, self.driver, self.logger)
        parkingPaymentPage = MyFfanMyParkingPaymentPage(self, self.driver, self.logger)
        '''parkingPaymentDetailsPage = MyFfanMyParkingPaymentDetailsPage(self, self.driver, self.logger)
        parkingPaymentMorePage = MyFfanMyParkingPaymentMorePage(self, self.driver, self.logger)
        parkingPaymentUnbundingPage = MyFfanMyParkingPaymentUnbundingPage(self, self.driver, self.logger)'''

        # Click "停车交费"， load "我的排队" page.
        dashboardPage.validSelf();
        dashboardPage.clickOnMy();
        myFfanPage.validSelf();
        myFfanPage.clickOnParkingPayment();
        parkingPaymentPage.validSelf();

        # Bunding VIN
        parkingPaymentPage.waitBySeconds(2);
        '''parkingPaymentPage.clickOnBanding();
        parkingPaymentPage.inputVIN();
        parkingPaymentPage.clickOnNextBtn();
        parkingPaymentDetailsPage.validSelf();

        # Unbunding VIN
        parkingPaymentDetailsPage.clickOnMore();
        parkingPaymentMorePage.waitBySeconds(2);
        parkingPaymentMorePage.clickOnUnbundingBtn();
        parkingPaymentUnbundingPage.clickOnUnbundingBtn();
        parkingPaymentPage.validSelf();'''

        #检查入口项目
        '''itemList = (u"附近停车场", u"停车券", u"停车记录", u"帮助")
        titleList = (u"停车场列表", u"停车优惠券", u"停车记录", u"停车帮助")
        for i in range(len(titleList)):
            parkingPaymentPage.clickAndValidItems(itemList[i], titleList[i])
            parkingPaymentPage.waitBySeconds(2)'''

if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(WoDeTingCheJiaoFeiTestCase)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = os.path.join(reportpath, 'Feifan_automation_test_report_' + now + '.html')
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Feifan_automation_test_report', description='Result for test')
    runner.run(suite)