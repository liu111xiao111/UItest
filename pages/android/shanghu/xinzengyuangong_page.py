# -*- coding: utf-8 -*-

from api.api import API
from pages.android.common.super_page import SuperPage
from pages.android.shanghu.xinzengyuangong_page_configs import XinZengYuanGongPageConfigs as XZYGPC
from pages.logger import logger


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
        logger.info("Click 选择角色操作 begin")
        logger.info("Click 选择角色 begin")
        API().clickElementByResourceId(self.testcase,
                                       self.driver,
                                       self.logger,
                                       XZYGPC.resource_id_choose,
                                       XZYGPC.verify_timeout)
        API().waitBySeconds(2)
        API().screenShot(self.driver, "xuanZeJueSe")
        logger.info("Click 选择角色 end")
        logger.info("Click 游客角色 begin")
        API().clickElementByText(self.testcase,
                                       self.driver,
                                       self.logger,
                                       XZYGPC.text_role,
                                       XZYGPC.verify_timeout)
        API().screenShot(self.driver, "xuanZeJueSe")
        logger.info("Click 游客角色 end")
        logger.info("Click 确定 begin")
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 XZYGPC.text_confirm,
                                 XZYGPC.verify_timeout)
        logger.info("Click 确定 end")
        logger.info("Click 选择角色操作 end")

    def inputUserName(self):
        '''
        usage: 输入用户名
        '''
        logger.info("Input 用户名 begin")
        API().inputStringByResourceId(self.testcase,
                                      self.driver,
                                      self.logger,
                                      XZYGPC.resource_id_name,
                                      XZYGPC.account_name,
                                      XZYGPC.verify_timeout)
        logger.info("Input 用户名 end")

    def inputPhone(self):
        '''
        usage: 输入手机号
        '''
        logger.info("Input 手机号 begin")
        API().inputStringByResourceId(self.testcase,
                                      self.driver,
                                      self.logger,
                                      XZYGPC.resource_id_phone,
                                      XZYGPC.account_phone,
                                      XZYGPC.verify_timeout)
        logger.info("Input 手机号 end")

    def clickOnSave(self):
        '''
        usage: 选择保存
        '''
        logger.info("Click 保存 begin")
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 XZYGPC.text_save,
                                 XZYGPC.verify_timeout)
        logger.info("Click 保存 end")

    def clickOnChangeRole(self):
        '''
        usage: 变更角色
        '''
        logger.info("Click 角色 radio button begin")
        API().clickElementByResourceId(self.testcase,
                                       self.driver,
                                       self.logger,
                                       XZYGPC.resource_id_choose,
                                       XZYGPC.verify_timeout)

        API().waitBySeconds(3)

        API().screenShot(self.driver, "xuanZeJueSe")
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
        API().screenShot(self.driver, "xuanZeJueSe")
        logger.info("Click 角色 radio button end")

    def inputEditName(self):
        '''
        usage: 编辑姓名
        '''
        logger.info("Input 姓名 begin")
        name = API().getTextByResourceId(self.testcase,
                                         self.driver,
                                         self.logger,
                                         XZYGPC.resource_id_name,
                                         XZYGPC.verify_timeout)

        name = name + "ceshi"
        if len(name) > 20:
            name = "ceshi"
        API().inputStringByResourceId(self.testcase,
                                      self.driver,
                                      self.logger,
                                      XZYGPC.resource_id_name,
                                      name,
                                      XZYGPC.verify_timeout)
        logger.info("Input 姓名 end")
