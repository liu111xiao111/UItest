# -*- coding:utf-8 -*-

from com.qa.automation.appium.api.api_new import API
from com.qa.automation.appium.pages.ios.common.super_page import SuperPage
from com.qa.automation.appium.pages.ios.ffan.my_fei_fan_card_page_configs import MyFeiFanCardPageConfigs


class MyFeiFanCardPage(SuperPage):
    '''
    作者 宋波
    首页=>我的飞凡=>我的飞凡卡
    '''

    def __init__(self, testcase, driver, logger):
        '''
        Constructor
        '''

        super(MyFeiFanCardPage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        '''
        usage: verify whether the current page is correct page.
        '''

        API().assertElementByName(self.testcase, self.driver, self.logger,
                                  MyFeiFanCardPageConfigs.resource_id_my_fei_fan_card_title_st,
                                  MyFeiFanCardPageConfigs.assert_view_timeout)

    def clickOnTransactionRecord(self):
        '''
        usage: click on the transaction record button.
        '''

        API().clickElementByName(self.testcase, self.driver, self.logger,
                                 MyFeiFanCardPageConfigs.resource_id_transaction_record_st,
                                 MyFeiFanCardPageConfigs.click_on_button_timeout)

    def clickOnPayemntsSettings(self):
        '''
        usage: click on the payments settings button.
        '''

        API().clickElementByName(self.testcase, self.driver, self.logger,
                                 MyFeiFanCardPageConfigs.resource_id_payments_settings_st,
                                 MyFeiFanCardPageConfigs.click_on_button_timeout)


if __name__ == '__main__':
    pass
