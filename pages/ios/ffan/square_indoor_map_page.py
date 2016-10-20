# -*- coding: utf-8 -*-

from api.api import API
from pages.ios.common.superPage import SuperPage
from pages.ios.ffan.square_indoor_map_page_configs import SquareIndoorMapPageConfigs as SIMPC


class SquareIndoorMapPage(SuperPage):
    '''
    作者 刘涛
    首页=>广场=>室内地图
    '''
    def __init__(self, testcase, driver, logger):
        super(SquareIndoorMapPage, self).__init__(testcase, driver, logger);

    def validSelf(self):
        '''
        usage : 判断"室内地图"显示是否正常
        '''
        API().assertElementByName(self.testcase,
                                  self.driver,
                                  self.logger,
                                  SIMPC.name_verify_indoor,
                                  18)

    def clickOnMapAr(self):
        '''
        usage : 点击地图菜单
        '''
        API().clickElementByName(self.testcase,
                                 self.driver,
                                 self.logger,
                                 SIMPC.name_map_ar_button,
                                 20)


    def clickOnFoodMap(self):
        '''
        usage : 点击 "美食地图"
        '''
        API().clickElementByName(self.testcase,
                                 self.driver,
                                 self.logger,
                                 SIMPC.name_food_map,
                                 10)

    def validSelfFood(self):
        '''
        usage : 判断"美食地图"显示是否正常
        '''
        if API().validElementByName(self.testcase,
                                 self.driver,
                                 self.logger,
                                 SIMPC.name_verify_indoor,
                                 18):
            API().assertFalse(self.testcase, self.logger, True)
