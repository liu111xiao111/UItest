# -*- coding: utf-8 -*-

from com.qa.automation.appium.api.api_new import API
from com.qa.automation.appium.pages.android.common.super_page import SuperPage

class SalesPromotionActiveDetailsPage(SuperPage):
    '''
    作者 刘涛
    首页=>优惠活动=>活动详情页
    '''
    def __init__(self,testcase,driver,logger):
        super(SalesPromotionActiveDetailsPage, self).__init__(testcase, driver, logger);

    def validSelf(self, itemtext="default"):
        '''
            usage : "活动详情" 页加载是否正确
        '''
        API().assertElementByContentDesc(self.testcase,
                                         self.driver,
                                         self.logger,
                                         itemtext,
                                         10)
