# -*- coding: utf-8 -*-

from com.qa.automation.appium.pages.android.ffan.square_coupon_page_configs import SquareCouponPageConfigs
from com.qa.automation.appium.api.api import API
from com.qa.automation.appium.pages.android.common.super_page import SuperPage


'''
    usage : 广场模块，优惠券
'''
class SquareCouponPage(SuperPage):
    def __init__(self, testcase, driver, logger):
        super(SquareCouponPage, self).__init__(testcase=testcase, driver=driver, logger=logger);

    def validSelf(self):
        API().assert_view_by_xpath_android(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                           xpath=SquareCouponPageConfigs.xpath_coupon_list_first_item)

    '''
        usage : click list item
    '''

    def clickOnListItem(self):
        API().click_view_by_xpath(testcase=self.testcase, driver=self.driver, logger=self.driver,
                                  xpath=SquareCouponPageConfigs.xpath_coupon_list_first_item)


if __name__ == '__main__':
    pass;