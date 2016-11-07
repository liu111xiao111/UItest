# -*- coding: utf-8 -*-

from api.api import API
from pages.android.common.super_page import SuperPage
from pages.android.shanghu.jueseguanli_page_configs import JueSeGuanLiPageConfigs as JSGLPC


class JueSeGuanLiPage(SuperPage):
    '''
    作者 乔佳溪
    角色管理
    '''
    def __init__(self, testcase, driver, logger):
        super(JueSeGuanLiPage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        '''
        usage : 进入到员工管理页（正常状态），验证正常状态
        '''
        API().getElementsByResourceId(self.testcase,
                                      self.driver,
                                      self.logger,
                                      JSGLPC.resource_id_role,
                                      JSGLPC.verify_timeout)
        API().getElementsByResourceId(self.testcase,
                                      self.driver,
                                      self.logger,
                                      JSGLPC.resource_id_creator,
                                      JSGLPC.verify_timeout)
        API().getElementsByResourceId(self.testcase,
                                      self.driver,
                                      self.logger,
                                      JSGLPC.resource_id_create_time,
                                      JSGLPC.verify_timeout)

    def clickOnAddRole(self):
        '''
        usage: 点击新增角色
        '''
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 JSGLPC.text_add_role,
                                 JSGLPC.verify_timeout)
