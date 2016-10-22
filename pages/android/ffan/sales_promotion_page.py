# -*- coding: utf-8 -*-

from api.api import API
from pages.android.common.super_page import SuperPage
from pages.android.ffan.sales_promotion_page_configs import SalesPromotionPageConfigs as SPPC


class SalesPromotionPage(SuperPage):
    '''
    作者 刘涛
    首页=>优惠活动
    '''
    def __init__(self,testcase,driver,logger):
        super(SalesPromotionPage, self).__init__(testcase, driver, logger);

    def validSelf(self):
        '''
            usage : 判断 "优惠活动" 页显示是否正确
        '''
        API().assertElementByResourceId(self.testcase,
                                        self.driver,
                                        self.logger,
                                        SPPC.resource_id_tv_coupon_tv,
                                        60)
 
    def clickOnActiveTab(self):
        '''
            usage : 点击优惠券tab
        '''   
        API().clickElementByResourceId(self.testcase,
                                       self.driver,
                                       self.logger,
                                       SPPC.resource_id_tv_active_tv,
                                       10)

    def clickOnCouponTab(self):
        '''
            usage : 点击活动详情
        '''  
        API().clickElementByResourceId(self.testcase,
                                       self.driver,
                                       self.logger,
                                       SPPC.resource_id_tv_coupon_tv,
                                       10)
    
    def clickOnActiveDetails(self):
        '''
            usage : 点击优惠券详情
        '''
        API().clickElementByResourceId(self.testcase,
                                       self.driver,
                                       self.logger,
                                       SPPC.resource_id_tv_active_details_tv,
                                       10)

    def clickOnCouponItem(self):
        '''
            usage : 点击优惠券详情
        '''
        API().clickElementByResourceId(self.testcase,
                                       self.driver,
                                       self.logger,
                                       SPPC.resource_id_tv_coupon_details_tv,
                                       10)

    def clickOnSquareCouponDetails(self):
        '''
            usage : 点击广场优惠券详情列表
        '''
        API().clickElementByText(self.testcase,
                                  self.driver,
                                  self.logger,
                                  SPPC.test_special_store,
                                  30)

    def clickOnCouponDetails(self):
        '''
            usage : 点击活动列表
        '''
        # width = API().getWidthOfDevice(self.driver, self.logger)
        # hight = API().getHeightOfDevice(self.driver, self.logger)
        # for _ in range(4):
        #     API().scroll(self.driver, self.logger, width / 2, hight / 2, width / 2, hight / 3)
        API().clickElementByText(self.testcase,
                                  self.driver,
                                  self.logger,
                                  SPPC.test_special_store,
                                  20)

    def getActiveListNumber(self):
        '''
            usage : 获取活动列表
        '''
        activeListNumber = API().getElementsByResourceId(self.testcase,
                                                         self.driver,
                                                         self.logger,
                                                         SPPC.resource_id_tv_active_details_tv,
                                                         10)
        return activeListNumber

    def getCouponListNumber(self):
        '''
        usage: 获取优惠信息列表
        '''
        couponListNumber = API().getElementsByResourceId(self.testcase,
                                                         self.driver,
                                                         self.logger,
                                                         SPPC.resource_id_tv_active_details_tv,
                                                         10)
        return couponListNumber

    def getItemName(self):
        '''
        usage : 获得活动标题名称
        '''
        itemName = API().getTextByResourceId(self.testcase,
                                             self.driver,
                                             self.logger, 
                                             SPPC.resource_id_tv_active_details_tv,
                                             10)
        return itemName

    def validSelfCoupon(self):
        '''
            usage : 判断 "优惠券" 页显示是否正确
        '''
        API().assertElementByResourceId(self.testcase,
                                        self.driver,
                                        self.logger,
                                        SPPC.resource_id_tv_coupon_tv,
                                        10)

    def getItemNameByXpath(self):
        '''
        usage : 获得活动标题名称
        '''
        itemName = SPPC.test_special_store

        return itemName