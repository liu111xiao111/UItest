# -*- coding:utf-8 -*-

from selenium.common.exceptions import TimeoutException

from api.api import API
from pages.android.common.super_page import SuperPage
from pages.android.ffan.version_upgrade_page_configs import VersionUpgradePageConfigs as VUPC


class VersionUpgradePage(SuperPage):
    '''
    作者 宋波
    版本更新
    '''
    def __init__(self, testcase, driver, logger):
        super(VersionUpgradePage, self).__init__(testcase, driver, logger)

    def validSelf(self, assertable=True):
        '''
        usage: 验证版本更新
        '''

        if assertable:
            API().assertElementByResourceId(self.testcase,
                                            self.driver,
                                            self.logger,
                                            VUPC.resource_id_upgrade_cancel_button,
                                            VUPC.assert_view_timeout)
            return True
        else:
            res = API().validElementByResourceId(self.driver,
                                           self.logger,
                                           VUPC.resource_id_upgrade_cancel_button,
                                           VUPC.verify_view_timeout)
            if res:
                return True
            return False

    def cancelVersionUpgrade(self):
        '''
        usage: 取消版本更新
        '''

        API().clickElementByResourceId(self.testcase,
                                       self.driver,
                                       self.logger,
                                       VUPC.resource_id_upgrade_cancel_button,
                                       VUPC.verify_view_timeout)

    def confirmVersionUpgrade(self):
        '''
        usage: 确认版本更新
        '''

        API().clickElementByResourceId(self.testcase,
                                       self.driver,
                                       self.logger,
                                       VUPC.resource_id_upgrade_confirm_button,
                                       VUPC.verify_view_timeout)

    def validPercentage(self):
        '''
        usage: 验证进度
        '''

        API().assertElementByText(self.testcase,
                                  self.driver,
                                  self.logger,
                                  "100%",
                                  600)

    def invalidSelf(self):
        '''
        usage: 验证当前页面不是版本更新页面
        '''

        API().assertFalse(self.testcase,
                          self.logger,
                          API().validElementByResourceId(self.driver,
                                                         self.logger,
                                                         VUPC.resource_id_upgrade_cancel_button,
                                                         VUPC.assert_invalid_view_time))
