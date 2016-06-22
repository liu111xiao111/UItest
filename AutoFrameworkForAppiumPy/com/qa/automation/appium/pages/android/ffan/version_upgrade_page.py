# -*- coding:utf-8 -*-

from selenium.common.exceptions import TimeoutException

from selenium.common.exceptions import TimeoutException

from com.qa.automation.appium.api.api import API
from com.qa.automation.appium.pages.android.common.super_page import SuperPage
from com.qa.automation.appium.pages.android.ffan.version_upgrade_page_configs import VersionUpgradePageConfigs


class VersionUpgradePage(SuperPage):
    '''
    This is a version update page operation class.
    '''

    def __init__(self, testcase, driver, logger):
        '''
        Constructor
        '''

        super(VersionUpgradePage, self).__init__(testcase, driver, logger)

    def validSelf(self, assertable=True):
        '''
        usage: verify whether the current page is the version upgrade page.
        '''

        if assertable:
            API().assert_view_by_resourceID_Until_android(self.testcase, self.driver, self.logger,
                                                          VersionUpgradePageConfigs.resource_id_upgrade_cancel_button,
                                                          VersionUpgradePageConfigs.assert_view_timeout)
            return True
        else:
            try:
                API().find_view_by_resourceID_Until_android(self.driver, self.logger,
                                                            VersionUpgradePageConfigs.resource_id_upgrade_cancel_button,
                                                            VersionUpgradePageConfigs.verify_view_timeout)
                return True
            except TimeoutException:
                return False

    def cancelVersionUpgrade(self):
        '''
        usage: cancel version upgrade.
        '''

        API().click_view_by_resourceID_android(self.testcase, self.driver, self.logger,
                                               VersionUpgradePageConfigs.resource_id_upgrade_cancel_button)

    def confirmVersionUpgrade(self):
        '''
        usage: confirm version upgrade.
        '''

        API().click_view_by_resourceID_android(self.testcase, self.driver, self.logger,
                                               VersionUpgradePageConfigs.resource_id_upgrade_confirm_button)

    def validPercentage(self):
        '''
        usage: verity whether the percentage is 100%.
        '''

        API().find_view_by_text_Until_android(self.testcase, self.driver, self.logger, "100%", 600)

    def invalidSelf(self):
        '''
        usage: verify whether the current page is not the version upgrade page.
        '''

        API().assert_none_view_by_resource_id_until_android(self.testcase, self.driver, self.logger,
                                                            VersionUpgradePageConfigs.resource_id_upgrade_cancel_button,
                                                            VersionUpgradePageConfigs.assert_invalid_view_time)


if __name__ == '__main__':
    pass
