# -*- coding:utf-8 -*-

from com.qa.automation.appium.api.api import API
from com.qa.automation.appium.pages.android.common.super_page import SuperPage
from com.qa.automation.appium.pages.android.ffan.message_settings_page_configs import MessageSettingsPageConfigs


class MessageSettingsPage(SuperPage):
    '''
    This is message settings page operation class.
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

        API().assert_view_by_resourceID_Until(self.testcase, self.driver, self.logger, MessageSettingsPageConfigs.resource_id_message_settings_title, MessageSettingsPageConfigs.assert_view_timeout)

    def clickOnActivityPush(self):
        '''
        usage: click on the activity push switch.
        '''

        API().click_view_by_resourceID(self.testcase, self.driver, self.logger, MessageSettingsPageConfigs.resource_id_activity_push_compound_button, MessageSettingsPageConfigs.click_on_button_timeout)

if __name__ == '__main__':
    pass
