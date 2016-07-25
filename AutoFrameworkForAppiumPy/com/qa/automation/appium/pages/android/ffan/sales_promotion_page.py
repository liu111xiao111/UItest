# -*- coding: utf-8 -*-

from com.qa.automation.appium.api.api_new import API
from com.qa.automation.appium.pages.android.common.super_page import SuperPage
from com.qa.automation.appium.pages.android.ffan.sales_promotion_page_configs import SalesPromotionPageConfigs as SPPC


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
                                        SPPC.resource_id_tv_active_tv,
                                        10)
 
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

    def clickOnCouponDetails(self):
        '''
            usage : 获得活动列表的长度
        '''
        API().scrollToText(self.driver, self.logger, SPPC.text_special_store)
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 SPPC.text_special_store,
                                 10)

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
