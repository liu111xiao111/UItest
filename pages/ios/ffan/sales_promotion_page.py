# -*- coding: utf-8 -*-

from api.api import API
from pages.ios.common.superPage import SuperPage
from pages.ios.ffan.sales_promotion_page_configs import SalesPromotionPageConfigs


class SalesPromotionPage(SuperPage):
    '''
    作者 刘涛
    首页=>优惠活动
    '''

    def __init__(self, testcase, driver, logger):
        super(SalesPromotionPage, self).__init__(testcase=testcase , driver=driver, logger=logger);

    def validSelf(self):
        '''
            usage : 判断 "优惠活动" 页显示是否正确
        '''
        API().assertElementByName(testCase=self.testcase,
                                  driver=self.driver,
                                  logger=self.logger,
                                  name=SalesPromotionPageConfigs.name_tv_active_tv);

    def clickOnCouponTab(self):
        '''
            usage : 点击优惠券tab
        '''
        API().clickElementByName(self.testcase,
                                 self.driver,
                                 self.logger,
                                 SalesPromotionPageConfigs.name_tv_coupon_tv)

    def clickOnActiveDetails(self):
        '''
            usage : 点击活动详情
        '''
        API().clickElementByXpath(self.testcase,
                                  self.driver,
                                  self.logger,
                                  SalesPromotionPageConfigs.xpath_active_details_tv)

    def clickOnCouponDetails(self):
        '''
            usage : 点击优惠券详情
        '''
        API().clickElementByXpath(self.testcase,
                                  self.driver,
                                  self.logger,
                                  SalesPromotionPageConfigs.xpath_coupon_details_tv)

    def validSelfListNumber(self, expectLength):
        '''
            usage : 获得活动列表的长度
        '''
        activeListNumber = len(API().getElementsByType(testCase=self.testcase,
                                                       driver=self.driver,
                                                       logger=self.driver,
                                                       elementType=SalesPromotionPageConfigs.type_list_tv))

        API().assertGreaterEqual(testCase=self.testcase,
                                 logger=self.logger,
                                 listLength=activeListNumber,
                                 expectNum=expectLength)

    def getCouponListNumber(self):
        '''
            usage : Get coupon list number
        '''
        couponListNumber = API().getElementsByType(testCase=self.testcase,
                                                   driver=self.driver,
                                                   logger=self.logger,
                                                   elementType=SalesPromotionPageConfigs.type_list_tv)
        return couponListNumber;

    def getItemName(self):
        '''
        usage : 获得活动标题名称
        '''
        itemName = API().getTextByXpath(self.testcase,
                                        self.driver,
                                        self.logger,
                                        SalesPromotionPageConfigs.xpath_active_details_tv)
        return itemName;

if __name__ == '__main__':
    pass;
