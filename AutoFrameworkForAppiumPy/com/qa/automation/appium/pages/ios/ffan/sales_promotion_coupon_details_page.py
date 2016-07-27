# -*- coding: utf-8 -*-

from com.qa.automation.appium.api.api_new import API
from com.qa.automation.appium.pages.ios.common.super_page import SuperPage
from com.qa.automation.appium.pages.ios.ffan.sales_promotion_coupon_details_page_configs import SalesPromotionCouponDetailsPageConfigs

class SalesPromotionCouponDetailsPage(SuperPage):
    '''
    作者 刘涛
    首页=>优惠活动(优惠券)=>门店详情页
    '''

    def __init__(self,testcase,driver,logger):
        super(SalesPromotionCouponDetailsPage, self).__init__(testcase = testcase , driver = driver, logger = logger);

    def validSelf(self, itemtext="default"):
        '''
            usage : "优惠券" 页加载是否正确
        '''
        couponName = API().getTextByXpath(self.testcase,
                                        self.driver, 
                                        self.logger,
                                        SalesPromotionCouponDetailsPageConfigs.xpath_coupon_details_title_tv)
        API().assertEqual(self.testcase, self.logger, itemtext, couponName)

    def clickOnFreeOfChargeBtn(self):
        '''
            usage : 点击 "免费领取"
        '''
        API().clickElementByXpath(self.testcase,
                                  self.driver,
                                  self.logger,
                                  SalesPromotionCouponDetailsPageConfigs.xpath_get_free_ticket)

if __name__ == '__main__':
    pass;