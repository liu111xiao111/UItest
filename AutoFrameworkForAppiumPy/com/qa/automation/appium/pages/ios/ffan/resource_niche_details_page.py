# -*- coding:utf-8 -*-

from com.qa.automation.appium.api.api import API
from com.qa.automation.appium.pages.ios.common.super_page import SuperPage
from com.qa.automation.appium.pages.ios.ffan.resource_niche_details_page_configs import ResourceNicheDetailsPageConfigs

RNDPC = ResourceNicheDetailsPageConfigs()


class ResourceNicheDetailsPage(SuperPage):
    '''
    作者 宋波
    首页=>广场=>资源位详情
    '''

    def __init__(self, testcase, driver, logger):
        '''
        Constructor
        '''
        super(ResourceNicheDetailsPage, self).__init__(testcase,
                                                       driver,
                                                       logger)

    def validSelf(self):
        '''
        usage: verify whether the current page is correct page.
        '''

        API().assert_view_by_xpath_android(self.testcase, self.driver, self.logger,
                                           ResourceNicheDetailsPageConfigs.xpath_resource_niche_st,
                                           ResourceNicheDetailsPageConfigs.assert_view_timeout)

if __name__ == '__main__':
    pass
