# -*- coding:utf-8 -*-

from api.api import API
from pages.ios.common.superPage import SuperPage
from pages.ios.ffan.fei_fan_membership_page_configs import FeiFanMembershipPageConfigs
from pages.logger import logger

class FeiFanMembershipPage(SuperPage):
    '''
    作者 宋波
    首页=>我的飞凡=>我的会员卡包=>飞凡会员
    '''

    def __init__(self, testcase, driver, logger):
        '''
        Constructor
        '''

        super(FeiFanMembershipPage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        '''
        usage: verify whether the current page is correct page.
        '''
        logger.info("Check 我的会员卡包,飞凡会员 bengin")
        API().assertElementByName(self.testcase, self.driver, self.logger,
                                  FeiFanMembershipPageConfigs.resource_id_fei_fan_membership_title_st,
                                  FeiFanMembershipPageConfigs.assert_view_timeout)
        logger.info("Check 我的会员卡包,飞凡会员 end")
        API().screenShot(self.driver, "feiFanHuiYuan")


if __name__ == '__main__':
    pass
