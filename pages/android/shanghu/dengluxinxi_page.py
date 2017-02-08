# -*- coding: utf-8 -*-

from api.api import API
from pages.android.common.super_page import SuperPage
from pages.android.shanghu.dengluxinxi_page_configs import DengLuXinXiPageConfigs as DLXXPC
from pages.logger import logger


class DengLuXinXiPage(SuperPage):
    '''
    作者 乔佳溪
    登录信息
    '''
    def __init__(self, testcase, driver, logger):
        super(DengLuXinXiPage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        '''
        usage : 进入到登录信息页
        '''
        logger.info("Check 登录信息页面 begin")
        logger.info("Check 姓名 begin")
        user = API().getTextByResourceId(self.testcase,
                                        self.driver,
                                        self.logger,
                                        DLXXPC.resource_id_user,
                                        DLXXPC.assert_timeout)
        API().assertEqual(self.testcase, self.logger, user, DLXXPC.text_user)
        logger.info("Check 姓名 end")

        logger.info("Check 手机号 begin")
        phone = API().getTextByResourceId(self.testcase,
                                        self.driver,
                                        self.logger,
                                        DLXXPC.resource_id_phone,
                                        DLXXPC.assert_timeout)
        API().assertEqual(self.testcase, self.logger, phone, DLXXPC.test_phone)
        logger.info("Check 手机号 end")

        logger.info("Check 登录身份 begin")
        identity = API().getTextByResourceId(self.testcase,
                                        self.driver,
                                        self.logger,
                                        DLXXPC.resource_id_identity,
                                        DLXXPC.assert_timeout)
        API().assertEqual(self.testcase, self.logger, identity, DLXXPC.test_identity)
        logger.info("Check 登录身份 end")

        logger.info("Check 所属商户 begin")
        businessman = API().getTextByResourceId(self.testcase,
                                        self.driver,
                                        self.logger,
                                        DLXXPC.resource_id_businessman,
                                        DLXXPC.assert_timeout)
        API().assertEqual(self.testcase, self.logger, businessman, DLXXPC.test_businessman)
        logger.info("Check 所属商户 end")
        logger.info("Check 登录信息页面 end")

    def validSelfNewMember(self):
        '''
        usage : 进入到登录信息页
        '''
        logger.info("Check 登录信息页面 begin")
        logger.info("Check 用工姓名 begin")
        user = API().getTextByResourceId(self.testcase,
                                        self.driver,
                                        self.logger,
                                        DLXXPC.resource_id_user_new_member,
                                        DLXXPC.assert_timeout)
        API().assertEqual(self.testcase, self.logger, user, DLXXPC.text_user_new_member)
        logger.info("Check 用工姓名 end")
        logger.info("Check 手机号 begin")
        phone = API().getTextByResourceId(self.testcase,
                                        self.driver,
                                        self.logger,
                                        DLXXPC.resource_id_phone_user_new_member,
                                        DLXXPC.assert_timeout)
        API().assertEqual(self.testcase, self.logger, phone, DLXXPC.test_phone_new_member)
        logger.info("Check 手机号 end")
        logger.info("Check 身份 begin")
        identity = API().getTextByResourceId(self.testcase,
                                        self.driver,
                                        self.logger,
                                        DLXXPC.resource_id_identity_new_member,
                                        DLXXPC.assert_timeout)
        API().assertEqual(self.testcase, self.logger, identity, DLXXPC.test_identity_new_member)
        logger.info("Check 身份 end")
        logger.info("Check 商铺 begin")
        store = API().getTextByResourceId(self.testcase,
                                        self.driver,
                                        self.logger,
                                        DLXXPC.resource_id_store_new_member,
                                        DLXXPC.assert_timeout)
        API().assertEqual(self.testcase, self.logger, store, DLXXPC.test_store_new_member)
        logger.info("Check 商铺 end")
        logger.info("Check 所属广场 begin")
        square = API().getTextByResourceId(self.testcase,
                                        self.driver,
                                        self.logger,
                                        DLXXPC.resource_id_square_new_member,
                                        DLXXPC.assert_timeout)
        API().assertEqual(self.testcase, self.logger, square, DLXXPC.test_square_new_member)
        logger.info("Check 所属广场 end")
        logger.info("Check 登录信息页面 end")

