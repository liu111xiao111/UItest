# -*- coding: utf-8 -*-

from api.api import API
from pages.ios.common.superPage import SuperPage
from pages.ios.ffan.feifan_card_page_configs import FeiFanCardPageConfigs

FCPC = FeiFanCardPageConfigs()


class FeiFanCardPage(SuperPage):
    '''
    作者 宋波
    首页=>飞凡卡
    '''

    def __init__(self, testcase, driver, logger):
        super(FeiFanCardPage, self).__init__(testcase,
                                             driver,
                                             logger);

    '''
        usage : 检查是否加载出来
    '''
    def validSelf(self):
        API().assertElementByName(self.testcase,
                                  self.driver,
                                  self.logger,
                                  FeiFanCardPageConfigs.resource_id_score_st,
                                  FeiFanCardPageConfigs.assert_view_timeout)

    '''
        usage: 点击开卡
    '''
    def clickOnOpenCard(self):
        # API().clickElementByName(self.testcase,
        #                          self.driver,
        #                          self.logger,
        #                          FCPC.text_tv_open_tv,
        #                          FCPC.verify_click_timeout)
        API().clickElementByXpath(self.testcase, self.driver, self.logger,"//UIAApplication[1]/UIAWindow[1]/UIAButton[4]")


    '''
        usage : 点击账单
    '''
    def clickOnBill(self):
        API().clickElementByIosUiautomation(self.testcase, self.driver, self.logger,
                                            FeiFanCardPageConfigs.ios_uiautomation_bill_bt,
                                            FeiFanCardPageConfigs.click_on_button_timeout)


    def clickOnPocketMoney(self):
        '''
        usage : 点击零花钱
        '''
        API().click_view_by_resourceID(self.testcase,
                                       self.driver,
                                       self.logger,
                                       FCPC.resource_id_tv_pocket_money_tv)


    def clickOnIntegral(self):
        '''
            usage : 点击积分
        '''
        API().clickElementByName(self.testcase,
                                 self.driver,
                                 self.logger,
                                 FCPC.text_integral,
                                 FCPC.verify_click_timeout);


    def validFeiFanTongOtherEntrance(self,otherEntrancePageName, otherEntranceName):
        '''
        点击飞凡通其它入口并验证
        :param viewXpath:
        :param validValue:
        :return:
        '''
        print("KEYWORDS: %s" % otherEntranceName)

        # API().clickElementByName(self.testcase,
        #                          self.driver,
        #                          self.logger,
        #                          otherEntranceName,
        #                          FCPC.verify_click_timeout);

        API().assertElementByName(self.testcase, self.driver, self.logger, otherEntranceName,
                                  FCPC.assert_view_timeout)

        # API().clickElementByName(self.testcase,
        #                          self.driver,
        #                          self.logger,
        #                          u"返回",
        #                          FCPC.verify_click_timeout);



    def validFeifantongZiyuanwei(self):
        '''
        验证资源位
        '''
        API().clickElementByXpath(self.testcase, self.driver, self.logger,
                                  FCPC.xpath_ziyuanwei,
                                  FCPC.click_on_button_timeout)

        API().assertElementByXpath(self.testcase, self.driver, self.logger,
                                   FCPC.xpath_ziyuanwei_page,
                                   FCPC.assert_view_timeout)

if __name__ == '__main__':
    pass;
