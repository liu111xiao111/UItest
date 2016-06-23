#!/usr/bin/env python
# -*- coding:utf-8 -*-


from com.qa.automation.appium.api.api import API
from com.qa.automation.appium.pages.android.common.super_page import SuperPage
from com.qa.automation.appium.pages.android.ffan.goods_details_page_configs import GoodsDetailsPageConfigs


class GoodsDetailsPage(SuperPage):
    '''
    This is goods details page operation class.
    '''

    def __init__(self, testcase, driver, logger):
        '''
        Constructor
        '''

        super(GoodsDetailsPage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        '''
        usage: verify whether the current page is correct page.
        '''

        API().assert_view_by_resourceID_Until(self.testcase, self.driver, self.logger,
                                                      GoodsDetailsPageConfigs.resource_id_reource_goods_details_title,
                                                      GoodsDetailsPageConfigs.assert_view_timeout)


if __name__ == '__main__':
    pass
