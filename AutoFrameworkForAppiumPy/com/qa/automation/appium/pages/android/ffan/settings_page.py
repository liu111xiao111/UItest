# -*- coding: utf-8 -*-

from com.qa.automation.appium.api.api import API
from com.qa.automation.appium.pages.android.common.super_page import SuperPage
from com.qa.automation.appium.pages.android.ffan.settings_page_configs import SettingsPageConfigs


#   设置页面
class SettingsPage(SuperPage):
    def __init__(self, testcase, driver, logger):
        super(SettingsPage, self).__init__(testcase=testcase, driver=driver, logger=logger);

    def validSelf(self):
        API().assert_view_by_resourceID_Until(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                                      resource_id=SettingsPageConfigs.resource_id_setting_account_management_rl,
                                                      seconds=10);

    # 点击退出当前账号button
    def clickOnQuitAccountBtn(self, confirmQuit=True):
        API().click_view_by_resourceID(self.testcase, driver=self.driver, logger=self.logger,
                                               resource_id=SettingsPageConfigs.resource_id_setting_btn_logout_rl);
        if confirmQuit:
            API().click_view_by_text_android(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                             text=SettingsPageConfigs.text_confirm_btn)
        else:
            API().click_view_by_text_android(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                             text=SettingsPageConfigs.text_cancel_btn)

    def clickOnAccountManagement(self):
        '''
        usage: click on the account management button.
        '''

        API().click_view_by_resourceID(self.testcase, self.driver, self.logger,
                                               SettingsPageConfigs.resource_id_account_management,
                                               SettingsPageConfigs.assert_view_timeout)


if __name__ == '__main__':
    pass;
