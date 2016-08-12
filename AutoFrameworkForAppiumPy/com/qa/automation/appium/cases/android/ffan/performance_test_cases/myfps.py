#!/usr/bin/env python
# coding:utf-8
import re
import os
import threading
from time import ctime,sleep
def my001():
    print 2
    n = 0
    f = open("D:\\abc.txt","r")
    mya = []
    lines = f.readlines()#读取全部内容[0-9]*
    for line in lines:
        try:
            repr(line)
            a,b,c = re.findall(r'[0-9]+.[0-9]+',line)
            a1 = float(a)
            b1 = float(b)
            c1 = float(c)
            myfps = a1+b1+c1
            mya.append(myfps)
        except Exception:
            pass
    j = len(mya)
    for i in range(j-1):
        n = mya[i]+n
    if n <= 2000:
        print (j-1)/2,u"        使用时间",n,u"毫秒"
    else:
        print u"帧数超范"
        n1 = "+2000"
        f111 = open(r'D:\\abc1.txt','a+')
        f111.write(str(n1)+"\n")
        f111.close()
    n1 = (j-1)/2
    f111 = open(r'D:\\abc1.txt','a+')
    f111.write(str(n1)+"\n")
    f111.close()
    print u"写入完成等待"
def my002():#飞凡
    sleep(3)
    print u"抓取数据"
    os.popen("adb shell dumpsys gfxinfo com.wanda.app.wanhui > D:\\abc.txt")
def my003():#美团
    sleep(3)
    print u"抓取数据"
    os.popen("adb shell dumpsys gfxinfo com.sankuai.meituan > D:\\abc.txt")
def my004():#大众点评
    sleep(3)
    print u"抓取数据"
    os.popen("adb shell dumpsys gfxinfo com.dianping.v1 > D:\\abc.txt")
def my005():#喵街
    sleep(3)
    print u"抓取数据"
    os.popen("adb shell dumpsys gfxinfo com.taobao.shoppingstreets > D:\\abc.txt")
print u"按1飞凡"
print u"按2美团"
print u"按3大众"
print u"按4喵街"
try:
    os.remove("D:\\abc1.txt")
except Exception:
    pass
i = 1
m = raw_input(u"开始选择")
if m == "1":
    while i<2:
        my002()
        my001()
elif m == "2":
    while i<2:
        my003()
        my001()
elif m == "3":
    while i<2:
        my004()
        my001()
elif m == "4":
    while i<2:
        my005()
        my001()
else:
    print u"就不运行哈哈哈哈哈！！！！！！！"
# def music(func):
#     print "%s. %s" %(func,ctime())
# def move(func):
#     sleep(5)
#     for i in range(3):
#         print "%s! %s" %(func,ctime())
# threads = []
# t1 = threading.Thread(target=music)
# t2 = threading.Thread(target=move,)
# threads.append(t2)#
# if __name__ == '__main__':
#     for t in threads:
#         t.setDaemon(True)
#         t.start()
#     sleep(6)
#     print u"完成 %s" %ctime()







