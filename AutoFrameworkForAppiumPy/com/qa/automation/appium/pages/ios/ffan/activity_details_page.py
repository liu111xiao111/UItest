# -*- coding:utf-8 -*-

from com.qa.automation.appium.api.api import API
from com.qa.automation.appium.pages.ios.common.super_page import SuperPage
from com.qa.automation.appium.pages.ios.ffan.activity_details_page_configs import ActivityDetailsPageConfigs


class ActivityDetailsPage(SuperPage):
    '''
    作者 宋波
    首页=>活动与优惠券=>活动详情
    '''

    def __init__(self, testcase, driver, logger):
        '''
        Constructor
        '''

        super(ActivityDetailsPage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        '''
        usage: verify whether the current page is correct page.
        '''

        API().assert_view_by_resourceID_Until(self.testcase, self.driver, self.logger,
                                              ActivityDetailsPageConfigs.resource_id_activity_details_title_st,
                                              ActivityDetailsPageConfigs.assert_view_timeout)

    def clickOnSharing(self):
        '''
        usage: click sharing button
        '''

        API().click_view_by_xpath(self.testcase, self.driver, self.logger,
                                  ActivityDetailsPageConfigs.xpath_sharing_bt,
                                  ActivityDetailsPageConfigs.click_on_button_timeout)

if __name__ == '__main__':
    pass
