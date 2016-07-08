# -*- coding: utf-8 -*-

import os,sys
from subprocess import Popen, PIPE

#sys.path.append(os.path.dirname(os.path.dirname(__file__)))



# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

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