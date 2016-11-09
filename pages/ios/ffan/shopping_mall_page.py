# -*- coding:utf-8 -*-

import operator

from api.api import API
from pages.ios.common.superPage import SuperPage
from pages.ios.ffan.shopping_mall_page_configs import ShoppingMallPageConfigs
from pages.logger import logger


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
        logger.info("Check 购物中心 begin")
        API().assertElementByName(testCase=self.testcase,
                                  driver=self.driver,
                                  logger=self.logger,
                                  name=SMP.name_shopping_mall_title)
        API().screenShot(self.driver, "gouWuZhongXin")
        logger.info("Check 购物中心 end")

    def clickOnTotalTab(self):
        '''
        usage: 点击全部tab
        '''
        logger.info("Click 全部 begin")
        API().clickElementByXpath(testCase = self.testcase,
                                  driver = self.driver,
                                  logger = self.logger,
                                  xpath = SMP.xpath_tab_title_1,
                                  timeout = SMP.click_on_button_timeout)
        logger.info("Click 全部 end")

    def clickOnShoppingTab(self):
        '''
        usage: 点击购物中心tab
        '''
        logger.info("Click 购物中心 begin")
        API().clickElementByXpath(testCase = self.testcase,
                                  driver = self.driver,
                                  logger = self.logger,
                                  xpath = SMP.xpath_tab_title_2,
                                  timeout = SMP.click_on_button_timeout)
        logger.info("Click 购物中心 end")

    def clickOnGoodsTab(self):
        '''
        usage: 点击百货tab
        '''
        logger.info("Click 百货 begin")
        API().clickElementByXpath(testCase = self.testcase,
                                  driver = self.driver,
                                  logger = self.logger,
                                  xpath = SMP.xpath_tab_title_3,
                                  timeout = SMP.click_on_button_timeout)
        logger.info("Click 百货 end")

    def validListView(self):
        '''
        usage: 验证tab页面
        '''
        logger.info("Check tab页面 begin")
        API().assertElementByType(self.testcase,
                                  self.driver,
                                  self.logger,
                                  SMP.class_plaza_id,
                                  SMP.assert_view_timeout)
        API().screenShot(self.driver, "tab")
        logger.info("Check tab页面 end")

    def validDistance(self):
        '''
        usage: 验证距离排序
        '''
        prev_plaza_distance = "0"
        cellList = API().getElementsByType(self.testcase,
                                           self.driver,
                                           self.logger,
                                           'UIATableCell',
                                           20)
        plaza_number = len(cellList)
        if plaza_number > 1:
            for i in range(1, plaza_number+1):
                uia_string = SMP.views_xpath+ "UIATableCell[" + str(i) +"]/UIAStaticText[3]"
                text = API().getTextByXpath(self.testcase,
                                            self.driver,
                                            self.logger,
                                            uia_string)
                current_plaza_distance = text.split(SMP.view_text_distance)[0]
                if operator.gt(prev_plaza_distance, current_plaza_distance):
                    self.testcase.assertTrue(False, "The plaza distance is not ordered.")
                prev_plaza_distance = text.split(SMP.view_text_distance)[0]
