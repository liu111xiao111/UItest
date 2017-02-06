# -*- coding:utf-8 -*-

from api.api import API
from pages.ios.common.superPage import SuperPage
from pages.ios.ffan.my_membership_card_package_page_configs import MyMembershipCardPackagePageConfigs


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
                                  MyMembershipCardPackagePageConfigs.name_my_membership_card_package_title_st,
                                  MyMembershipCardPackagePageConfigs.assert_view_timeout)

    def clickOnLeHuoKa(self):
        '''
        usage: click on the LeHuoKa button.
        '''

        API().clickElementByName(self.testcase, self.driver, self.logger,
                                 MyMembershipCardPackagePageConfigs.name_le_huo_ka_st,
                                 MyMembershipCardPackagePageConfigs.click_on_button_timeout)


if __name__ == '__main__':
    pass
