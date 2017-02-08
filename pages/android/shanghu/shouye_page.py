# -*- coding: utf-8 -*-

from api.api import API
from pages.android.common.super_page import SuperPage
from pages.android.shanghu.shouye_page_configs import ShouYePageConfigs as SYPC
from pages.android.shanghu.shezhi_page import SheZhiPage
from pages.logger import logger


class ShouYePage(SuperPage):
    '''
    作者 乔佳溪
    首页
    '''
    def __init__(self, testcase, driver, logger):
        super(ShouYePage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        '''
        usage : 进入首页,检查标题
        '''
        logger.info("Check 首页 begin")
        title = API().getTextByResourceId(self.testcase,
                                        self.driver,
                                        self.logger,
                                        SYPC.resource_id_title,
                                        SYPC.verify_timeout)

        API().assertGreaterEqual(self.testcase, self.logger, title, SYPC.text_store)
        logger.info("Check 首页 end")

    def clickOnUser(self):
        '''
        usage: 点击用户
        '''
        logger.info("Click 用户 icon begin")
        API().clickElementByResourceId(self.testcase,
                                       self.driver,
                                       self.logger,
                                       SYPC.resource_id_user,
                                       SYPC.verify_timeout)
        logger.info("Click 用户 icon end")

    def validLogin(self):
        '''
        usage : 验证首页是否登录
        '''
        logger.info("Check 是否登录 begin")
        rtn = API().validElementByResourceId(self.driver,
                                             self.logger,
                                             SYPC.resource_id_title,
                                             SYPC.verify_timeout)
        if rtn:
            title = API().getTextByResourceId(self.testcase,
                                              self.driver,
                                              self.logger,
                                              SYPC.resource_id_title,
                                              SYPC.verify_timeout)
            if title != SYPC.text_store:
                self.clickOnSetting()
                SheZhiPage.clickOnLogout(self)
                rtn = False
        logger.info("Check 是否登录 end")
        return rtn

    def clickOnSetting(self):
        '''
        usage: 点击设置
        '''
        logger.info("Click 设置 begin")
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 SYPC.text_setting,
                                 SYPC.verify_timeout)
        logger.info("Click 设置 end")

    def clickOnMemberManager(self):
        '''
        usage: 点击员工管理
        '''
        logger.info("Click 员工管理 begin")
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 SYPC.text_member_manager,
                                 SYPC.verify_timeout)
        logger.info("Click 员工管理 end")

    def clickOnRoleManager(self):
        '''
        usage: 点击角色管理
        '''
        logger.info("Click 角色管理 begin")
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 SYPC.text_role_manager,
                                 SYPC.verify_timeout)
        logger.info("Click 角色管理 end")

    def clickOnOrderManager(self):
        '''
        usage: 点击订单管理
        '''
        logger.info("Click 订单管理 begin")
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 SYPC.text_order_manager,
                                 SYPC.verify_timeout)
        logger.info("Click 订单管理 end")

    def clickOnLefuBill(self):
        '''
        usage: 点击乐付账单
        '''
        logger.info("Click 乐付账单 begin")
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 SYPC.text_lefu_bill,
                                 SYPC.verify_timeout)
        logger.info("Click 乐付账单 end")

    def clickOnShangXueYuan(self):
        '''
        usage: 点击商学院
        '''
        logger.info("Click 商学院 begin")
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 SYPC.text_business_college,
                                 SYPC.verify_timeout)
        logger.info("Click 商学院 end")

    def clickOnXiaoXiZhongXin(self):
        '''
        usage: 点击消息
        '''
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 SYPC.text_message,
                                 SYPC.verify_timeout)

    def clickOnShangPinGuanLi(self):
        '''
        usage: 点击商品管理
        '''
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 SYPC.text_goods_manager,
                                 SYPC.verify_timeout)
