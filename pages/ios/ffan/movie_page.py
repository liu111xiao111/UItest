#!/usr/bin/env python
# -*- coding:utf-8 -*-

from api.api import API
from pages.ios.common.superPage import SuperPage
from pages.ios.ffan.movie_page_configs import MoviePageConfigs


class MoviePage(SuperPage):
    '''
    作者 宋波
    首页=>电影
    '''

    def __init__(self, testcase, driver, logger):
        '''
        Constructor
        '''

        super(MoviePage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        '''
        usage: verify whether the current page is the switch city page.
        '''

        API().assertElementByName(self.testcase, self.driver, self.logger,
                                  MoviePageConfigs.text_movie_title,
                                  MoviePageConfigs.assert_view_timeout)

    def clickOnSeatPickingAndBuyingTicket(self):
        '''
        usage: click seat picking and buying ticket button
        '''

        for _ in range(3):
            tempTest = API().getTextByXpath(self.testcase, self.driver, self.logger,
                                            MoviePageConfigs.xpath_seat_picking_and_buying_ticket_bt,
                                            MoviePageConfigs.get_timeout)
            print(tempTest)
            if "选座购票" == tempTest:
                break
            self.scrollAsScreenPercent(0.5, 0.5, 0.1, 0.5)

        API().clickElementByXpath(self.testcase, self.driver, self.logger,
                                  MoviePageConfigs.xpath_seat_picking_and_buying_ticket_bt,
                                  MoviePageConfigs.click_on_button_timeout)
        
    def getFileName(self):
        fileName = API().getTextByXpath(self.testcase, self.driver, self.logger,
                                            MoviePageConfigs.xpath_film_name,
                                            MoviePageConfigs.get_timeout)
        print(fileName)
        return fileName
        
if __name__ == '__main__':
    pass
