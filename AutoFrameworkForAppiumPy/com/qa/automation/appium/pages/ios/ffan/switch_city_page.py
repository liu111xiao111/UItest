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
        super(SwitchCityPage, self).__init__(testcase, driver, logger)

    def validSelf(self, assertable=True):
        '''
        usage:验证城市切换
        '''

        if assertable:
            API().assertElementByName(self.testcase, self.driver, self.logger,
                                      SwitchCityPageConfigs.resource_id_switch_city_cancel_bt,
                                      SwitchCityPageConfigs.assert_view_timeout)
        else:
            return API().validElementByName(self.driver, self.logger,
                                            SwitchCityPageConfigs.resource_id_switch_city_cancel_bt,
                                            SwitchCityPageConfigs.verify_view_timeout)

    def cancelSwitchCity(self):
        '''
        usage: 取消城市切换
        '''

        API().clickElementByName(self.testcase, self.driver, self.logger,
                                 SwitchCityPageConfigs.resource_id_switch_city_cancel_bt,
                                 SwitchCityPageConfigs.click_on_button_timeout)

    def confirmSwitchCity(self):
        '''
        usage: 确认城市切换
        '''

        API().clickElementByName(self.testcase, self.driver, self.logger,
                                 SwitchCityPageConfigs.resource_id_switch_city_switch_bt,
                                 SwitchCityPageConfigs.click_on_button_timeout)

    def invalidSelf(self):
        '''
        usage: 验证当前界面不是选择城市界面
        '''

        API().assertFalse(self.testcase, self.logger,
                          API().validElementByName(self.driver, self.logger,
                                                   SwitchCityPageConfigs.resource_id_switch_city_cancel_bt,
                                                   SwitchCityPageConfigs.assert_invalid_view_time))

    def inputBeijing(self):
        '''
        usage:输入北京市
        '''
        API().inputStringByXpath(self.testcase, self.driver, self.logger,
                                SwitchCityPageConfigs.xpath_city_input,
                                SwitchCityPageConfigs.name_city_beijing,
                                SwitchCityPageConfigs.click_on_button_timeout)

    def inputCities(self, cityName):
        '''
        usage: input the city.
        '''

        API().inputStringByXpath(self.testcase, self.driver, self.logger,
                                SwitchCityPageConfigs.xpath_city_input,
                                cityName, SwitchCityPageConfigs.click_on_button_timeout)

    def getCityOrientation(self):
        '''
        usage: 获取城市定位
        '''

        return API().getTextByXpath(self.testcase, self.driver, self.logger,
                                    SwitchCityPageConfigs.xpath_hint_content_st,
                                    SwitchCityPageConfigs.get_view_timeout).split(u"为")[1]
    def clickOnCityListFirst(self):
        API().clickElementByXpath(self.testcase, self.driver, self.logger,
                                  SwitchCityPageConfigs.xpath_city_list_one,
                                  SwitchCityPageConfigs.click_on_button_timeout)
