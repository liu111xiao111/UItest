# -*- coding: utf-8 -*-

from api.api import API
from pages.ios.common.superPage import SuperPage
from pages.ios.ffan.shopping_details_category_page_configs import ShoppingDetailsCategoryPageConfigs as SDCPC
from pages.logger import logger

class ShoppingDetailsCategoryPage(SuperPage):
    '''
    作者 刘涛
    首页=>购物=>详情页
    '''

    def __init__(self, testcase, driver, logger):
        super(ShoppingDetailsCategoryPage, self).__init__(testcase=testcase , driver=driver, logger=logger);

    def validSelf(self):
        '''
        usage : 判断商品详情页中“首页”、“商品”、“门店”显示是否正确
        '''
        logger.info("Check 商品 begin")
#         API().assertElementByName(testCase=self.testcase,
#                                   driver=self.driver,
#                                   logger=self.logger,
#                                   name=ShoppingDetailsCategoryPageConfigs.text_dashboard)
        API().assertElementByName(self.testcase, self.driver, self.logger,
                                  SDCPC.name_goods_st, SDCPC.click_on_button_timeout)

#         API().assertElementByName(testCase=self.testcase,
#                                   driver=self.driver,
#                                   logger=self.logger,
#                                   name=ShoppingDetailsCategoryPageConfigs.text_store)
        logger.info("Check 商品 end")
        API().screenShot(self.driver, "shangPinXiangQing")

    def clickOnMyFavorite(self):
        '''
        usage: Click on the my favorite.
        '''

#         API().clickElementByName(self.testcase, self.driver, self.logger,
#                                   SDCPC.name_my_favorite_st, SDCPC.click_on_button_timeout)

        API.clickElementByName(self.testcase, self.driver, self.logger,
                               SDCPC.xpath_my_favorite_st, SDCPC.click_on_button_timeout)

    def clickOnShop(self):
        '''
        usage: Click on the shop.
        '''

        self.scrollAsScreenPercent(0.5, 0.6, 0.5, 0.3)
        API().clickElementByXpath(self.testcase, self.driver, self.logger,
                                  SDCPC.xpath_shop_name_st, SDCPC.click_on_button_timeout)

if __name__ == '__main__':
    pass;
