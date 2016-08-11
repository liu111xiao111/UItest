import os
import time
import subprocess
from com.qa.automation.appium.configs.driver_configs import appPackage_ffan


now = time.strftime('%Y%m%d%H%M%S')
resourcesDirectory = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(
                                os.path.dirname(os.path.abspath(__file__)))))) + "/resources/"


def getPid():
    print("\nGet the PID by the package name")
    pidFile = "pid_" + now + ".txt"
    cmdpid = "%sadb shell ps | grep %s | awk '{print $2}' | head -n 1 > %s" % (resourcesDirectory, appPackage_ffan, pidFile)
    os.system(cmdpid)
    f = open(pidFile)
    pid = f.readline()
    if os.path.exists(pidFile):
        os.remove(pidFile)
    print(pid)
    return pid

def getCPU():
    pid = getPid()

    print("Start the CPU test, please run the app and keep operation until the Test complete")
    cpu = "dumpsys cpuinfo | grep " + pid
    cmdcpu = "%sadb shell \"%s\"" % (resourcesDirectory, cpu)
    f1 = open("CPU_" + appPackage_ffan + "_" + now + ".txt", "a")

    for x in range(0, 120): 
        pipe = subprocess.Popen(cmdcpu, shell=True, stdout = f1).stdout
        time.sleep(1)
    f1.close()
    f2 = open("CPU_" + appPackage_ffan + "_" + now + ".txt", "r")
    totalcpu = []
    originals = f2.readlines()
    f2.close
    for contents in originals:
        try:
            total = contents.split("/" + appPackage_ffan + ":")[0].split("%")[0]
            totalcpu.append(total)
        except:
            continue
    logName = "CPU_" + appPackage_ffan + "_" + now + ".txt"
    f = open(logName, "a")
    f.write("Below is the CPU usage: " + '\n')
    for i in range (len(totalcpu)):
        f.write(totalcpu[i] + '\n')
        time.sleep(1)
        f.close
    print("getCPU Test complete, go to " + logName + " and see the details")


def getMemory():

    print("\nStart the Memory test, please run the app and keep operation until the Test complete")
    pss = "dumpsys meminfo " + appPackage_ffan + " | grep TOTAL"
    cmdpss = "%sadb shell \"%s\"" % (resourcesDirectory, pss)
    f1 = open("PSS_" + appPackage_ffan + "_" + now + ".txt", "a")
    for x in range(0,120): 
        pipe = subprocess.Popen(cmdpss, shell=True, stdout = f1).stdout
        time.sleep(1)
    f1.close()
    f2 = open("PSS_" + appPackage_ffan + "_" + now + ".txt", "r")
    totalHeapSize = []
    originals = f2.readlines()
    f2.close
    for contents in originals:
        try:
            total = contents.split("   ")[3]
            totalHeapSize.append(total)
        except:
            continue
    logName = "PSS_" + appPackage_ffan + "_" + now + ".txt"
    f = open(logName, "a")
    f.write("Below is the memory(pss): " + '\n')
    for i in range (len(totalHeapSize)):
        m = int(totalHeapSize[i])/1024
        f.write(str(m) + '\n')
        #f.write(totalHeapSize[i] + '\n')
        time.sleep(1)
        f.close
    print("getMemory Test complete, go to " + logName + " and see the details\n")

getCPU()
getMemory()