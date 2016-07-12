# -*- coding: utf-8 -*-

from com.qa.automation.appium.pages.android.ffan.square_indoor_map_page_configs import SquareIndoorMapPageConfigs
from com.qa.automation.appium.api.api import API
from com.qa.automation.appium.pages.android.common.super_page import SuperPage


class SquareIndoorMapPage(SuperPage):
    def __init__(self, testcase, driver, logger):
        super(SquareIndoorMapPage, self).__init__(testcase=testcase, driver=driver, logger=logger);

    def validSelf(self):
        '''
        usage : Load "室内地图" page， according to textview in "室内地图", check "室内地图" page whether load correctly.
        '''
        API().assert_view_by_resourceID_Until(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                                      resource_id=SquareIndoorMapPageConfigs.name_indoor_map,
                                                      seconds=18);

    def clickOnFoodMap(self):
        '''
        usage : Click "美食地图" page.
        '''
        API().click_view_by_resourceID(testcase = self.testcase, driver=self.driver,logger=self.logger,resource_id=SquareIndoorMapPageConfigs.name_food_map)

    def validSelfFood(self):
        '''
        usage : Load "美食地图" page.
        '''
        API().assert_view_by_resourceID_Until(testcase = self.testcase, driver = self.driver,logger = self.logger ,
                                                resource_id = SquareIndoorMapPageConfigs.name_food_map,seconds=18);

if __name__ == '__main__':
    pass;