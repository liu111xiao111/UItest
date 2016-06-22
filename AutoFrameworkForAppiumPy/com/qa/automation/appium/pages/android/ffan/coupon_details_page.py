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

        API().assert_view_by_resourceID_Until_android(self.testcase, self.driver, self.logger,
                                                      CouponDetailsPageConfigs.resource_id_coupon_details_title,
                                                      CouponDetailsPageConfigs.assert_view_timeout)

    def clickOnReceiveFree(self):
        '''
        usage: click on the receive free button.
        '''

        API().click_view_by_text_android(self.testcase, self.driver, self.logger,
                                         CouponDetailsPageConfigs.text_receive_free_button,
                                         CouponDetailsPageConfigs.click_on_button_timeout);


if __name__ == '__main__':
    pass
