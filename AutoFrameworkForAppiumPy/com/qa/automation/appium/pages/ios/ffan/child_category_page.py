# -*- coding:utf-8 -*-

from com.qa.automation.appium.pages.ios.ffan.child_category_page_configs import ChildCategoryPageConfigs
from com.qa.automation.appium.pages.ios.common.super_page import SuperPage
from com.qa.automation.appium.api.api import API

CCPC = ChildCategoryPageConfigs

class ChildCategoryPage(SuperPage):
    '''
    作者 刘涛
    首页＝>亲子
    '''

    def __init__(self, testcase, driver, logger):
        """
        Constructor
        """

        super(ChildCategoryPage, self).__init__(testcase , driver, logger)

    '''
        usage : 进入亲子儿童页面，根据亲子的textview,检查找亲子儿童页面是否加载出来.
    '''
    def validSelf(self):
        API().assert_view_by_resourceID_Until(self.testcase,
                                              self.driver,
                                              self.logger,
                                              CCPC.name_child_title,
                                              CCPC.click_on_button_timeout)

    '''
        usage : 点击门店的listView
    '''
    def clickListFirstItem(self):
        tempText = API().get_view_by_xpath_ios(self.driver,
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
                                       CCPC.resource_id_ll_other_store_ll)

        '''
        usage: 获取项目名称
        '''
    def getItemName(self):
        itemName = API().get_view_by_xpath_ios(driver=self.driver,
                                               logger=self.logger,
                                               xpath=CCPC.xpath_store_title).text
        return itemName

        '''
        usage: 判断项目名称是否一致
        '''
    def validKeywords(self, keywords, itemName):
        API().assert_equal(test_case=self.testcase,driver=self.driver,logger=self.logger,
                           actual_text=itemName,expect_text=keywords)

if __name__ == '__main__':
    pass