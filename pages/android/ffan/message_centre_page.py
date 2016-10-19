# -*- coding:utf-8 -*-

from api.api import API
from pages.android.common.super_page import SuperPage
from pages.android.ffan.message_centre_page_configs import MessageCentrePageConfigs as MCPC


class MessageCentrePage(SuperPage):
    '''
    作者 宋波
    首页=>我的飞凡=>消息中心
    '''

    def __init__(self, testcase, driver, logger):
        super(MessageCentrePage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        '''
        usage: 验证消息中心
        '''
        API().assertElementByResourceId(self.testcase,
                                        self.driver,
                                        self.logger,
                                        MCPC.resource_id_message_centre_title,
                                        MCPC.assert_view_timeout)

    def clickOnSettings(self):
        '''
        usage: 点击设置
        '''
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 MCPC.text_settings_button,
                                 MCPC.click_on_button_timeout)

    def clickOnFeiFanActivity(self):
        '''
        usage: 点击飞凡活动
        '''
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 MCPC.text_fei_fan_activity,
                                 MCPC.click_on_button_timeout)

    def clickOnSquareDynamic(self):
        '''
        usage: 点击广场动态
        '''
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 MCPC.text_square_dynamic,
                                 MCPC.click_on_button_timeout)

    def clickOnBrandActivity(self):
        '''
        usage: 点击品牌活动
        '''
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 MCPC.text_brand_activity,
                                 MCPC.click_on_button_timeout)

    def clickOnStoreMessage(self):
        '''
        usage: 点击商户信息
        '''
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 MCPC.text_store_message,
                                 MCPC.click_on_button_timeout)
