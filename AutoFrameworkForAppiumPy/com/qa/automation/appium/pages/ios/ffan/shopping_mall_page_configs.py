# -*- coding:utf-8 -*-

'''
    首页->购物中心页面配置
'''
class ShoppingMallPageConfigs(object):
    # Assert view time out
    assert_view_timeout = 10

    # Click button time out
    click_on_button_timeout = 10

    # Shopping mall title
    name_shopping_mall_title = u"百货"

    # 购物广场class
    class_plaza_id = "UIATableCell"

    # 全部
    xpath_tab_title_1 = "//UIAApplication[1]/UIAWindow[1]/UIAButton[1]"

    # 全部
    xpath_tab_title_2 = "//UIAApplication[1]/UIAWindow[1]/UIAButton[2]"

    # 全部
    xpath_tab_title_3 = "//UIAApplication[1]/UIAWindow[1]/UIAButton[3]"

    view_text_distance = u"公里"

    views_uia_string = ".tableViews()[0].cells()"

    def __init__(self):
        pass
