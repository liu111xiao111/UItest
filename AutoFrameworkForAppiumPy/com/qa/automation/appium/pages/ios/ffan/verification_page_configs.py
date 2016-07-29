# -*- coding: utf-8 -*-

class VerificationPageConfigs():

    # Assert view time out
    assert_view_timeout = 10

    # Assert invalid view time out
    assert_invalid_view_time = 3

    # Click button time out
    click_on_button_timeout = 10

    # Verification title
    name_title_st = u"验证"
    xpath_title_st = "//UIAApplication[1]/UIAWindow[1]/UIANavigationBar[1]/UIAStaticText[1]"

    # Skip
    name_skip_bt = u"跳过"
    xpath_skip_bt = "//UIAApplication[1]/UIAWindow[1]/UIANavigationBar[1]/UIAButton[2]"


    def __init__(self):
        pass
