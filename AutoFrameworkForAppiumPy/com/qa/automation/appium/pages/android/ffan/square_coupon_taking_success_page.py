# -*- coding: utf-8 -*-

import os, sys

# sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from com.qa.automation.appium.pages.android.ffan.square_coupon_taking_success_page_configs import \
    SquareCouponTakingSuccessPageConfigs
from com.qa.automation.appium.api.api import API
from com.qa.automation.appium.pages.android.common.super_page import SuperPage

from appium import webdriver

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

'''
    usage : 广场模块 ,优惠券　领劵成功页面
'''


class SquareCouponTakingSuccessPage(SuperPage):
    def __init__(self, testcase, driver, logger):
        super(SquareCouponTakingSuccessPage, self).__init__(testcase=testcase, driver=driver, logger=logger);

    def validSelf(self):
        API().assert_view_by_text_android(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                          text=SquareCouponTakingSuccessPageConfigs.text_taking_success)


if __name__ == '__main__':
    pass;