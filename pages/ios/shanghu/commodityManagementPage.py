# -*- coding:utf-8 -*-

from pages.ios.common.superPage import SuperPage
from api.api import API
from pages.ios.shanghu.shanghuPageConfig import Xpath
from pages.ios.shanghu.shanghuPageConfig import Name
from pages.ios.shanghu.shanghuPageConfig import Text

class CommodityManagement(SuperPage):

    def back(self):
        '''
        返回动作
        :return:
        '''
        API().clickElementByName(self.testcase, self.driver, self.logger, Name.back_icon)

    def enterCommodityManagementModule(self):
        '''
        进入商品管理模块
        :return:
        '''
        API().clickElementByName(self.testcase,self.driver,self.logger,Name.commodity_management_text)


    def clickCheckPendingButton(self):
        '''
        点击待审核
        :return:
        '''
        API().clickElementByName(self.testcase, self.driver, self.logger, Name.commodity_management_pending)

    def checkCheckPendingItem(self):
        '''
        检查待审核内商品,点击商品,检查内容
        :return:
        '''
        #得到商品名称
        commodityName = API().getTextByXpath(self.testcase, self.driver, self.logger, Xpath.commodity_management_sale_check_pending)
        #点击进入商品详情页
        API().clickElementByXpath(self.testcase,self.driver, self.logger,Xpath.commodity_management_sale_check_pending)

        commodityNameTemp = API().getTextByXpath(self.testcase, self.driver, self.logger, "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAWebView[1]/UIAStaticText[4]")

        API().assertTrue(self.testcase,self.logger,commodityName == commodityNameTemp)

        self.back()
        self.back()


    def clickPassingButton(self):
        '''
        点击通过
        :return:
        '''
        API().clickElementByName(self.testcase, self.driver, self.logger, Name.commodity_management_passing)

    def checkCheckPassingItem(self):
        '''
        检查已经通过商品,点击商品,检查内容
        :return:
        '''
        commodityName = API().getTextByXpath(self.testcase, self.driver, self.logger,
                                             "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAWebView[1]/UIAStaticText[1]")
        # 点击进入商品详情页
        API().clickElementByXpath(self.testcase, self.driver, self.logger,
                                  "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAWebView[1]/UIAStaticText[1]")

        commodityNameTemp = API().getTextByXpath(self.testcase, self.driver, self.logger,
                                                 "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAWebView[1]/UIAStaticText[4]")

        API().assertTrue(self.testcase, self.logger, commodityName == commodityNameTemp)

        self.back()
        self.back()
