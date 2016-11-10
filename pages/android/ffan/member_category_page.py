# -*- coding: utf-8 -*-

from api.api import API
from pages.android.common.super_page import SuperPage
from pages.android.ffan.member_category_page_configs import MemberPageConfigs as MPC
from pages.logger import logger


class MemberPage(SuperPage):
    '''
    作者 陈诚
    首页=>广场=>会员
    '''
    def __init__(self, testcase, driver, logger):
        super(MemberPage, self).__init__(testcase, driver, logger);

    def validSelf(self):
        '''
        usage : 检查会员类目是否加载出来
        '''
        logger.info("Check 会员页面 begin")
        API().assertElementByResourceId(self.testcase, self.driver, self.logger,
                                        MPC.resource_id_title_tv_member_tv);
        logger.info("Check 会员页面 end")
