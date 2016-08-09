# -*- coding: utf-8 -*-

from com.qa.automation.appium.api.api_new import API
from com.qa.automation.appium.pages.android.common.super_page import SuperPage
from com.qa.automation.appium.pages.android.ffan.sales_promotion_coupon_details_page_configs import SalesPromotionCouponDetailsPageConfigs as SPCDPC

class SalesPromotionCouponDetailsPage(SuperPage):
    '''
    作者 刘涛
    首页=>优惠活动(优惠券)=>门店详情页
    '''

    def __init__(self,testcase,driver,logger):
        super(SalesPromotionCouponDetailsPage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        '''
            usage : "优惠券" 页加载是否正确
        '''
        API().assertElementByContentDesc(self.testcase,
                                         self.driver,
                                         self.logger,
                                         SPCDPC.text_tv_coupon_details,
                                         10)

    def clickOnFreeOfChargeBtn(self):
        '''
            usage : 点击 "免费领取"
        ''' 
        API().clickElementByContentDesc(self.testcase,
                                        self.driver,
                                        self.logger,
                                        SPCDPC.text_receive_free_button,
                                        10)
