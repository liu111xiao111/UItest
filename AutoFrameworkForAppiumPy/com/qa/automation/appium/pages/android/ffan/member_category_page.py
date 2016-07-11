# -*- coding: utf-8 -*-

from com.qa.automation.appium.pages.android.ffan.member_category_page_configs import MemberPageConfigs
from com.qa.automation.appium.api.api import API
from com.qa.automation.appium.pages.android.common.super_page import SuperPage

# 会员类目
class MemberPage(SuperPage):
    def __init__(self, testcase, driver, logger):
        super(MemberPage, self).__init__(testcase=testcase, driver=driver, logger=logger);

    '''
        usage : 检查会员类目是否加载出来
    '''

    def validSelf(self):
        API().assert_view_by_resourceID_Until(testcase=self.testcase, driver=self.driver, logger=self.logger,
                                                      resource_id=MemberPageConfigs.resource_id__tv_member_tv,
                                                      seconds=5);


if __name__ == '__main__':
    pass;