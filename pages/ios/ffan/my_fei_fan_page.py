# -*- coding:utf-8 -*-

import logging

from api.api import API
from pages.ios.common.superPage import SuperPage
from pages.ios.ffan.my_fei_fan_page_configs import MyFeiFanPageConfigs


class MyFeiFanPage(SuperPage):
    '''
    作者 宋波
    首页=>我的飞凡
    '''

    def __init__(self, testcase, driver, logger):
        '''
        Constructor
        '''

        super(MyFeiFanPage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        '''
        usage: verify whether the current page is correct page.
        '''
        logging.info('Verify whether the current page is my feifan page.')
        API().assertElementByName(self.testcase, self.driver, self.logger,
                                  MyFeiFanPageConfigs.resource_id_my_fei_fan_title_st,
                                  MyFeiFanPageConfigs.assert_view_timeout)

    def validLoginStatus(self, assertable=True):
        '''
        usage: Verify whether the current status is login.
        '''
        logging.info('Verify the loging status.')
        if assertable:
            API().assertElementByName(self.testcase, self.driver, self.logger,
                                      MyFeiFanPageConfigs.resource_id_nickname_st,
                                      MyFeiFanPageConfigs.assert_view_timeout)
            return True
        else:
            return API().validElementByName(self.driver, self.logger,
                                            MyFeiFanPageConfigs.resource_id_nickname_st,
                                            MyFeiFanPageConfigs.assert_view_timeout)

    def validLogoutStatus(self):
        '''
        usage: Verify whether the current status is logout.
        '''
        logging.info('Verify the logout status.')
        for _ in range(3):
            self.scrollAsScreenPercent(0.5, 0.4, 0.5, 0.6)
        API().assertElementByName(self.testcase, self.driver, self.logger,
                                  MyFeiFanPageConfigs.resource_id_login_bt,
                                  MyFeiFanPageConfigs.assert_view_timeout)

    def clickOnLogin(self):
        '''
        usage: click on the login button.
        '''
        logging.info('Click on the login button.')
        API().clickElementByName(self.testcase, self.driver, self.logger,
                                 MyFeiFanPageConfigs.resource_id_login_bt,
                                 MyFeiFanPageConfigs.assert_view_timeout)

    def clickOnSettings(self):
        '''
        usage: click on the settings button.
        '''
        logging.info('Click on the settings button.')
        for _ in range(3):
            self.scrollAsScreenPercent(0.5, 0.8, 0.5, 0.2)
        API().clickElementByName(self.testcase, self.driver, self.logger,
                                 MyFeiFanPageConfigs.resource_id_settings_st,
                                 MyFeiFanPageConfigs.click_on_button_timeout)

    def clickOnMessageCentre(self):
        '''
        usage: click on the message centre button.
        '''
        logging.info('Click on the message centre button.')
        API().clickElementByXpath(self.testcase, self.driver, self.logger,
                                  MyFeiFanPageConfigs.xpath_message_centre_bt,
                                  MyFeiFanPageConfigs.click_on_button_timeout)

    def clickOnMembershipCardPackage(self):
        '''
        usage: click on the membership card package button.
        '''
        logging.info('Click on the member ship card package button.')
        API().clickElementByXpath(self.testcase, self.driver, self.logger,
                                  MyFeiFanPageConfigs.xpath_membership_card_package_st,
                                  MyFeiFanPageConfigs.click_on_button_timeout)

    def clickOnNickname(self):
        '''
        usage: click on the nickname button.
        '''
        logging.info('Click on the nickname button.')
        API().clickElementByName(self.testcase, self.driver, self.logger,
                                 MyFeiFanPageConfigs.resource_id_nickname_st,
                                 MyFeiFanPageConfigs.click_on_button_timeout)

    def clickOnMyFeiFanCard(self):
        '''
        usage: click on the my fei fan card button.
        '''
        logging.info('Click on the my fei fan card button.')
        for _ in range(3):
            self.scrollAsScreenPercent(0.5, 0.8, 0.5, 0.2)
        API().clickElementByName(self.testcase, self.driver, self.logger,
                                 MyFeiFanPageConfigs.resource_id_my_fei_fan_card_st,
                                 MyFeiFanPageConfigs.click_on_button_timeout)


if __name__ == '__main__':
    pass
