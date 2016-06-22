#! /Library/Frameworks/Python.framework/Versions/2.7/bin/python
# -*- coding: utf-8 -*-

import os, sys


# reload(sys)
# sys.setdefaultencoding('utf8')

class DashboardConfigs:
    def __init__(self):
        pass;

    # 飞凡商家title
    resource_id_title_textview = "title"
    text_title_textview = "飞凡商家"

    #  登录信息图标
    resource_id_loginInfoIcon_imageview = "login_info_icon"

    resource_id_etCodeEdit_edittext = "et_code_edit"
    text_etCodeEdit_edittext = "请输入提货码或券码"

    #  搜索图标
    resource_id_searchbtn_imageview = "index_search_btn"

    resource_id_indexScan_textview = "index_scan"
    text_indexScan_textview = "扫码验证"

    resource_id_indexHistory_textview = "index_history"
    text_indexHistory_textview = "验证历史"

    text_orderManager_textview = "订单管理"
    text_turnOver_textview = "收款流水";
    text_staffManage_textview = "员工管理"
    text_refundAfterSale_textview = "退款售后"
    text_marketingManage_textview = "营销管理"
    text_accountCheckManage_textview = "对账管理"
    text_storeAnalyse_textview = "店铺分析"
    text_marketingAnalyse_textview = "营销分析"

    text_firstPage_textview = "首页"
    text_msg_textview = "消息"
    text_settings_textview = "设置"
