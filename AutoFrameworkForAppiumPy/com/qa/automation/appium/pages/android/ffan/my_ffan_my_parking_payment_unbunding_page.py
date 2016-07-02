# -*- coding: utf-8 -*-

import os

#sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from com.qa.automation.appium.api.api import API
from com.qa.automation.appium.pages.android.common.super_page import SuperPage
from com.qa.automation.appium.pages.android.ffan.my_ffan_my_parking_payment_unbunding_page_configs import MyFfanMyParkingPaymentUnbundingPageConfigs

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class MyFfanMyParkingPaymentUnbundingPage(SuperPage):

    def __init__(self,testcase,driver,logger):
        super(MyFfanMyParkingPaymentUnbundingPage, self).__init__(testcase=testcase , driver=driver, logger=logger);

    def clickOnUnbundingBtn(self):
        '''
            usage: 点击"更多"
        ''' 
        API().click_view_by_text_android(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                         text = MyFfanMyParkingPaymentUnbundingPageConfigs.text_confirm);

if __name__ == '__main__':
    pass;