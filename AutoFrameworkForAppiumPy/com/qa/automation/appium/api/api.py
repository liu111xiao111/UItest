#! /Library/Frameworks/Python.framework/Versions/2.7/bin/python
# -*- coding: utf-8 -*-

import sys,time
reload(sys)
sys.setdefaultencoding('utf8')

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException

class API:

    def __init__(self):
        pass

    '''
    ***********************************************************************************
        click methods
    ***********************************************************************************
    '''

    def clickViewByResourceID(self, driver="default", resource_id="default"):
        driver.find_element_by_id(resource_id).click()

    def clickTextViewByAndroid(self, driver="default", text="default"):
        web_element = self.getTextViewByAndroid(driver=driver, text=text)
        web_element.click()

    '''
    ***********************************************************************************
        find methods
    ***********************************************************************************
    '''

    '''
        used by android api
        parameters:
            view_text : 已知view的text,根据已知view text获取view
            viewClassName : 预查找的兄弟节点的class name
        应用场景 : 某些多tab ui,点击tab后,tab对应的view状态属性不变,而且增加兄弟view的方式来标识状态.
    '''

    def getBrotherViewByClassNameByAndroid(self, driver="default", view_text="default", viewClassName="default"):
        selector = 'new UiSelector().text("%s").fromParent(new UiSelector().className("%s"))' % (
        view_text, viewClassName)
        return driver.find_element_by_android_uiautomator(selector)


    def getViewByResourceID(self, driver="default", resource_id="default"):
        return driver.find_element_by_id(resource_id)

    def getTextViewByAndroid(self,driver="default",text="default"):
        return driver.find_element_by_android_uiautomator('new UiSelector().text("'+text+'")')

    '''
        used by android api
        parameters:
            textContains : 查找的view包含的字段部分
    '''
    def getViewTextContainsByAndroid(self,driver="default",textContains="default"):
        selector='new UiSelector().textContains("%s")' % (textContains)
        return driver.find_element_by_android_uiautomator(selector)

    '''
        used by android api
        parameters:
            textStartsWith : 查找的view包含的字段头部分
    '''
    def getViewTextStartsWithByAndroid(self,driver="default",textStartsWith="default"):
        selector='new UiSelector().textContains("%s")' % (textStartsWith)
        return driver.find_element_by_android_uiautomator(selector)

    '''
        used by android api
        parameters:
            textMatches : 通过正则表达式的方式查找view e.g. textMatches="^Add.*"
    '''

    def getViewTextMatchesByAndroid(self, driver="default", textMatches="default"):
        selector = 'new UiSelector().textContains("%s")' % (textMatches)
        return driver.find_element_by_android_uiautomator(selector)

    '''
        used by android api
        parameters:
            textMatches : 通过正则表达式的方式查找view e.g. className="android.widget.ImageView"
    '''

    def getViewByClassNameByAndroid(self, driver="default", className="default"):
        selector = 'new UiSelector().className("%s")' % (className)
        return driver.find_element_by_android_uiautomator(selector)

    '''
        usage : 显式等待方法
        parameters:
            resource_id : 查找view的resource id
            seconds : 等待的最大市场,单位秒
        应用场景 : 查找的view展现时间受网络状态影响,显式等待时间设置后,会最大等待seconds秒,如果小于seconds view出现,直接进行下一流程,如果等于seconds未出现,raise TimeoutException
    '''
    def findViewByResourceIDUntil(self,driver="default",resource_id="default",seconds="10"):
        wdw = WebDriverWait(driver=driver,timeout=seconds)
        return wdw.until(EC.presence_of_element_located((By.ID,resource_id)))

    '''
    ***********************************************************************************
        assert methods
    ***********************************************************************************
    '''

    '''
        用法和findViewByResourceIDUntil,增加结果申明判断.
    '''

    def assertViewByResourceIDUntil(self, test_case="default", driver="default", resource_id="default", seconds="500"):
        try:
            test_case.assertIsNotNone(
                self.findViewByResourceIDUntil(driver=driver, resource_id=resource_id, seconds=seconds),
                "resource id none")
        except NoSuchElementException, e:
            test_case.assertTrue(False, "resource id %s none" % (resource_id))
        except TimeoutException, e:
            test_case.assertTrue(False,
                                 "get resource id %s timeout until %s seconds" % (resource_id, seconds))

    def assertViewByResourceID(self, test_case="default", driver="default", resource_id="default"):
        try:
            test_case.assertIsNotNone(self.getViewByResourceID(driver, resource_id),
                                      "resource id %s none" % (resource_id))
        except NoSuchElementException, e:
            test_case.assertIsNotNone(None,
                                      "resource id %s none" % (resource_id))

    '''
    ***********************************************************************************
        common methods
    ***********************************************************************************
    '''

    def waitBySeconds(self,seconds=1):
        time.sleep(seconds)













