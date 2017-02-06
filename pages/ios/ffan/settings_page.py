# -*- coding: utf-8 -*-

from api.api import API
from pages.ios.common.superPage import SuperPage
from pages.ios.ffan.settings_page_configs import SettingsPageConfigs
from pages.logger import logger


class SettingsPage(SuperPage):
    '''
    作者 宋波
    首页=>我的飞凡=>设置
    '''

    def __init__(self, testcase, driver, logger):
        super(SettingsPage, self).__init__(testcase=testcase, driver=driver, logger=logger);

    def validSelf(self):
        logger.info("Check 我的设置 begin")
        API().assertElementByName(self.testcase, self.driver, self.logger,
                                  SettingsPageConfigs.name_title_st,
                                  SettingsPageConfigs.assert_view_timeout)
        logger.info("Check 我的设置 end")
        API().screenShot(self.driver, "setting")

    def clickOnQuitAccountBtn(self, confirmQuit=True):
        logger.info("Click 退出登录 begin")
        API().clickElementByName(self.testcase, self.driver, self.logger,
                                 SettingsPageConfigs.name_exit_from_current_account_st,
                                 SettingsPageConfigs.click_on_button_timeout)
        if confirmQuit:
            API().clickElementByName(self.testcase, self.driver, self.logger,
                                     SettingsPageConfigs.name_confirm_bt,
                                     SettingsPageConfigs.click_on_button_timeout)
        else:
            API().clickElementByName(self.testcase, self.driver, self.logger,
                                     SettingsPageConfigs.name_cancel_bt,
                                     SettingsPageConfigs.click_on_button_timeout)
        logger.info("Click 退出登录 end")

    def clickOnAccountManagement(self):
        '''
        usage: click on the account management button.
        '''
        logger.info("Click 账户管理 begin")
        API().clickElementByName(self.testcase, self.driver, self.logger,
                                 SettingsPageConfigs.name_account_management_st,
                                 SettingsPageConfigs.assert_view_timeout)
        logger.info("Click 账户管理 end")

    def clickOnPaySettings(self):
        '''
        usage:点击支付设置
        '''
        logger.info("Click 支付设置 begin")
        API().clickElementByName(self.testcase, self.driver, self.logger,
                                 SettingsPageConfigs.name_pay_settings,
                                 SettingsPageConfigs.click_on_button_timeout)
        logger.info("Click 支付设置 end")

    def clickOnMianmiPaySettings(self):
        '''
        usage: click on the small account password-less payments button.
        '''
        logger.info("Click 免密支付 begin")
        API().clickElementByName(self.testcase, self.driver, self.logger,
                                 SettingsPageConfigs.name_mianmi_page_settings,
                                 SettingsPageConfigs.click_on_button_timeout)
        logger.info("Click 免密支付 end")


if __name__ == '__main__':
    pass;
