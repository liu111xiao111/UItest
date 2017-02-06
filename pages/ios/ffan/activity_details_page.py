# -*- coding:utf-8 -*-

from api.api import API
from pages.ios.common.superPage import SuperPage
from pages.ios.ffan.activity_details_page_configs import ActivityDetailsPageConfigs


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

        API().assertElementByName(self.testcase, self.driver, self.logger,
                                  ActivityDetailsPageConfigs.name_activity_details_title_st,
                                  ActivityDetailsPageConfigs.assert_view_timeout)

    def clickOnSharing(self):
        '''
        usage: click sharing button
        '''

        API().clickElementByXpath(self.testcase, self.driver, self.logger,
                                  ActivityDetailsPageConfigs.xpath_sharing_bt,
                                  ActivityDetailsPageConfigs.click_on_button_timeout)

if __name__ == '__main__':
    pass
