import os
import time
import subprocess

global path,package
# path = "G:\\performance\\"
path = "C:\\"
package = raw_input("please input package: ")
pid = raw_input("please input the pid: ")

def getCPU(package,pid):

	# print "Get the PID by the package name"
	# cmdpid = "adb shell ps | grep " + package + "$"
	# os.popen(cmdpid)
	# ff = open(path + "PID_" + package + ".txt","w")
	# pipe = subprocess.Popen(cmdpid, shell=True, stdout = ff).stdout
	# time.sleep(1)
	# ff.close()
	# ff2 = open(path + "PID_" + package + ".txt","r")
	# originals = ff2.readlines()
	# for x in originals:
	# 	thispid = x.split("    ")[1]
	# 	pid = thispid.split("  ")[0]
	# print pid

	print "Start the CPU test, please run the app and keep operation until the Test complete"
	cpu = "dumpsys cpuinfo | grep " + pid
	cmdcpu = "adb shell " + "\"" + cpu + "\""
	now = time.strftime('%Y%m%d%H%M%S')
	f1 = open(path + "CPU_" + package + "_" + now + ".txt", "a")
	for x in xrange(0,120): 
		pipe = subprocess.Popen(cmdcpu, shell=True, stdout = f1).stdout
		time.sleep(1)
	f1.close()
	f2 = open(path + "CPU_" + package + "_" + now + ".txt", "r")
	totalcpu = []
	originals = f2.readlines()
	f2.close
	for contents in originals:
		try:
			total = contents.split("/" + package + ":")[0].split("%")[0]
			# print total + "%"
			totalcpu.append(total + "%")
		except:
			continue
	f = open(path + "CPU_" + package + "_" + now + ".txt", "a")
	f.write("Below is the CPU usage: " + '\n')
	for i in range (len(totalcpu)):
		f.write(totalcpu[i] + '\n')
		time.sleep(1)
		f.close
	print "getCPU Test complete, go to " + path + " and see the details"


def getMemory(package):

	print "Start the Memory test, please run the app and keep operation until the Test complete"
	pss = "dumpsys meminfo " + package + " | grep TOTAL"
	cmdpss = "adb shell " + "\"" + pss + "\""
	now = time.strftime('%Y%m%d%H%M%S')
	f1 = open(path + "PSS_" + package + "_" + now + ".txt", "a")
	for x in xrange(0,120): 
		pipe = subprocess.Popen(cmdpss, shell=True, stdout = f1).stdout
		time.sleep(1)
	f1.close()
	f2 = open(path + "PSS_" + package + "_" + now + ".txt", "r")
	totalHeapSize = []
	originals = f2.readlines()
	f2.close
	for contents in originals:
		try:
			total = contents.split("   ")[6]
			# print total + "KB"
			totalHeapSize.append(total)
		except:
			continue
	f = open(path + "PSS_" + package + "_" + now + ".txt", "a")
	f.write("Below is the memory(pss): " + '\n')
	for i in range (len(totalHeapSize)):
		m = int(totalHeapSize[i])/1024
		f.write(str(m) + '\n')
		time.sleep(1)
		f.close
	print "getMemory Test complete, go to " + path + " and see the details"


getCPU(package,pid)
getMemory(package)