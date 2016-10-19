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

    # Click button time out
    click_on_button_timeout = 10

    # Upgrade cancel button
    resource_id_upgrade_cancel_bt = u"取消"

    # Upgrade confirm button
    resource_id_upgrade_confirm_bt = u"确定"

    def __init__(self):
        pass