# -*- coding: utf-8 -*-

from _ast import IsNot
import sys
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By


class API(object):

    def __init__(self):
        pass;

    '''
    ***********************************************************************************
        find methods
    ***********************************************************************************
    '''

    def find_view_by_name(self,driver,logger,text):
        return driver.find_element_by_ios_uiautomation()

    '''
        usage: by both android and ios api
        parameters:
            driver: appium driver
            logger: logging
            resource id : view resource id, or view name
        return : view of the sepecified resource id

    '''
    def get_view_by_resourceID(self, driver, logger, resource_id="default"):
        return driver.find_element_by_id(resource_id);

    '''
        usage: by android api
        parameters:
            driver: appium driver
            logger: logging
            selector : android selector string
        return : view of the sepecified selector
    '''

    def get_view_by_uiautomator_android(self, driver, logger, selector="default"):
        return driver.find_element_by_android_uiautomator(selector);

    '''
        usage : by android api
        parameters:
            driver : appium driver
            logger : logging
            text : 已知view的text,根据已知view text获取view
            viewClassName : 预查找的兄弟节点的class name,view class name在父节点具有唯一性
        应用场景 : 某些多tab ui,点击tab后,tab对应的view状态属性不变,而且增加兄弟view的方式来标识状态.
    '''

    def get_brother_by_class_name_android(self, driver, logger, text="default", viewClassName="default"):
        selector = 'new UiSelector().text("%s").fromParent(new UiSelector().className("%s"))' % (
            text, viewClassName);
        return self.get_view_by_uiautomator_android(driver=driver, logger=logger, selector=selector);

    '''
        usage: by android api
        parameters:
            driver: appium driver
            logger: logging
            resource id : view resource id
        return : view of the sepecified text

    '''

    def get_view_text_equal_android(self, driver, logger, text="default"):
        return self.get_view_by_uiautomator_android(driver=driver, logger=logger,
                                                    selector='new UiSelector().text("' + text + '")');

    '''
        usage : by android api
        parameters:
            driver : appium driver
            logger : logging
            textContains : 查找的view包含的字段部分
        return : view of the sepecified text
    '''

    def get_view_text_contains_android(self, driver, logger, textContains="default"):
        selector = 'new UiSelector().textContains("%s")' % (textContains);
        return self.get_view_by_uiautomator_android(driver=driver, logger=logger, selector=selector);

    '''
        used by android api
        parameters:
            driver : appium driver
            logger : logging
            textStartsWith : 查找的view包含的字段头部分
        return : view of the sepecified text
    '''

    def get_view_text_starts_with_android(self, driver, logger, textStartsWith="default"):
        selector = 'new UiSelector().textStartWith("%s")' % (textStartsWith);
        return self.get_view_by_uiautomator_android(driver=driver, logger=logger, selector=selector);

    '''
        used by android api
            driver: appium driver
            logger: logging
            parameters:
                textMatches : 通过正则表达式的方式查找view e.g. textMatches="^Add.*"
            return : view of the sepecified text
    '''

    def get_view_text_matches_android(self, driver, logger, textMatches="default"):
        selector = 'new UiSelector().textContains("%s")' % (textMatches);
        return self.get_view_by_uiautomator_android(driver=driver, logger=logger, selector=selector);

    '''
        used by android api
        parameters:
            driver: appium driver
            logger: logging
            textMatches : 通过正则表达式的方式查找view e.g. className="android.widget.ImageView"
        return : view of the class name (the only one)
    '''

    def get_view_by_class_name_android(self, driver, logger, className="default"):
        selector = 'new UiSelector().className("%s")' % (className);
        return self.get_view_by_uiautomator_android(driver=driver, logger=logger, selector=selector);

    '''
        usage : 显式等待方法
        parameters:
            driver: appium driver
            logger: logging
            resource_id : 查找view的resource id
            seconds : 等待的最大市场,单位秒,默认十秒
        应用场景 : 查找的view展现时间受网络状态影响,显式等待时间设置后,会最大等待seconds秒,如果小于seconds view出现,直接进行下一流程,如果等于seconds未出现,raise TimeoutException
    '''

    def find_view_by_resourceID_Until_android(self, driver, logger, resource_id="default", seconds=10):
        wdw = WebDriverWait(driver=driver, timeout=seconds);
        return wdw.until(EC.presence_of_element_located((By.ID, resource_id)));

    def find_view_by_text_Until_android(self, driver, logger, text="default", seconds=10):
        wdw = WebDriverWait(driver=driver, timeout=seconds);
        return wdw.until(
            EC.text_to_be_present_in_element((MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("' + text + '")'),
                                             text));

    def find_view_by_content_desc_Until_android(self, driver, logger, content_desc="default", seconds=10):
        wdw = WebDriverWait(driver=driver, timeout=seconds);
        return wdw.until(EC.presence_of_element_located((By.NAME, content_desc)))

    def find_view_by_xpath_Until_android(self, driver, logger, xpath="default", seconds=10):
        wdw = WebDriverWait(driver=driver, timeout=seconds);
        return wdw.until(EC.presence_of_element_located((By.XPATH, xpath)))

    '''
    ***********************************************************************************
        click methods
    ***********************************************************************************
    '''

    def click_view_by_resourceID_android(self, testcase, driver, logger, resource_id, seconds=10):

        try:
            wdw = WebDriverWait(driver=driver, timeout=seconds)
            findResult = wdw.until(EC.presence_of_element_located((By.ID, resource_id)))
            if findResult is not None:
                self.get_view_by_resourceID(driver=driver, logger=logger, resource_id=resource_id).click();
        except NoSuchElementException:
            testcase.assertTrue(False, "resource_id %s none" % (resource_id))
        except TimeoutException:
            testcase.assertIsNotNone(None, "get resource_id %s timeout until %s seconds" % (resource_id, seconds))

    def click_view_by_text_android(self, testcase, driver, logger, text="default", seconds=10):

        try:
            wdw = WebDriverWait(driver=driver, timeout=seconds)
            findResult = wdw.until(EC.text_to_be_present_in_element(
                (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("' + text + '")'), text));
            if findResult is not None:
                web_element = self.get_view_text_equal_android(driver=driver, logger=logger, text=text)
                web_element.click()
        except NoSuchElementException:
            testcase.assertTrue(False, "text %s none" % (text))
        except TimeoutException:
            testcase.assertIsNotNone(None, "get text %s timeout until %s seconds" % (text, seconds))

    def click_view_by_xpath(self, testcase, driver, logger, xpath, seconds=10):
        try:
            wdw = WebDriverWait(driver=driver, timeout=seconds)
            findResult = wdw.until(EC.presence_of_element_located((By.XPATH, xpath)))
            if findResult is not None:
                driver.find_element_by_xpath(xpath).click();
        except NoSuchElementException:
            # logger.d("no such element")
            testcase.assertTrue(False, "xpath %s none" % (xpath))
        except TimeoutException:
            logger.d("get xpath timeout")
            testcase.assertIsNotNone(None, "get xpath %s timeout until %s seconds" % (xpath, seconds))

    def click_view_by_content_desc(self, testcase, driver, logger, content_desc, seconds=10):
        try:
            wdw = WebDriverWait(driver=driver, timeout=seconds)
            findResult = wdw.until(EC.presence_of_element_located((By.NAME, content_desc)))
            if findResult is not None:
                self.find_view_by_content_desc_Until_android(driver=driver, logger=logger,
                                                             content_desc=content_desc).click()
        except NoSuchElementException:
            testcase.assertTrue(False, "content_desc %s none" % (content_desc))
        except TimeoutException:
            testcase.assertIsNotNone(None, "get content_desc %s timeout until %s seconds" % (content_desc, seconds))

    def click_back_key(self, driver, logger):
        # logger.d("click back key , keycode ======== 4",)
        driver.press_keycode(4);
        time.sleep(2)

    '''
    ***********************************************************************************
        scroll method
    ***********************************************************************************
    '''

    def scroll(self, driver, logger, start_x, start_y, end_x, end_y, duration=None):
        # logger.d("swipe ========","from : " + start_x + " , ", start_y + " , ","to :" + end_x + " , ", end_y)
        driver.swipe(start_x=start_x, start_y=start_y, end_x=end_x, end_y=end_y, duration=duration);


    '''
    ***********************************************************************************
        get device width 
    ***********************************************************************************
    '''

    def get_width_of_device(self, driver, logger):
        x = driver.get_window_size()['width']
        # logger.d("window size = d%" + x);
        return x;

    '''
    ***********************************************************************************
        get device height 
    ***********************************************************************************
    '''

    def get_height_of_device(self, driver, logger):
        y = driver.get_window_size()['height']
        # logger.d("window size = d%" + y)
        return y;

    '''
    ***********************************************************************************
        assert methods
    ***********************************************************************************
    '''

    '''
        用法和findViewByText,增加结果申明判断.
    '''

    def assert_view_by_text_android(self, testcase, driver, logger, text="default", seconds=10):
        try:
            testcase.assertIsNotNone(
                # self.get_view_text_equal_android(driver=driver, logger=logger, text=text),
                # "resource id none"
                self.find_view_by_text_Until_android(driver=driver, logger=logger, text=text, seconds=10)
            )
        except NoSuchElementException as e:
            testcase.assertTrue(False, "text %s none" % (text))

        except TimeoutException as e:
            testcase.assertIsNotNone(None, "get text %s timeout until %s seconds" % (text, seconds))

    '''
        用法和findViewByResourceIDUntil,增加结果申明判断.
    '''

    def assert_view_by_resourceID_Until(self, testcase, driver, logger, resource_id="default", seconds=10):
        try:
            testcase.assertIsNotNone(
                self.find_view_by_resourceID_Until_android(driver=driver, logger=logger, resource_id=resource_id,
                                                           seconds=seconds), "resource id none")
        except NoSuchElementException as e:
            testcase.assertTrue(False, "resource id %s none" % (resource_id))
        except TimeoutException as e:
            testcase.assertTrue(False,
                                "get resource id %s timeout until %s seconds" % (resource_id, seconds))

    def assert_none_view_by_resource_id_until_android(self, testcase, driver, logger, resource_id="default",
                                                      seconds=10):
        '''
           usage : verify whether the current page is the version upgrade page.
        '''
        try:
            testcase.assertIsNotNone(self.find_view_by_resourceID_Until_android(driver, logger, resource_id, seconds),
                                     "resource id none")
        except TimeoutException:
            testcase.assertTrue(True, "resource id %s is not none" % (resource_id))

    def assert_view_by_resourceID_android(self, testcase, logger, driver, resource_id="default"):
        try:
            testcase.assertIsNotNone(self.get_view_by_resourceID(driver=driver, logger=logger, resource_id=resource_id),
                                     "resource id %s not none" % (resource_id))
        except NoSuchElementException as e:
            testcase.assertIsNotNone(None,
                                     "resource id %s none" % (resource_id))

    def assert_view_by_xpath_android(self, testcase, driver, logger, xpath="default", seconds=10):
        try:
            testcase.assertIsNotNone(
                self.find_view_by_xpath_Until_android(driver=driver, logger=logger, xpath=xpath, seconds=10))
        except NoSuchElementException as e:
            testcase.assertTrue(False, "content_desc %s none" % (xpath))

        except TimeoutException as e:
            testcase.assertIsNotNone(None, "get xpath %s timeout until %s seconds" % (xpath, seconds))

    '''
    ***********************************************************************************
        common methods
    ***********************************************************************************
    '''

    def scroll_to_text(self, driver, logger, text):
        el = driver.find_element_by_android_uiautomator(
            'new UiScrollable(new UiSelector().scrollable(true).instance(0)).'
            'scrollIntoView(new UiSelector().text("%s").instance(0))' % (text))

    def scrollFromElToEl(self, driver, logger, el1, el2):
        driver.scroll(el1, el2)

    def wait_by_seconds(self, seconds=1):
        time.sleep(seconds)

    '''
        ***********************************************************************************
            input methods
        ***********************************************************************************
        '''

    '''
        用法根据resource_id 定位输入框，并输入String内容.
    '''

    def input_view_by_resourceID_android(self, driver, logger, resource_id, string):
        input_field = self.get_view_by_resourceID(driver=driver, logger=logger, resource_id=resource_id)
        input_field.send_keys(string)

    def hidden_keyborad(self, driver):
        driver.hide_keyboard();
