# -*- coding:utf-8 -*-

from api.api import API
from pages.ios.common.superPage import SuperPage
from pages.ios.ffan.personal_information_page_configs import PersonalInformationPageConfigs
from pages.logger import logger


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
        logger.info("Check 个人信息 begin")
        API().assertElementByName(self.testcase, self.driver, self.logger,
                                  PersonalInformationPageConfigs.name_nickname_st,
                                  PersonalInformationPageConfigs.assert_view_timeout)
        logger.info("Check 个人信息 end")
        API().screenShot(self.driver, "myInfo")


if __name__ == '__main__':
    pass
