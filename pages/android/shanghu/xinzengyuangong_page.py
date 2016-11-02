# -*- coding: utf-8 -*-

from api.api import API
from pages.android.common.super_page import SuperPage
from pages.android.shanghu.xinzengyuangong_page_configs import XinZengYuanGongPageConfigs as XZYGPC


class XinZengYuanGongPage(SuperPage):
    '''
    作者 乔佳溪
    员工管理
    '''
    def __init__(self, testcase, driver, logger):
        super(XinZengYuanGongPage, self).__init__(testcase, driver, logger)

    def clickOnChooseRole(self):
        '''
        usage: 选择角色
        '''
        API().clickElementByResourceId(self.testcase,
                                       self.driver,
                                       self.logger,
                                       XZYGPC.resource_id_choose,
                                       XZYGPC.verify_timeout)
        API().waitBySeconds(2)
        API().clickElementByText(self.testcase,
                                       self.driver,
                                       self.logger,
                                       XZYGPC.text_role,
                                       XZYGPC.verify_timeout)
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 XZYGPC.text_confirm,
                                 XZYGPC.verify_timeout)

    def inputUserName(self):
        '''
        usage: 输入用户名
        '''
        API().inputStringByResourceId(self.testcase,
                                      self.driver,
                                      self.logger,
                                      XZYGPC.resource_id_name,
                                      XZYGPC.account_name,
                                      XZYGPC.verify_timeout)

    def inputPhone(self):
        '''
        usage: 输入手机号
        '''
        API().inputStringByResourceId(self.testcase,
                                      self.driver,
                                      self.logger,
                                      XZYGPC.resource_id_phone,
                                      XZYGPC.account_phone,
                                      XZYGPC.verify_timeout)

    def clickOnSave(self):
        '''
        usage: 选择保存
        '''
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 XZYGPC.text_save,
                                 XZYGPC.verify_timeout)

    def clickOnChangeRole(self):
        '''
        usage: 变更角色
        '''
        API().clickElementByResourceId(self.testcase,
                                       self.driver,
                                       self.logger,
                                       XZYGPC.resource_id_choose,
                                       XZYGPC.verify_timeout)

        API().waitBySeconds(3)

        API().scrollToText(self.testcase,
                           self.driver,
                           self.logger,
                           XZYGPC.text_edit_role)

        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 XZYGPC.text_edit_role,
                                 XZYGPC.verify_timeout)

        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 XZYGPC.text_confirm,
                                 XZYGPC.verify_timeout)

    def inputEditName(self):
        '''
        usage: 编辑用户名
        '''
        name = API().getTextByResourceId(self.testcase,
                                         self.driver,
                                         self.logger,
                                         XZYGPC.resource_id_name,
                                         XZYGPC.verify_timeout)

        name = name + "ceshi"
        API().inputStringByResourceId(self.testcase,
                                      self.driver,
                                      self.logger,
                                      XZYGPC.resource_id_name,
                                      name,
                                      XZYGPC.verify_timeout)
