# -*- coding:utf-8 -*-

from pages.ios.common.superPage import SuperPage
from api.api import API
from pages.ios.shanghu.shanghuPageConfig import Xpath
from pages.ios.shanghu.shanghuPageConfig import Name
from pages.ios.shanghu.shanghuPageConfig import Text
from pages.logger import logger

class OrderFormManagementPage(SuperPage):

    def validSelf(self):

        logger.info('Check 订单管理 begin')
        API().assertElementByName(self.testcase,
                                  self.driver,
                                  self.logger,
                                  Name.order_form_management)
        logger.info('Check 订单管理 end')

    def getOrderInfo(self):
        '''
        获取订单信息
        :return:
        '''
        logger.info('Get 订单信息 begin')
        itemContext = API().getTextByXpath(self.testcase,self.driver,self.logger,Xpath.order_management_first_item)

        global orderFormNumber
        global orderFormStatus
        global orderFormBuyer
        global orderFormDate
        global orderFormTotal
        global amountPaid

        logger.info('Get 订单号')
        orderFormNumber = itemContext[10:24].strip()
        logger.info('Get 订单状态')
        orderFormStatus = itemContext[34:38].strip()
        logger.info('Get 电话号')
        orderFormBuyer = itemContext[46:57].strip()
        # 截取得电话号后四位
        orderFormBuyer = orderFormBuyer[7:11]
        logger.info('Get 订单日期')
        orderFormDate = itemContext[67:86].strip()
        logger.info('Get 订单总额')
        orderFormTotal = itemContext[110:116].strip()
        orderFormTotal = orderFormTotal[1:]
        logger.info('Get 支付总额')
        amountPaid = itemContext[125:131].strip()
        amountPaid = amountPaid[1:]
        logger.info('Get 订单信息 end')

    def clickFirstItemOfOrderList(self):
        '''
        点击第一个订单,进入订单详情
        :return:
        '''
        logger.info('Click 第一个订单 begin')
        API().clickElementByXpath(self.testcase,self.driver,self.logger,Xpath.order_management_first_item)
        logger.info('Click 第一个订单 end')
        API().screenShot(self.driver,'firstOrder')


    def validOrderDetail(self):
        '''
        验证订单详情
        :return:
        '''
        logger.info('Check 订单详情 begin')
        API().assertElementByName(self.testcase,
                                  self.driver,
                                  self.logger,
                                  Name.order_detail)
        logger.info('Check 订单详情 end')

    def checkAllOrderDetail(self,whichcase = "JiaoYiGuanBi"):
        '''
        检查全部订单信息
        :return:
        '''
        logger.info('check 订单信息 begin')
        orderInfoArr = (orderFormNumber, orderFormStatus, orderFormDate )
        # 获取订单详情页, 各个item内容
        orderFormNumberTemp = API().getTextByXpath(self.testcase,
                                                   self.driver,
                                                   self.logger,
                                                   Xpath.order_number,
                                                   20)
        orderFormStatusTemp = API().getTextByXpath(self.testcase,
                                                   self.driver,
                                                   self.logger,
                                                   Xpath.order_status)

        orderFormDateTemp = API().getTextByXpath(self.testcase,
                                                  self.driver,
                                                  self.logger,
                                                  Xpath.order_date)

        orderInfoArrTemp= (orderFormNumberTemp, orderFormStatusTemp, orderFormDateTemp)

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
