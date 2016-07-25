# -*- coding:utf-8 -*-

from com.qa.automation.appium.api.api_new import API
from com.qa.automation.appium.pages.android.common.super_page import SuperPage
from com.qa.automation.appium.pages.android.ffan.coupon_details_page_configs import CouponDetailsPageConfigs as CDPC


class CouponDetailsPage(SuperPage):
    '''
    作者 宋波
    首页=>惠生活页面=>券详情
    '''

    def __init__(self, testcase, driver, logger):
        super(CouponDetailsPage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        '''
        usage: 验证券详情界面
        '''
        API().assertElementByResourceId(self.testcase,
                                        self.driver,
                                        self.logger,
                                        CDPC.resource_id_coupon_details_title,
                                        CDPC.assert_view_timeout)

    def clickOnReceiveFree(self):
        '''
        usage: 点击免费领取按钮
        '''
        webview = API().validElementByClassName(self.driver,
                                                self.logger,
                                                "android.webkit.WebView",
                                                CDPC.assert_invalid_view_time)
        webview_1 = webview.find_element_by_android_uiautomator("new UiSelector().className(android.webkit.WebView)")
        textview = webview_1.find_element_by_accessibility_id(CDPC.text_receive_free_button)
        textview.click()

    def clickOnSharing(self):
        '''
        usage: 点击分享
        '''

        API().clickElementByXpath(self.testcase,
                                  self.driver,
                                  self.logger,
                                  CDPC.xpath_sharing_button,
                                  CDPC.click_on_button_timeout)
