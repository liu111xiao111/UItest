# -*- coding: utf-8 -*-

from com.qa.automation.appium.api.api import API
from com.qa.automation.appium.pages.ios.common.super_page import SuperPage
from com.qa.automation.appium.pages.ios.ffan.settings_page_configs import SettingsPageConfigs


#   设置页面
class SettingsPage(SuperPage):
    def __init__(self, testcase, driver, logger):
        super(SettingsPage, self).__init__(testcase=testcase, driver=driver, logger=logger);

    def validSelf(self):
        API().assert_view_by_resourceID_Until(self.testcase, self.driver, self.logger,
                                              SettingsPageConfigs.resource_id_title_st,
                                              SettingsPageConfigs.assert_view_timeout)

    # 点击退出当前账号button
    def clickOnQuitAccountBtn(self, confirmQuit=True):
        API().click_view_by_resourceID(self.testcase, self.driver, self.logger,
                                       SettingsPageConfigs.resource_id_exit_from_current_account_st,
                                       SettingsPageConfigs.click_on_button_timeout)
        if confirmQuit:
            API().click_view_by_resourceID(self.testcase, self.driver, self.logger,
                                           SettingsPageConfigs.resource_id_confirm_bt,
                                           SettingsPageConfigs.click_on_button_timeout)
        else:
            API().click_view_by_resourceID(self.testcase, self.driver, self.logger,
                                           SettingsPageConfigs.resource_id_cancel_bt,
                                           SettingsPageConfigs.click_on_button_timeout)

    def clickOnAccountManagement(self):
        '''
        usage: click on the account management button.
        '''

        API().click_view_by_resourceID(self.testcase, self.driver, self.logger,
                                               SettingsPageConfigs.resource_id_account_management,
                                               SettingsPageConfigs.assert_view_timeout)


if __name__ == '__main__':
    pass;
