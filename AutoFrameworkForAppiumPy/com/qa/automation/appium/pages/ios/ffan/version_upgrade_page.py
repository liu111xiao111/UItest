# -*- coding:utf-8 -*-

from com.qa.automation.appium.api.api_new import API
from com.qa.automation.appium.pages.ios.common.super_page import SuperPage
from com.qa.automation.appium.pages.ios.ffan.version_upgrade_page_configs import VersionUpgradePageConfigs


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
            API().assertElementByName(self.testcase, self.driver, self.logger,
                                      VersionUpgradePageConfigs.resource_id_upgrade_cancel_bt,
                                      VersionUpgradePageConfigs.assert_view_timeout)
            return True
        else:
            return API().validElementByName(self.driver, self.logger,
                                            VersionUpgradePageConfigs.resource_id_upgrade_cancel_bt,
                                            VersionUpgradePageConfigs.verify_view_timeout)

    def cancelVersionUpgrade(self):
        '''
        usage: cancel version upgrade.
        '''

        API().clickElementByName(self.testcase, self.driver, self.logger,
                                 VersionUpgradePageConfigs.resource_id_upgrade_cancel_bt,
                                 VersionUpgradePageConfigs.click_on_button_timeout)

    def confirmVersionUpgrade(self):
        '''
        usage: confirm version upgrade.
        '''

        API().click_view_by_resourceID(self.testcase, self.driver, self.logger,
                                       VersionUpgradePageConfigs.resource_id_upgrade_confirm_bt,
                                       VersionUpgradePageConfigs.click_on_button_timeout)

    def validPercentage(self):
        '''
        usage: verity whether the percentage is 100%.
        '''

        API().find_view_by_text_Until_android(self.testcase, self.driver, self.logger, "100%", 600)

    def invalidSelf(self):
        '''
        usage: verify whether the current page is not the version upgrade page.
        '''

        API().assertFalse(self.testcase, self.logger,
                          API().validElementByName(self.driver, self.logger,
                                                   VersionUpgradePageConfigs.resource_id_upgrade_cancel_bt,
                                                   VersionUpgradePageConfigs.assert_invalid_view_time))


if __name__ == '__main__':
    pass
