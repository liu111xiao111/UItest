# -*- coding:utf-8 -*-

from api.api import API
from pages.ios.common.superPage import SuperPage
from pages.ios.ffan.coupon_details_page_configs import CouponDetailsPageConfigs


class CouponDetailsPage(SuperPage):
    '''
    作者 宋波
    首页=>惠生活页面=>券详情
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

    def clickOnSharing(self):
        '''
        usage: click sharing button
        '''

        API().click_view_by_xpath(self.testcase, self.driver, self.logger, CouponDetailsPageConfigs.xpath_sharing_button, CouponDetailsPageConfigs.click_on_button_timeout)


if __name__ == '__main__':
    pass
