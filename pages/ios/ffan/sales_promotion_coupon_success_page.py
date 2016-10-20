# -*- coding: utf-8 -*-

import logging
from api.api import API
from pages.ios.common.superPage import SuperPage
from pages.ios.ffan.sales_promotion_coupon_success_page_configs import SalesPromotionCouponSuccessPageConfigs


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
        logging.info('Verify sales promotion coupon.')
        API().assertElementByName(testCase=self.testcase,
                                  driver=self.driver,
                                  logger=self.logger,
                                  name=SalesPromotionCouponSuccessPageConfigs.name_tv_coupon_success_tv,
                                  timeout=20)

    def getCouponDetails(self):
        '''
            usage : "优惠券" details correctly.
        '''
        logging.info('Get coupon details.')
        orderDetails = API().getTextByXpath(self.testcase,
                                        self.driver, 
                                        self.logger,
                                        SalesPromotionCouponSuccessPageConfigs.xpath_tv_coupon_details_tv)
        return orderDetails[5:];

    def clickOnCheckMyTicketBtn(self):
        '''
            usage : 点击 "查看订单" button.
        '''
        logging.info('Click on check my ticket button.')
        API().clickElementByXpath(self.testcase,
                                  self.driver,
                                  self.logger,
                                  SalesPromotionCouponSuccessPageConfigs.xpath_click_my_ticket_button)

if __name__ == '__main__':
    pass;
