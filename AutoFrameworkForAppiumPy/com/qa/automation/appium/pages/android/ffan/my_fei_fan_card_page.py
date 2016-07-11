# -*- coding:utf-8 -*-

from com.qa.automation.appium.api.api import API
from com.qa.automation.appium.pages.android.common.super_page import SuperPage
from com.qa.automation.appium.pages.android.ffan.my_fei_fan_card_page_configs import MyFeiFanCardPageConfigs


class MyFeiFanCardPage(SuperPage):
    '''
    This is a my fei fan card page operation class.
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

        API().assert_view_by_resourceID_Until(self.testcase, self.driver, self.logger, MyFeiFanCardPageConfigs.resource_id_my_fei_fan_card_title, MyFeiFanCardPageConfigs.assert_view_timeout)

    def clickOnTransactionRecord(self):
        '''
        usage: click on the transaction record button.
        '''

        API().click_view_by_text_android(self.testcase, self.driver, self.logger, MyFeiFanCardPageConfigs.text_transaction_record_button, MyFeiFanCardPageConfigs.click_on_button_timeout)

    def clickOnPayemntsSettings(self):
        '''
        usage: click on the payments settings button.
        '''

        API().click_view_by_text_android(self.testcase, self.driver, self.logger, MyFeiFanCardPageConfigs.text_payments_settings_button, MyFeiFanCardPageConfigs.click_on_button_timeout)

if __name__ == '__main__':
    pass
