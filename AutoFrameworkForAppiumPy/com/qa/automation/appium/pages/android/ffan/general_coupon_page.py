# -*- coding:utf-8 -*-

from __init__ import *

from com.qa.automation.appium.api.api import API
from com.qa.automation.appium.pages.android.common.super_page import SuperPage
from com.qa.automation.appium.pages.android.ffan.general_coupon_page_configs import GeneralCouponPageConfigs


class GeneralCouponPage(SuperPage):
    '''
    This is general coupon page operation class.
    '''


    def __init__(self, testcase, driver, logger):
        '''
        Constructor
        '''

        super(GeneralCouponPage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        '''
        usage: verify whether the current page is correct.
        '''

        API().assert_view_by_resourceID_Until(self.testcase, self.driver, self.logger,
                                              GeneralCouponPageConfigs.resource_id_general_coupon_title,
                                              GeneralCouponPageConfigs.assert_view_timeout)

    def clickOnImmediatelyToReceive(self):
        '''
        usage: click on the immediately to receive button.
        '''

        API().click_view_by_xpath(self.testcase, self.driver, self.logger,
                                  GeneralCouponPageConfigs.xpath_immediately_to_receive,
                                  GeneralCouponPageConfigs.click_on_button_timeout)

if __name__ == '__main__':
    pass
