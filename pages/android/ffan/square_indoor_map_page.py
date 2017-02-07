# -*- coding: utf-8 -*-

from api.api import API
from pages.android.common.super_page import SuperPage
from pages.android.ffan.square_indoor_map_page_configs import SquareIndoorMapPageConfigs as SIMPC
from pages.logger import logger


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
        logger.info("Check 室内地图页面 begin")
        API().assertElementByXpath(self.testcase,
                                        self.driver,
                                        self.logger,
                                        SIMPC.xpath_indoor_map,
                                        18)
        logger.info("Check 室内地图页面 end")

    def clickOnSwitchMap(self):
        '''
        usage : 点击 "选择地图"
        '''
        API().clickElementByResourceId(self.testcase,
                                       self.driver,
                                       self.logger,
                                       SIMPC.resource_id_map,
                                       10)

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
                                        SIMPC.resource_id_food_detail,
                                        18)
