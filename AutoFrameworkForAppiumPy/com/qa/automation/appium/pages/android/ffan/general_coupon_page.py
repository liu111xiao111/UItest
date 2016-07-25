# -*- coding:utf-8 -*-

from com.qa.automation.appium.api.api_new import API
from com.qa.automation.appium.pages.android.common.super_page import SuperPage
from com.qa.automation.appium.pages.android.ffan.general_coupon_page_configs import GeneralCouponPageConfigs as GCPC


class GeneralCouponPage(SuperPage):
    '''
    作者 宋波
    首页=>广场=>通用券
    '''
    def __init__(self, testcase, driver, logger):
        super(GeneralCouponPage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        '''
        usage: 验证通用券界面
        '''
        API().assertElementByResourceId(self.testcase,
                                        self.driver,
                                        self.logger,
                                        GCPC.resource_id_general_coupon_title,
                                        GCPC.assert_view_timeout)

    def clickOnImmediatelyToReceive(self):
        '''
        usage: 点击马上领取
        '''

        API().clickElementByXpath(self.testcase,
                                  self.driver,
                                  self.logger,
                                  GCPC.xpath_immediately_to_receive,
                                  GCPC.click_on_button_timeout)
