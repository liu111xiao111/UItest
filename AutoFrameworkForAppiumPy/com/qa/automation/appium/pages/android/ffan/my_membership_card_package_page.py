# -*- coding:utf-8 -*-

from __init__ import *

from com.qa.automation.appium.api.api import API
from com.qa.automation.appium.pages.android.common.super_page import SuperPage
from com.qa.automation.appium.pages.android.ffan.my_membership_card_package_page_configs import \
    MyMembershipCardPackagePageConfigs


class MyMembershipCardPackagePage(SuperPage):
    '''
    This is membership card package page operation class.
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

        API().assert_view_by_resourceID_Until(self.testcase, self.driver, self.logger,
                                                      MyMembershipCardPackagePageConfigs.resource_id_my_membership_card_package_title,
                                                      MyMembershipCardPackagePageConfigs.assert_view_timeout)

    def clickOnLeHuoKa(self):
        '''
        usage: click on the LeHuoKa button.
        '''

        API().click_view_by_resourceID(self.testcase, self.driver, self.logger,
                                               MyMembershipCardPackagePageConfigs.resource_id_le_huo_ka_button,
                                               MyMembershipCardPackagePageConfigs.click_on_button_timeout)


if __name__ == '__main__':
    pass
