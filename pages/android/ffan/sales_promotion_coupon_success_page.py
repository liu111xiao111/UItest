# -*- coding: utf-8 -*-

from api.api import API
from pages.android.common.super_page import SuperPage
from pages.android.ffan.sales_promotion_coupon_success_page_configs import SalesPromotionCouponSuccessPageConfigs as SPCSPC


class SalesPromotionCouponSuccessPage(SuperPage):
    '''
    作者 刘涛
    首页=>优惠活动(优惠券)=>门店详情页=>领券成功页
    '''
    def __init__(self,testcase,driver,logger):
        super(SalesPromotionCouponSuccessPage, self).__init__(testcase, driver, logger);

    def validSelf(self):
        '''
            usage : 判断 "领券成功"
        '''
        API().assertElementByResourceId(self.testcase,
                                        self.driver,
                                        self.logger,
                                        SPCSPC.resource_id_tv_coupon_success_title_tv,
                                        10)

    def getCouponDetails(self):
        '''
            usage : "优惠券" details correctly.
        '''
        orderDetails = API().getTextByResourceId(self.testcase,
                                                 self.driver,
                                                 self.logger,
                                                SPCSPC.resource_id_tv_coupon_details_tv,
                                                10)
        return orderDetails

    def clickOnCheckMyTicketBtn(self):
        '''
            usage : 点击 "查看订单" button.
        '''
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 SPCSPC.text_check_my_ticket_button,
                                 10)