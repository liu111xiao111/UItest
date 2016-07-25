# -*- coding: utf-8 -*-

import time

from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class API(object):
    '''
    UI自动化测试接口
    '''
    def __init__(self):
        pass


    '''
    ********************************************************************************************
    通用基本方法
    ********************************************************************************************
    '''
    '''
        Usage: 界面滑动方法
        parameters:
            start_x:  起始 x 轴坐标
            start_y: 起始 y 轴坐标
            end_x: 结束 x 轴坐标
            end_y: 结束 y 轴坐标
            duration: 滑动时间，单位ms
    '''
    def scroll(self, driver, logger, start_x, start_y, end_x, end_y, duration=None):
        driver.swipe(start_x, start_y, end_x, end_y, duration)

    '''
        Usage: 获取当前设备屏幕宽度方法
        parameters:
            driver: appium driver
            logger: logging
        return: 返回当前设备屏幕宽度
    '''
    def getWidthOfDevice(self, driver, logger):
        width = driver.get_window_size()['width']
        return width

    '''
        Usage: 获取当前设备屏幕高度方法
        parameters:
            driver: appium driver
            logger: logging
        return: 返回当前设备屏幕高度
    '''
    def getHeightOfDevice(self, driver, logger):
        height = driver.get_window_size()['height']
        return height

    '''
        Usage: 等待方法
        parameters:
            timeout: 等待时间，单位秒
    '''
    def waitBySeconds(self, timeout=1):
        time.sleep(timeout)

    '''
        Usage: 截图方法
        parameters:
            driver: appium driver
            pic_name: 截图名称
    '''
    def screenShot(self, driver, pic_name="myfeifan_auto_test"):
        driver.save_screenshot(pic_name + ".png")

    '''
        usage : 页面输入方法
        parameters:
            testcase: unittest testcase
            driver: appium driver
            logger: logging
            xPath : 页面element的 xpath属性
            string : 需要输入的值
            timeout: 超时时间,单位秒,默认十秒。
    '''
    def inputStringByXpath(self, testcase, driver, logger, xPath, string, timeout = 10):
        try:
            input_field = self._findElementByXpath(driver, logger, xPath, timeout)
        except TimeoutException:
            testcase.assertTrue(False, "Get element by xPath [%s] timeout" % (xPath))
        else:
            testcase.assertTrue(False, "Can not get element by xPath [%s]" % (xPath))

        input_field.click()
        input_field.send_keys(string)

    '''
    ********************************************************************************************
    Android平台基本方法
    ********************************************************************************************
    '''

    '''
        usage : 点击返回按钮方法 （适用Android平台）
        parameters:
            driver: appium driver
            logger: logging
    '''
    def clickBackKeyForAndroid(self, driver, logger):
        driver.press_keycode(4)
        time.sleep(2)

    '''
        usage : 滑动页面到指定文本控件方法 （适用Android平台）
        parameters:
            driver: appium driver
            logger: logging
            text: 页面element的text属性
    '''
    def scrollToText(self, driver, logger, text):
        driver.find_element_by_android_uiautomator(
            'new UiScrollable(new UiSelector().scrollable(true).instance(0)).'
            'scrollIntoView(new UiSelector().text("%s").instance(0))' % (text))

    '''
        usage : 页面输入方法 （适用Android设备）
        parameters:
            testcase: unittest testcase
            driver: appium driver
            logger: logging
            resourceId : 页面element的 resource id属性
            string : 需要输入的值
            timeout: 超时时间,单位秒,默认十秒。
    '''
    def inputStringByResourceId(self, testcase, driver, logger, resourceId, string, timeout = 10):
        try:
            input_field = self._findElementByResourceId(driver, logger, resourceId, timeout)
        except TimeoutException:
            testcase.assertTrue(False, "Get element by resource id [%s] timeout" % (resourceId))
        else:
            testcase.assertTrue(False, "Can not get element by resource id [%s]" % (resourceId))

        input_field.click()
        input_field.send_keys(string)

    '''
        usage : 页面输入方法 （适用Android设备）
        parameters:
            testcase: unittest testcase
            driver: appium driver
            logger: logging
            className : 页面element的 class name属性
            string : 需要输入的值
            timeout: 超时时间,单位秒,默认十秒。
    '''
    def inputStringByClassName(self, testcase, driver, logger, className, string, timeout = 10):
        try:
            input_field = self._findElementByClassName(driver, logger, className, timeout)
        except TimeoutException:
            testcase.assertTrue(False, "Get element by class name [%s] timeout" % (className))
        else:
            testcase.assertTrue(False, "Can not get element by class name [%s]" % (className))

        input_field.click()
        input_field.send_keys(string)


    '''
    ********************************************************************************************
    IOS 平台基本方法
    ********************************************************************************************
    '''

    '''
        usage : 点击返回按钮方法 （适用IOS平台）
        parameters:
            testcase: unittest testcase
            driver: appium driver
            logger: logging
            xPath : 页面返回按钮的 xpath属性
            timeout : 超时时间,单位秒,默认十秒。
    '''
    def clickBackKeyForIos(self, testcase, driver, logger, xPath, timeout=10):
        self.clickElementByxPath(testcase, driver, logger, xPath, timeout)
        time.sleep(2)

    '''
        usage : 页面输入方法 （适用IOS平台）
        parameters:
            testcase: unittest testcase
            driver: appium driver
            logger: logging
            name : 页面element的 name属性
            string : 需要输入的值
            timeout: 超时时间,单位秒,默认十秒。
    '''
    def inputStringByName(self, testcase, driver, logger, name, string, timeout = 10):
        try:
            input_field = self._findElementByResourceId(driver, logger, name, timeout)
        except TimeoutException:
            testcase.assertTrue(False, "Get element by name [%s] timeout" % (name))
        else:
            testcase.assertTrue(False, "Can not get element by name [%s]" % (name))

        input_field.click()
        input_field.send_keys(string)

    '''
        usage : 页面输入方法 （适用IOS平台）
        parameters:
            testcase: unittest testcase
            driver: appium driver
            logger: logging
            elementType : 页面element的 type属性
            string : 需要输入的值
            timeout: 超时时间,单位秒,默认十秒。
    '''
    def inputStringByType(self, testcase, driver, logger, elementType, string, timeout = 10):
        try:
            input_field = self._findElementByClassName(driver, logger, elementType, timeout)
        except TimeoutException:
            testcase.assertTrue(False, "Get element by element type [%s] timeout" % (elementType))
        else:
            testcase.assertTrue(False, "Can not get element by element type [%s]" % (elementType))

        input_field.click()
        input_field.send_keys(string)


    '''
    ********************************************************************************************
    Android 获取多个element方法
    ********************************************************************************************
    '''

    '''
        usage : 获取页面多个element (适用Android平台)
        parameters:
            testcase: unittest testcase
            driver: appium driver
            logger: logging
            resourceId : 页面element的 resource id属性
            timeout : 超时时间,单位秒,默认十秒。
        return : 返回element列表
    '''
    def getElementsByResourceId(self, testcase, driver, logger, resourceId="default", timeout=10):
        try:
            return self._findElementsByResourceId(driver, logger, resourceId, timeout)
        except TimeoutException:
            testcase.assertTrue(False, "Get elements by resource id [%s] timeout" % (resourceId))
        else:
            testcase.assertTrue(False, "Can not get elements by resource id [%s]" % (resourceId))

    '''
        usage : 获取页面多个element (适用Android平台)
        parameters:
            testcase: unittest testcase
            driver: appium driver
            logger: logging
            className : 页面element的 class name属性
            timeout : 超时时间,单位秒,默认十秒。
        return : 返回element列表
    '''
    def getElementsByClassName(self, testcase, driver, logger, className="default", timeout=10):
        try:
            return self._findElementsByClassName(driver, logger, className, timeout)
        except TimeoutException:
            testcase.assertTrue(False, "Get elements by class name [%s] timeout" % (className))
        else:
            testcase.assertTrue(False, "Can not get elements by class name [%s]" % (className))

    '''
        usage : 获取页面多个element (适用Android平台)
        parameters:
            testcase: unittest testcase
            driver: appium driver
            logger: logging
            text : 页面element的 text属性
            timeout : 超时时间,单位秒,默认十秒。
        return : 返回element列表
    '''
    def getElementsByText(self, testcase, driver, logger, text="default", timeout=10):
        try:
            return self._findElementsByText(driver, logger, text, timeout)
        except TimeoutException:
            testcase.assertTrue(False, "Get elements by text [%s] timeout" % (text))
        else:
            testcase.assertTrue(False, "Can not get elements by text [%s]" % (text))

    '''
        usage : 获取页面多个element (适用Android平台)
        parameters:
            testcase: unittest testcase
            driver: appium driver
            logger: logging
            contentDesc : 页面element的 content description属性
            timeout : 超时时间,单位秒,默认十秒。
        return : 返回element列表
    '''
    def getElementsByContentDesc(self, testcase, driver, logger, contentDesc="default", timeout=10):
        try:
            return self._findElementsByContentDesc(driver, logger, contentDesc, timeout)
        except TimeoutException:
            testcase.assertTrue(False, "Get elements by content description [%s] timeout" % (contentDesc))
        else:
            testcase.assertTrue(False, "Can not get elements by content description [%s]" % (contentDesc))

    '''
        usage : 获取页面多个element (适用Android平台)
        parameters:
            testcase: unittest testcase
            driver: appium driver
            logger: logging
            containsText : 页面element的 contains text
            timeout : 超时时间,单位秒,默认十秒。
        return : 返回element列表
    '''
    def getElementsByContainsText(self, testcase, driver, logger, containsText="default", timeout=10):
        try:
            return self._findElementsByContainsText(driver, logger, containsText, timeout)
        except TimeoutException:
            testcase.assertTrue(False, "Get elements by contains text [%s] timeout" % (containsText))
        else:
            testcase.assertTrue(False, "Can not get elements by contains text [%s]" % (containsText))

    '''
        usage : 获取页面多个element (适用Android平台)
        parameters:
            testcase: unittest testcase
            driver: appium driver
            logger: logging
            textStartWith : 页面element的 text start with
            timeout : 超时时间,单位秒,默认十秒。
        return : 返回element列表
    '''
    def getElementsByTextStartWith(self, testcase, driver, logger, textStartWith="default", timeout=10):
        try:
            return self._findElementsByTextStartWith(driver, logger, textStartWith, timeout)
        except TimeoutException:
            testcase.assertTrue(False, "Get elements by text start with [%s] timeout" % (textStartWith))
        else:
            testcase.assertTrue(False, "Can not get elements by text start with [%s]" % (textStartWith))


    '''
    ********************************************************************************************
    IOS 获取多个element方法
    ********************************************************************************************
    '''

    '''
        usage : 获取页面多个element (适用IOS平台)
        parameters:
            testcase: unittest testcase
            driver: appium driver
            logger: logging
            name : 页面element的 name
            timeout : 超时时间,单位秒,默认十秒。
        return : 返回element列表
    '''
    def getElementsByName(self, testcase, driver, logger, name="default", timeout=10):
        try:
            return self._findElementsByResourceId(driver, logger, name, timeout)
        except TimeoutException:
            testcase.assertTrue(False, "Get elements by name [%s] timeout" % (name))
        else:
            testcase.assertTrue(False, "Can not get elements by name [%s]" % (name))

    '''
        usage : 获取页面多个element (适用IOS平台)
        parameters:
            testcase: unittest testcase
            driver: appium driver
            logger: logging
            elementType : 页面element的 element type
            timeout : 超时时间,单位秒,默认十秒。
        return : 返回element列表
    '''
    def getElementsByType(self, testcase, driver, logger, elementType="default", timeout=10):
        try:
            return self._findElementsByClassName(driver, logger, elementType, timeout)
        except TimeoutException:
            testcase.assertTrue(False, "Get elements by element type [%s] timeout" % (elementType))
        else:
            testcase.assertTrue(False, "Can not get elements by element type [%s]" % (elementType))

    '''
        usage : 获取页面多个element (适用IOS平台)
        parameters:
            testcase: unittest testcase
            driver: appium driver
            logger: logging
            uiaString : 页面element的 uia string
            timeout : 超时时间,单位秒,默认十秒。
        return : 返回element列表
    '''
    def getElementsByIosUiautomation(self, testcase, driver, logger, uiaString="default", timeout=10):
        try:
            return self._findElementsByIosUiautomation(driver, logger, uiaString, timeout)
        except TimeoutException:
            testcase.assertTrue(False, "Get elements by uia string [%s] timeout" % (uiaString))
        else:
            testcase.assertTrue(False, "Can not get elements by uia string [%s]" % (uiaString))


    '''
    ********************************************************************************************
    通用获取element text方法
    ********************************************************************************************
    '''

    '''
        usage : 获取页面element text方法
        parameters:
            testcase: unittest testcase
            driver: appium driver
            logger: logging
            xPath : 页面element的 xpath
            timeout : 超时时间,单位秒,默认十秒。
        return : 返回element text
    '''
    def getTextByxPath(self, testcase, driver, logger, xPath="default", timeout=10):
        try:
            return self._findElementByXpath(driver, logger, xPath, timeout).text
        except TimeoutException:
            testcase.assertTrue(False, "Get element text by xPath [%s] timeout" % (xPath))
        else:
            testcase.assertTrue(False, "Can not get element text by xPath [%s]" % (xPath))


    '''
    ********************************************************************************************
    Android 获取element text方法
    ********************************************************************************************
    '''

    '''
        usage : 获取页面element text方法 (适用Android平台)
        parameters:
            testcase: unittest testcase
            driver: appium driver
            logger: logging
            resourceId : 页面element的 resource id
            timeout : 超时时间,单位秒,默认十秒。
        return : 返回element text
    '''
    def getTextByResourceId(self, testcase, driver, logger, resourceId="default", timeout=10):
        try:
            return self._findElementByResourceId(driver, logger, resourceId, timeout).text
        except TimeoutException:
            testcase.assertTrue(False, "Get element text by resource id [%s] timeout" % (resourceId))
        else:
            testcase.assertTrue(False, "Can not get element text by resource id [%s]" % (resourceId))

    '''
        usage : 获取页面element text方法 (适用Android平台)
        parameters:
            testcase: unittest testcase
            driver: appium driver
            logger: logging
            className : 页面element的 class name
            timeout : 超时时间,单位秒,默认十秒。
        return : 返回element text
    '''
    def getTextByClassName(self, testcase, driver, logger, className="default", timeout=10):
        try:
            return self._findElementByClassName(driver, logger, className, timeout).text
        except TimeoutException:
            testcase.assertTrue(False, "Get element text by class name [%s] timeout" % (className))
        else:
            testcase.assertTrue(False, "Can not get element text by class name [%s]" % (className))

    '''
        usage : 获取页面element text方法 (适用Android平台)
        parameters:
            testcase: unittest testcase
            driver: appium driver
            logger: logging
            containsText : 页面element的模糊匹配
            timeout : 超时时间,单位秒,默认十秒。
        return : 返回element text
    '''
    def getTextByContainsText(self, testcase, driver, logger, containsText="default", timeout=10):
        try:
            return self._findElementByContainsText(driver, logger, containsText, timeout).text
        except TimeoutException:
            testcase.assertTrue(False, "Get element text by contains text [%s] timeout" % (containsText))
        else:
            testcase.assertTrue(False, "Can not get element text by contains text [%s]" % (containsText))

    '''
        usage : 获取页面element text方法 (适用Android平台)
        parameters:
            testcase: unittest testcase
            driver: appium driver
            logger: logging
            textStartWith : 页面element的text start with
            timeout : 超时时间,单位秒,默认十秒。
        return : 返回element text
    '''
    def getTextByTextStartWith(self, testcase, driver, logger, textStartWith="default", timeout=10):
        try:
            return self._findElementByTextStartWith(driver, logger, textStartWith, timeout).text
        except TimeoutException:
            testcase.assertTrue(False, "Get element text by text start with [%s] timeout" % (textStartWith))
        else:
            testcase.assertTrue(False, "Can not get element text by text start with [%s]" % (textStartWith))


    '''
    ********************************************************************************************
    IOS 获取element text方法
    ********************************************************************************************
    '''

    '''
        usage : 获取页面element text方法 (适用IOS平台)
        parameters:
            testcase: unittest testcase
            driver: appium driver
            logger: logging
            elementType : 页面element的 element type
            timeout : 超时时间,单位秒,默认十秒。
        return : 返回element text
    '''
    def getTextByType(self, testcase, driver, logger, elementType="default", timeout=10):
        try:
            return self._findElementByClassName(driver, logger, elementType, timeout).text
        except TimeoutException:
            testcase.assertTrue(False, "Get element text by element type [%s] timeout" % (elementType))
        else:
            testcase.assertTrue(False, "Can not get element text by element type [%s]" % (elementType))

    '''
        usage : 获取页面element text方法 (适用IOS平台)
        parameters:
            testcase: unittest testcase
            driver: appium driver
            logger: logging
            uiaString : 页面element的 uia string
            timeout : 超时时间,单位秒,默认十秒。
        return : 返回element text
    '''
    def getTextByIosUiautomation(self, testcase, driver, logger, uiaString="default", timeout=10):
        try:
            return self._findElementByIosUiautomation(driver, logger, uiaString, timeout).text
        except TimeoutException:
            testcase.assertTrue(False, "Get element text by uia string [%s] timeout" % (uiaString))
        else:
            testcase.assertTrue(False, "Can not get element text by uia string [%s]" % (uiaString))


    '''
    ********************************************************************************************
    通用点击操作方法
    ********************************************************************************************
    '''

    '''
        usage : 页面element点击操作方法
        parameters:
            testcase: unittest testcase
            driver: appium driver
            logger: logging
            xPath : 点击element的 xpath
            timeout : 超时时间,单位秒,默认十秒。
    '''
    def clickElementByxPath(self, testcase, driver, logger, xPath="default", timeout=10):
        try:
            self._findElementByXpath(driver, logger, xPath, timeout).click()
        except TimeoutException:
            testcase.assertTrue(False, "Click element by xPath [%s] timeout" % (xPath))
        else:
            testcase.assertTrue(False, "Can not click element by xPath [%s]" % (xPath))


    '''
    ********************************************************************************************
    Android 点击操作方法
    ********************************************************************************************
    '''

    '''
        usage : 页面element点击操作方法 （适用Android平台）
        parameters:
            testcase: unittest testcase
            driver: appium driver
            logger: logging
            resourceID : 断言element的 resource id
            timeout : 超时时间,单位秒,默认十秒。
    '''
    def clickElementByResourceId(self, testcase, driver, logger, resourceID, timeout=10):
        try:
            self._findElementByResourceID(driver, logger, resourceID, timeout).click()
        except TimeoutException:
            testcase.assertTrue(False, "Click element by resource id [%s] timeout" % (resourceID))
        else:
            testcase.assertTrue(False, "Can not click element by resource id [%s]" % (resourceID))

    '''
        usage : 页面element点击操作方法 （适用Android平台）
        parameters:
            testcase: unittest testcase
            driver: appium driver
            logger: logging
            className : 断言element的 class name
            timeout : 超时时间,单位秒,默认十秒。
    '''
    def clickElementByClassName(self, testcase, driver, logger, className, timeout=10):
        try:
            self._findElementByClassName(driver, logger, className, timeout).click()
        except TimeoutException:
            testcase.assertTrue(False, "Click element by class name [%s] timeout" % (className))
        else:
            testcase.assertTrue(False, "Can not click element by class name [%s]" % (className))

    '''
        usage : 页面element点击操作方法 （适用Android平台）
        parameters:
            testcase: unittest testcase
            driver: appium driver
            logger: logging
            text : 断言element的 text
            timeout : 超时时间,单位秒,默认十秒。
    '''
    def clickElementByText(self, testcase, driver, logger, text, timeout=10):
        try:
            self._findElementByText(driver, logger, text, timeout).click()
        except TimeoutException:
            testcase.assertTrue(False, "Click element by text [%s] timeout" % (text))
        else:
            testcase.assertTrue(False, "Can not click element by text [%s]" % (text))

    '''
        usage : 页面element点击操作方法 （适用Android平台）
        parameters:
            testcase: unittest testcase
            driver: appium driver
            logger: logging
            contentDesc : 断言element的 content description
            timeout : 超时时间,单位秒,默认十秒。
    '''
    def clickElementByContentDesc(self, testcase, driver, logger, contentDesc, timeout=10):
        try:
            self._findElementByContentDesc(driver, logger, contentDesc, timeout).click()
        except TimeoutException:
            testcase.assertTrue(False, "Click element by content description [%s] timeout" % (contentDesc))
        else:
            testcase.assertTrue(False, "Can not click element by content description [%s]" % (contentDesc))

    '''
        usage : 页面element点击操作方法 （适用Android平台）
        parameters:
            testcase: unittest testcase
            driver: appium driver
            logger: logging
            contentDesc : 断言element的 contains text
            timeout : 超时时间,单位秒,默认十秒。
    '''
    def clickElementByContainsText(self, testcase, driver, logger, containsText, timeout=10):
        try:
            self._findElementByContainsText(driver, logger, containsText, timeout).click()
        except TimeoutException:
            testcase.assertTrue(False, "Click element by contains text [%s] timeout" % (containsText))
        else:
            testcase.assertTrue(False, "Can not click element by contains text [%s]" % (containsText))

    '''
        usage : 页面element点击操作方法 （适用Android平台）
        parameters:
            testcase: unittest testcase
            driver: appium driver
            logger: logging
            textStartWith : 断言element的 text start with
            timeout : 超时时间,单位秒,默认十秒。
    '''
    def clickElementByTextStartWith(self, testcase, driver, logger, textStartWith, timeout=10):
        try:
            self._findElementByTextStartWith(driver, logger, textStartWith, timeout).click()
        except TimeoutException:
            testcase.assertTrue(False, "Click element by text start with [%s] timeout" % (textStartWith))
        else:
            testcase.assertTrue(False, "Can not click element by text start with [%s]" % (textStartWith))


    '''
    ********************************************************************************************
    IOS 点击操作方法
    ********************************************************************************************
    '''

    '''
        usage : 页面element点击操作方法 （适用IOS平台）
        parameters:
            testcase: unittest testcase
            driver: appium driver
            logger: logging
            name : 断言element的 name
            timeout : 超时时间,单位秒,默认十秒。
    '''
    def clickElementByName(self, testcase, driver, logger, name, timeout=10):
        try:
            self._findElementByResourceId(driver, logger, name, timeout).click()
        except TimeoutException:
            testcase.assertTrue(False, "Click element by name [%s] timeout" % (name))
        else:
            testcase.assertTrue(False, "Can not click element by name [%s]" % (name))

    '''
        usage : 页面element点击操作方法 （适用IOS平台）
        parameters:
            testcase: unittest testcase
            driver: appium driver
            logger: logging
            elementType : 断言element的 element type
            timeout : 超时时间,单位秒,默认十秒。
    '''
    def clickElementByType(self, testcase, driver, logger, elementType, timeout=10):
        try:
            self._findElementByClassName(driver, logger, elementType, timeout).click()
        except TimeoutException:
            testcase.assertTrue(False, "Click element by element type [%s] timeout" % (elementType))
        else:
            testcase.assertTrue(False, "Can not click element by element type [%s]" % (elementType))

    '''
        usage : 页面element点击操作方法 （适用IOS平台）
        parameters:
            testcase: unittest testcase
            driver: appium driver
            logger: logging
            uiaString : 断言element的 uia string
            timeout : 超时时间,单位秒,默认十秒。
    '''
    def clickElementByIosUiautomation(self, testcase, driver, logger, uiaString, timeout=10):
        try:
            self._findElementByIosUiautomation(driver, logger, uiaString, timeout)
        except TimeoutException:
            testcase.assertTrue(False, "Click element by uia string [%s] timeout" % (uiaString))
        else:
            testcase.assertTrue(False, "Can not click element by uia string [%s]" % (uiaString))

    
    '''
    ********************************************************************************************
    通用验证element方法
    ********************************************************************************************
    '''
    '''
        usage : 页面element验证方法
        parameters:
            testcase: unittest testcase
            driver: appium driver
            logger: logging
            xPath : 验证element的 xpath
            timeout : 超时时间,单位秒,默认十秒。
    '''
    def validElementByxPath(self, testcase, driver, logger, xPath="default", timeout=10):
        try:
            return self._findElementByXpath(driver, logger, xPath, timeout)
        except:
            return False


    '''
    ********************************************************************************************
    Android 验证element方法
    ********************************************************************************************
    '''
    '''
        usage : 页面element验证方法 (适用Android平台)
        parameters:
            testcase: unittest testcase
            driver: appium driver
            logger: logging
            resourceId : 验证element的 resource id
            timeout : 超时时间,单位秒,默认十秒。
    '''
    def validElementByResourceId(self, testcase, driver, logger, resourceId="default", timeout=10):
        try:
            return self._findElementByResourceId(driver, logger, resourceId, timeout)
        except:
            return False

    '''
        usage : 页面element验证方法 (适用Android平台)
        parameters:
            testcase: unittest testcase
            driver: appium driver
            logger: logging
            className : 验证element的 class name
            timeout : 超时时间,单位秒,默认十秒。
    '''
    def validElementByClassName(self, testcase, driver, logger, className="default", timeout=10):
        try:
            return self._findElementByClassName(driver, logger, className, timeout)
        except:
            return False

    '''
        usage : 页面element验证方法 (适用Android平台)
        parameters:
            testcase: unittest testcase
            driver: appium driver
            logger: logging
            text : 验证element的 text
            timeout : 超时时间,单位秒,默认十秒。
    '''
    def validElementByText(self, testcase, driver, logger, text="default", timeout=10):
        try:
            return self._findElementByText(driver, logger, text, timeout)
        except:
            return False

    '''
        usage : 页面element验证方法 (适用Android平台)
        parameters:
            testcase: unittest testcase
            driver: appium driver
            logger: logging
            contentDesc : 验证element的 content description
            timeout : 超时时间,单位秒,默认十秒。
    '''
    def validElementByContentDesc(self, testcase, driver, logger, contentDesc="default", timeout=10):
        try:
            return self._findElementByContentDesc(driver, logger, contentDesc, timeout)
        except:
            return False

    '''
        usage : 页面element验证方法 (适用Android平台)
        parameters:
            testcase: unittest testcase
            driver: appium driver
            logger: logging
            containsText : 验证element的模糊匹配方法
            timeout : 超时时间,单位秒,默认十秒。
    '''
    def validElementByContainsText(self, testcase, driver, logger, containsText="default", timeout=10):
        try:
            return self._findElementByContainsText(driver, logger, containsText, timeout)
        except:
            return False

    '''
        usage : 页面element验证方法 (适用Android平台)
        parameters:
            testcase: unittest testcase
            driver: appium driver
            logger: logging
            textStartWith : 验证element的以text开头的元素
            timeout : 超时时间,单位秒,默认十秒。
    '''
    def validElementByTextStartWith(self, testcase, driver, logger, textStartWith="default", timeout=10):
        try:
            return self._findElementByTextStartWith(driver, logger, textStartWith, timeout)
        except:
            return False


    '''
    ********************************************************************************************
    IOS 验证方法
    ********************************************************************************************
    '''
    '''
        usage : 页面element验证方法 (适用IOS平台)
        parameters:
            testcase: unittest testcase
            driver: appium driver
            logger: logging
            name : 验证element的 name
            timeout : 超时时间,单位秒,默认十秒。
    '''
    def validElementByName(self, testcase, driver, logger, name="default", timeout=10):
        try:
            return self._findElementByResourceId(driver, logger, name, timeout)
        except:
            return False

    '''
        usage : 页面element验证方法 (适用IOS平台)
        parameters:
            testcase: unittest testcase
            driver: appium driver
            logger: logging
            elementType : 验证element的 type
            timeout : 超时时间,单位秒,默认十秒。
    '''
    def validElementByType(self, testcase, driver, logger, elementType="default", timeout=10):
        try:
            return self._findElementByClassName(driver, logger, elementType, timeout)
        except:
            return False

    '''
        usage : 页面element验证方法 (适用IOS平台)
        parameters:
            testcase: unittest testcase
            driver: appium driver
            logger: logging
            uiaString : 验证element的 uia string
            timeout : 超时时间,单位秒,默认十秒。
    '''
    def validElementByIosUiautomation(self, testcase, driver, logger, uiaString="default", timeout=10):
        try:
            return self._findElementByIosUiautomation(driver, logger, uiaString, timeout)
        except:
            return False


    '''
    ********************************************************************************************
    通用断言element方法
    ********************************************************************************************
    '''

    '''
        ************************************************************************
        1. 通用断言单一element方法
        ************************************************************************
    '''

    '''
        usage : 页面element验证方法
        parameters:
            testcase: unittest testcase
            driver: appium driver
            logger: logging
            xPath : 断言element的 xpath
            timeout : 超时时间,单位秒,默认十秒。
    '''
    def assertElementByxPath(self, testcase, driver, logger, xPath="default", timeout=10):
        try:
            self._findElementByXpath(driver, logger, xPath, timeout)
        except TimeoutException:
            testcase.assertTrue(False, "Get element by xPath [%s] timeout" % (xPath))
        else:
            testcase.assertTrue(False, "Can not get element by xPath [%s]" % (xPath))


    '''
        ************************************************************************
        2. 通用断言多个element方法 （只需一个验证成功，即为成功）
        ************************************************************************
    '''

    '''
        usage : 页面多个element验证方法
        parameters:
            testcase: unittest testcase
            driver: appium driver
            logger: logging
            xPaths : 断言多个element的xpath列表
            timeout : 超时时间,单位秒,默认十秒。
        return : 返回assert命中element
    '''
    def assertElementsByxPaths(self, testcase, driver, logger, xPaths=[], timeout=10):
        testcase.assertTrue(xPaths, "The xpath list is empty.")
        for xpath in xPaths:
            try:
                return self._findElementByXpath(driver, logger, xpath, timeout)
            except TimeoutException:
                continue
            else:
                continue
        testcase.assertTrue(False, "Can not get elements by xpath list.")


    '''
    ********************************************************************************************
    Android 断言element方法
    ********************************************************************************************
    '''

    '''
        ************************************************************************
        1. Android 断言单一element方法
        ************************************************************************
    '''

    '''
        usage : 页面element验证方法 (适用Android平台)
        parameters:
            testcase: unittest testcase
            driver: appium driver
            logger: logging
            resourceId : 断言element的 resource id
            timeout : 超时时间,单位秒,默认十秒。
    '''
    def assertElementByResourceId(self, testcase, driver, logger, resourceId="default", timeout=10):
        try:
            self._findElementByResourceId(driver, logger, resourceId, timeout)
        except TimeoutException:
            testcase.assertTrue(False, "Get element by resource id [%s] timeout" % (resourceId))
        else:
            testcase.assertTrue(False, "Can not get element by resource id [%s]" % (resourceId))

    '''
        usage : 页面element验证方法 (适用Android平台)
        parameters:
            testcase: unittest testcase
            driver: appium driver
            logger: logging
            className : 断言element的 class name
            timeout : 超时时间,单位秒,默认十秒。
    '''
    def assertElementByClassName(self, testcase, driver, logger, className="default", timeout=10):
        try:
            self._findElementByClassName(driver, logger, className, timeout)
        except TimeoutException:
            testcase.assertTrue(False, "Get element by class name [%s] timeout" % (className))
        else:
            testcase.assertTrue(False, "Can not get element by class name [%s]" % (className))

    '''
        usage : 页面element验证方法 (适用Android平台)
        parameters:
            testcase: unittest testcase
            driver: appium driver
            logger: logging
            text : 断言element的 text
            timeout : 超时时间,单位秒,默认十秒。
    '''
    def assertElementByText(self, testcase, driver, logger, text="default", timeout=10):
        try:
            self._findElementByText(driver, logger, text, timeout)
        except TimeoutException:
            testcase.assertTrue(False, "Get element by text [%s] timeout" % (text))
        else:
            testcase.assertTrue(False, "Can not get element by text [%s]" % (text))

    '''
        usage : 页面element验证方法 (适用Android平台)
        parameters:
            testcase: unittest testcase
            driver: appium driver
            logger: logging
            contentDesc : 断言element的 content description
            timeout : 超时时间,单位秒,默认十秒。
    '''
    def assertElementByContentDesc(self, testcase, driver, logger, contentDesc="default", timeout=10):
        try:
            self._findElementByContentDesc(driver, logger, contentDesc, timeout)
        except TimeoutException:
            testcase.assertTrue(False, "Get element by content description [%s] timeout" % (contentDesc))
        else:
            testcase.assertTrue(False, "Can not get element by content description [%s]" % (contentDesc))

    '''
        usage : 页面element验证方法 (适用Android平台)
        parameters:
            testcase: unittest testcase
            driver: appium driver
            logger: logging
            containsText : 断言element的模糊匹配方法
            timeout : 超时时间,单位秒,默认十秒。
    '''
    def assertElementByContainsText(self, testcase, driver, logger, containsText="default", timeout=10):
        try:
            self._findElementByContainsText(driver, logger, containsText, timeout)
        except TimeoutException:
            testcase.assertTrue(False, "Get element by contains text [%s] timeout" % (containsText))
        else:
            testcase.assertTrue(False, "Can not get element by contains text [%s]" % (containsText))

    '''
        usage : 页面element验证方法 (适用Android平台)
        parameters:
            testcase: unittest testcase
            driver: appium driver
            logger: logging
            textStartWith : 断言element的以text开头的元素
            timeout : 超时时间,单位秒,默认十秒。
    '''
    def assertElementByTextStartWith(self, testcase, driver, logger, textStartWith="default", timeout=10):
        try:
            self._findElementByTextStartWith(driver, logger, textStartWith, timeout)
        except TimeoutException:
            testcase.assertTrue(False, "Get element by text start with [%s] timeout" % (textStartWith))
        else:
            testcase.assertTrue(False, "Can not get element by text start with [%s]" % (textStartWith))


    '''
        ************************************************************************
        2. Android 断言多个element方法 （只需一个验证成功，即为成功）
        ************************************************************************
    '''

    '''
        usage : 页面多个element验证方法 (适用Android平台)
        parameters:
            testcase: unittest testcase
            driver: appium driver
            logger: logging
            resourceIds : 断言多个element的resource id列表
            timeout : 超时时间,单位秒,默认十秒。
        return : 返回assert命中element
    '''
    def assertElementsByResourceIds(self, testcase, driver, logger, resourceIds=[], timeout=10):
        testcase.assertTrue(resourceIds, "The resource id list is empty.")
        for resourceId in resourceIds:
            try:
                return self._findElementByResourceId(driver, logger, resourceId, timeout)
            except TimeoutException:
                continue
            else:
                continue
        testcase.assertTrue(False, "Can not get elements by resource id list.")

    '''
        usage : 页面多个element验证方法 (适用Android平台)
        parameters:
            testcase: unittest testcase
            driver: appium driver
            logger: logging
            classNames : 断言多个element的class name列表
            timeout : 超时时间,单位秒,默认十秒。
        return : 返回assert命中element
    '''
    def assertElementsByClassNames(self, testcase, driver, logger, classNames=[], timeout=10):
        testcase.assertTrue(classNames, "The class name list is empty.")
        for className in classNames:
            try:
                return self._findElementByClassName(driver, logger, className, timeout)
            except TimeoutException:
                continue
            else:
                continue
        testcase.assertTrue(False, "Can not get elements by class name list.")

    '''
        usage : 页面多个element验证方法 (适用Android平台)
        parameters:
            testcase: unittest testcase
            driver: appium driver
            logger: logging
            texts : 断言多个element的text列表
            timeout : 超时时间,单位秒,默认十秒。
        return : 返回assert命中element
    '''
    def assertElementsByTexts(self, testcase, driver, logger, texts=[], timeout=10):
        testcase.assertTrue(texts, "The text list is empty.")
        for text in texts:
            try:
                return self._findElementByText(driver, logger, text, timeout)
            except TimeoutException:
                continue
            else:
                continue
        testcase.assertTrue(False, "Can not get elements by text list.")

    '''
        usage : 页面多个element验证方法 (适用Android平台)
        parameters:
            testcase: unittest testcase
            driver: appium driver
            logger: logging
            contentDescs : 断言多个element的 content description 列表
            timeout : 超时时间,单位秒,默认十秒。
        return : 返回assert命中element
    '''
    def assertElementsByContentDescs(self, testcase, driver, logger, contentDescs=[], timeout=10):
        testcase.assertTrue(contentDescs, "The content description list is empty.")
        for contentDesc in contentDescs:
            try:
                return self._findElementByContentDesc(driver, logger, contentDesc, timeout)
            except TimeoutException:
                continue
            else:
                continue
        testcase.assertTrue(False, "Can not get elements by content description list.")

    '''
        usage : 页面多个element验证方法 (适用Android平台)
        parameters:
            testcase: unittest testcase
            driver: appium driver
            logger: logging
            containsTexts : 断言多个element的 contains text 列表
            timeout : 超时时间,单位秒,默认十秒
        return : 返回assert命中element
    '''
    def assertElementsByContainsTexts(self, testcase, driver, logger, containsTexts=[], timeout=10):
        testcase.assertTrue(containsTexts, "The contains text list is empty.")
        for containsText in containsTexts:
            try:
                return self._findElementByContainsText(driver, logger, containsText, timeout)
            except TimeoutException:
                continue
            else:
                continue
        testcase.assertTrue(False, "Can not get elements by contains text list.")

    '''
        usage : 页面多个element验证方法 (适用Android平台)
        parameters:
            testcase: unittest testcase
            driver: appium driver
            logger: logging
            textStartWiths : 断言多个element的 text start with 列表
            timeout : 超时时间,单位秒,默认十秒。
        return : 返回assert命中element
    '''
    def assertElementsByTextStartWiths(self, testcase, driver, logger, textStartWiths=[], timeout=10):
        testcase.assertTrue(textStartWiths, "The text start with list is empty.")
        for textStartWith in textStartWiths:
            try:
                return self._findElementByTextStartWith(driver, logger, textStartWith, timeout)
            except TimeoutException:
                continue
            else:
                continue
        testcase.assertTrue(False, "Can not get elements by text start with list.")


    '''
    ********************************************************************************************
    IOS 断言方法
    ********************************************************************************************
    '''

    '''
        ************************************************************************
        1. IOS 断言单一element方法
        ************************************************************************
    '''

    '''
        usage : 页面element验证方法 (适用IOS平台)
        parameters:
            testcase: unittest testcase
            driver: appium driver
            logger: logging
            name : 断言element的 name
            timeout : 超时时间,单位秒,默认十秒。
    '''
    def assertElementByName(self, testcase, driver, logger, name="default", timeout=10):
        try:
            self._findElementByResourceId(driver, logger, name, timeout)
        except TimeoutException:
            testcase.assertTrue(False, "Get element by name [%s] timeout" % (name))
        else:
            testcase.assertTrue(False, "Can not get element by name [%s]" % (name))

    '''
        usage : 页面element验证方法 (适用IOS平台)
        parameters:
            testcase: unittest testcase
            driver: appium driver
            logger: logging
            elementType : 断言element的 element type
            timeout : 超时时间,单位秒,默认十秒。
    '''
    def assertElementByType(self, testcase, driver, logger, elementType="default", timeout=10):
        try:
            self._findElementByClassName(driver, logger, elementType, timeout)
        except TimeoutException:
            testcase.assertTrue(False, "Get element by element type [%s] timeout" % (elementType))
        else:
            testcase.assertTrue(False, "Can not get element by element type [%s]" % (elementType))

    '''
        usage : 页面element验证方法 (适用IOS平台)
        parameters:
            testcase: unittest testcase
            driver: appium driver
            logger: logging
            uiaString : 断言element的 uia string
            timeout : 超时时间,单位秒,默认十秒。
    '''
    def assertElementByIosUiautomation(self, testcase, driver, logger, uiaString="default", timeout=10):
        try:
            self._findElementByIosUiautomation(driver, logger, uiaString, timeout)
        except TimeoutException:
            testcase.assertTrue(False, "Get element by uia string [%s] timeout" % (uiaString))
        else:
            testcase.assertTrue(False, "Can not get element by uia string [%s]" % (uiaString))


    '''
        ************************************************************************
        2. IOS 断言多个element方法 （只需一个验证成功，即为成功）
        ************************************************************************
    '''

    '''
        usage : 页面多个element验证方法 (适用IOS平台)
        parameters:
            testcase: unittest testcase
            driver: appium driver
            logger: logging
            names : 断言多个element的 name 列表
            timeout : 超时时间,单位秒,默认十秒。
        return : 返回assert命中element
    '''
    def assertElementsByNames(self, testcase, driver, logger, names=[], timeout=10):
        testcase.assertTrue(names, "The name list is empty.")
        for name in names:
            try:
                return self._findElementByResourceId(driver, logger, name, timeout)
            except TimeoutException:
                continue
            else:
                continue
        testcase.assertTrue(False, "Can not get elements by name list.")

    '''
        usage : 页面多个element验证方法 (适用IOS平台)
        parameters:
            testcase: unittest testcase
            driver: appium driver
            logger: logging
            elementTypes : 断言多个element的 element type 列表
            timeout : 超时时间,单位秒,默认十秒。
        return : 返回assert命中element
    '''
    def assertElementsByElementTypes(self, testcase, driver, logger, elementTypes=[], timeout=10):
        testcase.assertTrue(elementTypes, "The element type list is empty.")
        for elementType in elementTypes:
            try:
                return self._findElementByClassName(driver, logger, elementType, timeout)
            except TimeoutException:
                continue
            else:
                continue
        testcase.assertTrue(False, "Can not get elements by element type list.")

    '''
        usage : 页面多个element验证方法 (适用IOS平台)
        parameters:
            testcase: unittest testcase
            driver: appium driver
            logger: logging
            uiaStrings : 断言多个element的 uia string 列表
            timeout : 超时时间,单位秒,默认十秒。
        return : 返回assert命中element
    '''
    def assertElementsByIosUiautomations(self, testcase, driver, logger, uiaStrings=[], timeout=10):
        testcase.assertTrue(uiaStrings, "The uia string list is empty.")
        for uiaString in uiaStrings:
            try:
                return self._findElementByIosUiautomation(driver, logger, uiaString, timeout)
            except TimeoutException:
                continue
            else:
                continue
        testcase.assertTrue(False, "Can not get elements by uia string list.")


    '''
    ********************************************************************************************
    页面查找element方法
    ********************************************************************************************
    '''
    '''
        ************************************************************************
        1. 查找单一element方法
        ************************************************************************
    '''

    '''
        usage : 显式等待方法
        parameters:
            driver: appium driver
            logger: logging
            resourceId : 查找element的resource id
            timeout : 超时时间,单位秒,默认十秒。
        应用场景 : 查找的element展现时间受网络状态影响,显式等待时间设置后,会最大等待timeout秒,
                  如果小于timeout,element出现,直接进行下一流程,如果等于timeout未出现,
                  抛出TimeoutException异常。
    '''
    def _findElementByResourceId(self, driver, logger, resourceId="default", timeout=10):
        wdw = WebDriverWait(driver=driver, timeout=timeout)
        return wdw.until(EC.presence_of_element_located((By.ID, resourceId)))

    '''
        usage : 显式等待方法
        parameters:
            driver: appium driver
            logger: logging
            xPath : 查找element的xpath
            timeout : 超时时间,单位秒,默认十秒。
        return : 返回查找的element
        应用场景 : 查找的element展现时间受网络状态影响,显式等待时间设置后,会最大等待timeout秒,
                  如果小于timeout,element出现,直接进行下一流程,如果等于timeout未出现,
                  抛出TimeoutException异常。
    '''
    def _findElementByXpath(self, driver, logger, xPath="default", timeout=10):
        wdw = WebDriverWait(driver=driver, timeout=timeout)
        return wdw.until(EC.presence_of_element_located((By.XPATH, xPath)))

    '''
        usage : 显式等待方法
        parameters:
            driver: appium driver
            logger: logging
            className : 查找element的class name
            timeout : 超时时间,单位秒,默认十秒。
        return : 返回查找的element
        应用场景 : 查找的view展现时间受网络状态影响,显式等待时间设置后,会最大等待seconds秒,如果小于seconds view出现,直接进行下一流程,如果等于seconds未出现,raise TimeoutException
    '''
    def _findElementByClassName(self, driver, logger, className="default", timeout=10):
        wdw = WebDriverWait(driver=driver, timeout=timeout)
        return wdw.until(EC.presence_of_element_located((By.CLASS_NAME, className)))

    '''
        usage : 显式等待方法 （只适用Android平台）
        parameters:
            driver: appium driver
            logger: logging
            text : 查找element的text
            timeout : 超时时间,单位秒,默认十秒。
        return : 返回查找的element
        应用场景 : 查找的element展现时间受网络状态影响,显式等待时间设置后,会最大等待timeout秒,
                  如果小于timeout,element出现,直接进行下一流程,如果等于timeout未出现,
                  抛出TimeoutException异常。
    '''
    def _findElementByText(self, driver, logger, text="default", timeout=10):
        wdw = WebDriverWait(driver=driver, timeout=timeout);
        return wdw.until(
            EC.text_to_be_present_in_element((MobileBy.ANDROID_UIAUTOMATOR,
                                              'new UiSelector().text("' + text + '")'),
                                             text))

    '''
        usage : 显式等待方法 （只适用Android平台）
        parameters:
            driver: appium driver
            logger: logging
            contentDesc : 查找element的content description
            timeout : 超时时间,单位秒,默认十秒。
        return : 返回查找的element
        应用场景 : 查找的element展现时间受网络状态影响,显式等待时间设置后,会最大等待timeout秒,
                  如果小于timeout,element出现,直接进行下一流程,如果等于timeout未出现,
                  抛出TimeoutException异常。
    '''
    def _findElementByContentDesc(self, driver, logger, contentDesc="default", timeout=10):
        wdw = WebDriverWait(driver=driver, timeout=timeout);
        return wdw.until(
            EC.presence_of_element_located((MobileBy.ANDROID_UIAUTOMATOR,
                                            'new UiSelector().description("' + contentDesc + '")')))

    '''
        usage : 显式等待方法 （只适用Android平台）
        parameters:
            driver: appium driver
            logger: logging
            containsText : 查找element的模糊匹配方法
            timeout : 超时时间,单位秒,默认十秒。
        return : 返回查找的element
        应用场景 : 查找的element展现时间受网络状态影响,显式等待时间设置后,会最大等待timeout秒,
                  如果小于timeout,element出现,直接进行下一流程,如果等于timeout未出现,
                  抛出TimeoutException异常。
    '''
    def _findElementByContainsText(self, driver, logger, containsText="default", timeout=10):
        wdw = WebDriverWait(driver=driver, timeout=timeout);
        return wdw.until(
            EC.presence_of_element_located((MobileBy.ANDROID_UIAUTOMATOR,
                                            'new UiSelector().textContains("' + containsText + '")')))

    '''
        usage : 显式等待方法 （只适用Android平台）
        parameters:
            driver: appium driver
            logger: logging
            textStartWith : 查找以text开始的element
            timeout : 超时时间,单位秒,默认十秒。
        return : 返回查找的element
        应用场景 : 查找的element展现时间受网络状态影响,显式等待时间设置后,会最大等待timeout秒,
                  如果小于timeout,element出现,直接进行下一流程,如果等于timeout未出现,
                  抛出TimeoutException异常。
    '''
    def _findElementByTextStartWith(self, driver, logger, textStartWith="default", timeout=10):
        wdw = WebDriverWait(driver=driver, timeout=timeout);
        return wdw.until(
            EC.presence_of_element_located((MobileBy.ANDROID_UIAUTOMATOR,
                                            'new UiSelector().textStartWith("' + textStartWith + '")')))

    '''
        usage : 显式等待方法 （只适用IOS平台）
        parameters:
            driver: appium driver
            logger: logging
            uiaString : 查找element的instruments
            timeout : 超时时间,单位秒,默认十秒。
        return : 返回查找的element
        应用场景 : 查找的element展现时间受网络状态影响,显式等待时间设置后,会最大等待timeout秒,
                  如果小于timeout,element出现,直接进行下一流程,如果等于timeout未出现,
                  抛出TimeoutException异常。
    '''
    def _findElementByIosUiautomation(self, driver, logger, uiaString="default", timeout=10):
        wdw = WebDriverWait(driver=driver, timeout=timeout);
        return wdw.until(
            EC.presence_of_element_located((MobileBy.IOS_UIAUTOMATION, uiaString)))


    '''
        ************************************************************************
        2. 查找多个相同属性element方法
        ************************************************************************
    '''

    '''
        usage : 显式等待方法
        parameters:
            driver: appium driver
            logger: logging
            resourceId : 查找element的resource id
            timeout : 超时时间,单位秒,默认十秒。
        return : 返回查找的element列表
        应用场景 : 查找的element展现时间受网络状态影响,显式等待时间设置后,会最大等待timeout秒,
                  如果小于timeout,element出现,直接进行下一流程,如果等于timeout未出现,
                  抛出TimeoutException异常。
    '''
    def _findElementsByResourceId(self, driver, logger, resourceId="default", timeout=10):
        wdw = WebDriverWait(driver=driver, timeout=timeout)
        return wdw.until(EC.presence_of_all_elements_located((By.ID, resourceId)))

    '''
        usage : 显式等待方法
        parameters:
            driver: appium driver
            logger: logging
            className : 查找element的class name
            timeout : 超时时间,单位秒,默认十秒。
        return : 返回查找的element列表
        应用场景 : 查找的view展现时间受网络状态影响,显式等待时间设置后,会最大等待seconds秒,如果小于seconds view出现,直接进行下一流程,如果等于seconds未出现,raise TimeoutException
    '''
    def _findElementsByClassName(self, driver, logger, className="default", timeout=10):
        wdw = WebDriverWait(driver=driver, timeout=timeout)
        return wdw.until(EC.presence_of_all_elements_located((By.CLASS_NAME, className)))

    '''
        usage : 显式等待方法 （只适用Android平台）
        parameters:
            driver: appium driver
            logger: logging
            text : 查找element的text
            timeout : 超时时间,单位秒,默认十秒。
        return : 返回查找的element列表
        应用场景 : 查找的element展现时间受网络状态影响,显式等待时间设置后,会最大等待timeout秒,
                  如果小于timeout,element出现,直接进行下一流程,如果等于timeout未出现,
                  抛出TimeoutException异常。
    '''
    def _findElementsByText(self, driver, logger, text="default", timeout=10):
        wdw = WebDriverWait(driver=driver, timeout=timeout);
        return wdw.until(
            EC.presence_of_all_elements_located((MobileBy.ANDROID_UIAUTOMATOR,
                                                 'new UiSelector().text("' + text + '")')))

    '''
        usage : 显式等待方法 （只适用Android平台）
        parameters:
            driver: appium driver
            logger: logging
            contentDesc : 查找element的content description
            timeout : 超时时间,单位秒,默认十秒。
        return : 返回查找的element列表
        应用场景 : 查找的element展现时间受网络状态影响,显式等待时间设置后,会最大等待timeout秒,
                  如果小于timeout,element出现,直接进行下一流程,如果等于timeout未出现,
                  抛出TimeoutException异常。
    '''
    def _findElementsByContentDesc(self, driver, logger, contentDesc="default", timeout=10):
        wdw = WebDriverWait(driver=driver, timeout=timeout);
        return wdw.until(
            EC.presence_of_all_elements_located((MobileBy.ANDROID_UIAUTOMATOR,
                                                 'new UiSelector().description("' + contentDesc + '")')))

    '''
        usage : 显式等待方法 （只适用Android平台）
        parameters:
            driver: appium driver
            logger: logging
            containsText : 查找element的模糊匹配方法
            timeout : 超时时间,单位秒,默认十秒。
        return : 返回查找的element列表
        应用场景 : 查找的element展现时间受网络状态影响,显式等待时间设置后,会最大等待timeout秒,
                  如果小于timeout,element出现,直接进行下一流程,如果等于timeout未出现,
                  抛出TimeoutException异常。
    '''
    def _findElementsByContainsText(self, driver, logger, containsText="default", timeout=10):
        wdw = WebDriverWait(driver=driver, timeout=timeout);
        return wdw.until(
            EC.presence_of_all_elements_located((MobileBy.ANDROID_UIAUTOMATOR,
                                                 'new UiSelector().textContains("' + containsText + '")')))

    '''
        usage : 显式等待方法 （只适用Android平台）
        parameters:
            driver: appium driver
            logger: logging
            textStartWith : 查找以text开始的element
            timeout : 超时时间,单位秒,默认十秒。
        return : 返回查找的element列表
        应用场景 : 查找的element展现时间受网络状态影响,显式等待时间设置后,会最大等待timeout秒,
                  如果小于timeout,element出现,直接进行下一流程,如果等于timeout未出现,
                  抛出TimeoutException异常。
    '''
    def _findElementsByTextStartWith(self, driver, logger, textStartWith="default", timeout=10):
        wdw = WebDriverWait(driver=driver, timeout=timeout);
        return wdw.until(
            EC.presence_of_all_elements_located((MobileBy.ANDROID_UIAUTOMATOR,
                                                 'new UiSelector().textStartWith("' + textStartWith + '")')))

    '''
        usage : 显式等待方法 （只适用IOS平台）
        parameters:
            driver: appium driver
            logger: logging
            uiaString : 查找element的instruments
            timeout : 超时时间,单位秒,默认十秒。
        return : 返回查找的element列表
        应用场景 : 查找的element展现时间受网络状态影响,显式等待时间设置后,会最大等待timeout秒,
                  如果小于timeout,element出现,直接进行下一流程,如果等于timeout未出现,
                  抛出TimeoutException异常。
    '''
    def _findElementsByIosUiautomation(self, driver, logger, uiaString="default", timeout=10):
        wdw = WebDriverWait(driver=driver, timeout=timeout);
        return wdw.until(
            EC.presence_of_all_elements_located((MobileBy.IOS_UIAUTOMATION, uiaString)))
