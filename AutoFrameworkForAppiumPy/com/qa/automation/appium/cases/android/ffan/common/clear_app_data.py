# -*- coding: utf-8 -*-

import os, sys
from subprocess import Popen, PIPE

# sys.path.append(os.path.dirname(os.path.dirname(__file__)))



# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

'''
    usage :  进入应用的首页
'''


class ClearAppData:
    def __init__(self):
        pass

    def clearData(self):
        cmd = 'adb shell pm clear com.wanda.app.wanhui'
        p = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE)

        out, err = p.communicate()

        # print "Return code: ", p.returncode
        # print out.rstrip(), err.rstrip()


if __name__ == '__main__':
    clearAppData = ClearAppData()
    clearAppData.clearData()
