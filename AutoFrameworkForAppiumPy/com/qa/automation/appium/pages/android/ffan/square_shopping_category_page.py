# -*- coding: utf-8 -*-

from com.qa.automation.appium.api.api import API
from com.qa.automation.appium.pages.android.common.super_page import SuperPage
from com.qa.automation.appium.pages.android.ffan.square_shopping_category_page_configs import SquareShoppingPageConfigs


'''
    usage: 广场模块中，像下滑动，爱购物界面
'''
class SquareShoppingPage(SuperPage):
    def __init__(self, testcase, driver, logger):
        super(SquareShoppingPage, self).__init__(testcase=testcase, driver=driver, logger=logger);

    '''
        usage : 进入广场模块，检查是否加载出来
    '''

    def validSelf(self):
        API().assert_view_by_resourceID_Until(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                                      resource_id=SquareShoppingPageConfigs.resource_id_iv_find_iv,
                                                      seconds=10);

    def clickOnSubCommodity(self):
        '''
        usage: click on the sub-commodity button.
        '''

        tempText = API().get_view_by_resourceID(self.driver, self.logger, SquareShoppingPageConfigs.resource_id_sub_commodity_button).text
        API().click_view_by_resourceID(self.testcase, self.driver, self.logger, SquareShoppingPageConfigs.resource_id_sub_commodity_button, SquareShoppingPageConfigs.click_on_button_timeout)
        return tempText


if __name__ == '__main__':
    pass;
