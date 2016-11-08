# -*- coding: utf-8 -*-

from api.api import API
from pages.android.common.super_page import SuperPage
from pages.android.shanghu.yuangongguanli_page_configs import YuanGongGuanLiPageConfigs as YGGLPC
from pages.android.shanghu.xinzengyuangong_page_configs import XinZengYuanGongPageConfigs as XZYGPC


class YuanGongGuanLiPage(SuperPage):
    '''
    作者 乔佳溪
    员工管理
    '''
    def __init__(self, testcase, driver, logger):
        super(YuanGongGuanLiPage, self).__init__(testcase, driver, logger)

    def validNormalStatus(self):
        '''
        usage : 进入到员工管理页（正常状态），验证正常状态
        '''
        API().getElementsByResourceId(self.testcase,
                                      self.driver,
                                      self.logger,
                                      YGGLPC.resource_id_name,
                                      YGGLPC.verify_timeout)
        API().getElementsByResourceId(self.testcase,
                                      self.driver,
                                      self.logger,
                                      YGGLPC.resource_id_store,
                                      YGGLPC.verify_timeout)
        API().getElementsByResourceId(self.testcase,
                                      self.driver,
                                      self.logger,
                                      YGGLPC.resource_id_role,
                                      YGGLPC.verify_timeout)
        API().getElementsByResourceId(self.testcase,
                                      self.driver,
                                      self.logger,
                                      YGGLPC.resource_id_phone,
                                      YGGLPC.verify_timeout)
        API().getElementsByResourceId(self.testcase,
                                      self.driver,
                                      self.logger,
                                      YGGLPC.resource_id_creator,
                                      YGGLPC.verify_timeout)
        API().getElementsByResourceId(self.testcase,
                                      self.driver,
                                      self.logger,
                                      YGGLPC.resource_id_create_time,
                                      YGGLPC.verify_timeout)

    def validFreezeStatus(self):
        '''
        usage : 进入到员工管理页（冻结状态），验证冻结状态
        '''
        API().getElementsByResourceId(self.testcase,
                                      self.driver,
                                      self.logger,
                                      YGGLPC.resource_id_name,
                                      YGGLPC.verify_timeout)
        API().getElementsByResourceId(self.testcase,
                                      self.driver,
                                      self.logger,
                                      YGGLPC.resource_id_store,
                                      YGGLPC.verify_timeout)
        API().getElementsByResourceId(self.testcase,
                                      self.driver,
                                      self.logger,
                                      YGGLPC.resource_id_role,
                                      YGGLPC.verify_timeout)
        API().getElementsByResourceId(self.testcase,
                                      self.driver,
                                      self.logger,
                                      YGGLPC.resource_id_phone,
                                      YGGLPC.verify_timeout)
        API().getElementsByResourceId(self.testcase,
                                      self.driver,
                                      self.logger,
                                      YGGLPC.resource_id_creator,
                                      YGGLPC.verify_timeout)
        API().getElementsByResourceId(self.testcase,
                                      self.driver,
                                      self.logger,
                                      YGGLPC.resource_id_create_time,
                                      YGGLPC.verify_timeout)

    def clickOnNormalStatus(self):
        '''
        usage: 点击正常状态
        '''
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 YGGLPC.text_normal_status,
                                 YGGLPC.verify_timeout)

    def clickOnFreezeStatus(self):
        '''
        usage: 点击冻结状态
        '''
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 YGGLPC.text_freeze_status,
                                 YGGLPC.verify_timeout)

    def clickOnAddMember(self):
        '''
        usage: 点击新增员工
        '''
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 YGGLPC.text_add_member,
                                 YGGLPC.verify_timeout)


    def validAddMember(self):
        '''
        usage : 验证新增员工
        '''
        name = API().getTextByResourceId(self.testcase,
                                         self.driver,
                                         self.logger,
                                         YGGLPC.resource_id_name,
                                         YGGLPC.verify_timeout)
        API().assertEqual(self.testcase, self.logger, name, XZYGPC.account_name)

        store = API().getTextByResourceId(self.testcase,
                                          self.driver,
                                          self.logger,
                                          YGGLPC.resource_id_store,
                                          YGGLPC.verify_timeout)
        API().assertEqual(self.testcase, self.logger, store, XZYGPC.text_store)

        role = API().getTextByResourceId(self.testcase,
                                         self.driver,
                                         self.logger,
                                         YGGLPC.resource_id_role,
                                         YGGLPC.verify_timeout)
        API().assertEqual(self.testcase, self.logger, role, XZYGPC.text_role)

        phone = API().getTextByResourceId(self.testcase,
                                          self.driver,
                                          self.logger,
                                          YGGLPC.resource_id_name,
                                          YGGLPC.verify_timeout)
        API().assertEqual(self.testcase, self.logger, phone, XZYGPC.account_phone)

        creator = API().getTextByResourceId(self.testcase,
                                            self.driver,
                                            self.logger,
                                            YGGLPC.resource_id_creator,
                                            YGGLPC.verify_timeout)
        API().assertEqual(self.testcase, self.logger, creator, XZYGPC.text_creator)

        API().getElementsByResourceId(self.testcase,
                                      self.driver,
                                      self.logger,
                                      YGGLPC.resource_id_create_time,
                                      YGGLPC.verify_timeout)

    def clickOnEdit(self):
        '''
        usage: 点击编辑
        '''
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 YGGLPC.text_edit,
                                 YGGLPC.verify_timeout)

    def clickOnFreeze(self):
        '''
        usage: 点击冻结
        '''
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 YGGLPC.text_freeze,
                                 YGGLPC.verify_timeout)
        API().waitBySeconds(2)
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 YGGLPC.text_freeze_confirm,
                                 YGGLPC.verify_timeout)

    def clickOnUnfreeze(self):
        '''
        usage: 点击解冻
        '''
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 YGGLPC.text_unfreeze,
                                 YGGLPC.verify_timeout)
        API().waitBySeconds(2)
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 YGGLPC.text_freeze_confirm,
                                 YGGLPC.verify_timeout)

    def getMemberInfo(self):
        '''
        usage: 获得员工信息
        '''
        memberInfo = API().getTextByResourceId(self.testcase,
                                  self.driver,
                                  self.logger,
                                  YGGLPC.resource_id_name,
                                  YGGLPC.verify_timeout)
        return memberInfo

    def validFreezeMemberInfo(self, memerInfo = "defult"):
        '''
        usage : 进入到员工管理页（冻结状态），验证冻结状态
        '''
        name = API().getElementsByResourceId(self.testcase,
                                             self.driver,
                                             self.logger,
                                             YGGLPC.resource_id_freeze_name,
                                             YGGLPC.verify_timeout)
        API().assertEqual(self.testcase, self.logger, name, memerInfo)

    def getFreezeMemberInfo(self):
        '''
        usage: 获得需要解冻的员工信息
        '''
        memberInfo = API().getTextByResourceId(self.testcase,
                                  self.driver,
                                  self.logger,
                                  YGGLPC.resource_id_freeze_name,
                                  YGGLPC.verify_timeout)
        return memberInfo

    def validNormalMemberInfo(self, memerInfo = "defult"):
        '''
        usage : 进入到员工管理页（正常状态），验证正常状态
        '''
        API().getElementsByText(self.testcase,
                                self.driver,
                                self.logger,
                                memerInfo,
                                YGGLPC.verify_timeout)

    def validFreezeData(self):
        '''
        usage : 验证冻结状态tab是否存在数据
        '''
        data = API().validElementByResourceId(self.driver,
                                              self.logger,
                                              YGGLPC.resource_id_freeze_name,
                                              YGGLPC.verify_timeout)
        return data

    def clickOnDelete(self):
        '''
        usage: 点击删除
        '''
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 YGGLPC.text_delete,
                                 YGGLPC.verify_timeout)
        API().waitBySeconds(2)
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 YGGLPC.text_freeze_confirm,
                                 YGGLPC.verify_timeout)

    def validDeleteMember(self, memberInfo = "default"):
        '''
        usage : 验证删除员工信息是否已删除
        '''
        deleteMember = API().validElementByText(self.driver,
                                                self.logger,
                                                memberInfo,
                                                YGGLPC.verify_timeout)

        if deleteMember:
            API().assertTrue(self.testcase, self.logger, False)

    def validEditMember(self, memberInfo = "default"):
        '''
        usage : 验证编辑后的员工信息
        '''
        API().getElementsByContainsText(self.testcase,
                                      self.driver,
                                      self.logger,
                                      memberInfo,
                                      YGGLPC.verify_timeout)
