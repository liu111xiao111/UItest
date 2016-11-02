# -*- coding: utf-8 -*-

from api.api import API
from pages.android.common.super_page import SuperPage
from pages.android.shanghu.dengluxinxi_page_configs import DengLuXinXiPageConfigs as DLXXPC


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
        user = API().getTextByResourceId(self.testcase,
                                        self.driver,
                                        self.logger,
                                        DLXXPC.resource_id_user,
                                        DLXXPC.assert_timeout)
        API().assertEqual(self.testcase, self.logger, user, DLXXPC.text_user)

        phone = API().getTextByResourceId(self.testcase,
                                        self.driver,
                                        self.logger,
                                        DLXXPC.resource_id_phone,
                                        DLXXPC.assert_timeout)
        API().assertEqual(self.testcase, self.logger, phone, DLXXPC.test_phone)

        identity = API().getTextByResourceId(self.testcase,
                                        self.driver,
                                        self.logger,
                                        DLXXPC.resource_id_identity,
                                        DLXXPC.assert_timeout)
        API().assertEqual(self.testcase, self.logger, identity, DLXXPC.test_identity)


        businessman = API().getTextByResourceId(self.testcase,
                                        self.driver,
                                        self.logger,
                                        DLXXPC.resource_id_businessman,
                                        DLXXPC.assert_timeout)
        API().assertEqual(self.testcase, self.logger, businessman, DLXXPC.test_businessman)
