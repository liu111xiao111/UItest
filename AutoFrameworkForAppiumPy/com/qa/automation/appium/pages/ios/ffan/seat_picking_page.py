# -*- coding:utf-8 -*-

from com.qa.automation.appium.api.api import API
from com.qa.automation.appium.pages.ios.common.super_page import SuperPage
from com.qa.automation.appium.pages.ios.ffan.seat_picking_page_configs import SeatPickingPageConfigs


class SeatPickingPage(SuperPage):
    '''
    作者 宋波
    首页=>电影=>电影详情=>选座
    '''

    def __init__(self, testcase, driver, logger):
        '''
        Constructor
        '''

        super(SeatPickingPage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        '''
        usage: verify whether the current page is correct page.
        '''

        API().assert_view_by_xpath_android(self.testcase, self.driver, self.logger,
                                           SeatPickingPageConfigs.xpath_seat_picking_title_st,
                                           SeatPickingPageConfigs.assert_view_timeout)


    def validKeywords(self, keywords):
        '''
        usage: verify whether the keyword is correct.
        '''

        print("KEYWORDS: %s" % keywords)

        API().assert_view_by_resourceID_Until(self.testcase, self.driver, self.logger,
                                              keywords, SeatPickingPageConfigs.assert_view_timeout)

if __name__ == '__main__':
    pass
