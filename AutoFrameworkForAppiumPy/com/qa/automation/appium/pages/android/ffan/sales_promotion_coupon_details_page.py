# -*- coding: utf-8 -*-

import os

#sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from com.qa.automation.appium.api.api import API
from com.qa.automation.appium.pages.android.common.super_page import SuperPage
from com.qa.automation.appium.pages.android.ffan.sales_promotion_coupon_details_page_configs import SalesPromotionCouponDetailsPageConfigs
# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class SalesPromotionCouponDetailsPage(SuperPage):

    def __init__(self,testcase,driver,logger):
        super(SalesPromotionCouponDetailsPage, self).__init__(testcase = testcase , driver = driver, logger = logger);

    def validSelf(self):
        '''
            usage : "优惠券" whether loading correctly.
        '''
        API().assert_view_by_resourceID_Until(testcase = self.testcase, driver = self.driver, logger = self.logger,
                                              resource_id = SalesPromotionCouponDetailsPageConfigs.resource_id_tv_coupon_details_tv, seconds = 10)

    def clickOnFreeOfChargeBtn(self):
        '''
            usage : Click on "免费领取" button.
        ''' 
        '''webview = API().find_view_by_class_name_both(driver=self.driver, logger=self.logger,
                                                     className="android.webkit.WebView")
        webview_1 = webview.find_element_by_android_uiautomator("new UiSelector().className(android.webkit.WebView)")
        textview = webview_1.find_element_by_accessibility_id(SalesPromotionCouponDetailsPageConfigs.text_receive_free_button)
        textview.click()'''
        '''API().click_view_by_content_desc(testcase = self.testcase, driver = self.driver, logger = self.logger,
                                         content_desc = SalesPromotionCouponDetailsPageConfigs.text_receive_free_button, seconds = 10)'''
        '''API().get_view_by_class_name_android(driver=self.driver, logger=self.logger,
                                             className="android.webkit.WebView").click()'''
        API().click_view_by_xpath(testcase = self.testcase, driver = self.driver, logger = self.logger, xpath = SalesPromotionCouponDetailsPageConfigs.xpath_get_free_ticket, seconds = 10)


if __name__ == '__main__':
    pass;