# -*- coding: utf-8 -*-

from com.qa.automation.appium.api.api_new import API
from com.qa.automation.appium.pages.ios.common.super_page import SuperPage
from com.qa.automation.appium.pages.ios.ffan.settings_page_configs import SettingsPageConfigs


class SettingsPage(SuperPage):
    '''
    作者 宋波
    首页=>我的飞凡=>设置
    '''

    def __init__(self, testcase, driver, logger):
        super(SettingsPage, self).__init__(testcase=testcase, driver=driver, logger=logger);

    def validSelf(self):
        API().assertElementByName(self.testcase, self.driver, self.logger,
                                  SettingsPageConfigs.resource_id_title_st,
                                  SettingsPageConfigs.assert_view_timeout)

    def clickOnQuitAccountBtn(self, confirmQuit=True):
        API().clickElementByName(self.testcase, self.driver, self.logger,
                                 SettingsPageConfigs.resource_id_exit_from_current_account_st,
                                 SettingsPageConfigs.click_on_button_timeout)
        if confirmQuit:
            API().clickElementByName(self.testcase, self.driver, self.logger,
                                     SettingsPageConfigs.resource_id_confirm_bt,
                                     SettingsPageConfigs.click_on_button_timeout)
        else:
            API().clickElementByName(self.testcase, self.driver, self.logger,
                                     SettingsPageConfigs.resource_id_cancel_bt,
                                     SettingsPageConfigs.click_on_button_timeout)

    def clickOnAccountManagement(self):
        '''
        usage: click on the account management button.
        '''

        API().clickElementByName(self.testcase, self.driver, self.logger,
                                 SettingsPageConfigs.resource_id_account_management_st,
                                 SettingsPageConfigs.assert_view_timeout)


if __name__ == '__main__':
    pass;
