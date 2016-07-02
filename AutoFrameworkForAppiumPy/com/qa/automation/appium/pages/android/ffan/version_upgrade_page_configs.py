# -*- coding:utf-8 -*-

class VersionUpgradePageConfigs(object):
    '''
    This is a configuration class for VersionUpdatePage class.
    '''

    # Assert view time out
    assert_view_timeout = 10

    # Verify view time out
    verify_view_timeout = 10

    # Assert invalid view time out
    assert_invalid_view_time = 3

    # Upgrade cancel button
    resource_id_upgrade_cancel_button = "com.wanda.app.wanhui:id/upgrade_cancel"

    # Upgrade confirm button
    resource_id_upgrade_confirm_button = "com.wanda.app.wanhui:id/upgrade_confirm"

    def __init__(self):
        pass