# -*- coding:utf-8 -*-

from __init__ import *

from com.qa.automation.appium.pages.android.ffan.child_category_page_configs import ChildCategoryPageConfigs
from com.qa.automation.appium.pages.android.common.super_page import SuperPage
from com.qa.automation.appium.api.api import API

CCPC = ChildCategoryPageConfigs


#   首页点击 美食
class ChildCategoryPage(SuperPage):
    def __init__(self, testcase, driver, logger):
        """
        Constructor
        """

        super(ChildCategoryPage, self).__init__(testcase , driver, logger)

    '''
        usage : 进入美食页面，根据餐饮的textview,检查找餐饮页面是否加载出来.
    '''

    def validSelf(self):
        API().assert_view_by_resourceID_Until(self.testcase,
                                              self.driver,
                                              self.logger,
                                              CCPC.resource_id_ll_child_play_ll,
                                              CCPC.click_on_button_timeout)

    '''
        usage : 点击门店的listView
    '''
    def clickListFirstItem(self):
        tempText = API().get_view_by_xpath_android(self.testcase,
                                           self.driver,
                                           self.logger,
                                           CCPC.xpath_store_list_1).text

        API().click_view_by_xpath(self.testcase,
                                  self.driver,
                                  self.logger, 
                                  CCPC.xpath_store_list_1)

        API().click_view_by_xpath(self.testcase,
                                  self.driver,
                                  self.logger,
                                  CCPC.xpath_store_list_2,
                                  CCPC.click_on_button_timeout)

        return tempText

    '''
        usage : 点击亲子游乐
    '''
    def clickOnChildPlay(self):
        API().click_view_by_resourceID(self.testcase,
                                       self.driver,
                                       self.logger,
                                       CCPC.resource_id_ll_child_play_ll)

    '''
        usage : 点击儿童教育
    '''
    def clickOnChildEducation(self):
        API().click_view_by_resourceID(self.testcase,
                                       self.driver,
                                       self.logger,
                                       CCPC.resource_id_ll_child_education_ll)

    '''
        usage : 点击亲子购物
    '''
    def clickOnChildShopping(self):
        API().click_view_by_resourceID(self.testcase,
                                       self.driver,
                                       self.logger,
                                       CCPC.resource_id_ll_child_shopping_ll)

    '''
        usage : 点击亲子购物
    '''
    def clickOnOtherStore(self):
        API().click_view_by_resourceID(self.testcase,
                                       self.driver,
                                       self.logger,
                                       CCPC.resource_id_ll_other_store_ll);

        '''
        usage: verify whether the keyword is correct.
        '''
    def validKeywords(self, keywords):
        API().assert_view_by_content_desc_android(self.testcase,
                                                  self.driver,
                                                  self.logger,
                                                  keywords,
                                                  CCPC.click_on_button_timeout)

if __name__ == '__main__':
    pass