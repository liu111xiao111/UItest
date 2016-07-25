# -*- coding: utf-8 -*-

from com.qa.automation.appium.api.api_new import API
from com.qa.automation.appium.pages.android.common.super_page import SuperPage
from com.qa.automation.appium.pages.android.ffan.store_image_text_details_page_configs import StoreImageTextDetailsPageConfigs as SITDPC


class StoreImageTextDetailsPage(SuperPage):
    '''
    作者 宋波
    首页=>搜索页=>门店信息=>门店图文详情
    '''
    def __init__(self, testcase, driver, logger):
        super(StoreImageTextDetailsPage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        '''
        usage: 验证门店图文详情界面
        '''
        API().assertElementByResourceId(self.testcase,
                                        self.driver,
                                        self.logger,
                                        SITDPC.resource_id_store_image_text_details,
                                        SITDPC.assert_view_timeout)

    def validKeywords(self, keywords):
        '''
        usage: 验证关键字
        '''
        API().assertElementByContentDesc(self.testcase,
                                         self.driver,
                                         self.logger,
                                         keywords,
                                         SITDPC.assert_view_timeout)
