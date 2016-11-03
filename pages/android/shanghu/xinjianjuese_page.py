# -*- coding: utf-8 -*-

from api.api import API
from pages.android.common.super_page import SuperPage
from pages.android.shanghu.xinjianjuese_page_configs import XinJianJueSePageConfigs as XJJSPC


class XinJianJueSePage(SuperPage):
    '''
    作者 乔佳溪
    角色管理
    '''
    def __init__(self, testcase, driver, logger):
        super(XinJianJueSePage, self).__init__(testcase, driver, logger)

    def clickOnChooseRole(self):
        '''
        usage: 选择角色
        '''
        API().clickElementByResourceId(self.testcase,
                                       self.driver,
                                       self.logger,
                                       XJJSPC.resource_id_choose,
                                       XJJSPC.verify_timeout)
        API().waitBySeconds(2)

        roleList = API().getElementsByType(self.testcase,
                                           self.driver,
                                           self.logger,
                                           XJJSPC.type_role,
                                           XJJSPC.verify_timeout)
        print(len(roleList))
        for _ in range(len(roleList)):
            API().clickElementByType(self.testcase,
                                     self.driver,
                                     self.logger,
                                     XJJSPC.type_role,
                                     XJJSPC.verify_timeout)

        API().clickElementByResourceId(self.testcase,
                                       self.driver,
                                       self.logger,
                                       XJJSPC.resource_id_save,
                                       XJJSPC.verify_timeout)

    def validChooseRole(self):
        '''
        usage: 选择角色
        '''
        roleStatus = API().getTextByResourceId(self.testcase,
                                               self.driver,
                                               self.logger,
                                               XJJSPC.resource_id_choose,
                                               XJJSPC.verify_timeout)
        API().assertEqual(self.testcase, self.logger, roleStatus, XJJSPC.account_role)

    def inputUserName(self):
        '''
        usage: 输入用户名
        '''
        API().inputStringByResourceId(self.testcase,
                                      self.driver,
                                      self.logger,
                                      XJJSPC.resource_id_name,
                                      XJJSPC.account_name,
                                      XJJSPC.verify_timeout)

    def inputRoleInstruction(self):
        '''
        usage: 输入角色说明
        '''
        API().inputStringByResourceId(self.testcase,
                                      self.driver,
                                      self.logger,
                                      XJJSPC.resource_id_option,
                                      XJJSPC.text_instruction,
                                      XJJSPC.verify_timeout)

    def clickOnSave(self):
        '''
        usage: 选择保存
        '''
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 XJJSPC.text_save,
                                 XJJSPC.verify_timeout)

    def validAddRole(self):
        '''
        usage: 验证新建角色是否正确
        '''
        name = API().getTextByResourceId(self.testcase,
                                         self.driver,
                                         self.logger,
                                         XJJSPC.resource_id_name,
                                         XJJSPC.verify_timeout)

        API().assertEqual(self.testcase, self.logger, name, XJJSPC.account_name)