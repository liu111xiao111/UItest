# -*- coding:utf-8 -*-

from pages.ios.common.superPage import SuperPage
from api.api import API
from pages.ios.shanghu.shanghuPageConfig import Xpath
from pages.ios.shanghu.shanghuPageConfig import Name
from pages.ios.shanghu.shanghuPageConfig import Text

class OrderFormManagementPage(SuperPage):

    orderFormName = ""
    orderFormStatus = ""
    orderFormBuyer = ""
    orderFormNumber = ""
    orderFormDate = ""
    orderFormTotal = ""
    amountPaid = ""

    #def getOrderInfo(self):
