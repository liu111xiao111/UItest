#!/usr/bin/env python
# -*- coding:utf-8 -*-

from com.qa.automation.appium.api.api import API
from com.qa.automation.appium.pages.android.common.super_page import SuperPage
from com.qa.automation.appium.pages.android.ffan.hui_life_page_configs import HuiLifePageConfigs


class HuiLifePage(SuperPage):
    '''
    This is hui life page operation class.
    '''

    def __init__(self, testcase, driver, logger):
        '''
        Constructor
        '''

        super(HuiLifePage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        '''
        usage: verify whether the current page is correct page.
        '''

        API().assert_view_by_text_android(self.testcase, self.driver, self.logger,
                                          HuiLifePageConfigs.text_activity_button,
                                          HuiLifePageConfigs.assert_view_timeout)

    def clickOnActivity(self):
        '''
        usage: click on the activity button.
        '''

        API().click_view_by_text_android(self.testcase, self.driver, self.logger,
                                         HuiLifePageConfigs.text_activity_button,
                                         HuiLifePageConfigs.click_on_button_timeout);

    def clickOnPrivilege(self):
        '''
        usage: click on the privilege button.
        '''

        API().click_view_by_text_android(self.testcase, self.driver, self.logger,
                                         HuiLifePageConfigs.text_privilege_button,
                                         HuiLifePageConfigs.click_on_button_timeout);

    def clickOnSpecificActivity(self):
        '''
        usage: click on the specific activity button.
        '''

        API().click_view_by_resourceID(self.testcase, self.driver, self.logger,
                                               HuiLifePageConfigs.resource_id_specific_activity_button,
                                               HuiLifePageConfigs.click_on_button_timeout);

    def clickOnSpecificPrivilege(self):
        '''
        usage: click on the specific privilege button.
        '''

        API().click_view_by_resourceID(self.testcase, self.driver, self.logger,
                                               HuiLifePageConfigs.resource_id_specific_privilege_button,
                                               HuiLifePageConfigs.click_on_button_timeout);


# API().scroll_to_text(self.driver, self.logger, HuiLifePageConfigs.text_specific_activity_title)
#         API().click_view_by_xpath(self.testcase, self.driver, self.logger, HuiLifePageConfigs.xpath_specific_privilege_button, HuiLifePageConfigs.click_on_button_timeout)

if __name__ == '__main__':
    pass
