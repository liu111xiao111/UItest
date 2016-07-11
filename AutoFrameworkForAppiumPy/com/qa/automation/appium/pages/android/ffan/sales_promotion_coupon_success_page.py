# -*- coding: utf-8 -*-

from com.qa.automation.appium.api.api import API
from com.qa.automation.appium.pages.android.common.super_page import SuperPage
from com.qa.automation.appium.pages.android.ffan.sales_promotion_coupon_success_page_configs import SalesPromotionCouponSuccessPageConfigs


class SalesPromotionCouponSuccessPage(SuperPage):

    def __init__(self,testcase,driver,logger):
        super(SalesPromotionCouponSuccessPage, self).__init__(testcase = testcase , driver = driver, logger = logger);

    def validSelf(self):
        '''
            usage : Check "领券成功" whether loading correctly.
        '''
        API().assert_view_by_resourceID_Until(testcase = self.testcase, driver = self.driver, logger = self.logger,
                                              resource_id = SalesPromotionCouponSuccessPageConfigs.resource_id_tv_coupon_success_title_tv, seconds = 10)

    def getCouponDetails(self):
        '''
            usage : "优惠券" details correctly.
        '''
        orderDetails = API().get_view_by_resourceID(self.driver, self.logger,
                                                    SalesPromotionCouponSuccessPageConfigs.resource_id_tv_coupon_details_tv).text
        return orderDetails;

    def clickOnCheckMyTicketBtn(self):
        '''
            usage : Click on "查看我的票券" button.
        ''' 
        API().click_view_by_text_android(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                         text=SalesPromotionCouponSuccessPageConfigs.text_check_my_ticket_button)

if __name__ == '__main__':
    pass;