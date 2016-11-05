# -*- coding: utf-8 -*-

from api.api import API
from pages.android.common.super_page import SuperPage
from pages.android.shanghu.shangpinguanli_page_configs import ShangPinGuanLiPageConfigs as SPGLPC


class ShangPinGuanLiPage(SuperPage):
    '''
    作者 乔佳溪
    商品管理
    '''
    def __init__(self, testcase, driver, logger):
        super(ShangPinGuanLiPage, self).__init__(testcase, driver, logger)

    def validSelf(self):
        '''
        usage : 进入到商品管理页,检查标题
        '''
        API().assertElementByText(self.testcase,
                                  self.driver,
                                  self.logger,
                                  SPGLPC.text_title,
                                  SPGLPC.assert_timeout)

    def clickOnSales(self):
        '''
        usage: 点击限时抢购
        '''
        API().clickElementByText(self.testcase,
                                 self.driver,
                                 self.logger,
                                 SPGLPC.text_sales,
                                 SPGLPC.assert_timeout)

    def clickOnGoods(self):
        '''
        usage: 点击普通商品
        '''
        API().clickElementByText(self.testcase,
                                       self.driver,
                                       self.logger,
                                       SPGLPC.text_goods,
                                       SPGLPC.assert_timeout)

    def validTempSave(self):
        '''
        usage : 验证临时保存
        '''

        tempSave= API().getTextByXpath(self.testcase,
                                       self.driver,
                                       self.logger,
                                       SPGLPC.xpath_list_temp_save,
                                       SPGLPC.assert_timeout)
        #itemNumber.append(tempSave)

        API().clickElementByXpath(self.testcase,
                                  self.driver,
                                  self.logger,
                                  SPGLPC.xpath_list_temp_save,
                                  SPGLPC.assert_timeout)

        if tempSave != '0':
            tempSaveImg = API().getElementsByContainsText(self.testcase,
                                                          self.driver,
                                                          self.logger,
                                                          SPGLPC.text_contain_word_temp_save,
                                                          SPGLPC.assert_timeout)

            API().assertGreaterEqual(self.testcase, self.logger, int(tempSave), len(tempSaveImg))

    def validToBeExamined(self):
        '''
        usage : 验证待审核
        '''

        toBeExamined = API().getTextByXpath(self.testcase,
                                            self.driver,
                                            self.logger,
                                            SPGLPC.xpath_list_to_be_examined,
                                            SPGLPC.assert_timeout)
        #itemNumber.append(toBeExamined)

        API().clickElementByXpath(self.testcase,
                                  self.driver,
                                  self.logger,
                                  SPGLPC.xpath_list_to_be_examined,
                                  SPGLPC.assert_timeout)

        if toBeExamined != '0':
            toBeExaminedImg = API().getElementsByContainsText(self.testcase,
                                                              self.driver,
                                                              self.logger,
                                                              SPGLPC.text_contain_word_temp_save,
                                                              SPGLPC.assert_timeout)
            API().assertGreaterEqual(self.testcase, self.logger, int(toBeExamined), len(toBeExaminedImg))

    def validPassed(self):
        '''
        usage : 验证已通过
        '''
        passed = API().getTextByXpath(self.testcase,
                                            self.driver,
                                            self.logger,
                                            SPGLPC.xpath_list_passed,
                                            SPGLPC.assert_timeout)
        #itemNumber.append(passed)

        API().clickElementByXpath(self.testcase,
                                  self.driver,
                                  self.logger,
                                  SPGLPC.xpath_list_passed,
                                  SPGLPC.assert_timeout)

        if passed != '0':
            passedImg = API().getElementsByContainsText(self.testcase,
                                                        self.driver,
                                                        self.logger,
                                                        SPGLPC.text_contain_word_temp_save,
                                                        SPGLPC.assert_timeout)
            API().assertGreaterEqual(self.testcase, self.logger, int(passed), len(passedImg))

    def validReject(self):
        '''
        usage : 验证已驳回
        '''
        rejectInfo = API().getTextByXpath(self.testcase,
                                         self.driver,
                                         self.logger,
                                         SPGLPC.xpath_list_reject,
                                         SPGLPC.assert_timeout)
        #itemNumber.append(rejectInfo)

        API().clickElementByXpath(self.testcase,
                                  self.driver,
                                  self.logger,
                                  SPGLPC.xpath_list_reject,
                                  SPGLPC.assert_timeout)

        if rejectInfo != '0':
            rejectImg = API().getElementsByContainsText(self.testcase,
                                                        self.driver,
                                                        self.logger,
                                                        SPGLPC.text_contain_word_temp_save,
                                                        SPGLPC.assert_timeout)
            API().assertGreaterEqual(self.testcase, self.logger, int(rejectInfo), len(rejectImg))

    def clickBackKeyForSales(self):
        '''
        usage : 在限时抢购页面，点击返回按钮
        '''
        API().clickElementByType(self.testcase,
                                 self.driver,
                                 self.logger,
                                 SPGLPC.type_back_btn,
                                 SPGLPC.assert_timeout)
        API().waitBySeconds(2)

    def getTempSaveDetails(self):
        '''
        usage : 在临时保存页面，取得标题
        '''
        tempSaveTitle = API().getTextByXpath(self.testcase,
                                                      self.driver,
                                                      self.logger,
                                                      SPGLPC.xpath_temp_save,
                                                      SPGLPC.assert_timeout)
        return tempSaveTitle.strip()

    def getToBeExaminedDetails(self):
        '''
        usage : 在待审核页面，取得标题
        '''
        toBeExaminedTitle = API().getTextByXpath(self.testcase,
                                                      self.driver,
                                                      self.logger,
                                                      SPGLPC.xpath_to_be_examtined,
                                                      SPGLPC.assert_timeout)
        return toBeExaminedTitle.strip()

    def getPassedDetails(self):
        '''
        usage : 在已通过页面，取得标题
        '''
        passedTitle = API().getTextByXpath(self.testcase,
                                                      self.driver,
                                                      self.logger,
                                                      SPGLPC.xpath_passed,
                                                      SPGLPC.assert_timeout)
        return passedTitle.strip()

    def getRejectDetails(self):
        '''
        usage : 在已驳回页面，取得标题
        '''
        rejectTitle = API().getTextByXpath(self.testcase,
                                                      self.driver,
                                                      self.logger,
                                                      SPGLPC.xpath_reject,
                                                      SPGLPC.assert_timeout)
        return rejectTitle.strip()

    def validDetails(self, title = "default"):
        '''
        usage : 验证详细页面
        '''
        API().getElementsByText(self.testcase,
                                self.driver,
                                self.logger,
                                title,
                                SPGLPC.assert_timeout)

    def getGoodsNumber(self):
        '''
        usage : 在普通商品页面取得个条目数量
        '''
        itemNumber = []
        tempSave= API().getTextByXpath(self.testcase,
                                       self.driver,
                                       self.logger,
                                       SPGLPC.xpath_list_temp_save,
                                       SPGLPC.assert_timeout)

        itemNumber.append(tempSave)

        toBeExamined = API().getTextByXpath(self.testcase,
                                            self.driver,
                                            self.logger,
                                            SPGLPC.xpath_list_to_be_examined,
                                            SPGLPC.assert_timeout)

        itemNumber.append(toBeExamined)

        passed = API().getTextByXpath(self.testcase,
                                            self.driver,
                                            self.logger,
                                            SPGLPC.xpath_list_passed,
                                            SPGLPC.assert_timeout)

        itemNumber.append(passed)

        rejectInfo = API().getTextByXpath(self.testcase,
                                         self.driver,
                                         self.logger,
                                         SPGLPC.xpath_list_reject,
                                         SPGLPC.assert_timeout)

        itemNumber.append(rejectInfo)

        return itemNumber

    def clickOnTempSaveDetails(self):
        '''
        usage: 点击详情
        '''
        API().clickElementByXpath(self.testcase,
                                       self.driver,
                                       self.logger,
                                       SPGLPC.xpath_temp_save,
                                       SPGLPC.assert_timeout)

    def clickOnToBeExaminedDetails(self):
        '''
        usage: 点击详情
        '''
        API().clickElementByXpath(self.testcase,
                                       self.driver,
                                       self.logger,
                                       SPGLPC.xpath_to_be_examtined,
                                       SPGLPC.assert_timeout)

    def clickOnPassedDetails(self):
        '''
        usage: 点击详情
        '''
        API().clickElementByXpath(self.testcase,
                                       self.driver,
                                       self.logger,
                                       SPGLPC.xpath_passed,
                                       SPGLPC.assert_timeout)

    def clickOnRejectDetails(self):
        '''
        usage: 点击详情
        '''
        API().clickElementByXpath(self.testcase,
                                       self.driver,
                                       self.logger,
                                       SPGLPC.xpath_reject,
                                       SPGLPC.assert_timeout)
