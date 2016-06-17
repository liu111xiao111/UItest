# -*- coding:utf-8 -*-

from selenium.common.exceptions import TimeoutException

from com.qa.automation.appium.api.api import API
from com.qa.automation.appium.pages.android.common.super_page import SuperPage
from com.qa.automation.appium.pages.android.ffan.switch_city_page_configs import SwitchCityPageConfigs


class SwitchCityPage(SuperPage):
    '''
    This is a switch city page operation class.
    '''


    def __init__(self, testcase, driver, logger):
        '''
        Constructor
        '''

        super(SwitchCityPage, self).__init__(testcase, driver, logger)

    def validSelf(self, assertable=True):
        '''
        usage: verify whether the current page is the switch city page.
        '''

        if assertable:
            API().assert_view_by_resourceID_Until_android(self.testcase, self.driver, self.logger, SwitchCityPageConfigs.resource_id_switch_city_cancel_button, SwitchCityPageConfigs.assert_view_timeout)
            return True
        else:
            try:
                API().find_view_by_resourceID_Until_android(self.driver, self.logger, SwitchCityPageConfigs.resource_id_switch_city_cancel_button, SwitchCityPageConfigs.verify_view_timeout)
                return True
            except TimeoutException:
                return False

    def cancelSwitchCity(self):
        '''
        usage: cancel switch city.
        '''

        API().click_view_by_resourceID_android(self.testcase, self.driver, self.logger, SwitchCityPageConfigs.resource_id_switch_city_cancel_button)

    def confirmSwitchCity(self):
        '''
        usage: confirm switch city.
        '''

        API().click_view_by_resourceID_android(self.testcase, self.driver, self.logger, SwitchCityPageConfigs.resource_id_switch_city_switch_button)

    def invalidSelf(self):
        '''
        usage: verify whether the current page is not the switch city page.
        '''

        API().assert_none_view_by_resource_id_until_android(self.testcase, self.driver, self.logger, SwitchCityPageConfigs.resource_id_switch_city_cancel_button, SwitchCityPageConfigs.assert_invalid_view_time)

if __name__ == '__main__':
    pass
