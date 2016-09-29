# -*- coding: utf-8 -*-

from api.api import API
from pages.android.common.super_page import SuperPage
from pages.android.ffan.famous_details_category_page_configs import FamousDetailsCategoryPageConfigs as FDCPC


class FamousDetailsCategoryPage(SuperPage):
    '''
    作者 刘涛
    首页＝>品牌(推荐)=>详情页
    '''
    def __init__(self,testcase,driver,logger):
        super(FamousDetailsCategoryPage, self).__init__(testcase, driver,  logger);

    def validSelf(self):
        '''
        usage : 验证推荐详情页
        '''
        texts = [FDCPC.text_dashboardpage, FDCPC.text_store]
        API().assertElementsByTexts(self.testcase,
                                    self.driver,
                                    self.logger,
                                    texts,
                                    FDCPC.assert_view_timeout)
