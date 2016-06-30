#!/usr/bin/env python
# -*- coding:utf-8 -*-

from com.qa.automation.appium.api.api import API
from com.qa.automation.appium.pages.android.common.super_page import SuperPage
from com.qa.automation.appium.pages.android.ffan.coupon_details_page_configs import CouponDetailsPageConfigs


class CouponDetailsPage(SuperPage):
    '''
    This is hui life page operation class.
    '''

    def __init__(self, testcase, driver, logger):
        '''
        Constructor
        '''

        super(CouponDetailsPage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        '''
        usage: verify whether the current page is correct page.
        '''

        API().assert_view_by_resourceID_Until(self.testcase, self.driver, self.logger,
                                                      CouponDetailsPageConfigs.resource_id_coupon_details_title,
                                                      CouponDetailsPageConfigs.assert_view_timeout)

    def clickOnReceiveFree(self):
        '''
        usage: click on the receive free button.
        '''

        # API().click_view_by_text_android(self.testcase, self.driver, self.logger,
        #                                  CouponDetailsPageConfigs.text_receive_free_button,
        #                                  CouponDetailsPageConfigs.click_on_button_timeout);

        webview = API().find_view_by_class_name_both(driver=self.driver, logger=self.logger,
                                                     className="android.webkit.WebView")
        webview_1 = webview.find_element_by_android_uiautomator("new UiSelector().className(android.webkit.WebView)")
        textview = webview_1.find_element_by_accessibility_id(CouponDetailsPageConfigs.text_receive_free_button)
        textview.click()


if __name__ == '__main__':
    pass
