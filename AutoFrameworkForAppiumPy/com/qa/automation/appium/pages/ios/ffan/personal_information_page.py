# -*- coding:utf-8 -*-

from com.qa.automation.appium.api.api_new import API
from com.qa.automation.appium.pages.ios.common.super_page import SuperPage
from com.qa.automation.appium.pages.ios.ffan.personal_information_page_configs import PersonalInformationPageConfigs


class PersonalInformationPage(SuperPage):
    '''
    作者 宋波
    首页=>我的飞凡=>个人信息
    '''

    def __init__(self, testcase, driver, logger):
        '''
        Constructor
        '''

        super(PersonalInformationPage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        '''
        usage: verify whether the current page is correct page.
        '''

        API().assertElementByName(self.testcase, self.driver, self.logger,
                                  PersonalInformationPageConfigs.resource_id_nickname_st,
                                  PersonalInformationPageConfigs.assert_view_timeout)


if __name__ == '__main__':
    pass
