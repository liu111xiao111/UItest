'''
Created on Nov 17, 2016

@author: qiaojx
'''

import os
import time
import datetime
import argparse
import glob
import shutil
import xlrd
import xlsxwriter
import zipfile 
from xlutils.copy import copy
from tools.utility.constants import INSIDELOOPNUM,OUTLOOPNUM
import openpyxl

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

from tools.utility.constants import *


class DataHandler(object):
    def __init__(self):
        self.rsPath = ''
        self.testCase = ''

    def handle(self, rsPath):
        self.rsPath = rsPath
        self.reportPath = os.path.join(self.rsPath, 'attachment')
        self.logPath = os.path.join(self.reportPath, 'log')

        self._summaryLogData()
        self._addZipFile()

    def getLogData(self,testCase):
        self.testCase = testCase
        return self._parserLogData()

    #把Log文件信息打包 
    def _addZipFile(self):
        zipf = zipfile.ZipFile('log.zip', 'w')
        pre_len = len(os.path.dirname(self.logPath))
        for parent, dirnames, filenames in os.walk(self.logPath):
            for filename in filenames:
                pathfile = os.path.join(parent, filename)
                arcname = pathfile[pre_len:].strip(os.path.sep)
                zipf.write(pathfile, arcname)
        zipf.close()
        zipFileName = os.path.join(self.reportPath, 'log.zip')
        shutil.move("log.zip", zipFileName)

    def _summaryLogData(self):
        if not os.path.exists(self.logPath):
            os.makedirs(self.logPath)

        cmdCP = "cp -R %s/[0-9] %s" % (self.rsPath, self.logPath)
        os.system(cmdCP)

        tmpFile = os.path.join(self.logPath, 'tmp.txt')
        cmdFind = 'find %s -type d -name "screenshot" > %s' % (self.logPath, tmpFile)
        os.system(cmdFind)
        rmPath = open(tmpFile, 'r')
        while 1:
            line = rmPath.readline()
            if not line:
                break
            else:
                cmdRM = "rm -rf %s" % (line)
                os.system(cmdRM)
        if os.path.exists(tmpFile):
            os.remove(tmpFile)

    def _parserLogData(self):
        i = 0
        caseErrorInfo = {'ANR': 0, 'JRT': 0, 'NDK': 0}
        tmpFile = os.path.join(self.logPath, '%s.txt') % self.testCase
        cmdFind = 'find %s -name "%s*.log" > %s' % (self.logPath, self.testCase, tmpFile)
        os.system(cmdFind)
        if os.path.exists(tmpFile):
            logCasePath = open(tmpFile, 'r')
            logPaths = logCasePath.readlines()
            logCasePath.close()
            if logPaths != []:
                for logPath in logPaths:
                    caseLogFile = logPath[:-1]
                    if os.path.exists(caseLogFile):
                        logInfo = open(caseLogFile, 'r')
                        logLines = logInfo.readlines()
                        logInfo.close()
                        for logLine in logLines:
                            if logLine.find("crash") != -1:
                                caseErrorInfo['ANR'] += 1
                            elif logLine.find("anr") != -1:
                                caseErrorInfo['ANR'] += 1
                            elif logLine.find("Reading a NULL string not supported here.") != -1:
                                i += 1
                                caseErrorInfo['JRT'] += 1
                            elif logLine.find("Got null root node from accessibility - Retrying...") != -1:
                                caseErrorInfo['JRT'] += 1
                caseErrorInfo['JRT'] = caseErrorInfo['JRT'] - (i-1)

        if os.path.exists(tmpFile):
            os.remove(tmpFile)

        return caseErrorInfo


class Handler(object):
    def __init__(self, deviceType):
        self.rsPath = ''
        self.reportPath = ''
        self.workbook = ''
        self.dataLength = 0
        self.dataList = {u'quanchengsousuo': {'ANR': 0, 'JRT': 0, 'NDK': 0}, 
                         u'gouwuzhongxin': {'ANR': 0, 'JRT': 0, 'NDK': 0},
                         u'meishihui': {'ANR': 0, 'JRT': 0, 'NDK': 0},
                         u'guangchangsousuo': {'ANR': 0, 'JRT': 0, 'NDK': 0},
                         u'guangchangzhaodian': {'ANR': 0, 'JRT': 0, 'NDK': 0},
                         u'guangchangpaidui': {'ANR': 0, 'JRT': 0, 'NDK': 0},
                         u'guangchangtingche': {'ANR': 0, 'JRT': 0, 'NDK': 0},
                         u'guangchangmaidan': {'ANR': 0, 'JRT': 0, 'NDK': 0},
                         u'wodedenglu': {'ANR': 0, 'JRT': 0, 'NDK': 0},
                         u'wodetuichu': {'ANR': 0, 'JRT': 0, 'NDK': 0}}
        if deviceType == 'Android':
            from configs.androidConfig import appVersion, phoneVersion, buildVersion, deviceID, deviceNet
        elif deviceType == 'IOS':
            from configs.iosConfig import appVersion, phoneVersion, buildVersion, deviceID, deviceNet
        else:
            raise

        self.deviceType = deviceType
        self.appVersion = appVersion
        self.phoneVersion = phoneVersion
        self.buildVersion = buildVersion
        self.deviceID = deviceID
        self.deviceNet = deviceNet

    def handle(self, rsPath):
        self.rsPath = rsPath
        self._mkReportDir()
        try:
            resourcesDirectory = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/resources/"
            xlsFileTemplate = os.path.join(resourcesDirectory, u'templateStability.xlsx')
            shutil.copy(xlsFileTemplate,self.reportPath)
            dataHandler = DataHandler()
            dataHandler.handle(rsPath=self.rsPath)
            for testCase in (STABILITY_CASE_FOLDER_LIST.values()):
                caseErrorInfo = dataHandler.getLogData(testCase=testCase)
                self.dataList[testCase]['ANR'] = caseErrorInfo['ANR']
                self.dataList[testCase]['JRT'] = caseErrorInfo['JRT']
                self.dataList[testCase]['NDK'] = caseErrorInfo['NDK']
            xlsFile = os.path.join(self.reportPath, u'templateStability.xlsx')
        except Exception as e:
            print(e)
        finally:
            self._writeExcel(xlsFile)

    def _mkReportDir(self):
        '''
        创建报告目录, 包含excel报告,log压缩包
        '''
        self.reportPath = os.path.join(self.rsPath, 'attachment')
        if os.path.exists(self.reportPath):
            timestamp = os.path.getmtime(self.reportPath)
            date = datetime.datetime.fromtimestamp(timestamp).strftime('%Y_%m_%d_%H_%M_%S')
            newDirName = 'report_' + date

            newLogDir = os.path.join(self.rsPath, newDirName)
            try:
                os.renames(self.reportPath, newLogDir)
            except Exception as e:
                raise IOError('Modify the [%s] directory name failed with following error: \n'
                              '%s' % (self.reportPath, e))

        try:
            os.makedirs(self.reportPath)
        except Exception as e:
            raise IOError('Create the [%s] directory failed with following error: \n'
                          '%s' % (self.reportPath, e))

    def _writeExcel(self, file='file.xls'):

        try:
            wb = openpyxl.load_workbook(file)
            for sheet_name in STABILITY_REPORT_SHEET:
                ws = wb.get_sheet_by_name(sheet_name)
                if sheet_name == u'测试环境':
                    ws['C4'] = self.phoneVersion
                    ws['C5'] = self.buildVersion
                    ws['C9'] = self.appVersion
                    ws['A13'] = self.deviceNet
                elif sheet_name == u'全城搜索':
                    ws['C4'] = INSIDELOOPNUM * OUTLOOPNUM
                    ws['C5'] = self.dataList['quanchengsousuo']['ANR'] + self.dataList['quanchengsousuo']['JRT'] + self.dataList['quanchengsousuo']['NDK']
                    ws['C6'] = self.dataList['quanchengsousuo']['ANR']
                    print(self.dataList['quanchengsousuo']['JRT'])
                    ws['C7'] = self.dataList['quanchengsousuo']['JRT']
                    ws['C8'] = self.dataList['quanchengsousuo']['NDK']
                elif sheet_name == u'购物中心':
                    ws['C4'] = INSIDELOOPNUM * OUTLOOPNUM
                    ws['C5'] = self.dataList['gouwuzhongxin']['ANR'] + self.dataList['gouwuzhongxin']['JRT'] + self.dataList['gouwuzhongxin']['NDK']
                    ws['C6'] = self.dataList['gouwuzhongxin']['ANR']
                    ws['C7'] = self.dataList['gouwuzhongxin']['JRT']
                    ws['C8'] = self.dataList['gouwuzhongxin']['NDK']
                elif sheet_name == u'美食汇':
                    ws['C4'] = INSIDELOOPNUM * OUTLOOPNUM
                    ws['C5'] = self.dataList['meishihui']['ANR'] + self.dataList['meishihui']['JRT'] + self.dataList['meishihui']['NDK']
                    ws['C6'] = self.dataList['meishihui']['ANR']
                    ws['C7'] = self.dataList['meishihui']['JRT']
                    ws['C8'] = self.dataList['meishihui']['NDK']
                elif sheet_name == u'广场搜索':
                    ws['C4'] = INSIDELOOPNUM * OUTLOOPNUM
                    ws['C5'] = self.dataList['guangchangsousuo']['ANR'] + self.dataList['guangchangsousuo']['JRT'] + self.dataList['guangchangsousuo']['NDK']
                    ws['C6'] = self.dataList['guangchangsousuo']['ANR']
                    ws['C7'] = self.dataList['guangchangsousuo']['JRT']
                    ws['C8'] = self.dataList['guangchangsousuo']['NDK']
                elif sheet_name == u'广场找店':
                    ws['C4'] = INSIDELOOPNUM * OUTLOOPNUM
                    ws['C5'] = self.dataList['guangchangzhaodian']['ANR'] + self.dataList['guangchangzhaodian']['JRT'] + self.dataList['guangchangzhaodian']['NDK']
                    ws['C6'] = self.dataList['guangchangzhaodian']['ANR']
                    ws['C7'] = self.dataList['guangchangzhaodian']['JRT']
                    ws['C8'] = self.dataList['guangchangzhaodian']['NDK']
                elif sheet_name == u'广场排队':
                    ws['C4'] = INSIDELOOPNUM * OUTLOOPNUM
                    ws['C5'] = self.dataList['guangchangpaidui']['ANR'] + self.dataList['guangchangpaidui']['JRT'] + self.dataList['guangchangpaidui']['NDK']
                    ws['C6'] = self.dataList['guangchangpaidui']['ANR']
                    ws['C7'] = self.dataList['guangchangpaidui']['JRT']
                    ws['C8'] = self.dataList['guangchangpaidui']['NDK']
                elif sheet_name == u'广场停车':
                    ws['C4'] = INSIDELOOPNUM * OUTLOOPNUM
                    ws['C5'] = self.dataList['guangchangtingche']['ANR'] + self.dataList['guangchangtingche']['JRT'] + self.dataList['guangchangtingche']['NDK']
                    ws['C6'] = self.dataList['guangchangtingche']['ANR']
                    ws['C7'] = self.dataList['guangchangtingche']['JRT']
                    ws['C8'] = self.dataList['guangchangtingche']['NDK']
                elif sheet_name == u'广场买单':
                    ws['C4'] = OUTLOOPNUM
                    ws['C5'] = self.dataList['guangchangmaidan']['ANR'] + self.dataList['guangchangmaidan']['JRT'] + self.dataList['guangchangmaidan']['NDK']
                    ws['C6'] = self.dataList['guangchangmaidan']['ANR']
                    ws['C7'] = self.dataList['guangchangmaidan']['JRT']
                    ws['C8'] = self.dataList['guangchangmaidan']['NDK']
                elif sheet_name == u'我的登录':
                    ws['C4'] = INSIDELOOPNUM * OUTLOOPNUM
                    ws['C5'] = self.dataList['wodedenglu']['ANR'] + self.dataList['wodedenglu']['JRT'] + self.dataList['wodedenglu']['NDK']
                    ws['C6'] = self.dataList['wodedenglu']['ANR']
                    ws['C7'] = self.dataList['wodedenglu']['JRT']
                    ws['C8'] = self.dataList['wodedenglu']['NDK']
                elif sheet_name == u'我的退出':
                    ws['C4'] = INSIDELOOPNUM * OUTLOOPNUM
                    ws['C5'] = self.dataList['wodetuichu']['ANR'] + self.dataList['wodetuichu']['JRT'] + self.dataList['wodetuichu']['NDK']
                    ws['C6'] = self.dataList['wodetuichu']['ANR']
                    ws['C7'] = self.dataList['wodetuichu']['JRT']
                    ws['C8'] = self.dataList['wodetuichu']['NDK']
            xlsFile = os.path.join(self.reportPath, u'飞凡稳定性评测报告%s.xlsx' % time.strftime("%Y%m%d"))
            wb.save(xlsFile)
            if os.path.exists(file):
                os.remove(file)
        except:
            print("no sheet in %s named %s" % file,sheet_name)


if __name__ == "__main__":
    handler = Handler('Android')
    resultsPath = "%s/report/stability/%s/%s" % ("/Users/uasd-qiaojx/Desktop", '2016/12/12', '1')
    if os.path.exists(resultsPath):
        handler.handle(resultsPath)
