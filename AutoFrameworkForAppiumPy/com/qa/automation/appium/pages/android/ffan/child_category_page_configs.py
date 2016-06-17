# -*- coding: utf-8 -*-

import os,sys


class ChildCategoryPageConfigs():
    
    
    #常量命名规则 resource_id指明资源类型是resource id;iv_center_tab view id name;iv指明view类型image view
    
    # 亲自游乐
    resource_id_ll_child_play_ll = "com.feifan.qinzi:id/main_page_shop_flag_layout1";
    #儿童教育
    resource_id_ll_child_education_ll = "com.feifan.qinzi:id/main_page_shop_flag_layout2";
    #亲子购物
    resource_id_ll_child_shopping_ll = "com.feifan.qinzi:id/main_page_shop_flag_layout3";
    #其它门店
    resource_id_ll_other_store_ll = "com.feifan.qinzi:id/main_page_shop_flag_other";
    
    
    #xpath
    #亲自游乐 儿童教育 亲子购物 其他门店 点击进去后的listview 的第一个的xpath
    xpath_store_list_1= "//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.ListView[1]/android.widget.RelativeLayout[1]";
    
    
    # text指明类型为text label,后面是文字的拼音
    text_chile_category = "儿童教育";
    
    
    def __init__(self):
        pass;

