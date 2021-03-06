# -*- coding:utf-8 -*-

from api.api import API
from pages.android.common.super_page import SuperPage
from pages.android.ffan.switch_city_page_configs import SwitchCityPageConfigs as SCPC
from pages.logger import logger


class SwitchCityPage(SuperPage):
    '''
    作者 宋波
    城市切换
    '''

    def __init__(self, testcase, driver, logger):
        super(SwitchCityPage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        '''
        usage: 验证切换城市
        '''
        logger.info("Check 切换城市Popup begin")
        rtn = API().validElementByResourceId(self.driver, self.logger,
                                                  SCPC.resource_id_switch_city_cancel_button,
                                                  SCPC.verify_view_timeout)
        logger.info("Check 切换城市Popup end")
        return rtn

    def cancelSwitchCity(self):
        '''
        usage: 取消切换城市
        '''
        logger.info("Click 切换城市Popup 取消 button begin")
        API().clickElementByResourceId(self.testcase, self.driver, self.logger,
                                       SCPC.resource_id_switch_city_cancel_button,
                                       SCPC.verify_view_timeout)
        logger.info("Click 切换城市Popup 取消 button end")

    def confirmSwitchCity(self):
        '''
        usage: 确认切换城市
        '''
        API().clickElementByResourceId(self.testcase, self.driver, self.logger,
                                       SCPC.resource_id_switch_city_switch_button,
                                       SCPC.verify_view_timeout)

    def invalidSelf(self):
        '''
        usage: 验证当前页面不是切换城市页面
        '''
        logger.info("Check 取消切换城市 begin")
        res = API().validElementByResourceId(self.driver, self.logger,
                                             SCPC.resource_id_switch_city_cancel_button,
                                             SCPC.assert_invalid_view_time)
        API().assertFalse(self.testcase, self.logger, res)
        logger.info("Check 取消切换城市 end")

    def getCityOrientation(self):
        '''
        usage: 获取城市定位
        '''

        return API().getTextByXpath(self.testcase, self.driver, self.logger,
                                    SCPC.xpath_hint_content_st, SCPC.get_view_timeout).split()[1]

    def validSelfCity(self):
        '''
        usage: 验证当前页面不是切换城市页面
        '''
        logger.info("Check 当前城市为北京市 begin")
        cityName = API().getTextByXpath(self.testcase, self.driver, self.logger,
                                    SCPC.xpath_city_name, SCPC.get_view_timeout)
        API().assertEqual(self.testcase, self.logger, cityName, SCPC.text_city_name)
        logger.info("Check 当前城市为北京市 end")
