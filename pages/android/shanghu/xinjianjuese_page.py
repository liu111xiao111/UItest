# -*- coding: utf-8 -*-

from api.api import API
from pages.android.common.super_page import SuperPage
from pages.android.shanghu.xinjianjuese_page_configs import XinJianJueSePageConfigs as XJJSPC
from api.logger import logger


class XinJianJueSePage(SuperPage):
    '''
    作者 乔佳溪
    角色管理
    '''
    def __init__(self, testcase, driver, logger):
        super(XinJianJueSePage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        '''
        usage: 验证新建角色页面
        '''
        logger.info("Check 新建角色页面 begin")
        API().assertElementByText(self.testcase,
                                               self.driver,
                                               self.logger,
                                               XJJSPC.text_new_role_title,
                                               XJJSPC.verify_timeout)
        logger.info("Check 新建角色页面 end")

    def clickOnFunctionalAutority(self):
        '''
        usage: 选择角色权限
        '''
        logger.info("Click 角色权限 begin")
        API().clickElementByResourceId(self.testcase,
                                       self.driver,
                                       self.logger,
                                       XJJSPC.resource_id_choose,
                                       XJJSPC.verify_timeout)
        API().waitBySeconds(2)

        API().screenShot(self.driver, "xuanZeJueSe")
        for i in range(10):
            xpath_checkbox_role_order = "//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[%s]/android.widget.RelativeLayout[1]/android.widget.CheckBox[1]" % (i+1)

            API().clickElementByXpath(self.testcase,
                                      self.driver,
                                      self.logger,
                                      xpath_checkbox_role_order,
                                      XJJSPC.verify_timeout)
        API().screenShot(self.driver, "xuanZeJueSe")
        logger.info("Click 角色权限 end")

    def validFunctionalAutority(self):
        '''
        usage: 验证功能权限
        '''
        logger.info("Check 功能权限 begin")
        roleStatus = API().getTextByResourceId(self.testcase,
                                               self.driver,
                                               self.logger,
                                               XJJSPC.resource_id_choose,
                                               XJJSPC.verify_timeout)
        API().assertEqual(self.testcase, self.logger, roleStatus, XJJSPC.account_role)
        logger.info("Check 功能权限 end")

    def inputRoleName(self):
        '''
        usage: 输入角色名
        '''
        logger.info("Input 角色名 begin")
        API().inputStringByResourceId(self.testcase,
                                      self.driver,
                                      self.logger,
                                      XJJSPC.resource_id_name,
                                      XJJSPC.account_name,
                                      XJJSPC.verify_timeout)
        logger.info("Input 角色名 end")

    def inputRoleInstruction(self):
        '''
        usage: 输入角色说明
        '''
        logger.info("Input 角色说明 begin")
        API().inputStringByResourceId(self.testcase,
                                      self.driver,
                                      self.logger,
                                      XJJSPC.resource_id_option,
                                      XJJSPC.text_instruction,
                                      XJJSPC.verify_timeout)
        logger.info("Input 角色说明 end")

    def clickOnSave(self):
        '''
        usage: 选择保存
        '''
        logger.info("Click 保存 begin")
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 XJJSPC.text_save,
                                 XJJSPC.verify_timeout)
        logger.info("Click 保存 end")

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
