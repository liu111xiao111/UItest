# -*- coding:utf-8 -*-

from api.api import API
from pages.ios.common.superPage import SuperPage
from pages.ios.ffan.resource_niche_details_page_configs import ResourceNicheDetailsPageConfigs

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

        API().assertElementByXpath(self.testcase, self.driver, self.logger,
                                   ResourceNicheDetailsPageConfigs.xpath_resource_niche_st,
                                   ResourceNicheDetailsPageConfigs.assert_view_timeout)

if __name__ == '__main__':
    pass
