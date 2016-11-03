# -*- coding: utf-8 -*-
import time
import datetime
from api.api import API
from pages.android.common.super_page import SuperPage
from pages.android.shanghu.lefuzhangdan_page_configs import LeFuZhangDanPageConfigs as LFZDPC


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
        API().clickElementByText(self.testcase,
                                        self.driver,
                                        self.logger,
                                        LFZDPC.text_user_defined,
                                        LFZDPC.verify_timeout)

    def validCalendar(self):
        '''
        usage: 验证日历
        '''
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

    def clickOnStartDate(self):
        '''
        usage: 选择当前日期的前一天
        '''
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

        return startDate

    def validSeachDate(self, startDate = "default"):
        '''
        usage: 验证查询日期
        '''
        searchDate = API().getTextByResourceId(self.testcase,
                                               self.driver,
                                               self.logger,
                                               LFZDPC.resouce_id_search_date,
                                               LFZDPC.verify_timeout)

        searchEndDate = time.strftime('%Y-%m-%d')

        searchContent = u"查询时间 : " + startDate + u"至" + searchEndDate

        API().assertEqual(self.testcase,
                          self.logger,
                          searchDate,
                          searchContent)

    def validOrderInfo(self):
        '''
        usage: 验证订单信息
        '''
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
