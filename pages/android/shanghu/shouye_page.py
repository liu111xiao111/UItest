# -*- coding: utf-8 -*-

from api.api import API
from pages.android.common.super_page import SuperPage
from pages.android.shanghu.shouye_page_configs import ShouYePageConfigs as SYPC


class ShouYePage(SuperPage):
    '''
    作者 乔佳溪
    首页
    '''
    def __init__(self, testcase, driver, logger):
        super(ShouYePage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        '''
        usage : 进入到选择门店页,检查标题
        '''
        title = API().getTextByResourceId(self.testcase,
                                        self.driver,
                                        self.logger,
                                        SYPC.resource_id_title,
                                        SYPC.verify_timeout)

        API().assertEqual(self.testcase, self.logger, title, SYPC.text_store)

    def clickOnUser(self):
        '''
        usage: 点击用户
        '''
        API().clickElementByResourceId(self.testcase,
                                       self.driver,
                                       self.logger,
                                       SYPC.resource_id_user,
                                       SYPC.verify_timeout)

    def validLogin(self):
        '''
        usage : 验证首页是否登录
        '''
        rtn = API().validElementByResourceId(self.driver,
                                             self.logger,
                                             SYPC.resource_id_title,
                                             SYPC.verify_timeout)
        return rtn

    def clickOnSetting(self):
        '''
        usage: 点击设置
        '''
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 SYPC.text_setting,
                                 SYPC.verify_timeout)

    def clickOnMemberManager(self):
        '''
        usage: 点击员工管理
        '''
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 SYPC.text_member_manager,
                                 SYPC.verify_timeout)

    def clickOnRoleManager(self):
        '''
        usage: 点击角色管理
        '''
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 SYPC.text_role_manager,
                                 SYPC.verify_timeout)

    def clickOnOrderManager(self):
        '''
        usage: 点击订单管理
        '''
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 SYPC.text_order_manager,
                                 SYPC.verify_timeout)
