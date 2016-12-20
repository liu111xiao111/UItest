# -*- coding:utf-8 -*-

from pages.ios.common.superPage import SuperPage
from api.api import API
from pages.ios.shanghu.shanghuPageConfig import Xpath
from pages.ios.shanghu.shanghuPageConfig import Name
from pages.ios.shanghu.shanghuPageConfig import Text
from pages.logger import logger

class OrderFormManagementPage(SuperPage):

    def getOrderInfo(self):
        '''
        获取订单信息
        :return:
        '''
        itemContext = API().getTextByXpath(self.testcase,self.driver,self.logger,Xpath.order_management_first_item)

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
        logger.info('Click 第一个订单 begin')
        API().clickElementByXpath(self.testcase,self.driver,self.logger,Xpath.order_management_first_item)
        logger.info('Click 第一个订单 end')
        API().screenShot(self.driver,'firstOrder')


    def checkAllOrderDetail(self,whichcase = "JiaoYiGuanBi"):
        '''
        检查全部订单信息
        :return:
        '''
        logger.info('check 订单信息 begin')
        orderInfoArr = (orderFormNumber, orderFormStatus, orderFormBuyer, orderFormDate )
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
        #全部订单和交易关闭订单,一个界面,但是phonnumber xpath 不同
        if(whichcase=="QuanBuDingDan"):
            phoneNumberXpath = "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAWebView[1]/UIAStaticText[31]"
        else:
            phoneNumberXpath = "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAWebView[1]/UIAStaticText[31]"

        #滑动显示电话号码,再获取value
        logger.info('Scroll to 电话号码 begin')
        API().iosScrollToElement(self.driver,self.logger,phoneNumberXpath,
                                 '18612819429')
        orderFormBuyerTemp = API().getTextByXpath(self.testcase,
                                                  self.driver,
                                                  self.logger,
                                                  phoneNumberXpath)
        logger.info('Scroll to 电话号码 begin')
        print('debug order %s' % orderFormBuyerTemp)

        # 截取得电话号后四位
        orderFormBuyerTemp = orderFormBuyerTemp[7:11]

        orderFormTotalTemp = orderFormTotalTemp[1:]
        # print(orderFormTotalTemp)
        # print(orderFormTotal)

        amountPaidTemp = amountPaidTemp[1:]

        orderInfoArrTemp= (orderFormNumberTemp, orderFormStatusTemp, orderFormBuyerTemp, orderFormDateTemp)

        for index in range(len(orderInfoArr)):
            logger.info('order info: ' + orderInfoArr[index].strip())
            print("orderInfoArr %s : " + orderInfoArr[index].strip())
            print("orderInfoArrTemp %s : " + orderInfoArrTemp[index].strip())

            API().assertTrue(self.testcase,self.logger,orderInfoArrTemp[index].strip() == orderInfoArr[index].strip())
        logger.info('check 订单信息 end')

        API().screenShot(self.driver,'orderInfo')



    def clickAllOrderStatusButton(self):
        '''
        点击全部状态按钮
        :return:
        '''
        logger.info('Click 全部状态 begin')
        API().clickElementByName(self.testcase,
                                 self.driver,
                                 self.logger,
                                 Name.all_order_status)
        logger.info('Click 全部状态 end')
        API().screenShot(self.driver,'allStatus')

    def clickTradingClosedButton(self):
        '''
        点击交易关闭按钮
        :return:
        '''
        logger.info('Click 关闭状态 begin')
        API().clickElementByName(self.testcase,
                                 self.driver,
                                 self.logger,
                                 Name.trading_closed_status)
        logger.info('Click 关闭状态 end')
        API().screenShot(self.driver,'closedStatus')
