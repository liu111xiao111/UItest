# -*- coding: utf-8 -*-

from api.api import API
from utility.device_info_util import DeviceInfoUtil
from pages.android.common.super_page import SuperPage
from pages.android.ffan.food_category_page_configs import FoodCategoryPageConfigs as FCPC
from pages.logger import logger


class FoodCategoryPage(SuperPage):
    '''
    作者 刘涛
    首页＝>美食汇
    '''
    def __init__(self, testcase, driver, logger):
        super(FoodCategoryPage, self).__init__(testcase, driver, logger)

    '''
        usage: 美食主界面，根据美食种类button入口，检查美食主页面是否加载出来.
    '''
    def validFoodHomePage(self):
        '''
        usage: 美食主界面，根据美食种类button入口，检查美食主页面是否加载出来.
        '''
        logger.info("Check 美食汇页面 begin")
        API().assertElementByText(self.testcase,
                                  self.driver,
                                  self.logger,
                                  FCPC.view_text_tiltle,
                                  FCPC.verify_view_timeout)
        logger.info("Check 美食汇页面 end")

    def validRestaurant(self):
        '''
        usage : 进入美食子页面，根据餐饮的textview, 检查找餐饮页面是否加载出来.
        '''
        '''API().assertElementByResourceId(self.testcase,
                                        self.driver,
                                        self.logger,
                                        FCPC.resource_id_tv_restaurant_tv,
                                        FCPC.verify_view_timeout)'''
        API().assertElementByText(self.testcase,
                                  self.driver,
                                  self.logger,
                                  FCPC.view_text_tiltle,
                                  FCPC.verify_view_timeout)

    def validCoupon(self):
        '''
        usage : 进入优惠打折界面，根据餐饮的textview, 检查找优惠页面是否加载出来.
        '''
        API().assertElementByResourceId(self.testcase,
                                        self.driver,
                                        self.logger,
                                        FCPC.resource_id_tv_restaurant_tv,
                                        FCPC.verify_view_timeout)

    def validGrabCoupons(self):
        '''
        usage: 进入抢券界面，根据餐饮的textview, 检查抢券界面是否加载出来.
        '''
        API().assertElementByResourceId(self.testcase,
                                         self.driver,
                                         self.logger,
                                         FCPC.resource_id_back,
                                         FCPC.verify_view_timeout)

    def validModules(self):
        '''
        usage: 点击美食主界面的所有入口并验证
        '''
        '''restaurantList = API().getElementsByResourceId(self.testcase,
                                                       self.driver,
                                                       self.logger,
                                                       FCPC.resource_id_bt_restaurant_bt,
                                                       FCPC.verify_view_timeout)'''
        width = API().getWidthOfDevice(self.driver, self.logger)
        hight = API().getHeightOfDevice(self.driver, self.logger)
        for _ in range(3):
            API().scroll(self.driver, self.logger, width / 2, hight / 2, width / 2, hight / 3)
        API().clickElementByText(self.testcase,
                                     self.driver,
                                     self.logger,
                                     FCPC.text_all_food,
                                     FCPC.click_view_timeout)
        restaurantList = (u"火锅", u"面包甜点", u"小吃快餐", u"韩国料理", u"西餐",
                          u"江浙菜", u"川菜")
        for restaurant in restaurantList:
            logger.info("Check 入口(%s) begin" % restaurant)
            API().clickElementByText(self.testcase,
                                     self.driver,
                                     self.logger,
                                     restaurant,
                                     FCPC.click_view_timeout)
            API().waitBySeconds(3)
            self.validRestaurant()
            API().screenShot(self.driver, "meiShiHuiRuKou")
            self.clickOnStoreList(restaurant)
            self.validStoreList()
            API().screenShot(self.driver, "menDianXiangQing")
            API().clickBackKeyForAndroid(self.driver, self.logger)
            API().screenShot(self.driver, "meiShiHui")
#             if restaurant == u"火锅":
#                 API().clickElementByXpath(self.testcase,
#                                       self.driver,
#                                       self.logger,
#                                       FCPC.xpath_food_type_v5,
#                                       FCPC.click_view_timeout)
#             else:
            API().clickElementByXpath(self.testcase,
                                  self.driver,
                                  self.logger,
                                  FCPC.xpath_food_type_v5,
                                  FCPC.click_view_timeout)
            API().screenShot(self.driver, "meiShiHuiRuKou")
            logger.info("Check 入口(%s) end" % restaurant)

    def validModulesForStability(self, outsideLoop=1, insideLoop=1):
        '''
        usage: 点击美食主界面的所有入口并验证
        '''
#         width = API().getWidthOfDevice(self.driver, self.logger)
#         hight = API().getHeightOfDevice(self.driver, self.logger)
#         for _ in range(2):
#             API().scroll(self.driver, self.logger, width / 2, hight / 2, width / 2, hight / 3)
        API().clickElementByText(self.testcase,
                                     self.driver,
                                     self.logger,
                                     FCPC.text_all_food,
                                     FCPC.click_view_timeout)
        restaurantList = (u"火锅", u"面包甜点", u"小吃快餐", u"韩国料理", u"西餐",
                          u"江浙菜", u"咖啡厅")
        i = 4
        for restaurant in restaurantList:
            logger.info("Check 入口(%s) begin" % restaurant)
            API().clickElementByText(self.testcase,
                                     self.driver,
                                     self.logger,
                                     restaurant,
                                     FCPC.click_view_timeout)
            API().waitBySeconds(3)
            self.validRestaurant()
            API().screenShotForStability(self.driver, "meishihui", outsideLoop, insideLoop, str(i))
            self.clickOnStoreList(restaurant)
            self.validStoreList()
            API().screenShotForStability(self.driver, "meishihui", outsideLoop, insideLoop, str(i+1))
            API().clickBackKeyForAndroid(self.driver, self.logger)
            API().screenShotForStability(self.driver, "meishihui", outsideLoop, insideLoop, str(i+2))
            API().clickElementByXpath(self.testcase,
                                      self.driver,
                                      self.logger,
                                      FCPC.xpath_food_type_v5,
                                      FCPC.click_view_timeout)
            API().screenShotForStability(self.driver, "meishihui", outsideLoop, insideLoop, str(i+3))
            i = i + 4
            logger.info("Check 入口(%s) end" % restaurant)

    def clickOnCoupon(self):
        '''
        usage : 点击优惠打折
        '''
        API().clickElementByResourceId(self.testcase,
                                       self.driver,
                                       self.logger,
                                       FCPC.resource_id_bt_coupon_bt,
                                       FCPC.click_view_timeout)

    def clickOnGrabCoupons(self):
        '''
        usage : 点击抢券
        '''
        logger.info("Click 抢券 begin")
#         version = DeviceInfoUtil().getBuildVersion()
#         if int(version.split(".")[0]) < 5:
#         width = API().getWidthOfDevice(self.driver, self.logger)
#         hight = API().getHeightOfDevice(self.driver, self.logger)
#         for _ in range(3):
#             API().scroll(self.driver, self.logger, width / 2, hight / 2, width / 2, hight / 3)
#         API().clickElementByResourceId(self.testcase,
#                                        self.driver,
#                                        self.logger,
#                                        FCPC.resource_id_bt_grab_bt,
#                                        FCPC.click_view_timeout)
#         else:
#             API().clickElementByText(self.testcase,
#                                            self.driver,
#                                            self.logger,
#                                            FCPC.text_grab_bt,
#                                            FCPC.click_view_timeout)
        API().clickElementByXpath(self.testcase,
                                  self.driver,
                                  self.logger,
                                  FCPC.xpath_sales,
                                  FCPC.click_view_timeout)
        logger.info("Click 抢券 begin")

    def clickOnGrabCouponsForStability(self):
        '''
        usage : 点击抢券
        '''
        logger.info("Click 抢券 begin")
#         version = DeviceInfoUtil().getBuildVersion()
#         if int(version.split(".")[0]) < 5:
        width = API().getWidthOfDevice(self.driver, self.logger)
        hight = API().getHeightOfDevice(self.driver, self.logger)
        for _ in range(6):
            API().scroll(self.driver, self.logger, width / 2, hight / 2, width / 2, hight / 3)
        API().clickElementByResourceId(self.testcase,
                                       self.driver,
                                       self.logger,
                                       FCPC.resource_id_bt_grab_bt,
                                       FCPC.click_view_timeout)
#         else:
#             API().clickElementByText(self.testcase,
#                                            self.driver,
#                                            self.logger,
#                                            FCPC.text_grab_bt,
#                                            FCPC.click_view_timeout)
        logger.info("Click 抢券 begin")

    def clickOnStoreList(self, restaurant):
        '''
        usage : 点击门店列表
        '''
        logger.info("Click 门店列表 begin")
#         if restaurant == u"火锅":
#         API().clickElementByXpath(self.testcase,
#                                   self.driver,
#                                   self.logger,
#                                   FCPC.xpath_store_list,
#                                   FCPC.click_view_timeout)
#         else:
        API().clickElementByXpath(self.testcase,
                                  self.driver,
                                  self.logger,
                                  FCPC.xpath_store_list_v5,
                                  FCPC.click_view_timeout)
        logger.info("Click 门店列表 end")

    def validStoreList(self):
        '''
        usage: 进入抢券界面，根据餐饮的textview, 检查抢券界面是否加载出来.
        '''
        logger.info("Check 门店列表 begin")
        API().assertElementByText(self.testcase,
                                         self.driver,
                                         self.logger,
                                         FCPC.text_store_details,
                                         FCPC.verify_view_timeout)
        logger.info("Check 门店列表 end")

    def clickOnLePay(self):
        '''
        usage : 点击乐付
        '''
        API().clickElementByXpath(self.testcase,
                                  self.driver,
                                  self.logger,
                                  FCPC.xpath_maidan,
                                  FCPC.click_view_timeout)
