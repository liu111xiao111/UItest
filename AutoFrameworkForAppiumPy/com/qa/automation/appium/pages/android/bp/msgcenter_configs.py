#! /Library/Frameworks/Python.framework/Versions/2.7/bin/python
# -*- coding: utf-8 -*-

import os, sys


# reload(sys)
# sys.setdefaultencoding('utf8')

class MessageCenterConfigs:
    def __init__(self):
        pass;

    # 消息中心title
    resource_id_title_textview = "header_center_title"
    text_title_textview = "消息中心"

    # 通知公告tab resource id
    resource_id_msgNotice_textview = "tv_message_notice"
    text_msgNotice_textview = "通知公告"

    # 系统消息tab resource id
    resource_id_msgSystem_textview = "tv_message_system"
    text_msgSystem_textview = "系统消息"
