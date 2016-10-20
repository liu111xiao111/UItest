# -*- coding:utf-8 -*-

from api.api import API
from pages.android.common.super_page import SuperPage
from pages.android.ffan.dashboard_shake_page_configs import DashboardShakePageConfigs as DSPC


class DashboardShakePage(SuperPage):
    '''
    作者 乔佳溪
    首页＝>摇一摇
    '''
    def __init__(self, testcase, driver, logger):
        super(DashboardShakePage, self).__init__(testcase , driver, logger)

    def validSelf(self):
        '''
        usage : 进入摇一摇页面
        '''
        API().assertElementByResourceId(self.testcase,
                                        self.driver,
                                        self.logger,
                                        DSPC.resource_id_shake,
                                        DSPC.verify_element_timeout)
