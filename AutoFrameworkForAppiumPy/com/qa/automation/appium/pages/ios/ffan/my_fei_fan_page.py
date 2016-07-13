# -*- coding:utf-8 -*-

from com.qa.automation.appium.api.api import API
from com.qa.automation.appium.pages.ios.common.super_page import SuperPage
from com.qa.automation.appium.pages.ios.ffan.my_fei_fan_page_configs import MyFeiFanPageConfigs


class MyFeiFanPage(SuperPage):
    '''
    This is a My FeiFan page operation class.
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

        API().assert_view_by_resourceID_Until(self.testcase, self.driver, self.logger,
                                              MyFeiFanPageConfigs.resource_id_my_fei_fan_title_st,
                                              MyFeiFanPageConfigs.assert_view_timeout)

    def validLoginStatus(self):
        '''
        usage: Verify whether the current status is login.
        '''

        API().assert_view_by_resourceID_Until(self.testcase, self.driver, self.logger,
                                              MyFeiFanPageConfigs.resource_id_nickname_st,
                                              MyFeiFanPageConfigs.assert_view_timeout)

    def validLogoutStatus(self):
        '''
        usage: Verify whether the current status is logout.
        '''

        for _ in range(3):
            self.scrollAsScreenPercent(0.5, 0.4, 0.5, 0.6)
        API().assert_view_by_resourceID_Until(self.testcase, self.driver, self.logger,
                                              MyFeiFanPageConfigs.resource_id_login_bt,
                                              MyFeiFanPageConfigs.assert_view_timeout)

    def clickOnLogin(self):
        '''
        usage: click on the login button.
        '''

        API().click_view_by_resourceID(self.testcase, self.driver, self.logger,
                                               MyFeiFanPageConfigs.resource_id_login_button);

    def clickOnSettings(self):
        '''
        usage: click on the settings button.
        '''

        for _ in range(3):
            self.scrollAsScreenPercent(0.5, 0.8, 0.5, 0.2)
        API().click_view_by_resourceID(self.testcase, self.driver, self.logger,
                                       MyFeiFanPageConfigs.resource_id_settings_st,
                                       MyFeiFanPageConfigs.click_on_button_timeout)

    def clickOnMessageCentre(self):
        '''
        usage: click on the message centre button.
        '''

        API().click_view_by_resourceID(self.testcase, self.driver, self.logger,
                                               MyFeiFanPageConfigs.resource_id_message_centre_button,
                                               MyFeiFanPageConfigs.click_on_button_timeout);

    def clickOnMembershipCardPackage(self):
        '''
        usage: click on the membership card package button.
        '''

        API().click_view_by_text_android(self.testcase, self.driver, self.logger,
                                         MyFeiFanPageConfigs.text_membership_card_package_button,
                                         MyFeiFanPageConfigs.click_on_button_timeout);

    def clickOnNickname(self):
        '''
        usage: click on the nickname button.
        '''

        API().click_view_by_resourceID(self.testcase, self.driver, self.logger,
                                               MyFeiFanPageConfigs.resource_id_nickname_button,
                                               MyFeiFanPageConfigs.click_on_button_timeout);

    def clickOnMyFeiFanCard(self):
        '''
        usage: click on the my fei fan card button.
        '''

        API().scroll_to_text(self.driver, self.logger, MyFeiFanPageConfigs.text_my_fei_fan_card)
        API().click_view_by_text_android(self.testcase, self.driver, self.logger,
										MyFeiFanPageConfigs.text_my_fei_fan_card)


if __name__ == '__main__':
    pass
