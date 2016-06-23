#!/usr/bin/env python
# -*- coding:utf-8 -*-


from com.qa.automation.appium.api.api import API
from com.qa.automation.appium.pages.android.common.super_page import SuperPage
from com.qa.automation.appium.pages.android.ffan.message_centre_page_configs import MessageCentrePageConfigs


class MessageCentrePage(SuperPage):
    '''
    This is message centre page operation class.
    '''

    def __init__(self, testcase, driver, logger):
        '''
        Constructor
        '''

        super(MessageCentrePage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        '''
        usage: verify whether the current page is the version upgrade page.
        '''

        API().assert_view_by_resourceID_Until(self.testcase, self.driver, self.logger,
                                                      MessageCentrePageConfigs.resource_id_message_centre_title,
                                                      MessageCentrePageConfigs.assert_view_timeout)

    def clickOnSettings(self):
        '''
        usage: click on the settings button.
        '''

        API().click_view_by_text_android(self.testcase, self.driver, self.logger,
                                         MessageCentrePageConfigs.text_settings_button,
                                         MessageCentrePageConfigs.click_on_button_timeout)


if __name__ == '__main__':
    pass
