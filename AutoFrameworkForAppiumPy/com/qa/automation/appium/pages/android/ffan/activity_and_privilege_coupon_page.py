# -*- coding:utf-8 -*-

from com.qa.automation.appium.api.api_new import API
from com.qa.automation.appium.pages.android.common.super_page import SuperPage
from com.qa.automation.appium.pages.android.ffan.activity_and_privilege_coupon_page_configs import ActivityAndPrivilegeCouponPageConfigs as APCPC


class ActivityAndPrivilegeCouponPage(SuperPage):
    '''
    作者 刘涛
    首页=>优惠券页面
    '''
    def __init__(self, testcase, driver, logger):
        super(ActivityAndPrivilegeCouponPage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        '''
        usage: 验证优惠券界面
        '''
        API().assertElementByResourceId(self.testcase,
                                        self.driver,
                                        self.logger,
                                        APCPC.resource_id_activity_title,
                                        APCPC.assert_view_timeout)

    def clickOnActivity(self):
        '''
        usage: 点击活动
        '''
        API().clickElementByResourceId(self.testcase,
                                       self.driver,
                                       self.logger, 
                                       APCPC.resource_id_activity_title,
                                       APCPC.click_on_button_timeout)

    def clickOnSpecificActivity(self):
        '''
        usage: 点击具体活动
        '''
        API().clickElementByResourceId(self.testcase,
                                       self.driver,
                                       self.logger,
                                       APCPC.resource_id_specific_activity_button,
                                       APCPC.click_on_button_timeout)

    def clickOnPrivilegeCoupon(self):
        '''
        usage: 点击优惠券
        '''

        API().clickElementByResourceId(self.testcase,
                                       self.driver,
                                       self.logger,
                                       APCPC.resource_id_privilege_coupon_title,
                                       APCPC.click_on_button_timeout)

    def clickOnSpecificPrivilegeCoupon(self):
        '''
        usage: 点击特别优惠
        '''

        API().clickElementByResourceId(self.testcase,
                                       self.driver,
                                       self.logger,
                                       APCPC.resource_id_specific_privilege_coupon_button,
                                       APCPC.click_on_button_timeout)
