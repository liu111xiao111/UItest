# -*- coding: utf-8 -*-

from com.qa.automation.appium.api.api import API
from com.qa.automation.appium.pages.ios.common.super_page import SuperPage
from com.qa.automation.appium.pages.ios.ffan.sales_promotion_coupon_details_page_configs import SalesPromotionCouponDetailsPageConfigs

class SalesPromotionCouponDetailsPage(SuperPage):

    def __init__(self,testcase,driver,logger):
        super(SalesPromotionCouponDetailsPage, self).__init__(testcase = testcase , driver = driver, logger = logger);

    def validSelf(self, itemtext="default"):
        '''
            usage : "优惠券" 页加载是否正确
        '''
        couponName = API().get_view_by_xpath_ios(self.driver, self.logger,
                                    SalesPromotionCouponDetailsPageConfigs.xpath_coupon_details_title_tv).text
        API().assert_equal(self.testcase, self.driver, self.logger, itemtext, couponName)

    def clickOnFreeOfChargeBtn(self):
        '''
            usage : 点击 "免费领取"
        ''' 
        API().click_view_by_xpath(testcase = self.testcase, driver = self.driver, logger = self.logger,
                                       xpath = SalesPromotionCouponDetailsPageConfigs.xpath_get_free_ticket, seconds = 10)


if __name__ == '__main__':
    pass;