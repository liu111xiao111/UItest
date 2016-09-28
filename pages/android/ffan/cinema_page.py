# -*- coding:utf-8 -*-

from api.api import API
from pages.android.common.super_page import SuperPage
from pages.android.ffan.cinema_page_configs import CinemaPageConfigs as CPC


class CinemaPage(SuperPage):
    '''
    作者 陈诚
    首页=>电影=>电影详细信息=>电影院界面
    '''

    def __init__(self, testcase, driver, logger):
        super(CinemaPage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        '''
        usage: 验证电影院界面
        '''

        API().assertElementByResourceId(self.testcase,
                                        self.driver,
                                        self.logger,
                                        CPC.resource_id_cinema_title,
                                        CPC.assert_view_timeout)

    def clickOnBuyTicket(self):
        '''
        usage: 点击买票
        '''

        API().waitBySeconds(5)
        tempText = API().getTextByResourceId(self.testcase,
                                             self.driver,
                                             self.logger, 
                                             CPC.resource_id_movie_name_button,
                                             CPC.click_on_button_timeout)
                                                
        buy_btn = API().validElementByResourceId(self.driver,
                                                 self.logger,
                                                 CPC.resource_id_buy_ticket_button,
                                                 45)
        if not buy_btn:
            API().clickElementByXpath(self.testcase,
                                      self.driver,
                                      self.logger, 
                                      CPC.xpath_tomorrows_date_button, 
                                      CPC.click_on_button_timeout)
        API().clickElementByResourceId(self.testcase,
                                       self.driver,
                                       self.logger,
                                       CPC.resource_id_buy_ticket_button, 
                                       CPC.click_on_button_timeout)

        return tempText


    def validFilmRun(self):
        '''
        usage: 判断影片是否未上映
        '''
        width = API().getWidthOfDevice(self.driver, self.logger)
        hight = API().getHeightOfDevice(self.driver, self.logger)
        API().scroll(self.driver, self.logger, width / 2, hight / 2, width / 2, hight / 3)
        rtn = API().validElementByText(self.driver,
                                       self.logger,
                                       CPC.text_film_run,
                                       CPC.assert_view_timeout)
        return rtn
