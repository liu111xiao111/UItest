# -*- coding:utf-8 -*-

from api.api import API
from pages.ios.common.superPage import SuperPage
from pages.ios.ffan.activity_and_privilege_coupon_page_configs import ActivityAndPrivilegeCouponPageConfigs


class ActivityAndPrivilegeCouponPage(SuperPage):
    '''
    作者 宋波
    首页=>活动与优惠券
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

        API().assertElementByName(self.testcase, self.driver, self.logger,
                                  ActivityAndPrivilegeCouponPageConfigs.name_activity_title_bt,
                                  ActivityAndPrivilegeCouponPageConfigs.assert_view_timeout)

    def clickOnActivity(self):
        '''
        usage: click activity button
        '''

        API().clickElementByName(self.testcase, self.driver, self.logger,
                                 ActivityAndPrivilegeCouponPageConfigs.name_activity_title_bt,
                                 ActivityAndPrivilegeCouponPageConfigs.click_on_button_timeout)

    def clickOnSpecificActivity(self):
        '''
        usage: click specific activity button
        '''

        API().clickElementByXpath(self.testcase, self.driver, self.logger,
                                  ActivityAndPrivilegeCouponPageConfigs.xpath_specific_activity_st,
                                  ActivityAndPrivilegeCouponPageConfigs.click_on_button_timeout)

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
