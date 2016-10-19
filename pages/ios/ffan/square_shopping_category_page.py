# -*- coding: utf-8 -*-

from com.qa.automation.appium.api.api_new import API
from com.qa.automation.appium.pages.ios.common.super_page import SuperPage
from com.qa.automation.appium.pages.ios.ffan.square_shopping_category_page_configs import SquareShoppingPageConfigs


class SquareShoppingPage(SuperPage):
    '''
    作者 宋波
    首页=>广场=>爱购物
    '''

    def __init__(self, testcase, driver, logger):
        super(SquareShoppingPage, self).__init__(testcase=testcase, driver=driver, logger=logger);

    '''
        usage : 进入广场模块，检查是否加载出来
    '''
    def validSelf(self):
        API().assertElementByName(self.testcase, self.driver, self.logger,
                                  SquareShoppingPageConfigs.resource_id_commodity_title_st,
                                  SquareShoppingPageConfigs.click_on_button_timeout)

    def clickOnSubCommodity(self):
        '''
        usage: click on the sub-commodity button.
        '''

        tempText = API().getTextByXpath(self.testcase, self.driver, self.logger,
                                        SquareShoppingPageConfigs.xpath_sub_commodity_st,
                                        SquareShoppingPageConfigs.get_timeout)
        API().clickElementByXpath(self.testcase, self.driver, self.logger,
                                  SquareShoppingPageConfigs.xpath_sub_commodity_st,
                                  SquareShoppingPageConfigs.click_on_button_timeout)
        return tempText


if __name__ == '__main__':
    pass;
