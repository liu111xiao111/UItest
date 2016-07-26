# -*- coding: utf-8 -*-

from com.qa.automation.appium.api.api_new import API
from com.qa.automation.appium.pages.android.common.super_page import SuperPage
from com.qa.automation.appium.pages.android.ffan.square_indoor_map_page_configs import SquareIndoorMapPageConfigs as SIMPC


class SquareIndoorMapPage(SuperPage):
    '''
    作者 刘涛
    首页=>广场=>室内地图
    '''
    def __init__(self, testcase, driver, logger):
        super(SquareIndoorMapPage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        '''
        usage : 验证室内地图页面
        '''
        API().assertElementByResourceId(self.testcase,
                                        self.driver,
                                        self.logger,
                                        SIMPC.resource_id_indoor_map,
                                        18)

    def clickOnFoodMap(self):
        '''
        usage : 点击 "美食地图"
        '''
        API().clickElementByResourceId(self.testcase,
                                       self.driver,
                                       self.logger,
                                       SIMPC.resource_id_food_map,
                                       10)

    def validSelfFood(self):
        '''
        usage : 验证 "美食地图"
        '''
        API().assertElementByResourceId(self.testcase,
                                        self.driver,
                                        self.logger,
                                        SIMPC.resource_id_food_map,
                                        18)
