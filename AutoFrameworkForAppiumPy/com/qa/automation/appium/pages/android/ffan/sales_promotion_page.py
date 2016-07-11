# -*- coding: utf-8 -*-

from com.qa.automation.appium.pages.android.ffan.sales_promotion_page_configs import SalesPromotionPageConfigs
from com.qa.automation.appium.api.api import API
from com.qa.automation.appium.pages.android.common.super_page import SuperPage


class SalesPromotionPage(SuperPage):

    def __init__(self,testcase,driver,logger):
        super(SalesPromotionPage, self).__init__(testcase = testcase , driver = driver, logger = logger);

    def validSelf(self):
        '''
            usage : Check "优惠活动" whether loading correctly.
        '''
        API().assert_view_by_resourceID_Until(testcase = self.testcase, driver = self.driver, logger = self.logger,
                                              resource_id = SalesPromotionPageConfigs.resource_id_tv_active_tv, seconds = 10)
 
    def clickOnActiveTab(self):
        '''
            usage : Check active tab
        '''     
        API().click_view_by_resourceID(testcase = self.testcase, driver = self.driver, logger = self.logger,
                                       resource_id = SalesPromotionPageConfigs.resource_id_tv_active_tv)

    def clickOnCouponTab(self):
        '''
            usage : Check coupon tab
        '''     
        API().click_view_by_resourceID(testcase = self.testcase, driver = self.driver, logger = self.logger,
                                       resource_id = SalesPromotionPageConfigs.resource_id_tv_coupon_tv)
    
    def clickOnActiveDetails(self):
        '''
            usage : Check active details
        '''
        API().click_view_by_resourceID(testcase = self.testcase, driver = self.driver, logger = self.logger,
                                       resource_id = SalesPromotionPageConfigs.resource_id_tv_active_details_tv)

    def clickOnCouponDetails(self):
        '''
            usage : Check coupon details
        '''
        API().scroll_to_text(self.driver, self.logger, SalesPromotionPageConfigs.text_special_store)
        API().click_view_by_text_android(testcase = self.testcase, driver = self.driver, logger = self.logger,
                                       text = SalesPromotionPageConfigs.text_special_store)

    def getActiveListNumber(self):
        '''
            usage : Get active list number
        '''
        activeListNumber = API().get_views_by_resourceID(driver = self.driver, logger = self.logger,
                                                   resource_id = SalesPromotionPageConfigs.resource_id_tv_active_details_tv)
        return activeListNumber;

    def getCouponListNumber(self):
        '''
            usage : Get coupon list number
        '''
        couponListNumber = API().get_views_by_resourceID(driver = self.driver, logger = self.logger,
                                                   resource_id = SalesPromotionPageConfigs.resource_id_tv_active_details_tv)
        return couponListNumber;

    def getItemName(self):
        '''
        usage : Get item name.
        '''
        itemName = API().find_view_by_resourceID_Until_android(self.driver, self.logger, 
                                                    SalesPromotionPageConfigs.resource_id_tv_active_details_tv).text
        return itemName;

if __name__ == '__main__':
    pass;