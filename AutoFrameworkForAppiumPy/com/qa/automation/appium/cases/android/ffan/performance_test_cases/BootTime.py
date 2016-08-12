import os
import time
import subprocess

global path,activity,package
# path = "G:\\performance\\"
path = "C:\\"
activity = raw_input("please input activity: ")
package = raw_input("please input package: ")

def getWarmBootTime(package,activity):
	
	print "Start the WarmBoot test, please open the file until test complete"
	# startTime = "am start -W " + package + "/" + activity + " | grep -E " + "\'" + "TotalTime|WaitTime" + "\'" 
	bootTime = "am start -W " + package + "/" + activity + " | grep TotalTime"
	cmdam = "adb shell " + "\"" + bootTime + "\""
	keycode = "keyevent KEYCODE_BACK"
	cmdBack = "adb shell input " + keycode
	now = time.strftime('%Y%m%d%H%M%S')
	f1 = open(path + "WarmBootTime_" + package + "_" + now + ".txt", "a")
	for x in xrange(0,10):
		os.system(cmdBack)
		time.sleep(0.3)
		os.system(cmdBack)
		time.sleep(10)
		pipe = subprocess.Popen(cmdam, shell=True, stdout = f1).stdout
		time.sleep(5)
	f1.close()
	f2 = open(path + "WarmBootTime_" + package + "_" + now + ".txt", "r")
	allTime = []
	originals = f2.readlines()
	f2.close
	for contents in originals:
		try:
			total = contents.split(" ")[1]
			allTime.append(total)
			time.sleep(1)
		except:
			continue
	finalTime = 0
	for i in range (len(allTime)):
		finalTime = int (allTime[i]) + finalTime
		time.sleep(1)
	# print finalTime
	averageTime = finalTime/10
	# print averageTime
	f = open(path + "WarmBootTime_" + package + "_" + now + ".txt", "a")
	f.write("TotalTime: " + str(finalTime) + "\n")
	f.write("AverageTime: " + str(averageTime))
	time.sleep(1)
	f.close
	print "getWarmBootTime Test complete, go to " + path + " and see the details"



def getColdBootTime(package,activity):

	print "Start the ColdBoot test, please open the file until test complete"
	bootTime = "am start -W " + package + "/" + activity + " | grep TotalTime"
	cmdam = "adb shell " + "\"" + bootTime + "\""
	kill = "am force-stop " + package 
	cmdKill = "adb shell " + kill
	now = time.strftime('%Y%m%d%H%M%S')
	f1 = open(path + "ColdBootTime_" + package + "_" + now + ".txt", "a")
	for x in xrange(0,10):
		os.system(cmdKill)
		time.sleep(10)
		pipe = subprocess.Popen(cmdam, shell=True, stdout = f1).stdout
		time.sleep(10)
	f1.close()
	f2 = open(path + "ColdBootTime_" + package + "_" + now + ".txt", "r")
	allTime = []
	originals = f2.readlines()
	f2.close
	for contents in originals:
		try:
			total = contents.split(" ")[1]
			allTime.append(total)
			time.sleep(1)
		except:
			continue
	finalTime = 0
	for i in range (len(allTime)):
		finalTime = int (allTime[i]) + finalTime
		time.sleep(1)
	# print finalTime
	averageTime = finalTime/10
	# print averageTime
	f = open(path + "ColdBootTime_" + package + "_" + now + ".txt", "a")
	f.write("TotalTime: " + str(finalTime) + "\n")
	f.write("AverageTime: " + str(averageTime))
	time.sleep(1)
	f.close

	print "getColdBootTime Test complete, go to " + path + " and see the details"


getColdBootTime(package,activity)
getWarmBootTime(package,activity)
