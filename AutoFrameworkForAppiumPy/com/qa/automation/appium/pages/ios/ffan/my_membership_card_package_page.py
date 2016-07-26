# -*- coding:utf-8 -*-

from com.qa.automation.appium.api.api_new import API
from com.qa.automation.appium.pages.ios.common.super_page import SuperPage
from com.qa.automation.appium.pages.ios.ffan.my_membership_card_package_page_configs import MyMembershipCardPackagePageConfigs


class MyMembershipCardPackagePage(SuperPage):
    '''
    作者 宋波
    首页=>我的飞凡=>我的会员卡包
    '''

    def __init__(self, testcase, driver, logger):
        '''
        Constructor
        '''

        super(MyMembershipCardPackagePage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        '''
        usage: verify whether the current page is correct page.
        '''

        API().assertElementByName(self.testcase, self.driver, self.logger,
                                  MyMembershipCardPackagePageConfigs.resource_id_my_membership_card_package_title_st,
                                  MyMembershipCardPackagePageConfigs.assert_view_timeout)

    def clickOnLeHuoKa(self):
        '''
        usage: click on the LeHuoKa button.
        '''

        API().clickElementByName(self.testcase, self.driver, self.logger,
                                 MyMembershipCardPackagePageConfigs.resource_id_le_huo_ka_st,
                                 MyMembershipCardPackagePageConfigs.click_on_button_timeout)


if __name__ == '__main__':
    pass
