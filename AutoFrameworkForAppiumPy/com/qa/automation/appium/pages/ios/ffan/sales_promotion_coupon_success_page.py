# -*- coding: utf-8 -*-

from com.qa.automation.appium.api.api import API
from com.qa.automation.appium.pages.ios.common.super_page import SuperPage
from com.qa.automation.appium.pages.ios.ffan.sales_promotion_coupon_success_page_configs import SalesPromotionCouponSuccessPageConfigs


class SalesPromotionCouponSuccessPage(SuperPage):

    def __init__(self, testcase, driver, logger):
        super(SalesPromotionCouponSuccessPage, self).__init__(testcase=testcase , driver=driver, logger=logger);

    def validSelf(self):
        '''
            usage : 判断 "领券成功"
        '''
        API().assert_view_by_resourceID_Until(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                              resource_id=SalesPromotionCouponSuccessPageConfigs.name_tv_coupon_success_tv, seconds=10)

    def getCouponDetails(self):
        '''
            usage : "优惠券" details correctly.
        '''
        orderDetails = API().get_view_by_resourceID(self.driver, self.logger,
                                                    SalesPromotionCouponSuccessPageConfigs.xpath_tv_coupon_details_tv).text
        return orderDetails[5:];

    def clickOnCheckMyTicketBtn(self):
        '''
            usage : Click on "查看我的票券" button.
        '''
        API().assert_view_by_resourceID_Until(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                         resource_id=SalesPromotionCouponSuccessPageConfigs.text_check_my_ticket_button)

if __name__ == '__main__':
    pass;
