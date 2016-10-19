# -*- coding:utf-8 -*-

from api.api import API
from pages.android.common.super_page import SuperPage
from pages.android.ffan.goods_details_page_configs import GoodsDetailsPageConfigs as GDPC


class GoodsDetailsPage(SuperPage):
    '''
    作者 宋波
    首页=>广场=>爱购物=>商品详情
    '''

    def __init__(self, testcase, driver, logger):
        super(GoodsDetailsPage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        '''
        usage: 验证商品详情页面
        '''
        API().assertElementByResourceId(self.testcase, self.driver, self.logger,
                                        GDPC.resource_id_reource_goods_details_title,
                                        GDPC.assert_view_timeout)

    def validKeywords(self, keywords):
        '''
        usage: 验证关键字
        '''
        API().assertElementByContentDesc(self.testcase, self.driver, self.logger,
                                         keywords,
                                         GDPC.assert_view_timeout)
