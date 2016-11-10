# -*- coding: utf-8 -*-

from api.api import API
from pages.ios.common.superPage import SuperPage
from pages.ios.ffan.le_pay_details_page_configs import LePayDetailsPageConfigs

from pages.logger import logger


class LePayDetailsPage(SuperPage):
    '''
    作者 刘涛
    首页=>乐付=>输入乐付消费金额页
    '''

    def __init__(self, testcase, driver, logger):
        super(LePayDetailsPage, self).__init__(testcase=testcase, driver=driver, logger=logger);

    def validSelf(self):
        '''
        usage : 判断乐付买单输入金额页是否存在“确认购买”按钮
        '''
        logger.info("Check 买单详情 begin")
        API().assertElementByName(testCase=self.testcase,
                                  driver=self.driver,
                                  logger=self.logger,
                                  name=LePayDetailsPageConfigs.name_pay)
        logger.info("Check 买单详情 end")
        API().screenShot(self.driver, "maiDanXiangQing")

    def inputMoney(self):
        '''
        usage : 输入消费金额
        '''
        logger.info("Input 消费金额 begin")
        API().inputStringByXpath(self.testcase,
                                 self.driver,
                                 self.logger,
                                 LePayDetailsPageConfigs.xpath_total_money,
                                 LePayDetailsPageConfigs.total_money)
        logger.info("Input 消费金额 end")
        API().screenShot(self.driver, "xiaoFeiJinE")

    def clickOnPay(self):
        '''
        usage : Click "确认购买"
        '''
        logger.info("Click 确认购买 begin")
        API().clickElementByXpath(testCase = self.testcase,
                                  driver = self.driver,
                                  logger = self.logger,
                                  xpath = LePayDetailsPageConfigs.xpath_pay)

        logger.info("Click 确认购买 end")

if __name__ == '__main__':
    pass;