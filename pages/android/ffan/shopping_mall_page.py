# -*- coding:utf-8 -*-

import operator

from api.api import API
from pages.android.common.super_page import SuperPage
from pages.android.ffan.shopping_mall_page_configs import ShoppingMallPageConfigs as SMPC


class ShoppingMallPage(SuperPage):
    '''
    作者 刘涛
    首页=>购物中心
    '''
    def __init__(self, testcase, driver, logger):
        super(ShoppingMallPage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        '''
        usage: 验证购物中心页面
        '''
        API().assertElementByResourceId(self.testcase,
                                        self.driver,
                                        self.logger,
                                        SMPC.resource_id_shopping_mall_title,
                                        SMPC.assert_view_timeout)

    def clickOnTab(self, tab_number):
        '''
        usage: 点击 全部/商场/百货
        '''
        viewList = API().getElementsByResourceId(self.testcase,
                                                 self.driver,
                                                 self.logger,
                                                 SMPC.resource_id_tab_id,
                                                 SMPC.assert_view_timeout)
        viewList[tab_number-1].click()

    def validListView(self):
        '''
        usage: 验证标签页
        '''
        API().assertElementByResourceId(self.testcase,
                                        self.driver,
                                        self.logger,
                                        SMPC.resource_id_plaza_id,
                                        SMPC.assert_view_timeout)

    def validDistance(self):
        '''
        usage: 验证距离
        '''
        elementList = API().getElementsByContainsText(self.testcase,
                                                      self.driver,
                                                      self.logger,
                                                      SMPC.view_text_distance,
                                                      SMPC.assert_view_timeout)
        
        plaza_number = len(elementList)
        if plaza_number > 1:
            for i in range(1, plaza_number):
                current_plaza_distance = elementList[i].text.split(" ")[0]
                prev_plaza_distance = elementList[i-1].text.split(" ")[0]
                if operator.gt(prev_plaza_distance, current_plaza_distance):
                    API().assertTrue(self.testcase, self.logger, False)

    def clickOnBeijinTongzouMall(self):
        '''
        usage: 点击 "北京通州万达广场"
        '''
        API().scrollToText(self.testcase, self.driver, self.logger,
                           SMPC.text_beijing_tongzou_mall)
        API().clickElementByText(self.testcase, self.driver, self.logger,
                                 SMPC.text_beijing_tongzou_mall,
                                 SMPC.click_on_button_timeout)
