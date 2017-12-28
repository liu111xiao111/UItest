# -*- coding:utf-8 -*-
import random

from api.api import API
from pages.android.common.super_page import SuperPage
# 从之前的configs包中导入configs文件，并命名为DRG
from cases.android.ffan.film.movieReyingPurchase_configs import dianyingReyingGoupiao_configs as DRG
from pages.logger import logger


class dianyingReyingGoupiaoSeat_page(SuperPage):
    '''
    作者：吴聪
    位置：首页=>影片=>正在热映=>选择影城=>场次列表=>座位图
    '''
    def __init__(self,testcase,driver,logger):
        super(dianyingReyingGoupiaoSeat_page, self).__init__(testcase, driver, logger)

    def validSeat(self):
        '''
        usage: 验证座位图
        '''
        logger.info("Check 座位图 begin")
        API().assertElementByResourceId(self.testcase,
                                        self.driver,
                                        self.logger,
                                        DRG.resource_id_seat_title,
                                        DRG.assert_button_timeout)
        API().assertElementByResourceId(self.testcase,
                                        self.driver,
                                        self.logger,
                                        DRG.resource_id_movie_seat_info,
                                        DRG.assert_button_timeout)
        logger.info("Check 座位图 end")

    def clickSeatSubmit(self):
        '''
        usage: 先选择座位，再点击选好了
        '''
        logger.info("Click 选择座位 begin")
        API().clickElementByResourceId(self.testcase,
                                       self.driver,
                                       self.logger,
                                       DRG.resource_id_seat_select,
                                       DRG.click_on_button_timeout)
        n = 1
        while n < 20:
            API().clickElementByResourceId(self.testcase,
                                           self.driver,
                                           self.logger,
                                           DRG.resource_id_seat_submit,
                                           DRG.click_on_button_timeout)
            isSubmit = API().validElementByResourceId(self.driver,
                                                      self.logger,
                                                      DRG.resource_id_confirm_goods,
                                                      5)
            if isSubmit:
                logger.info("选择座位成功")
                break
            else:
                seatprice = API().getTextByResourceId(self.testcase,
                                                      self.driver,
                                                      self.logger,
                                                      DRG.resource_id_seat_price,
                                                      DRG.assert_button_timeout)
                print(seatprice)
                width = API().getWidthOfDevice(self.driver, self.logger) / 2
                height = API().getHeightOfDevice(self.driver, self.logger) / 2
                if seatprice == "0.0":
                    print("this is a seat block")
                    self.seatMove(width, height)
                else:
                    print("this is a seat irregular")
                    API().clickElementByResourceId(self.testcase,
                                                   self.driver,
                                                   self.logger,
                                                   DRG.resource_id_seat_select,
                                                   DRG.click_on_button_timeout)
                    self.seatMove(width, height)
            n += 1
        logger.info("Click 选择座位 end")

    # 抽象出来座位偏移的方法
    def seatMove(self, width, height):
        logger.info("当前座位未选中或选择不规则座位，滑动屏幕")
        wp = random.random() + 0.7
        hp = random.random() + 0.7
        API().scroll(self.driver, self.logger, width, height, width*wp, height*hp)
        logger.info("重新选择座位")
        API().clickElementByResourceId(self.testcase,
                                       self.driver,
                                       self.logger,
                                       DRG.resource_id_seat_select,
                                       DRG.click_on_button_timeout)

