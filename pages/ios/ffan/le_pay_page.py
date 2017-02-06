# -*- coding: utf-8 -*-

from api.api import API
from pages.ios.common.superPage import SuperPage
from pages.ios.ffan.le_pay_page_configs import LePayPageConfigs
from cases.logger import logger

class LePayPage(SuperPage):
    '''
    作者 刘涛
    首页=>买单
    '''

    def __init__(self, testcase, driver, logger):
        super(LePayPage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        logger.info("Check " + LePayPageConfigs.name_le_pay_navigation_bar +" begin")
        API().assertElementByName(self.testcase,
                                  self.driver,
                                  self.logger,
                                  LePayPageConfigs.name_le_pay_navigation_bar)
        logger.info("Check " + LePayPageConfigs.name_le_pay_navigation_bar + " end")
        API().screenShot(self.driver, "maiDan")

    def clickOnDetailsLePay(self):
        '''
        usage: 点击"乐付买单"
        '''
        logger.info("Click 买单 begin")
        API().clickElementByXpath(testCase=self.testcase,
                                  driver=self.driver,
                                  logger=self.logger,
                                  xpath=LePayPageConfigs.xpath_le_pay)
        logger.info("Click 买单 end")

    def validMaiDanPage(self):
        '''
        验证买单页面,以"消费金额"文字,作为验证
        '''
        logger.info("Check 买单详情页 begin")
        API().assertElementByName(self.testcase,
                                  self.driver,
                                  self.logger,
                                  LePayPageConfigs.name_total_pay)
        logger.info("Check 买单详情页 end")


    def inputSumOfConsumption(self):
        '''
        usage : 输入消费金额
        '''
        logger.info("Input 输入消费金额 begin")
        API().inputStringByXpath(self.testcase,
                                 self.driver,
                                 self.logger,
                                 LePayPageConfigs.xpath_sum_of_consumption,
                                 LePayPageConfigs.sum_of_consumption)
        logger.info("Input 输入消费金额 end")
        API().screenShot(self.driver, "xiaoFeiJinE")


    def clickOnConfirmPurchase(self):
        '''
        usage: 点击"确认购买"
        '''
        logger.info("Click 确认购买 begin")
        API().clickElementByXpath(testCase=self.testcase,
                                  driver=self.driver,
                                  logger=self.logger,
                                  xpath=LePayPageConfigs.xpath_confirm_purchase)
        logger.info("Click 确认购买 end")
        API().screenShot(self.driver, "queRenGouMai")

    def validFeiFanShouYinTai(self):
        '''
        验证飞凡收银台
        '''
        logger.info("Check 飞凡收银台 begin")
        API().assertElementByName(self.testcase,
                                  self.driver,
                                  self.logger,
                                  LePayPageConfigs.name_feifan_shouyintai)
        logger.info("Check 飞凡收银台 end")
        API().screenShot(self.driver, "feiFanShouYinTai")


    def clickOnConfirmCancel(self):
        '''
        usage: 点击"确认"
        '''
        logger.info("Click 确认 begin")
        API().clickElementByXpath(testCase=self.testcase,
                                  driver=self.driver,
                                  logger=self.logger,
                                  xpath=LePayPageConfigs.xpath_confirm_cancel)
        logger.info("Click 确认 end")
        API().screenShot(self.driver, "queRen")

if __name__ == '__main__':
    pass;
