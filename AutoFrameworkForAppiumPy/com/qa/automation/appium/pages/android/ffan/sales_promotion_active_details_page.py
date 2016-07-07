# -*- coding: utf-8 -*-

from __init__ import *

from com.qa.automation.appium.api.api import API
from com.qa.automation.appium.pages.android.common.super_page import SuperPage

class SalesPromotionActiveDetailsPage(SuperPage):

    def __init__(self,testcase,driver,logger):
        super(SalesPromotionActiveDetailsPage, self).__init__(testcase = testcase , driver = driver, logger = logger);

    def validSelf(self, itemtext="default"):
        '''
            usage : "活动详情" whether loading correctly.
        '''
        API().assert_view_by_content_desc_android(self.testcase, self.driver, self.logger, itemtext)


if __name__ == '__main__':
    pass;