# -*- coding: utf-8 -*-
import time
import datetime
from api.api import API
from pages.android.common.super_page import SuperPage
from pages.android.shanghu.lefuzhangdan_page_configs import LeFuZhangDanPageConfigs as LFZDPC
from pages.logger import logger


class LeFuZhangDanPage(SuperPage):
    '''
    作者 乔佳溪
    订单管理
    '''
    def __init__(self, testcase, driver, logger):
        super(LeFuZhangDanPage, self).__init__(testcase, driver, logger)

    def clickOnUserDefined(self):
        '''
        usage: 点击自定义
        '''
        logger.info("Click 自定义 begin")
        API().clickElementByText(self.testcase,
                                        self.driver,
                                        self.logger,
                                        LFZDPC.text_user_defined,
                                        LFZDPC.verify_timeout)
        logger.info("Click 自定义 end")

    def validCalendar(self):
        '''
        usage: 验证日历
        '''
        logger.info("Check 日历 begin")
        API().assertElementByText(self.testcase,
                                  self.driver,
                                  self.logger,
                                  LFZDPC.text_calendar_start,
                                  LFZDPC.verify_timeout)

        API().assertElementByText(self.testcase,
                                  self.driver,
                                  self.logger,
                                  LFZDPC.text_calendar_end,
                                  LFZDPC.verify_timeout)
        logger.info("Check 日历 end")

    def clickOnStartDate(self):
        '''
        usage: 选择当前日期的前一天
        '''
        logger.info("Click 当前日期的前一天 begin")
        date = time.strftime('%Y-%m-%d').split('-')
        yesDate = datetime.datetime.now() - datetime.timedelta(days = 1)
        beforeDate = yesDate.strftime('%Y-%m-%d').split('-')

        if date[2] == '01':
            day = date[2]
        else:
            day = beforeDate[2]

        if date[1] == '01':
            month = u"一月"
        elif date[1] == '02':
            month = u"二月"
        elif date[1] == '03':
            month = u"三月"
        elif date[1] == '04':
            month = u"四月"
        elif date[1] == '05':
            month = u"五月"
        elif date[1] == '06':
            month = u"六月"
        elif date[1] == '07':
            month = u"七月"
        elif date[1] == '08':
            month = u"八月"
        elif date[1] == '09':
            month = u"九月"
        elif date[1] == '10':
            month = u"十月"
        elif date[1] == '11':
            month = u"十一月"
        elif date[1] == '12':
            month = u"十二月"

        startDate = date[0] +  '-' + date[1] + '-' + day

        if day == '01':
            clickStartDate = day + " " + month + " " + date[0] + " selected"
        else:
            clickStartDate = day + " " + month + " " + date[0]
        API().clickElementByContentDesc(self.testcase,
                                        self.driver,
                                        self.logger,
                                        clickStartDate,
                                        LFZDPC.verify_timeout)

        API().clickElementByText(self.testcase,
                                        self.driver,
                                        self.logger,
                                        LFZDPC.text_confirm,
                                        LFZDPC.verify_timeout)
        logger.info("Click 当前日期的前一天 end")

        return startDate

    def validSeachDate(self, startDate = "default"):
        '''
        usage: 验证查询日期
        '''
        logger.info("Check 查询日期 begin")
        searchDate = API().getTextByResourceId(self.testcase,
                                               self.driver,
                                               self.logger,
                                               LFZDPC.resouce_id_search_date,
                                               LFZDPC.verify_timeout)

        searchEndDate = time.strftime('%Y-%m-%d')

        if(startDate.split('-')[2] == "01"):
            searchContent = u"查询时间 : " + startDate
        else:
            searchContent = u"查询时间 : " + startDate + u"至" + searchEndDate

        API().assertEqual(self.testcase,
                          self.logger,
                          searchDate,
                          searchContent)
        logger.info("Check 查询日期 end")

    def validOrderInfo(self):
        '''
        usage: 验证订单信息
        '''
        logger.info("Check 订单信息 begin")
        data = API().validElementByText(self.driver,
                                        self.logger,
                                        LFZDPC.text_pay_type,
                                        LFZDPC.verify_timeout)

        if data:
            payType = API().getElementsByResourceId(self.testcase,
                                                    self.driver,
                                                    self.logger,
                                                    LFZDPC.resource_id_type,
                                                    LFZDPC.verify_timeout)
            API().assertEqual(self.testcase, self.logger, payType, LFZDPC.text_lefu_pay)
        logger.info("Check 订单信息 end")
