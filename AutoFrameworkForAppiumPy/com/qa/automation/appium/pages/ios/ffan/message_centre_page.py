# -*- coding:utf-8 -*-

from com.qa.automation.appium.api.api_new import API
from com.qa.automation.appium.pages.ios.common.super_page import SuperPage
from com.qa.automation.appium.pages.ios.ffan.message_centre_page_configs import MessageCentrePageConfigs


class MessageCentrePage(SuperPage):
    '''
    作者 宋波
    首页=>我的飞凡=>消息中心
    '''

    def __init__(self, testcase, driver, logger):
        '''
        Constructor
        '''

        super(MessageCentrePage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        '''
        usage: verify whether the current page is the version upgrade page.
        '''

        API().assertElementByName(self.testcase, self.driver, self.logger,
                                  MessageCentrePageConfigs.resource_id_message_centre_title_st,
                                  MessageCentrePageConfigs.assert_view_timeout)

    def clickOnSettings(self):
        '''
        usage: click on the settings button.
        '''

        API().clickElementByName(self.testcase, self.driver, self.logger,
                                 MessageCentrePageConfigs.resource_id_settings_st,
                                 MessageCentrePageConfigs.click_on_button_timeout)

    def clickOnFeiFanActivity(self):
        '''
        usage: click on the fei fan activity button.
        '''

        API().clickElementByName(self.testcase, self.driver, self.logger,
                                 MessageCentrePageConfigs.resource_id_fei_fan_activity_st,
                                 MessageCentrePageConfigs.click_on_button_timeout)

    def clickOnSquareDynamic(self):
        '''
        usage: click on the square dynamic button.
        '''

        API().clickElementByName(self.testcase, self.driver, self.logger,
                                 MessageCentrePageConfigs.resource_id_square_dynamic_st,
                                 MessageCentrePageConfigs.click_on_button_timeout)

    def clickOnBrandActivity(self):
        '''
        usage: click on the brand activity button.
        '''

        API().clickElementByName(self.testcase, self.driver, self.logger,
                                 MessageCentrePageConfigs.resource_id_brand_activity_st,
                                 MessageCentrePageConfigs.click_on_button_timeout)

    def clickOnStoreMessage(self):
        '''
        usage: click on the store message button.
        '''

        API().clickElementByName(self.testcase, self.driver, self.logger,
                                 MessageCentrePageConfigs.resource_id_store_message_st,
                                 MessageCentrePageConfigs.click_on_button_timeout)


if __name__ == '__main__':
    pass
