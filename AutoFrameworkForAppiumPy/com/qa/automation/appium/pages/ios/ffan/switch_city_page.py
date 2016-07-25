# -*- coding:utf-8 -*-

from com.qa.automation.appium.api.api_new import API
from com.qa.automation.appium.pages.android.common.super_page import SuperPage
from com.qa.automation.appium.pages.ios.ffan.switch_city_page_configs import SwitchCityPageConfigs


class SwitchCityPage(SuperPage):
    '''
    作者 宋波
    城市切换
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
            API().assertElementByResourceId(self.testcase, self.driver, self.logger,
                                            SwitchCityPageConfigs.resource_id_switch_city_cancel_bt,
                                            SwitchCityPageConfigs.assert_view_timeout)
            return True
        else:
            return API().validElementByResourceId(self.testcase, self.driver, self.logger,
                                                  SwitchCityPageConfigs.resource_id_switch_city_cancel_bt,
                                                  SwitchCityPageConfigs.verify_view_timeout)

    def cancelSwitchCity(self):
        '''
        usage: cancel switch city.
        '''

        API().click_view_by_resourceID(self.testcase, self.driver, self.logger,
                                       SwitchCityPageConfigs.resource_id_switch_city_cancel_bt,
                                       SwitchCityPageConfigs.click_on_button_timeout)

    def confirmSwitchCity(self):
        '''
        usage: confirm switch city.
        '''

        API().click_view_by_resourceID(self.testcase, self.driver, self.logger,
                                       SwitchCityPageConfigs.resource_id_switch_city_switch_bt,
                                       SwitchCityPageConfigs.click_on_button_timeout)

    def invalidSelf(self):
        '''
        usage: verify whether the current page is not the switch city page.
        '''

        API().assert_none_view_by_resource_id_until_android(self.testcase, self.driver, self.logger,
                                                            SwitchCityPageConfigs.resource_id_switch_city_cancel_bt,
                                                            SwitchCityPageConfigs.assert_invalid_view_time)

if __name__ == '__main__':
    pass
