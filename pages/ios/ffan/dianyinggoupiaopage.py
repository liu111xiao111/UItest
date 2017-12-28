# -*- coding:utf-8 -*-

import operator

from api.api import API
from pages.ios.common.superPage import SuperPage
from pages.ios.ffan.dianyinggoupiao_page_configs import dianyinggoupiaoconfigs as DYGPC
from pages.logger import logger




class dianyinggoupiaopage(SuperPage):
    '''
    作者 刘潇
    电影购票
    '''

    def __init__(self, testcase, driver, logger):
        '''
        初始化
        '''
        super(dianyinggoupiaopage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        '''
        usage: 验证购物中心界面
        '''
        logger.info("Check 购物中心 begin")
        API().assertElementByName(testCase=self.testcase,
                                  driver=self.driver,
                                  logger=self.logger,
                                  name=DYGPC.xpath_xuanzuo
                                  )
        API().screenShot(self.driver, "gouWuZhongXin")
        logger.info("Check 购物中心 end")

    def clickOnxuanzuo(self):
        '''
        usage: 点击选座按钮
        '''
        logger.info("Click 选座按钮 begin")
        API().clickElementByXpath(testCase = self.testcase,
                                  driver = self.driver,
                                  logger = self.logger,
                                  xpath = DYGPC.xpath_xuanzuo,
                                  timeout = DYGPC.click_on_button_timeout)
        logger.info("Click 选座按钮 end")

    def clickOnyingcheng(self):
        '''
        usage: 点击选择影城
        '''
        logger.info("Click 选择影城 begin")
        API().clickElementByXpath(testCase = self.testcase,
                                  driver = self.driver,
                                  logger = self.logger,
                                  xpath = DYGPC.xpath_yingcheng,
                                  timeout = DYGPC.click_on_button_timeout)
        logger.info("Click 选择影城 end")

    def clickOnqiehuanchengshi(self):
        '''
        usage: 点击切换城市按钮
        '''
        logger.info("Click 切换城市按钮 begin")
        API().clickElementByXpath(testCase = self.testcase,
                                  driver = self.driver,
                                  logger = self.logger,
                                  xpath = DYGPC.xpath_qiehuanchengshi,
                                  timeout = DYGPC.click_on_button_timeout)
        logger.info("Click 切换城市按钮 end")


    def inputchengshi(self):
        '''
        usage: 输入城市名称
        '''
        logger.info("Input 输入城市名称 begin")
        API().inputStringByXpath(self.testcase, self.driver, self.logger,
                                 DYGPC.xpath_shuruchengshi,
                                 DYGPC.chengshiname,
                                 DYGPC.input_timeout)
        logger.info("Input 输入城市名称 end")


    def clickOnbaotoushi(self):
        '''
        usage: click on the search button.
        '''
        logger.info("Click 包头市 begin")
        API().clickElementByName(self.testcase, self.driver, self.logger,
                                 DYGPC.baotoushi,
                                 DYGPC.click_on_button_timeout)
        logger.info("Click 包头市 end")