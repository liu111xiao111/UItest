#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
Title: sharing_page.py
Package: com.qa.automation.appium.pages.android.ffan
Description: This is sharing page operation class.
Company: Neusoft
All rights Reserved, Designed By Zhaosheng Liu
@copyright: Copyright(C) 2016-2017
@author: Zhaosheng Liu
@date Jun 17, 2016 02:37:35 PM
Modification  History:
Date                Author                Version                Description
Jun 17, 2016        liuzhsh               V0.0.0.1               New file
Why & What is modified: TODO
'''

from com.qa.automation.appium.api.api import API
from com.qa.automation.appium.pages.android.common.super_page import SuperPage
from com.qa.automation.appium.pages.android.ffan.sharing_page_configs import SharingPageConfigs

class SharingPage(SuperPage):
    '''
    This is sharing page operation class.
    '''


    def __init__(self, testcase, driver, logger):
        '''
        Constructor
        '''

        super(SharingPage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        '''
        usage: verify whether the current page is correct page.
        '''

        API().assert_view_by_resourceID_Until(self.testcase, self.driver, self.logger, SharingPageConfigs.resource_id_sharing_title, SharingPageConfigs.assert_view_timeout)

    def validKeywords(self, keywords):
        '''
        usage: verify whether the keyword is correct.
        '''

        print("KEYWORDS: %s" % keywords)

        API().assert_view_by_text_android(self.testcase, self.driver, self.logger, keywords, SharingPageConfigs.assert_view_timeout)

if __name__ == '__main__':
    pass
