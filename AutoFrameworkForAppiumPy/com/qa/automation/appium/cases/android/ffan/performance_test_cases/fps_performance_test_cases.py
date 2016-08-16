#!/usr/bin/env python
# coding:utf-8
import re
import os
import time
import subprocess
from unittest import TestCase
from com.qa.automation.appium.configs.driver_configs import appPackage_ffan


appPackage_meituan = 'com.sankuai.meituan'
appPackage_dazhong = 'com.dianping.v1'
appPackage_miaojie = 'com.taobao.shoppingstreets'
now = time.strftime('%Y%m%d%H%M%S')
resourcesDirectory = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(
                                os.path.dirname(os.path.abspath(__file__)))))) + "/resources/"


class FpsPerformanceTestCases(TestCase):
    '''
    作者 刘涛
    流畅度情况性能测试
    '''

    def my001(self, logName):
        #print(2)
        n = 0
        f = open(logName,"r")
        mya = []
        lines = f.readlines()#读取全部内容[0-9]*
        print("ddd")
        print(lines)
        for line in lines:
            try:
                print("gggg")
                print(line)
                repr(line)
                print("AAAAAA")
                print(re.findall(r'[0-9]+.[0-9]+',line))
                print("BBBBB")
                #a,b,c = re.findall(r'[0-9]+.[0-9]+',line)
                a,b,c,d = re.findall(r'[0-9]+.[0-9]+',line)
                print("hhh")
                print(a)
                print("iii")
                a1 = float(a)
                print("jjjj")
                b1 = float(b)
                c1 = float(c)
                d1 = float(d)
                myfps = a1
                print("kkkk")
                myfps = a1+b1+c1+d1
                mya.append(myfps)
                print("llll")
                print(a1)
                print(b1)
                print(c1)
                print("ccc")
                print(mya)
            except Exception:
                pass
        j = len(mya)
        print("aaa")
        print(j)
        for i in range(j-1):
            n = mya[i]+n
            print("bbbbbb")
            print(n)
            print("CCCCCCC")
            print(i)
            print(j)
        if n <= 2000:
            #print (j-1)/2,u"        使用时间",n,u"毫秒"
            print((j-1)/2,u"        使用时间",n,u"毫秒")
        else:
            print(u"帧数超范")
            n1 = "+2000"
            f111 = open(r'FPS_performance_log.txt','a+')
            f111.write(str(n1)+"\n")
            f111.close()
        n1 = (j-1)/2
        print("eeee")
        print(j)
        print(n1)
        f111 = open(r'FPS_performance_log.txt','a+')
        f111.write(str(n1)+"\n")
        f111.close()
        print(u"写入完成等待")
    def my002(self):#飞凡
        time.sleep(3)
        print(u"抓取数据")
        logName = "FPS_%s_%s.txt" % (appPackage_ffan, now)
        f1 = open(logName, "a")
        cmdFps = "%sadb shell dumpsys gfxinfo %s" % (resourcesDirectory, appPackage_ffan)
        pipe = subprocess.Popen(cmdFps, shell=True, stdout = f1)
        pipe.stdout
        f1.close()
        return logName
    def my003(self):
        time.sleep(3)
        print(u"抓取数据")
        logName = "FPS_%s_%s.txt" % (appPackage_meituan, now)
        f1 = open(logName, "a")
        cmdFps = "%sadb shell dumpsys gfxinfo %s" % (resourcesDirectory, appPackage_meituan)
        pipe = subprocess.Popen(cmdFps, shell=True, stdout = f1)
        pipe.stdout
        f1.close()
        return logName
    def my004(self):#大众点评
        time.sleep(3)
        print(u"抓取数据")
        logName = "FPS_%s_%s.txt" % (appPackage_dazhong, now)
        f1 = open(logName, "a")
        cmdFps = "%sadb shell dumpsys gfxinfo %s" % (resourcesDirectory, appPackage_dazhong)
        pipe = subprocess.Popen(cmdFps, shell=True, stdout = f1)
        pipe.stdout
        f1.close()
        return logName
    def my005(self):#喵街
        time.sleep(3)
        print(u"抓取数据")
        logName = "FPS_%s_%s.txt" % (appPackage_miaojie, now)
        f1 = open(logName, "a")
        cmdFps = "%sadb shell dumpsys gfxinfo %s" % (resourcesDirectory, appPackage_miaojie)
        pipe = subprocess.Popen(cmdFps, shell=True, stdout = f1)
        pipe.stdout
        f1.close()
        return logName
    def getFps(self):
        print(u"按1飞凡")
        print(u"按2美团")
        print(u"按3大众")
        print(u"按4喵街")
        try:
            os.remove("FPS_performance_log.txt")
        except Exception:
            pass
        i = 1
        #m = raw_input(u"开始选择")
        m = input(u"开始选择")
        if m == "1":
            while i<2:
                logName = self.my002()
                self.my001(logName)
                print("fff")
                print(i)
        elif m == "2":
            while i<2:
                logName = self.my003()
                self.my001(logName)
        elif m == "3":
            while i<2:
                logName = self.my004()
                self.my001(logName)
        elif m == "4":
            while i<2:
                logName = self.my005()
                self.my001(logName)
        else:
            print(u"就不运行哈哈哈哈哈！！！！！！！")
