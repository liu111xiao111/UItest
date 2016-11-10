# -*- coding:utf-8 -*-

from api.api import API
from pages.ios.common.superPage import SuperPage
from pages.ios.ffan.message_settings_page_configs import MessageSettingsPageConfigs
from pages.logger import logger

class MessageSettingsPage(SuperPage):
    '''
    作者 宋波
    首页=>我的飞凡=>消息中心=>设置
    '''

    def __init__(self, testcase, driver, logger):
        '''
        Constructor
        '''

        super(MessageSettingsPage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        '''
        usage: verify whether the current page is correct.
        '''
        logger.info("Check 消息中心,设置 begin")
        API().assertElementByName(self.testcase, self.driver, self.logger,
                                  MessageSettingsPageConfigs.resource_id_message_settings_title_st,
                                  MessageSettingsPageConfigs.assert_view_timeout)
        logger.info("Check 消息中心,设置 end")
        API().screenShot(self.driver, "messageSetting")

    def clickOnActivityPush(self):
        '''
        usage: 活动推送
        '''
        logger.info("Click 活动推送 begin")
        API().clickElementByXpath(self.testcase, self.driver, self.logger,
                                  MessageSettingsPageConfigs.xpath_activity_push_compound_sc,
                                  MessageSettingsPageConfigs.click_on_button_timeout)
        logger.info("Click 活动推送 begin")

if __name__ == '__main__':
    pass
