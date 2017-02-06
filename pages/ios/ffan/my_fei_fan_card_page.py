# -*- coding:utf-8 -*-

from api.api import API
from pages.ios.common.superPage import SuperPage
from pages.ios.ffan.my_fei_fan_card_page_configs import MyFeiFanCardPageConfigs


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
                                  MyFeiFanCardPageConfigs.name_my_fei_fan_card_title_st,
                                  MyFeiFanCardPageConfigs.assert_view_timeout)

    def clickOnTransactionRecord(self):
        '''
        usage: click on the transaction record button.
        '''

        API().clickElementByName(self.testcase, self.driver, self.logger,
                                 MyFeiFanCardPageConfigs.name_transaction_record_st,
                                 MyFeiFanCardPageConfigs.click_on_button_timeout)
    
    def clickOnLinghuaqian(self):
        '''
        usage: click on the transaction record button.
        '''

        API().clickElementByName(self.testcase, self.driver, self.logger,
                                 MyFeiFanCardPageConfigs.name_linghuaqian_st,
                                 MyFeiFanCardPageConfigs.click_on_button_timeout)  
        
    def validLinghuaqian(self):
        '''
        usage: verify whether the current page is correct page.
        '''

        API().assertElementByName(self.testcase, self.driver, self.logger,
                                  MyFeiFanCardPageConfigs.name_linghuaqian_st,
                                  MyFeiFanCardPageConfigs.assert_view_timeout)      

    def clickOnPayemntsSettings(self):
        '''
        usage: click on the payments settings button.
        '''

        API().clickElementByName(self.testcase, self.driver, self.logger,
                                 MyFeiFanCardPageConfigs.name_payments_settings_st,
                                 MyFeiFanCardPageConfigs.click_on_button_timeout)


if __name__ == '__main__':
    pass
