# -*- coding:utf-8 -*-

from com.qa.automation.appium.api.api_new import API
from com.qa.automation.appium.pages.android.common.super_page import SuperPage
from com.qa.automation.appium.pages.android.ffan.activity_details_page_configs import ActivityDetailsPageConfigs as ADPC


class ActivityDetailsPage(SuperPage):
    '''
    作者 刘涛
    首页=>活动=>活动详情界面
    '''

    def __init__(self, testcase, driver, logger):
        super(ActivityDetailsPage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        '''
        usage: 验证活动详情界面
        '''
        API().assertElementByContentDesc(self.testcase,
                                         self.driver,
                                         self.logger,
                                         ADPC.content_desc_activity_detail,
                                         45)

    def clickOnSharing(self):
        '''
        usage: 点击分享按钮
        '''
        API().clickElementByXpath(self.testcase,
                                  self.driver,
                                  self.logger,
                                  ADPC.xpath_sharing_button,
                                  ADPC.click_on_button_timeout)
