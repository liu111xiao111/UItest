
# -*- coding: utf-8 -*-

import os
import time
import HTMLTestRunner

from unittest import TestCase
from unittest import TestLoader

from cases.android.ffan.common.test_prepare import TestPrepare
from pages.android.ffan.dashboard_page import DashboardPage
from pages.android.ffan.square_module_page import SquareModulePage
from pages.android.ffan.search_page import SearchPage
from pages.android.ffan.search_result_store_page import SearchResultStorePage
from configs.driver_configs import platformName_andr
from configs.driver_configs import appActivity_ffan
from configs.driver_configs import appPackage_ffan
from configs.driver_configs import deviceName_andr
from configs.driver_configs import driver_url
from driver.appium_driver import AppiumDriver
from utility.logger import Logger
from utility.device_info_util import DeviceInfoUtil
from cases.logger import logger


class GuangChangSouSuoTestCase(TestCase):
    '''
    回归用例： No.10
    用例名: 广场搜索
    广场详情页点击搜索进入搜索，搜索商家和品类，有正常结果显示（广场维度）
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
        TestPrepare(self, self.driver, self.logger).prepare(False)

    def testGuangChangSouSuo(self):
        # 验证首页
        dashboardPage = DashboardPage(self, self.driver, self.logger)
        dashboardPage.validSelf()
        dashboardPage.screenShot("aiGuangJie")

        # 首页(爱逛街页面)点击搜索,通过搜索进入“北京通州万达广场”
        dashboardPage.clickOnSearchView()
        searchPage = SearchPage(self, self.driver, self.logger)
        searchPage.validSelf()
        searchPage.screenShot("souSuo")
        searchPage.inputText("北京通州万达广场")
        searchPage.screenShot("souSuo")
        searchPage.waitBySeconds(5)
        searchPage.clickOnSearch()
        searchPage.waitBySeconds(5)
        searchPage.screenShot("souSuoJieGuo")
        searchPage.clickOnSearchResultFirstItem()
        squareModulePage = SquareModulePage(self, self.driver, self.logger)
        squareModulePage.waitBySeconds(5)
        squareModulePage.validSelf()
        squareModulePage.screenShot("guangChang")

        # 搜索商家
        squareModulePage.clickOnSearch()
        searchPage.validSelf()
        searchPage.screenShot("souSuo")
        searchPage.inputGuangChangStoreName()
        searchPage.screenShot("shuRuMenDian")
        searchPage.clickOnSearch()
        searchPage.validSearchResult(u"帝娜朵拉", "//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/com.wanda.sliding.SlidingLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.ListView[1]/android.widget.LinearLayout[1]/android.widget.ListView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.TextView[1]")
        searchPage.screenShot("souSuoJieGuo")
        searchPage.clickOnFindStoreFirstItem()
        searchResultStorePage = SearchResultStorePage(self, self.driver, self.logger)
        searchResultStorePage.validSelf()
        searchResultStorePage.screenShot("souSuoJieGuoXiangXi")

        # 搜索品牌
        searchResultStorePage.clickBackKey()
        searchPage.inputBrandName()
        searchPage.screenShot("souSuo")
        searchPage.clickOnSearch()
        searchPage.validSearchResult(u"adidas", u"//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/com.wanda.sliding.SlidingLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.ListView[1]/android.widget.LinearLayout[1]/android.widget.ListView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.TextView[1]")
        searchPage.screenShot("souSuoJieGuo")


if __name__ == "__main__":
    suite = TestLoader().loadTestsFromTestCase(GuangChangSouSuoTestCase)
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reportpath = os.getcwd()
    filename = os.path.join(reportpath, 'food-test_' + now + '.html')
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='food-test',
                                           description='Result for test')
    runner.run(suite)
