# -*- coding:utf-8 -*-

from com.qa.automation.appium.api.api_new import API
from com.qa.automation.appium.pages.android.common.super_page import SuperPage
from com.qa.automation.appium.pages.android.ffan.child_category_page_configs import ChildCategoryPageConfigs as CCPC


class ChildCategoryPage(SuperPage):
    '''
    作者 刘涛
    首页＝>亲子
    '''
    def __init__(self, testcase, driver, logger):
        super(ChildCategoryPage, self).__init__(testcase , driver, logger)

    def validSelf(self):
        '''
        usage : 进入美食页面，根据餐饮的textview,检查找餐饮页面是否加载出来.
        '''
        API().assertElementByResourceId(self.testcase,
                                        self.driver,
                                        self.logger,
                                        CCPC.resource_id_ll_child_play_ll,
                                        CCPC.click_on_button_timeout)

    def clickListFirstItem(self):
        '''
        usage : 点击门店的listView
        '''
        tempText = API().getTextByXpath(self.testcase,
                                        self.driver,
                                        self.logger,
                                        CCPC.xpath_store_list_1,
                                        CCPC.click_on_button_timeout)

        API().clickElementByXpath(self.testcase,
                                  self.driver,
                                  self.logger, 
                                  CCPC.xpath_store_list_1,
                                  CCPC.click_on_button_timeout)

        return tempText

    def clickOnChildPlay(self):
        '''
        usage : 点击亲子游乐
        '''
        API().clickElementByResourceId(self.testcase,
                                       self.driver,
                                       self.logger,
                                       CCPC.resource_id_ll_child_play_ll,
                                       CCPC.click_on_button_timeout)

    def clickOnChildEducation(self):
        '''
        usage : 点击儿童教育
        '''
        API().clickElementByResourceId(self.testcase,
                                       self.driver,
                                       self.logger,
                                       CCPC.resource_id_ll_child_education_ll,
                                       CCPC.click_on_button_timeout)

    def clickOnChildShopping(self):
        '''
        usage : 点击亲子购物
        '''
        API().clickElementByResourceId(self.testcase,
                                       self.driver,
                                       self.logger,
                                       CCPC.resource_id_ll_child_shopping_ll,
                                       CCPC.click_on_button_timeout)

    def clickOnOtherStore(self):
        '''
        usage : 点击其它
        '''
        API().clickElementByResourceId(self.testcase,
                                       self.driver,
                                       self.logger,
                                       CCPC.resource_id_ll_other_store_ll,
                                       CCPC.click_on_button_timeout)

    def validKeywords(self, keywords):
        '''
        usage: 验证关键字
        '''
        API().assertElementByContentDesc(self.testcase,
                                         self.driver,
                                         self.logger,
                                         keywords,
                                         CCPC.click_on_button_timeout)
