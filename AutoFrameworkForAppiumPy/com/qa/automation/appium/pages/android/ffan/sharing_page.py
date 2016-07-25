# -*- coding:utf-8 -*-

from com.qa.automation.appium.api.api_new import API
from com.qa.automation.appium.pages.android.common.super_page import SuperPage
from com.qa.automation.appium.pages.android.ffan.sharing_page_configs import SharingPageConfigs as SPC

class SharingPage(SuperPage):
    '''
    作者 刘涛
    首页=>活动=>活动详情界面=>分享界面
    '''

    def __init__(self, testcase, driver, logger):
        super(SharingPage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        '''
        usage: 验证分享界面
        '''
        API().assertElementByResourceId(self.testcase,
                                        self.driver,
                                        self.logger,
                                        SPC.resource_id_sharing_title,
                                        SPC.assert_view_timeout)

    def validKeywords(self, keywords):
        '''
        usage: 验证关键字
        '''
        API().assertElementByText(self.testcase,
                                  self.driver,
                                  self.logger,
                                  keywords,
                                  SPC.assert_view_timeout)
