# -*- coding: utf-8 -*-

from com.qa.automation.appium.api.api_new import API
from com.qa.automation.appium.pages.ios.common.super_page import SuperPage
from com.qa.automation.appium.pages.ios.ffan.sales_promotion_coupon_success_page_configs import SalesPromotionCouponSuccessPageConfigs


class SalesPromotionCouponSuccessPage(SuperPage):
    '''
    作者 刘涛
    首页=>优惠活动(优惠券)=>门店详情页=>领券成功页
    '''

    def __init__(self, testcase, driver, logger):
        super(SalesPromotionCouponSuccessPage, self).__init__(testcase=testcase , driver=driver, logger=logger);

    def validSelf(self):
        '''
            usage : 判断 "领券成功"
        '''
        API().assertElementByName(testCase=self.testcase,
                                  driver=self.driver,
                                  logger=self.logger,
                                  name=SalesPromotionCouponSuccessPageConfigs.name_tv_coupon_success_tv)

    def getCouponDetails(self):
        '''
            usage : "优惠券" details correctly.
        '''
        orderDetails = API().getTextByXpath(self.testcase,
                                        self.driver, 
                                        self.logger,
                                        SalesPromotionCouponSuccessPageConfigs.xpath_tv_coupon_details_tv)
        return orderDetails[5:];

    def clickOnCheckMyTicketBtn(self):
        '''
            usage : 点击 "查看订单" button.
        '''
        API().clickElementByXpath(self.testcase,
                                  self.driver,
                                  self.logger,
                                  SalesPromotionCouponSuccessPageConfigs.xpath_click_my_ticket_button)

if __name__ == '__main__':
    pass;
