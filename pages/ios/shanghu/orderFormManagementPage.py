# -*- coding:utf-8 -*-

from pages.ios.common.superPage import SuperPage
from api.api import API
from pages.ios.shanghu.shanghuPageConfig import Xpath
from pages.ios.shanghu.shanghuPageConfig import Name
from pages.ios.shanghu.shanghuPageConfig import Text


class OrderFormManagementPage(SuperPage):

    def getOrderInfo(self):
        '''
        获取订单信息
        :return:
        '''
        itemContext = API().getTextByXpath(self.testcase,self.driver,self.logger,Xpath.order_management_first_item)
        print(itemContext)

        global orderFormNumber
        global orderFormStatus
        global orderFormBuyer
        global orderFormDate
        global orderFormTotal
        global amountPaid

        orderFormNumber = itemContext[10:24].strip()
        orderFormStatus = itemContext[34:38].strip()
        orderFormBuyer = itemContext[46:57].strip()
        # 截取得电话号后四位
        orderFormBuyer = orderFormBuyer[7:11]
        orderFormDate = itemContext[67:86].strip()
        orderFormTotal = itemContext[110:116].strip()
        orderFormTotal = orderFormTotal[1:]
        amountPaid = itemContext[125:131].strip()
        amountPaid = amountPaid[1:]

    def clickFirstItemOfOrderList(self):
        '''
        点击第一个订单,进入订单详情
        :return:
        '''
        API().clickElementByXpath(self.testcase,self.driver,self.logger,Xpath.order_management_first_item)


    def checkAllOrderDetail(self):
        '''
        检查全部订单信息
        :return:
        '''

        orderInfoArr = (orderFormNumber, orderFormStatus, orderFormBuyer, orderFormDate, orderFormTotal, amountPaid)
        # 获取订单详情页, 各个item内容
        orderFormNumberTemp = API().getTextByXpath(self.testcase,
                                                   self.driver,
                                                   self.logger,
                                                   "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAWebView[1]/UIAStaticText[4]",
                                                   20)
        orderFormStatusTemp = API().getTextByXpath(self.testcase,
                                                   self.driver,
                                                   self.logger,
                                                   "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAWebView[1]/UIAStaticText[2]")
        orderFormBuyerTemp = API().getTextByXpath(self.testcase,
                                                  self.driver,
                                                  self.logger,
                                                  "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAWebView[1]/UIAStaticText[27]")
        orderFormDateTemp = API().getTextByXpath(self.testcase,
                                                  self.driver,
                                                  self.logger,
                                                  "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAWebView[1]/UIAStaticText[6]")
        orderFormTotalTemp = API().getTextByXpath(self.testcase,
                                                  self.driver,
                                                  self.logger,
                                                  "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAWebView[1]/UIAStaticText[8]")
        amountPaidTemp = API().getTextByXpath(self.testcase,
                                                  self.driver,
                                                  self.logger,
                                                  "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAWebView[1]/UIAStaticText[10]")
        # 截取得电话号后四位
        orderFormBuyerTemp = orderFormBuyerTemp[7:11]

        orderFormTotalTemp = orderFormTotalTemp[1:]

        amountPaidTemp = amountPaidTemp[1:]

        orderInfoArrTemp= (orderFormNumberTemp, orderFormStatusTemp, orderFormBuyerTemp, orderFormDateTemp, orderFormTotalTemp, amountPaidTemp)

        for index in range(len(orderInfoArr)):
            print(orderInfoArr[index].strip())
            print(orderInfoArrTemp[index].strip())

            API().assertTrue(self.testcase,self.logger,orderInfoArrTemp[index].strip() == orderInfoArr[index].strip())




