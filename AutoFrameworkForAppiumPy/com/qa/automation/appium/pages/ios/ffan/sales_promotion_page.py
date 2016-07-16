# -*- coding: utf-8 -*-

'''
    首页 -> 优惠页面
'''
from com.qa.automation.appium.api.api import API
from com.qa.automation.appium.pages.ios.common.super_page import SuperPage
from com.qa.automation.appium.pages.ios.ffan.sales_promotion_page_configs import SalesPromotionPageConfigs


class SalesPromotionPage(SuperPage):

    def __init__(self, testcase, driver, logger):
        super(SalesPromotionPage, self).__init__(testcase=testcase , driver=driver, logger=logger);

    def validSelf(self):
        '''
            usage : 判断 "优惠活动" 页显示是否正确
        '''
        API().assert_view_by_resourceID_Until(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                              resource_id=SalesPromotionPageConfigs.resource_id_tv_active_tv, seconds=10)

    def clickOnCouponTab(self):
        '''
            usage : 点击优惠券tab
        '''
        API().click_view_by_resourceID(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                       resource_id=SalesPromotionPageConfigs.resource_id_tv_coupon_tv)

    def clickOnActiveDetails(self):
        '''
            usage : 点击活动详情
        '''
        API().click_view_by_xpath(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                       xpath=SalesPromotionPageConfigs.xpath_active_details_tv)

    def clickOnCouponDetails(self):
        '''
            usage : 点击优惠券详情
        '''
        API().click_view_by_resourceID(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                       text=SalesPromotionPageConfigs.xpath_coupon_details_tv)

    def validSelfListNumber(self, expectLength):
        '''
            usage : 获得活动列表的长度
        '''
        
        activeListNumber = len(API().find_views_by_class_name_both(driver=self.driver, logger=self.logger,
                                                   className=SalesPromotionPageConfigs.type_list_tv))
        API().assert_greater_equal(test_case=self.testcase, driver=self.driver, logger=self.logger,
                                   list_len=activeListNumber, expect_num=expectLength)

    def getCouponListNumber(self):
        '''
            usage : Get coupon list number
        '''
        couponListNumber = API().get_views_by_resourceID(driver=self.driver, logger=self.logger,
                                                   resource_id=SalesPromotionPageConfigs.type_list_tv)
        return couponListNumber;

    def getItemName(self):
        '''
        usage : 获得活动标题名称
        '''
        itemName = API().get_view_by_xpath_ios(self.driver, self.logger,
                                                    SalesPromotionPageConfigs.xpath_active_details_tv).text
        return itemName;

if __name__ == '__main__':
    pass;
