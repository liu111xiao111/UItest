# -*- coding:utf-8 -*-

import subprocess
import os
import threading

class HuiGuiCeShi(object):
    pidList = []

    #总循环次数
    ALLCASE_LOOP_TIMES = 100;
    #每个case循环次数
    CASE_LOOP_TIMES = 10;

    COMMAND = "idevicesyslog"

    def __init__(self):
        pass


    def _saveLog(self):
        print('BEGIN get iOS log')
        '''
        保存log到回归测试目录
        :return:
        '''
        logcatFile = "/Users/auto/Desktop/testlog.txt"
        command = "%s > %s" % (self.COMMAND, logcatFile)
        os.system(command)
        print('DEBUG GET LOE END!')

    def _execCmd(self,cmd):
        r = os.popen(cmd)
        line = r.readlines()
        r.close()
        return line

    def _getIdevicelogPid(self):
        '''
        获取 IdevicelogPid
        :return:
        '''

        list = self.execCmd("ps -A | grep idevicesyslog")
        for item in list:
            self.pidList.append(item.split(' ')[0])
            #print(item.split(' '))


    def _killIdevicelogPid(self):
        '''
        kill IdevicelogPid
        :return:
        '''
        self.getIdevicelogPid()
        for pid in self.pidList:
            self.execCmd('kill %s' % pid)
            print(pid)


if __name__ == "__main__":

    #HuiGuiCeShi()._saveLog()

    t = threading.Thread(target=HuiGuiCeShi()._saveLog)
    t.start()


    #HuiGuiCeShi().killIdevicelogPid()


