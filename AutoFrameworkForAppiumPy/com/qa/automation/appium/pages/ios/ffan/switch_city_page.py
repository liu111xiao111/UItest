# -*- coding:utf-8 -*-

from com.qa.automation.appium.api.api_new import API
from com.qa.automation.appium.pages.android.common.super_page import SuperPage
from com.qa.automation.appium.pages.ios.ffan.switch_city_page_configs import SwitchCityPageConfigs as SCPC


class SwitchCityPage(SuperPage):
    '''
    作者 宋波
    城市切换
    '''

    def __init__(self, testcase, driver, logger):
        super(SwitchCityPage, self).__init__(testcase, driver, logger)

    def validSelf(self, assertable=True):
        '''
        usage:验证城市切换
        '''

        if assertable:
            API().assertElementByResourceId(self.testcase,
                                            self.driver,
                                            self.logger,
                                            SCPC.resource_id_switch_city_cancel_bt,
                                            SCPC.assert_view_timeout)
            return True
        else:
            return API().validElementByResourceId(self.driver,
                                                  self.logger,
                                                  SCPC.resource_id_switch_city_cancel_bt,
                                                  SCPC.verify_view_timeout)

    def cancelSwitchCity(self):
        '''
        usage: 取消城市切换
        '''

        API().clickElementByResourceId(self.testcase,
                                       self.driver,
                                       self.logger,
                                       SCPC.resource_id_switch_city_cancel_bt,
                                       SCPC.click_on_button_timeout)

    def confirmSwitchCity(self):
        '''
        usage: 确认城市切换
        '''

        API().click_view_by_resourceID(self.testcase,
                                       self.driver,
                                       self.logger,
                                       SCPC.resource_id_switch_city_switch_bt,
                                       SCPC.click_on_button_timeout)

    def invalidSelf(self):
        '''
        usage: 验证当前界面不是选择城市界面
        '''

        API().assertFalse(self.testcase,
                          self.logger,
                          API().validElementByResourceId(self.driver,
                                                         self.logger,
                                                         SCPC.resource_id_switch_city_cancel_bt,
                                                         SCPC.assert_invalid_view_time))
