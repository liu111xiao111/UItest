# -*- coding: utf-8 -*-

from com.qa.automation.appium.pages.ios.ffan.square_indoor_map_page_configs import SquareIndoorMapPageConfigs
from com.qa.automation.appium.api.api import API
from com.qa.automation.appium.pages.ios.common.super_page import SuperPage


class SquareIndoorMapPage(SuperPage):
    '''
    作者 刘涛
    首页=>广场=>室内地图
    '''

    def __init__(self, testcase, driver, logger):
        super(SquareIndoorMapPage, self).__init__(testcase=testcase, driver=driver, logger=logger);

    def validSelf(self):
        '''
        usage : 判断"室内地图"显示是否正常
        '''
        API().assert_view_by_resourceID_Until(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                                      resource_id=SquareIndoorMapPageConfigs.name_indoor_map,
                                                      seconds=18);

    def clickOnFoodMap(self):
        '''
        usage : 点击 "美食地图"
        '''
        API().click_view_by_resourceID(testcase = self.testcase, driver=self.driver,logger=self.logger,resource_id=SquareIndoorMapPageConfigs.name_food_map)

    def validSelfFood(self):
        '''
        usage : 判断"美食地图"显示是否正常
        '''
        API().assert_view_by_resourceID_Until(testcase = self.testcase, driver = self.driver,logger = self.logger ,
                                                resource_id = SquareIndoorMapPageConfigs.name_food_map,seconds=18);

if __name__ == '__main__':
    pass;