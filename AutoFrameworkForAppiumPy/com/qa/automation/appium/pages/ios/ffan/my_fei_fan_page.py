# -*- coding:utf-8 -*-

from com.qa.automation.appium.api.api_new import API
from com.qa.automation.appium.pages.ios.common.super_page import SuperPage
from com.qa.automation.appium.pages.ios.ffan.my_fei_fan_page_configs import MyFeiFanPageConfigs


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

        API().assertElementByResourceId(self.testcase, self.driver, self.logger,
                                        MyFeiFanPageConfigs.resource_id_my_fei_fan_title_st,
                                        MyFeiFanPageConfigs.assert_view_timeout)

    def validLoginStatus(self, assertable=True):
        '''
        usage: Verify whether the current status is login.
        '''

        if assertable:
            API().assertElementByResourceId(self.testcase, self.driver, self.logger,
                                            MyFeiFanPageConfigs.resource_id_nickname_st,
                                            MyFeiFanPageConfigs.assert_view_timeout)
            return True
        else:
            return API().validElementByResourceId(self.driver, self.logger,
                                                  MyFeiFanPageConfigs.resource_id_nickname_st,
                                                  MyFeiFanPageConfigs.assert_view_timeout)

    def validLogoutStatus(self):
        '''
        usage: Verify whether the current status is logout.
        '''

        for _ in range(3):
            self.scrollAsScreenPercent(0.5, 0.4, 0.5, 0.6)
        API().assertElementByResourceId(self.testcase, self.driver, self.logger,
                                        MyFeiFanPageConfigs.resource_id_login_bt,
                                        MyFeiFanPageConfigs.assert_view_timeout)

    def clickOnLogin(self):
        '''
        usage: click on the login button.
        '''

        API().clickElementByResourceId(self.testcase, self.driver, self.logger,
                                       MyFeiFanPageConfigs.resource_id_login_bt,
                                       MyFeiFanPageConfigs.assert_view_timeout)

    def clickOnSettings(self):
        '''
        usage: click on the settings button.
        '''

        for _ in range(3):
            self.scrollAsScreenPercent(0.5, 0.8, 0.5, 0.2)
        API().clickElementByResourceId(self.testcase, self.driver, self.logger,
                                       MyFeiFanPageConfigs.resource_id_settings_st,
                                       MyFeiFanPageConfigs.click_on_button_timeout)

    def clickOnMessageCentre(self):
        '''
        usage: click on the message centre button.
        '''

        API().clickElementByXpath(self.testcase, self.driver, self.logger,
                                  MyFeiFanPageConfigs.xpath_message_centre_bt,
                                  MyFeiFanPageConfigs.click_on_button_timeout)

    def clickOnMembershipCardPackage(self):
        '''
        usage: click on the membership card package button.
        '''

        API().click_view_by_xpath(self.testcase, self.driver, self.logger,
                                  MyFeiFanPageConfigs.xpath_membership_card_package_st,
                                  MyFeiFanPageConfigs.click_on_button_timeout)

    def clickOnNickname(self):
        '''
        usage: click on the nickname button.
        '''

        API().click_view_by_resourceID(self.testcase, self.driver, self.logger,
                                       MyFeiFanPageConfigs.resource_id_nickname_st,
                                       MyFeiFanPageConfigs.click_on_button_timeout)

    def clickOnMyFeiFanCard(self):
        '''
        usage: click on the my fei fan card button.
        '''

        for _ in range(3):
            self.scrollAsScreenPercent(0.5, 0.8, 0.5, 0.2)
        API().clickElementByResourceId(self.testcase, self.driver, self.logger,
                                       MyFeiFanPageConfigs.resource_id_my_fei_fan_card_st,
                                       MyFeiFanPageConfigs.click_on_button_timeout)


if __name__ == '__main__':
    pass
