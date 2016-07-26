# -*- coding:utf-8 -*-

import operator

from com.qa.automation.appium.api.api import API
from com.qa.automation.appium.pages.ios.common.super_page import SuperPage
from com.qa.automation.appium.pages.ios.ffan.shopping_mall_page_configs import ShoppingMallPageConfigs

SMP = ShoppingMallPageConfigs()

class ShoppingMallPage(SuperPage):
    '''
    作者 刘涛
    首页=>购物中心
    '''

    def __init__(self, testcase, driver, logger):
        '''
        初始化
        '''
        super(ShoppingMallPage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        '''
        usage: 验证购物中心界面
        '''
        API().assert_view_by_resourceID_Until(self.testcase,
                                              self.driver,
                                              self.logger,
                                              SMP.name_shopping_mall_title,
                                              SMP.assert_view_timeout)

    def clickOnTotalTab(self):
        '''
        usage: 点击全部tab
        '''
        API().click_view_by_xpath(self.testcase,
                                  self.driver,
                                  self.logger,
                                  SMP.xpath_tab_title_1,
                                  SMP.click_on_button_timeout)

    def clickOnShoppingTab(self):
        '''
        usage: 点击全部tab
        '''
        API().click_view_by_xpath(self.testcase,
                                  self.driver,
                                  self.logger,
                                  SMP.xpath_tab_title_2,
                                  SMP.click_on_button_timeout)

    def clickOnGoodsTab(self):
        '''
        usage: 点击全部tab
        '''
        API().click_view_by_xpath(self.testcase,
                                  self.driver,
                                  self.logger,
                                  SMP.xpath_tab_title_3,
                                  SMP.click_on_button_timeout)

    def validListView(self):
        '''
        usage: 验证tab页面
        '''
        API().assert_view_by_classname_both(self.testcase,
                                            self.driver,
                                            self.logger,
                                            SMP.class_plaza_id,
                                            SMP.assert_view_timeout)

    def validDistance(self):
        '''
        usage: 验证距离排序
        '''
        prev_plaza_distance = "0"
        cellList = API().find_elements_by_ios_uiautomation(self.driver,
                                                              self.logger,
                                                              SMP.views_uia_string)
        plaza_number = len(cellList)
        if plaza_number > 1:
            for i in range(0, plaza_number):
                uia_string = ".tableViews()[0].cells()[" + str(i) +"].staticTexts()[2]"
                element = API().find_element_by_ios_uiautomation(self.driver,
                                                                 self.logger,
                                                                 uia_string)
                current_plaza_distance = element.text.split(SMP.view_text_distance)[0]
                if operator.gt(prev_plaza_distance, current_plaza_distance):
                    self.testcase.assertTrue(False, "The plaza distance is not ordered.")
                prev_plaza_distance = element.text.split(SMP.view_text_distance)[0]

    def clickOnBeijinTongzouMall(self):
        '''
        usage: 点击 "北京通州万达广场"
        '''
        API().scroll_to_text(self.driver, self.logger, ShoppingMallPageConfigs.text_beijing_tongzou_mall)
        API().click_view_by_text_android(testcase = self.testcase, driver=self.driver, logger=self.logger,
                                         text=ShoppingMallPageConfigs.text_beijing_tongzou_mall);


if __name__ == '__main__':
    pass
