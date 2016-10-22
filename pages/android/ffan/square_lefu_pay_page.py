# -*- coding: utf-8 -*-

import operator
from api.api import API
from pages.android.common.super_page import SuperPage
from pages.android.ffan.square_lefu_pay_page_configs import SquareLefuPayPageConfigs as SLPPC


class SquareLefuPayPage(SuperPage):
    '''
    作者 刘涛
    首页=>乐付
    '''
    def __init__(self, testcase, driver, logger):
        super(SquareLefuPayPage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        '''
        usage : 验证乐付买单
        '''
        API().assertElementByResourceId(self.testcase, self.driver, self.logger,
                                        SLPPC.resource_id_lefu_pay_title,
                                        90)
        elementList = API().getElementsByContainsText(self.testcase,
                                                      self.driver,
                                                      self.logger,
                                                      SLPPC.view_text_distance,
                                                      90)
        
        plaza_number = len(elementList)
        if plaza_number > 1:
            for i in range(1, plaza_number):
                current_plaza_distance = elementList[i].text.split(" ")[0]
                prev_plaza_distance = elementList[i-1].text.split(" ")[0]
                if operator.gt(prev_plaza_distance, current_plaza_distance):
                    API().assertTrue(self.testcase, self.logger, False)

    def clickOnLefuPay(self):
        '''
        usage : 点击 "乐付买单"
        '''
        API().clickElementByResourceId(self.testcase, self.driver, self.logger,
                                       SLPPC.resource_id_lefu_pay,
                                       18)
