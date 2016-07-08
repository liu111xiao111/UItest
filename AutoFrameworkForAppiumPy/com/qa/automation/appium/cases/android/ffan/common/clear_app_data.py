# -*- coding: utf-8 -*-


from subprocess import Popen, PIPE
from __init__ import *

'''
    usage :  进入应用的首页
'''
class ClearAppData:

    def __init__(self):
        pass
    
    def clearData(self):
        cmd = 'adb shell pm clear com.wanda.app.wanhui'
        p = Popen(cmd , shell=True, stdout=PIPE, stderr=PIPE)
        
        out, err = p.communicate() 
        
        #print "Return code: ", p.returncode  
        #print out.rstrip(), err.rstrip()
        
        
if __name__ == '__main__':
    clearAppData = ClearAppData()
    clearAppData.clearData()
    
