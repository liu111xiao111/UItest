# -*- coding:utf-8 -*-

from com.qa.automation.appium.api.api import API
from com.qa.automation.appium.pages.android.common.super_page import SuperPage
from com.qa.automation.appium.pages.android.ffan.activity_and_privilege_coupon_page_configs import ActivityAndPrivilegeCouponPageConfigs


class ActivityAndPrivilegeCouponPage(SuperPage):
    '''
        首页 -> 优惠券页面.
    '''


    def __init__(self, testcase, driver, logger):
        '''
        Constructor
        '''

        super(ActivityAndPrivilegeCouponPage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        '''
        usage: verify whether the current page is correct page.
        '''

        API().assert_view_by_resourceID_Until(self.testcase, self.driver, self.logger, ActivityAndPrivilegeCouponPageConfigs.resource_id_activity_title, ActivityAndPrivilegeCouponPageConfigs.assert_view_timeout)

    def clickOnActivity(self):
        '''
        usage: click activity button
        '''

        API().click_view_by_resourceID(self.testcase, self.driver, self.logger, 
                                       ActivityAndPrivilegeCouponPageConfigs.resource_id_activity_title, ActivityAndPrivilegeCouponPageConfigs.click_on_button_timeout)

    def clickOnSpecificActivity(self):
        '''
        usage: click specific activity button
        '''

        API().click_view_by_resourceID(self.testcase, self.driver, self.logger, ActivityAndPrivilegeCouponPageConfigs.resource_id_specific_activity_button, ActivityAndPrivilegeCouponPageConfigs.click_on_button_timeout)

    def clickOnPrivilegeCoupon(self):
        '''
        usage: click privilege coupon button
        '''

        API().click_view_by_resourceID(self.testcase, self.driver, self.logger, ActivityAndPrivilegeCouponPageConfigs.resource_id_privilege_coupon_title, ActivityAndPrivilegeCouponPageConfigs.click_on_button_timeout)

    def clickOnSpecificPrivilegeCoupon(self):
        '''
        usage: click specific privilege coupon button
        '''

        API().click_view_by_resourceID(self.testcase, self.driver, self.logger, ActivityAndPrivilegeCouponPageConfigs.resource_id_specific_privilege_coupon_button, ActivityAndPrivilegeCouponPageConfigs.click_on_button_timeout)

if __name__ == '__main__':
    pass
