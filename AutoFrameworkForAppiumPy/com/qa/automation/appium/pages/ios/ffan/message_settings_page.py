# -*- coding:utf-8 -*-

from com.qa.automation.appium.api.api_new import API
from com.qa.automation.appium.pages.ios.common.super_page import SuperPage
from com.qa.automation.appium.pages.ios.ffan.message_settings_page_configs import MessageSettingsPageConfigs


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

        API().assertElementByResourceId(self.testcase, self.driver, self.logger,
                                        MessageSettingsPageConfigs.resource_id_message_settings_title_st,
                                        MessageSettingsPageConfigs.assert_view_timeout)

    def clickOnActivityPush(self):
        '''
        usage: click on the activity push switch.
        '''

        API().clickElementByXpath(self.testcase, self.driver, self.logger,
                                  MessageSettingsPageConfigs.xpath_activity_push_compound_sc,
                                  MessageSettingsPageConfigs.click_on_button_timeout)


if __name__ == '__main__':
    pass
