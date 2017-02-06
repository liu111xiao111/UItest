# -*- coding:utf-8 -*-

from api.api import API
from pages.ios.common.superPage import SuperPage
from pages.ios.ffan.brand_activity_page_configs import BrandActivityPageConfigs


class BrandActivityPage(SuperPage):
    '''
    作者 宋波
    首页=>我的飞凡=>消息中心=>品牌活动
    '''

    def __init__(self, testcase, driver, logger):
        '''
        Constructor
        '''

        super(BrandActivityPage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        '''
        usage: verify whether the current page is correct.
        '''

        API().assertElementByName(self.testcase, self.driver, self.logger,
                                  BrandActivityPageConfigs.name_square_dynamic_title_st,
                                  BrandActivityPageConfigs.assert_view_timeout)


if __name__ == '__main__':
    pass
