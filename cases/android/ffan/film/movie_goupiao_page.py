# -*- coding:utf-8 -*-

from api.api import API
from pages.android.common.super_page import SuperPage

from cases.android.ffan.film.movie_goupiao_page_configs import moviegoupiaoConfigs as MGPPC
from pages.logger import logger
from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time


class Moviegoupiaopage(SuperPage):
    '''
    作者 刘潇
    首页=>电影=>电影模块操作
    '''
    def __init__(self, testcase, driver, logger):
        super(Moviegoupiaopage, self).__init__(testcase, driver, logger)



    def validSelf(self):
        '''
        usage : 检查是否到了订单提交页面
        '''
        logger.info("Check 飞凡收银台 begin")
        API().assertElementByResourceId(self.testcase,
                                        self.driver,
                                        self.logger,
                                        MGPPC.resource_id_iv_dingdanqueren,
                                        90)
        logger.info("Check 飞凡收银台 end")

    def clickchengshi(self):
        '''
        usage: 点击左上角“城市"按钮
        '''
        logger.info("Click 切换城市 begin")
        API().clickElementByResourceId(self.testcase,
                                 self.driver,
                                 self.logger,
                                 MGPPC.resource_id_iv_chengshi,
                                 MGPPC.click_on_button_timeout)
        logger.info("Click 切换城市 end")



    def clickanyang(self):
        '''
        usage: 点击安阳市
        '''
        logger.info("Click 选择安阳市 begin")
        API().clickElementByResourceId(self.testcase,
                                 self.driver,
                                 self.logger,
                                 MGPPC.resource_id_iv_anyang,
                                 MGPPC.click_on_button_timeout)
        logger.info("Click 选择安阳市 end")

    def clickonbeijing(self):
        '''
        usage: 点击北京市
        '''
        logger.info("Click 选择北京市 begin")
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 MGPPC.text_movie_beijingshi_button,
                                 MGPPC.click_on_button_timeout)
        logger.info("Click 选择北京市 end")


    def clickyingyuan(self):
        '''
        usage: 点击影院按钮
        '''
        logger.info("Click 点击影院按钮 begin")
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 MGPPC.text_movie_yingyuan_button,
                                 MGPPC.click_on_button_timeout)
        logger.info("Click 点击影院按钮 end")




    def clickOnxuanzuo(self):
        '''
        usage: 点击“选座"按钮
        '''
        logger.info("Click 点击‘选座’按钮 begin")
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 MGPPC.text_movie_xuanzuo_button,
                                 MGPPC.click_on_button_timeout)
        logger.info("Click 点击‘选座’按钮 end")

    def clickOnyingpian(self):
        '''
        usage: 点击“影院"列表，进入影院详情
        '''
        logger.info("Click 点击‘影院’列表 begin")
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 MGPPC.text_movie_yingyuan_button,
                                 MGPPC.click_on_button_timeout)
        logger.info("Click 点击‘影院’列表 end")

    def clickonpingpai(self):
        '''
        usage: 点击“品牌"列表，展示所有影院
        '''
        logger.info("Click 点击‘品牌’按钮 begin")
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 MGPPC.text_movie_pingpai_button,
                                 MGPPC.click_on_button_timeout)
        logger.info("Click 点击‘品牌’按钮 end")

    def clickhengdian(self):
        '''
        usage: 点击“横店电影院"列表，展示横店电影院
        '''
        logger.info("Click 点击‘横店电影城’按钮 begin")
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 MGPPC.text_movie_hengdian_button,
                                 MGPPC.click_on_button_timeout)
        logger.info("Click 点击‘横店电影城’按钮 end")

    def clickonqita(self):
        '''
        usage: 点击“横店电影院"列表，展示横店电影院
        '''
        logger.info("Click 点击‘其他’按钮 begin")
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 MGPPC.text_movie_qita_button,
                                 MGPPC.click_on_button_timeout)
        logger.info("Click 点击‘其他’按钮 end")

    def clickonquanyeyingyuan(self):
        '''
        usage: 点击“劝业影院"列表，展示劝业影院
        '''
        logger.info("Click 点击‘劝业影院’按钮 begin")
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 MGPPC.text_movie_quanyeyingyuan_button,
                                 MGPPC.click_on_button_timeout)
        logger.info("Click 点击‘劝业影院’按钮 end")

    def clickyingyuanxiangqing(self):
        '''
        usage: 在列表页点击电影院，进入影院详情
        '''
        logger.info("Click 点击电影院 begin")
        API().clickElementByResourceId(self.testcase,
                                 self.driver,
                                 self.logger,
                                 MGPPC.resource_id_iv_yingyuan_jiage,
                                 MGPPC.click_on_button_timeout)
        logger.info("Click 点击电影院 end")

    def clickOnbuy(self):
        '''
        usage: 在影院详情中，点击选座/特惠按钮，跳转选座详情页
        '''
        logger.info("Click 点击选座按钮 begin")
        API().clickElementByResourceId(self.testcase,
                                 self.driver,
                                 self.logger,
                                 MGPPC.resource_id_iv_buy,
                                 MGPPC.click_on_button_timeout)
        logger.info("Click 点击选座按钮 end")






    def clickxuanhaole(self):
        '''
        usage: 在影院详情中，点击选好了按钮，跳转下单页
        '''
        logger.info("Click 点击选好了按钮 begin")
        API().clickElementByResourceId(self.testcase,
                                 self.driver,
                                 self.logger,
                                 MGPPC.resource_id_iv_xuanhaole,
                                 MGPPC.click_on_button_timeout)
        logger.info("Click 点击选好了按钮 end")

    def clickfanhuishouye(self):
        '''
        usage: 返回首页
        '''
        logger.info("Click 返回首页 begin")
        API().clickElementByResourceId(self.testcase,
                                 self.driver,
                                 self.logger,
                                 MGPPC.resource_id_iv_fanhuishouye,
                                 MGPPC.click_on_button_timeout)
        logger.info("Click 返回首页 end")

    def clicktijaiodingdan(self):
        '''
        usage: 点击提交订单按钮
        '''
        logger.info("Click 点击提交订单按钮 begin")
        API().clickElementByResourceId(self.testcase,
                                 self.driver,
                                 self.logger,
                                 MGPPC.resource_id_iv_tijiaodingdan,
                                 MGPPC.click_on_button_timeout)
        logger.info("Click 点击提交订单按钮 end")


    def clickxuanzuo(self):
        '''
        usage: 选择座位
        '''
        logger.info("Click 选择座位 begin")
        API().clickElementByResourceId(self.testcase,
                                 self.driver,
                                 self.logger,
                                 MGPPC.resource_id_iv_xuanzuo,
                                 MGPPC.click_on_button_timeout)
        logger.info("Click 选择座位 end")

    def clickfanhui(self):
        '''
        usage: 返回上一层
        '''
        logger.info("Click 返回按钮 begin")
        API().clickElementByResourceId(self.testcase,
                                 self.driver,
                                 self.logger,
                                 MGPPC.resource_id_iv_fanhui,
                                 MGPPC.click_on_button_timeout)
        logger.info("Click 返回按钮 end")

    def validbeijing(self):
        '''
        usage : 检查是否切换回了北京市
        '''
        logger.info("Check 北京市 begin")
        API().assertElementByText(self.testcase,
                                        self.driver,
                                        self.logger,
                                        MGPPC.text_movie_beijingshi_button,
                                        90)
        logger.info("Check 北京市 end")


    def validcity(self):
        '''
        usage: 验证城市按钮
        '''
        logger.info("check 验证切换城市按钮 begin")
        API().validElementByResourceId(self.driver,
                                       self.logger,
                                 MGPPC.resource_id_iv_chengshi,
                                 15)
        logger.info("check 验证切换城市按钮 end")


    def clickBackKey(self):
        '''
        usage: 验证城市按钮
        '''
        logger.info("click 点击系统返回按钮 begin")
        API().clickBackKeyForAndroid(self.driver,
                                       self.logger)
        logger.info("click 点击系统返回按钮 end")


    def inputchengshi(self):
        '''
        usage: 输入城市名
        '''
        logger.info("Input 输入城市名 begin")
        API().inputStringByResourceId(self.testcase,
                                      self.driver,
                                      self.logger,
                                      MGPPC.resource_id_iv_sousuochengshi,
                                      MGPPC.chengshi_name,
                                      10)
        logger.debug(MGPPC.chengshi_name)
        logger.info("Input 输入城市名 end")


    def clickonbaotoushi(self):
        '''
        usage: 选择包头市
        '''
        logger.info("Click 选择包头市 begin")
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 MGPPC.text_baotoushi,
                                 MGPPC.click_on_button_timeout)
        logger.info("Click 选择包头市 end")