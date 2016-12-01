# -*- coding: utf-8 -*-

import os


class ClearAppData:
    '''
        usage :  清除App数据
    '''
    def __init__(self, driver):
        '''
        初始化函数
        '''
        self.driver = driver

    def clearData(self):
        '''
        usage: 清除app数据
        '''
#         self.driver.reset()
        pass

    def clearLogcat(self):
        '''
        清理logcat缓存
        :return: None
        '''
        command = 'adb logcat -c'
        os.system(command)