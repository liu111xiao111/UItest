# -*- coding: utf-8 -*-

from com.qa.automation.appium.api.api import API
from com.qa.automation.appium.pages.android.common.super_page import SuperPage
from com.qa.automation.appium.pages.android.ffan.square_find_store_category_page_configs import SquareFindStoreConfigs

SFSC = SquareFindStoreConfigs()

'''
    usage : 广场模块，找店类目
'''
class SquareFindStorePage(SuperPage):
    def __init__(self, testcase, driver, logger):
        super(SquareFindStorePage, self).__init__(testcase=testcase, driver=driver, logger=logger);

    def validSelf(self):
        API().assert_view_by_resourceID_Until(self.testcase,
                                              self.driver,
                                              self.logger,
                                              SFSC.resource_id_tv_category_tv,
                                              SFSC.verify_view_timeout);

    '''
        usage : 点击search
    '''
    def clickOnSearch(self):
        API().click_view_by_resourceID(self.testcase,
                                       self.driver,
                                       self.logger,
                                       SFSC.resource_id_iv_search_iv)


if __name__ == '__main__':
    pass;