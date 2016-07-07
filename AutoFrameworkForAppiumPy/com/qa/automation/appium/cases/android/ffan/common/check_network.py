# -*- coding: utf-8 -*-

from subprocess import Popen, PIPE

from __init__ import *

CONNECTION = 0
NOCONNECTION = -1
NOFIND = -1

class CheckNetworkStatus:
    '''
        usage :  Check Network status.
    '''

    def __init__(self):
        pass
    
    def checkNetwork(self):
        cmd = 'adb shell ping -w 3 baidu.com'
        ret = Popen(cmd , shell=True, stdout=PIPE, stderr=PIPE)
        out, err = ret.communicate()
        if out.find('unknown') == NOFIND:
            return CONNECTION;
        else:
            print(err);
            return NOCONNECTION;
        

if __name__ == '__main__':
    checkNetworkStatus = CheckNetworkStatus()
    checkNetworkStatus.checkNetwork()