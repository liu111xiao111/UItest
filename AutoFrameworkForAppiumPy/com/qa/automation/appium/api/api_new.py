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
    def scroll(self, driver, logger, start_x, start_y, end_x, end_y, duration=None):
        '''
        Usage: 界面滑动方法
        parameters:
            start_x:  起始 x 轴坐标
            start_y: 起始 y 轴坐标
            end_x: 结束 x 轴坐标
            end_y: 结束 y 轴坐标
            duration: 滑动时间，单位ms
        '''
        driver.swipe(start_x, start_y, end_x, end_y, duration)

    def getWidthOfDevice(self, driver, logger):
        '''
        Usage: 获取当前设备屏幕宽度方法
        parameters:
            driver: appium driver
            logger: logging
        return: 返回当前设备屏幕宽度
        '''
        width = driver.get_window_size()['width']
        return width

    def getHeightOfDevice(self, driver, logger):
        '''
        Usage: 获取当前设备屏幕高度方法
        parameters:
            driver: appium driver
            logger: logging
        return: 返回当前设备屏幕高度
        '''
        height = driver.get_window_size()['height']
        return height

    def waitBySeconds(self, timeout=1):
        '''
        Usage: 等待方法
        parameters:
            timeout: 等待时间，单位秒
        '''
        time.sleep(timeout)

    def screenShot(self, driver, pic_name="myfeifan_auto_test"):
        '''
        Usage: 截图方法
        parameters:
            driver: appium driver
            pic_name: 截图名称
        '''
        driver.save_screenshot(pic_name + ".png")

    def inputStringByXpath(self, testcase, driver, logger, xpath, string, timeout=10):
        '''
        usage : 页面输入方法
        parameters:
            testcase: unittest testcase
            driver: appium driver
            logger: logging
            xpath : 页面element的 xpath属性
            string : 需要输入的值
            timeout: 超时时间,单位秒,默认十秒。
        '''
        try:
            input_field = self._findElementByXpath(driver, logger, xpath, timeout)
        except TimeoutException:
            testcase.assertTrue(False, "Get element by xpath [%s] timeout" % (xpath))
        except:
            testcase.assertTrue(False, "Can not get element by xpath [%s]" % (xpath))

        input_field.click()
        input_field.send_keys(string)

    '''
    ********************************************************************************************
    Android平台基本方法
    ********************************************************************************************
    '''
    def clickBackKeyForAndroid(self, driver, logger):
        '''
        usage : 点击返回按钮方法 （适用Android平台）
        parameters:
            driver: appium driver
            logger: logging
        '''
        driver.press_keycode(4)
        time.sleep(2)

    def scrollToText(self, driver, logger, text):
        '''
        usage : 滑动页面到指定文本控件方法 （适用Android平台）
        parameters:
            driver: appium driver
            logger: logging
            text: 页面element的text属性
        '''
        driver.find_element_by_android_uiautomator(
            'new UiScrollable(new UiSelector().scrollable(true).instance(0)).'
            'scrollIntoView(new UiSelector().text("%s").instance(0))' % (text))

    def inputStringByResourceId(self, testcase, driver, logger, resourceId, string, timeout=10):
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
        try:
            input_field = self._findElementByResourceId(driver, logger, resourceId, timeout)
        except TimeoutException:
            testcase.assertTrue(False, "Get element by resource id [%s] timeout" % (resourceId))
        except:
            testcase.assertTrue(False, "Can not get element by resource id [%s]" % (resourceId))

        input_field.click()
        input_field.send_keys(string)

    def inputStringByClassName(self, testcase, driver, logger, className, string, timeout=10):
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
        try:
            input_field = self._findElementByClassName(driver, logger, className, timeout)
        except TimeoutException:
            testcase.assertTrue(False, "Get element by class name [%s] timeout" % (className))
        except:
            testcase.assertTrue(False, "Can not get element by class name [%s]" % (className))

        input_field.click()
        input_field.send_keys(string)


    '''
    ********************************************************************************************
    IOS 平台基本方法
    ********************************************************************************************
    '''
    def clickBackKeyForIos(self, testcase, driver, logger, xpath, timeout=10):
        '''
        usage : 点击返回按钮方法 （适用IOS平台）
        parameters:
            testcase: unittest testcase
            driver: appium driver
            logger: logging
            xpath : 页面返回按钮的 xpath属性
            timeout : 超时时间,单位秒,默认十秒。
        '''
        self.clickElementByXpath(testcase, driver, logger, xpath, timeout)
        time.sleep(2)

    def inputStringByName(self, testcase, driver, logger, name, string, timeout=10):
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
        try:
            input_field = self._findElementByResourceId(driver, logger, name, timeout)
        except TimeoutException:
            testcase.assertTrue(False, "Get element by name [%s] timeout" % (name))
        except:
            testcase.assertTrue(False, "Can not get element by name [%s]" % (name))

        input_field.click()
        input_field.send_keys(string)

    def inputStringByType(self, testcase, driver, logger, elementType, string, timeout=10):
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
        try:
            input_field = self._findElementByClassName(driver, logger, elementType, timeout)
        except TimeoutException:
            testcase.assertTrue(False, "Get element by element type [%s] timeout" % (elementType))
        except:
            testcase.assertTrue(False, "Can not get element by element type [%s]" % (elementType))

        input_field.click()
        input_field.send_keys(string)


    '''
    ********************************************************************************************
    Android 获取多个element方法
    ********************************************************************************************
    '''
    def getElementsByResourceId(self, testcase, driver, logger, resourceId="default", timeout=10):
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
        try:
            return self._findElementsByResourceId(driver, logger, resourceId, timeout)
        except TimeoutException:
            testcase.assertTrue(False, "Get elements by resource id [%s] timeout" % (resourceId))
        except:
            testcase.assertTrue(False, "Can not get elements by resource id [%s]" % (resourceId))

    def getElementsByClassName(self, testcase, driver, logger, className="default", timeout=10):
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
        try:
            return self._findElementsByClassName(driver, logger, className, timeout)
        except TimeoutException:
            testcase.assertTrue(False, "Get elements by class name [%s] timeout" % (className))
        except:
            testcase.assertTrue(False, "Can not get elements by class name [%s]" % (className))

    def getElementsByText(self, testcase, driver, logger, text="default", timeout=10):
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
        try:
            return self._findElementsByText(driver, logger, text, timeout)
        except TimeoutException:
            testcase.assertTrue(False, "Get elements by text [%s] timeout" % (text))
        except:
            testcase.assertTrue(False, "Can not get elements by text [%s]" % (text))

    def getElementsByContentDesc(self, testcase, driver, logger, contentDesc="default", timeout=10):
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
        try:
            return self._findElementsByContentDesc(driver, logger, contentDesc, timeout)
        except TimeoutException:
            testcase.assertTrue(False, "Get elements by content description [%s] timeout" % (contentDesc))
        except:
            testcase.assertTrue(False, "Can not get elements by content description [%s]" % (contentDesc))

    def getElementsByContainsText(self, testcase, driver, logger, containsText="default", timeout=10):
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
        try:
            return self._findElementsByContainsText(driver, logger, containsText, timeout)
        except TimeoutException:
            testcase.assertTrue(False, "Get elements by contains text [%s] timeout" % (containsText))
        except:
            testcase.assertTrue(False, "Can not get elements by contains text [%s]" % (containsText))

    def getElementsByTextStartWith(self, testcase, driver, logger, textStartWith="default", timeout=10):
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
        try:
            return self._findElementsByTextStartWith(driver, logger, textStartWith, timeout)
        except TimeoutException:
            testcase.assertTrue(False, "Get elements by text start with [%s] timeout" % (textStartWith))
        except:
            testcase.assertTrue(False, "Can not get elements by text start with [%s]" % (textStartWith))


    '''
    ********************************************************************************************
    IOS 获取多个element方法
    ********************************************************************************************
    '''
    def getElementsByName(self, testcase, driver, logger, name="default", timeout=10):
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
        try:
            return self._findElementsByResourceId(driver, logger, name, timeout)
        except TimeoutException:
            testcase.assertTrue(False, "Get elements by name [%s] timeout" % (name))
        except:
            testcase.assertTrue(False, "Can not get elements by name [%s]" % (name))

    def getElementsByType(self, testcase, driver, logger, elementType="default", timeout=10):
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
        try:
            return self._findElementsByClassName(driver, logger, elementType, timeout)
        except TimeoutException:
            testcase.assertTrue(False, "Get elements by element type [%s] timeout" % (elementType))
        except:
            testcase.assertTrue(False, "Can not get elements by element type [%s]" % (elementType))

    def getElementsByIosUiautomation(self, testcase, driver, logger, uiaString="default", timeout=10):
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
        try:
            return self._findElementsByIosUiautomation(driver, logger, uiaString, timeout)
        except TimeoutException:
            testcase.assertTrue(False, "Get elements by uia string [%s] timeout" % (uiaString))
        except:
            testcase.assertTrue(False, "Can not get elements by uia string [%s]" % (uiaString))


    '''
    ********************************************************************************************
    通用获取element text方法
    ********************************************************************************************
    '''
    def getTextByXpath(self, testcase, driver, logger, xpath="default", timeout=10):
        '''
        usage : 获取页面element text方法
        parameters:
            testcase: unittest testcase
            driver: appium driver
            logger: logging
            xpath : 页面element的 xpath
            timeout : 超时时间,单位秒,默认十秒。
        return : 返回element text
        '''
        try:
            return self._findElementByXpath(driver, logger, xpath, timeout).text
        except TimeoutException:
            testcase.assertTrue(False, "Get element text by xpath [%s] timeout" % (xpath))
        except:
            testcase.assertTrue(False, "Can not get element text by xpath [%s]" % (xpath))


    '''
    ********************************************************************************************
    Android 获取element text方法
    ********************************************************************************************
    '''
    def getTextByResourceId(self, testcase, driver, logger, resourceId="default", timeout=10):
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
        try:
            return self._findElementByResourceId(driver, logger, resourceId, timeout).text
        except TimeoutException:
            testcase.assertTrue(False, "Get element text by resource id [%s] timeout" % (resourceId))
        except:
            testcase.assertTrue(False, "Can not get element text by resource id [%s]" % (resourceId))

    def getTextByClassName(self, testcase, driver, logger, className="default", timeout=10):
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
        try:
            return self._findElementByClassName(driver, logger, className, timeout).text
        except TimeoutException:
            testcase.assertTrue(False, "Get element text by class name [%s] timeout" % (className))
        except:
            testcase.assertTrue(False, "Can not get element text by class name [%s]" % (className))

    def getTextByContainsText(self, testcase, driver, logger, containsText="default", timeout=10):
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
        try:
            return self._findElementByContainsText(driver, logger, containsText, timeout).text
        except TimeoutException:
            testcase.assertTrue(False, "Get element text by contains text [%s] timeout" % (containsText))
        except:
            testcase.assertTrue(False, "Can not get element text by contains text [%s]" % (containsText))

    def getTextByTextStartWith(self, testcase, driver, logger, textStartWith="default", timeout=10):
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
        try:
            return self._findElementByTextStartWith(driver, logger, textStartWith, timeout).text
        except TimeoutException:
            testcase.assertTrue(False, "Get element text by text start with [%s] timeout" % (textStartWith))
        except:
            testcase.assertTrue(False, "Can not get element text by text start with [%s]" % (textStartWith))


    '''
    ********************************************************************************************
    IOS 获取element text方法
    ********************************************************************************************
    '''
    def getTextByType(self, testcase, driver, logger, elementType="default", timeout=10):
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
        try:
            return self._findElementByClassName(driver, logger, elementType, timeout).text
        except TimeoutException:
            testcase.assertTrue(False, "Get element text by element type [%s] timeout" % (elementType))
        except:
            testcase.assertTrue(False, "Can not get element text by element type [%s]" % (elementType))

    def getTextByIosUiautomation(self, testcase, driver, logger, uiaString="default", timeout=10):
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
        try:
            return self._findElementByIosUiautomation(driver, logger, uiaString, timeout).text
        except TimeoutException:
            testcase.assertTrue(False, "Get element text by uia string [%s] timeout" % (uiaString))
        except:
            testcase.assertTrue(False, "Can not get element text by uia string [%s]" % (uiaString))


    '''
    ********************************************************************************************
    通用点击操作方法
    ********************************************************************************************
    '''
    def clickElementByXpath(self, testcase, driver, logger, xpath="default", timeout=10):
        '''
        usage : 页面element点击操作方法
        parameters:
            testcase: unittest testcase
            driver: appium driver
            logger: logging
            xpath : 点击element的 xpath
            timeout : 超时时间,单位秒,默认十秒。
        '''
        try:
            self._findElementByXpath(driver, logger, xpath, timeout).click()
        except TimeoutException:
            testcase.assertTrue(False, "Click element by xpath [%s] timeout" % (xpath))
        except:
            testcase.assertTrue(False, "Can not click element by xpath [%s]" % (xpath))


    '''
    ********************************************************************************************
    Android 点击操作方法
    ********************************************************************************************
    '''
    def clickElementByResourceId(self, testcase, driver, logger, resourceID, timeout=10):
        '''
        usage : 页面element点击操作方法 （适用Android平台）
        parameters:
            testcase: unittest testcase
            driver: appium driver
            logger: logging
            resourceID : 断言element的 resource id
            timeout : 超时时间,单位秒,默认十秒。
        '''
        try:
            self._findElementByResourceID(driver, logger, resourceID, timeout).click()
        except TimeoutException:
            testcase.assertTrue(False, "Click element by resource id [%s] timeout" % (resourceID))
        except:
            testcase.assertTrue(False, "Can not click element by resource id [%s]" % (resourceID))

    def clickElementByClassName(self, testcase, driver, logger, className, timeout=10):
        '''
        usage : 页面element点击操作方法 （适用Android平台）
        parameters:
            testcase: unittest testcase
            driver: appium driver
            logger: logging
            className : 断言element的 class name
            timeout : 超时时间,单位秒,默认十秒。
        '''
        try:
            self._findElementByClassName(driver, logger, className, timeout).click()
        except TimeoutException:
            testcase.assertTrue(False, "Click element by class name [%s] timeout" % (className))
        except:
            testcase.assertTrue(False, "Can not click element by class name [%s]" % (className))

    def clickElementByText(self, testcase, driver, logger, text, timeout=10):
        '''
        usage : 页面element点击操作方法 （适用Android平台）
        parameters:
            testcase: unittest testcase
            driver: appium driver
            logger: logging
            text : 断言element的 text
            timeout : 超时时间,单位秒,默认十秒。
        '''
        try:
            self._findElementByText(driver, logger, text, timeout).click()
        except TimeoutException:
            testcase.assertTrue(False, "Click element by text [%s] timeout" % (text))
        except:
            testcase.assertTrue(False, "Can not click element by text [%s]" % (text))

    def clickElementByContentDesc(self, testcase, driver, logger, contentDesc, timeout=10):
        '''
        usage : 页面element点击操作方法 （适用Android平台）
        parameters:
            testcase: unittest testcase
            driver: appium driver
            logger: logging
            contentDesc : 断言element的 content description
            timeout : 超时时间,单位秒,默认十秒。
        '''
        try:
            self._findElementByContentDesc(driver, logger, contentDesc, timeout).click()
        except TimeoutException:
            testcase.assertTrue(False, "Click element by content description [%s] timeout" % (contentDesc))
        except:
            testcase.assertTrue(False, "Can not click element by content description [%s]" % (contentDesc))

    def clickElementByContainsText(self, testcase, driver, logger, containsText, timeout=10):
        '''
        usage : 页面element点击操作方法 （适用Android平台）
        parameters:
            testcase: unittest testcase
            driver: appium driver
            logger: logging
            contentDesc : 断言element的 contains text
            timeout : 超时时间,单位秒,默认十秒。
        '''
        try:
            self._findElementByContainsText(driver, logger, containsText, timeout).click()
        except TimeoutException:
            testcase.assertTrue(False, "Click element by contains text [%s] timeout" % (containsText))
        except:
            testcase.assertTrue(False, "Can not click element by contains text [%s]" % (containsText))

    def clickElementByTextStartWith(self, testcase, driver, logger, textStartWith, timeout=10):
        '''
        usage : 页面element点击操作方法 （适用Android平台）
        parameters:
            testcase: unittest testcase
            driver: appium driver
            logger: logging
            textStartWith : 断言element的 text start with
            timeout : 超时时间,单位秒,默认十秒。
        '''
        try:
            self._findElementByTextStartWith(driver, logger, textStartWith, timeout).click()
        except TimeoutException:
            testcase.assertTrue(False, "Click element by text start with [%s] timeout" % (textStartWith))
        except:
            testcase.assertTrue(False, "Can not click element by text start with [%s]" % (textStartWith))


    '''
    ********************************************************************************************
    IOS 点击操作方法
    ********************************************************************************************
    '''
    def clickElementByName(self, testcase, driver, logger, name, timeout=10):
        '''
        usage : 页面element点击操作方法 （适用IOS平台）
        parameters:
            testcase: unittest testcase
            driver: appium driver
            logger: logging
            name : 断言element的 name
            timeout : 超时时间,单位秒,默认十秒。
        '''
        try:
            self._findElementByResourceId(driver, logger, name, timeout).click()
        except TimeoutException:
            testcase.assertTrue(False, "Click element by name [%s] timeout" % (name))
        except:
            testcase.assertTrue(False, "Can not click element by name [%s]" % (name))

    def clickElementByType(self, testcase, driver, logger, elementType, timeout=10):
        '''
        usage : 页面element点击操作方法 （适用IOS平台）
        parameters:
            testcase: unittest testcase
            driver: appium driver
            logger: logging
            elementType : 断言element的 element type
            timeout : 超时时间,单位秒,默认十秒。
        '''
        try:
            self._findElementByClassName(driver, logger, elementType, timeout).click()
        except TimeoutException:
            testcase.assertTrue(False, "Click element by element type [%s] timeout" % (elementType))
        except:
            testcase.assertTrue(False, "Can not click element by element type [%s]" % (elementType))

    def clickElementByIosUiautomation(self, testcase, driver, logger, uiaString, timeout=10):
        '''
        usage : 页面element点击操作方法 （适用IOS平台）
        parameters:
            testcase: unittest testcase
            driver: appium driver
            logger: logging
            uiaString : 断言element的 uia string
            timeout : 超时时间,单位秒,默认十秒。
        '''
        try:
            self._findElementByIosUiautomation(driver, logger, uiaString, timeout)
        except TimeoutException:
            testcase.assertTrue(False, "Click element by uia string [%s] timeout" % (uiaString))
        except:
            testcase.assertTrue(False, "Can not click element by uia string [%s]" % (uiaString))


    '''
    ********************************************************************************************
    通用验证element方法
    ********************************************************************************************
    '''
    def validElementByXpath(self, testcase, driver, logger, xpath="default", timeout=10):
        '''
        usage : 页面element验证方法
        parameters:
            testcase: unittest testcase
            driver: appium driver
            logger: logging
            xpath : 验证element的 xpath
            timeout : 超时时间,单位秒,默认十秒。
        return: element或false
        '''
        try:
            return self._findElementByXpath(driver, logger, xpath, timeout)
        except:
            return False


    '''
    ********************************************************************************************
    Android 验证element方法
    ********************************************************************************************
    '''
    def validElementByResourceId(self, testcase, driver, logger, resourceId="default", timeout=10):
        '''
        usage : 页面element验证方法 (适用Android平台)
        parameters:
            testcase: unittest testcase
            driver: appium driver
            logger: logging
            resourceId : 验证element的 resource id
            timeout : 超时时间,单位秒,默认十秒。
        return: element或false
        '''
        try:
            return self._findElementByResourceId(driver, logger, resourceId, timeout)
        except:
            return False

    def validElementByClassName(self, testcase, driver, logger, className="default", timeout=10):
        '''
        usage : 页面element验证方法 (适用Android平台)
        parameters:
            testcase: unittest testcase
            driver: appium driver
            logger: logging
            className : 验证element的 class name
            timeout : 超时时间,单位秒,默认十秒。
        return: element或false
        '''
        try:
            return self._findElementByClassName(driver, logger, className, timeout)
        except:
            return False

    def validElementByText(self, testcase, driver, logger, text="default", timeout=10):
        '''
        usage : 页面element验证方法 (适用Android平台)
        parameters:
            testcase: unittest testcase
            driver: appium driver
            logger: logging
            text : 验证element的 text
            timeout : 超时时间,单位秒,默认十秒。
        return: element或false
        '''
        try:
            return self._findElementByText(driver, logger, text, timeout)
        except:
            return False

    def validElementByContentDesc(self, testcase, driver, logger, contentDesc="default", timeout=10):
        '''
        usage : 页面element验证方法 (适用Android平台)
        parameters:
            testcase: unittest testcase
            driver: appium driver
            logger: logging
            contentDesc : 验证element的 content description
            timeout : 超时时间,单位秒,默认十秒。
        return: element或false
        '''
        try:
            return self._findElementByContentDesc(driver, logger, contentDesc, timeout)
        except:
            return False

    def validElementByContainsText(self, testcase, driver, logger, containsText="default", timeout=10):
        '''
        usage : 页面element验证方法 (适用Android平台)
        parameters:
            testcase: unittest testcase
            driver: appium driver
            logger: logging
            containsText : 验证element的模糊匹配方法
            timeout : 超时时间,单位秒,默认十秒。
        return: element或false
        '''
        try:
            return self._findElementByContainsText(driver, logger, containsText, timeout)
        except:
            return False

    def validElementByTextStartWith(self, testcase, driver, logger, textStartWith="default", timeout=10):
        '''
        usage : 页面element验证方法 (适用Android平台)
        parameters:
            testcase: unittest testcase
            driver: appium driver
            logger: logging
            textStartWith : 验证element的以text开头的元素
            timeout : 超时时间,单位秒,默认十秒。
        return: element或false
        '''
        try:
            return self._findElementByTextStartWith(driver, logger, textStartWith, timeout)
        except:
            return False


    '''
    ********************************************************************************************
    IOS 验证方法
    ********************************************************************************************
    '''
    def validElementByName(self, testcase, driver, logger, name="default", timeout=10):
        '''
        usage : 页面element验证方法 (适用IOS平台)
        parameters:
            testcase: unittest testcase
            driver: appium driver
            logger: logging
            name : 验证element的 name
            timeout : 超时时间,单位秒,默认十秒。
        return: element或false
        '''
        try:
            return self._findElementByResourceId(driver, logger, name, timeout)
        except:
            return False

    def validElementByType(self, testcase, driver, logger, elementType="default", timeout=10):
        '''
        usage : 页面element验证方法 (适用IOS平台)
        parameters:
            testcase: unittest testcase
            driver: appium driver
            logger: logging
            elementType : 验证element的 type
            timeout : 超时时间,单位秒,默认十秒。
        return: element或false
        '''
        try:
            return self._findElementByClassName(driver, logger, elementType, timeout)
        except:
            return False

    def validElementByIosUiautomation(self, testcase, driver, logger, uiaString="default", timeout=10):
        '''
        usage : 页面element验证方法 (适用IOS平台)
        parameters:
            testcase: unittest testcase
            driver: appium driver
            logger: logging
            uiaString : 验证element的 uia string
            timeout : 超时时间,单位秒,默认十秒。
        '''
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
    def assertElementByXpath(self, testcase, driver, logger, xpath="default", timeout=10):
        '''
        usage : 页面element验证方法
        parameters:
            testcase: unittest testcase
            driver: appium driver
            logger: logging
            xpath : 断言element的 xpath
            timeout : 超时时间,单位秒,默认十秒。
        '''
        try:
            self._findElementByXpath(driver, logger, xpath, timeout)
        except TimeoutException:
            testcase.assertTrue(False, "Get element by xpath [%s] timeout" % (xpath))
        except:
            testcase.assertTrue(False, "Can not get element by xpath [%s]" % (xpath))


    '''
        ************************************************************************
        2. 通用断言多个element方法 （只需一个验证成功，即为成功）
        ************************************************************************
    '''
    def assertElementsByXpaths(self, testcase, driver, logger, xpaths=[], timeout=10):
        '''
        usage : 页面多个element验证方法
        parameters:
            testcase: unittest testcase
            driver: appium driver
            logger: logging
            xpaths : 断言多个element的xpath列表
            timeout : 超时时间,单位秒,默认十秒。
        return : 返回assert命中element
        '''
        testcase.assertTrue(xpaths, "The xpath list is empty.")
        for xpath in xpaths:
            try:
                return self._findElementByXpath(driver, logger, xpath, timeout)
            except TimeoutException:
                continue
            except:
                continue
        testcase.assertTrue(False, "Can not get elements by xpath list.")


    '''
        ************************************************************************
        3. 通用断言值方法
        ************************************************************************
    '''
    def assertEqual(self, test_case, logger, actual_text, expect_text):
        '''
        usage : 断言传入值相等
        parameters:
            testcase: unittest testcase
            logger: logging
            actual_text : 当前值
            expect_text : 预期值
        '''
        test_case.assertEqual(actual_text, expect_text,
                              msg="Actual text : %s != Expected text : %s" % (actual_text, expect_text))

    def assertNotEqual(self, test_case, logger, actual_text, expect_text):
        '''
        usage : 断言传入值不相等
        parameters:
            testcase: unittest testcase
            logger: logging
            actual_text : 当前值
            expect_text : 预期值
        '''
        test_case.assertNotEqual(actual_text, expect_text,
                                 msg="Actual text : %s == Expected text : %s" % (actual_text, expect_text))

    def assertGreaterEqual(self, test_case, logger, list_len, expect_num):
        '''
        usage : 断言传入值大于等于预期值
        parameters:
            testcase: unittest testcase
            logger: logging
            list_len : 当前值
            expect_text : 预期值
        '''
        test_case.assertGreaterEqual(list_len, expect_num,
                                     msg="Actual text : %s !> Expected text : %s" % (list_len, expect_num))

    def assertTrue(self, test_case, logger, result=True):
        '''
        usage : 断言传入值正确
        parameters:
            testcase: unittest testcase
            logger: logging
            result : 传入值
        '''
        test_case.assertTrue(result,
                             msg="Actual result : %s != Expected result : %s" % (result, True))

    def assertFalse(self, test_case, logger, result=False):
        '''
        usage : 断言传入值错误
        parameters:
            testcase: unittest testcase
            logger: logging
            result : 传入值
        '''
        test_case.assertFalse(result,
                             msg="Actual result : %s != Expected result : %s" % (result, False))


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
    def assertElementByResourceId(self, testcase, driver, logger, resourceId="default", timeout=10):
        '''
        usage : 页面element验证方法 (适用Android平台)
        parameters:
            testcase: unittest testcase
            driver: appium driver
            logger: logging
            resourceId : 断言element的 resource id
            timeout : 超时时间,单位秒,默认十秒。
        '''
        try:
            self._findElementByResourceId(driver, logger, resourceId, timeout)
        except TimeoutException:
            testcase.assertTrue(False, "Get element by resource id [%s] timeout" % (resourceId))
        except:
            testcase.assertTrue(False, "Can not get element by resource id [%s]" % (resourceId))

    def assertElementByClassName(self, testcase, driver, logger, className="default", timeout=10):
        '''
        usage : 页面element验证方法 (适用Android平台)
        parameters:
            testcase: unittest testcase
            driver: appium driver
            logger: logging
            className : 断言element的 class name
            timeout : 超时时间,单位秒,默认十秒。
        '''
        try:
            self._findElementByClassName(driver, logger, className, timeout)
        except TimeoutException:
            testcase.assertTrue(False, "Get element by class name [%s] timeout" % (className))
        except:
            testcase.assertTrue(False, "Can not get element by class name [%s]" % (className))

    def assertElementByText(self, testcase, driver, logger, text="default", timeout=10):
        '''
        usage : 页面element验证方法 (适用Android平台)
        parameters:
            testcase: unittest testcase
            driver: appium driver
            logger: logging
            text : 断言element的 text
            timeout : 超时时间,单位秒,默认十秒。
        '''
        try:
            self._findElementByText(driver, logger, text, timeout)
        except TimeoutException:
            testcase.assertTrue(False, "Get element by text [%s] timeout" % (text))
        except:
            testcase.assertTrue(False, "Can not get element by text [%s]" % (text))

    def assertElementByContentDesc(self, testcase, driver, logger, contentDesc="default", timeout=10):
        '''
        usage : 页面element验证方法 (适用Android平台)
        parameters:
            testcase: unittest testcase
            driver: appium driver
            logger: logging
            contentDesc : 断言element的 content description
            timeout : 超时时间,单位秒,默认十秒。
        '''
        try:
            self._findElementByContentDesc(driver, logger, contentDesc, timeout)
        except TimeoutException:
            testcase.assertTrue(False, "Get element by content description [%s] timeout" % (contentDesc))
        except:
            testcase.assertTrue(False, "Can not get element by content description [%s]" % (contentDesc))

    def assertElementByContainsText(self, testcase, driver, logger, containsText="default", timeout=10):
        '''
        usage : 页面element验证方法 (适用Android平台)
        parameters:
            testcase: unittest testcase
            driver: appium driver
            logger: logging
            containsText : 断言element的模糊匹配方法
            timeout : 超时时间,单位秒,默认十秒。
        '''
        try:
            self._findElementByContainsText(driver, logger, containsText, timeout)
        except TimeoutException:
            testcase.assertTrue(False, "Get element by contains text [%s] timeout" % (containsText))
        except:
            testcase.assertTrue(False, "Can not get element by contains text [%s]" % (containsText))

    def assertElementByTextStartWith(self, testcase, driver, logger, textStartWith="default", timeout=10):
        '''
        usage : 页面element验证方法 (适用Android平台)
        parameters:
            testcase: unittest testcase
            driver: appium driver
            logger: logging
            textStartWith : 断言element的以text开头的元素
            timeout : 超时时间,单位秒,默认十秒。
        '''
        try:
            self._findElementByTextStartWith(driver, logger, textStartWith, timeout)
        except TimeoutException:
            testcase.assertTrue(False, "Get element by text start with [%s] timeout" % (textStartWith))
        except:
            testcase.assertTrue(False, "Can not get element by text start with [%s]" % (textStartWith))


    '''
        ************************************************************************
        2. Android 断言多个element方法 （只需一个验证成功，即为成功）
        ************************************************************************
    '''
    def assertElementsByResourceIds(self, testcase, driver, logger, resourceIds=[], timeout=10):
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
        testcase.assertTrue(resourceIds, "The resource id list is empty.")
        for resourceId in resourceIds:
            try:
                return self._findElementByResourceId(driver, logger, resourceId, timeout)
            except TimeoutException:
                continue
            except:
                continue
        testcase.assertTrue(False, "Can not get elements by resource id list.")

    def assertElementsByClassNames(self, testcase, driver, logger, classNames=[], timeout=10):
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
        testcase.assertTrue(classNames, "The class name list is empty.")
        for className in classNames:
            try:
                return self._findElementByClassName(driver, logger, className, timeout)
            except TimeoutException:
                continue
            except:
                continue
        testcase.assertTrue(False, "Can not get elements by class name list.")

    def assertElementsByTexts(self, testcase, driver, logger, texts=[], timeout=10):
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
        testcase.assertTrue(texts, "The text list is empty.")
        for text in texts:
            try:
                return self._findElementByText(driver, logger, text, timeout)
            except TimeoutException:
                continue
            except:
                continue
        testcase.assertTrue(False, "Can not get elements by text list.")

    def assertElementsByContentDescs(self, testcase, driver, logger, contentDescs=[], timeout=10):
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
        testcase.assertTrue(contentDescs, "The content description list is empty.")
        for contentDesc in contentDescs:
            try:
                return self._findElementByContentDesc(driver, logger, contentDesc, timeout)
            except TimeoutException:
                continue
            except:
                continue
        testcase.assertTrue(False, "Can not get elements by content description list.")

    def assertElementsByContainsTexts(self, testcase, driver, logger, containsTexts=[], timeout=10):
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
        testcase.assertTrue(containsTexts, "The contains text list is empty.")
        for containsText in containsTexts:
            try:
                return self._findElementByContainsText(driver, logger, containsText, timeout)
            except TimeoutException:
                continue
            except:
                continue
        testcase.assertTrue(False, "Can not get elements by contains text list.")

    def assertElementsByTextStartWiths(self, testcase, driver, logger, textStartWiths=[], timeout=10):
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
        testcase.assertTrue(textStartWiths, "The text start with list is empty.")
        for textStartWith in textStartWiths:
            try:
                return self._findElementByTextStartWith(driver, logger, textStartWith, timeout)
            except TimeoutException:
                continue
            except:
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
    def assertElementByName(self, testcase, driver, logger, name="default", timeout=10):
        '''
        usage : 页面element验证方法 (适用IOS平台)
        parameters:
            testcase: unittest testcase
            driver: appium driver
            logger: logging
            name : 断言element的 name
            timeout : 超时时间,单位秒,默认十秒。
        '''
        try:
            self._findElementByResourceId(driver, logger, name, timeout)
        except TimeoutException:
            testcase.assertTrue(False, "Get element by name [%s] timeout" % (name))
        except:
            testcase.assertTrue(False, "Can not get element by name [%s]" % (name))

    def assertElementByType(self, testcase, driver, logger, elementType="default", timeout=10):
        '''
        usage : 页面element验证方法 (适用IOS平台)
        parameters:
            testcase: unittest testcase
            driver: appium driver
            logger: logging
            elementType : 断言element的 element type
            timeout : 超时时间,单位秒,默认十秒。
        '''
        try:
            self._findElementByClassName(driver, logger, elementType, timeout)
        except TimeoutException:
            testcase.assertTrue(False, "Get element by element type [%s] timeout" % (elementType))
        except:
            testcase.assertTrue(False, "Can not get element by element type [%s]" % (elementType))

    def assertElementByIosUiautomation(self, testcase, driver, logger, uiaString="default", timeout=10):
        '''
        usage : 页面element验证方法 (适用IOS平台)
        parameters:
            testcase: unittest testcase
            driver: appium driver
            logger: logging
            uiaString : 断言element的 uia string
            timeout : 超时时间,单位秒,默认十秒。
        '''
        try:
            self._findElementByIosUiautomation(driver, logger, uiaString, timeout)
        except TimeoutException:
            testcase.assertTrue(False, "Get element by uia string [%s] timeout" % (uiaString))
        except:
            testcase.assertTrue(False, "Can not get element by uia string [%s]" % (uiaString))


    '''
        ************************************************************************
        2. IOS 断言多个element方法 （只需一个验证成功，即为成功）
        ************************************************************************
    '''
    def assertElementsByNames(self, testcase, driver, logger, names=[], timeout=10):
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
        testcase.assertTrue(names, "The name list is empty.")
        for name in names:
            try:
                return self._findElementByResourceId(driver, logger, name, timeout)
            except TimeoutException:
                continue
            except:
                continue
        testcase.assertTrue(False, "Can not get elements by name list.")

    def assertElementsByElementTypes(self, testcase, driver, logger, elementTypes=[], timeout=10):
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
        testcase.assertTrue(elementTypes, "The element type list is empty.")
        for elementType in elementTypes:
            try:
                return self._findElementByClassName(driver, logger, elementType, timeout)
            except TimeoutException:
                continue
            except:
                continue
        testcase.assertTrue(False, "Can not get elements by element type list.")

    def assertElementsByIosUiautomations(self, testcase, driver, logger, uiaStrings=[], timeout=10):
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
        testcase.assertTrue(uiaStrings, "The uia string list is empty.")
        for uiaString in uiaStrings:
            try:
                return self._findElementByIosUiautomation(driver, logger, uiaString, timeout)
            except TimeoutException:
                continue
            except:
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
    def _findElementByResourceId(self, driver, logger, resourceId="default", timeout=10):
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
        wdw = WebDriverWait(driver=driver, timeout=timeout)
        return wdw.until(EC.presence_of_element_located((By.ID, resourceId)))

    def _findElementByXpath(self, driver, logger, xpath="default", timeout=10):
        '''
        usage : 显式等待方法
        parameters:
            driver: appium driver
            logger: logging
            xpath : 查找element的xpath
            timeout : 超时时间,单位秒,默认十秒。
        return : 返回查找的element
        应用场景 : 查找的element展现时间受网络状态影响,显式等待时间设置后,会最大等待timeout秒,
                  如果小于timeout,element出现,直接进行下一流程,如果等于timeout未出现,
                  抛出TimeoutException异常。
        '''
        wdw = WebDriverWait(driver=driver, timeout=timeout)
        return wdw.until(EC.presence_of_element_located((By.XPATH, xpath)))

    def _findElementByClassName(self, driver, logger, className="default", timeout=10):
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
        wdw = WebDriverWait(driver=driver, timeout=timeout)
        return wdw.until(EC.presence_of_element_located((By.CLASS_NAME, className)))

    def _findElementByText(self, driver, logger, text="default", timeout=10):
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
        wdw = WebDriverWait(driver=driver, timeout=timeout);
        return wdw.until(EC.presence_of_element_located((MobileBy.ANDROID_UIAUTOMATOR,
                                              'new UiSelector().text("' + text + '")')))

    def _findElementByContentDesc(self, driver, logger, contentDesc="default", timeout=10):
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
        wdw = WebDriverWait(driver=driver, timeout=timeout);
        return wdw.until(
            EC.presence_of_element_located((MobileBy.ANDROID_UIAUTOMATOR,
                                            'new UiSelector().description("' + contentDesc + '")')))

    def _findElementByContainsText(self, driver, logger, containsText="default", timeout=10):
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
        wdw = WebDriverWait(driver=driver, timeout=timeout);
        return wdw.until(
            EC.presence_of_element_located((MobileBy.ANDROID_UIAUTOMATOR,
                                            'new UiSelector().textContains("' + containsText + '")')))

    def _findElementByTextStartWith(self, driver, logger, textStartWith="default", timeout=10):
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
        wdw = WebDriverWait(driver=driver, timeout=timeout);
        return wdw.until(
            EC.presence_of_element_located((MobileBy.ANDROID_UIAUTOMATOR,
                                            'new UiSelector().textStartWith("' + textStartWith + '")')))

    def _findElementByIosUiautomation(self, driver, logger, uiaString="default", timeout=10):
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
        wdw = WebDriverWait(driver=driver, timeout=timeout);
        return wdw.until(
            EC.presence_of_element_located((MobileBy.IOS_UIAUTOMATION, uiaString)))


    '''
        ************************************************************************
        2. 查找多个相同属性element方法
        ************************************************************************
    '''
    def _findElementsByResourceId(self, driver, logger, resourceId="default", timeout=10):
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
        wdw = WebDriverWait(driver=driver, timeout=timeout)
        return wdw.until(EC.presence_of_all_elements_located((By.ID, resourceId)))

    def _findElementsByClassName(self, driver, logger, className="default", timeout=10):
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
        wdw = WebDriverWait(driver=driver, timeout=timeout)
        return wdw.until(EC.presence_of_all_elements_located((By.CLASS_NAME, className)))

    def _findElementsByText(self, driver, logger, text="default", timeout=10):
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
        wdw = WebDriverWait(driver=driver, timeout=timeout);
        return wdw.until(
            EC.presence_of_all_elements_located((MobileBy.ANDROID_UIAUTOMATOR,
                                                 'new UiSelector().text("' + text + '")')))

    def _findElementsByContentDesc(self, driver, logger, contentDesc="default", timeout=10):
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
        wdw = WebDriverWait(driver=driver, timeout=timeout);
        return wdw.until(
            EC.presence_of_all_elements_located((MobileBy.ANDROID_UIAUTOMATOR,
                                                 'new UiSelector().description("' + contentDesc + '")')))

    def _findElementsByContainsText(self, driver, logger, containsText="default", timeout=10):
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
        wdw = WebDriverWait(driver=driver, timeout=timeout);
        return wdw.until(
            EC.presence_of_all_elements_located((MobileBy.ANDROID_UIAUTOMATOR,
                                                 'new UiSelector().textContains("' + containsText + '")')))

    def _findElementsByTextStartWith(self, driver, logger, textStartWith="default", timeout=10):
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
        wdw = WebDriverWait(driver=driver, timeout=timeout);
        return wdw.until(
            EC.presence_of_all_elements_located((MobileBy.ANDROID_UIAUTOMATOR,
                                                 'new UiSelector().textStartWith("' + textStartWith + '")')))

    def _findElementsByIosUiautomation(self, driver, logger, uiaString="default", timeout=10):
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
        wdw = WebDriverWait(driver=driver, timeout=timeout);
        return wdw.until(
            EC.presence_of_all_elements_located((MobileBy.IOS_UIAUTOMATION, uiaString)))
