
#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import time
import smtplib
import pylab as pl

from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.image import MIMEImage
from com.qa.automation.appium.configs import constants

pl.mpl.rcParams['font.sans-serif'] = ['SimHei']


class PeformanceDraw(object):
    '''
    绘制性能数据图表图片
    '''

    def __init__(self, deviceType):
        if deviceType == 'android':
            from com.qa.automation.appium.configs.androidConfig import appVersion, phoneVersion, buildVersion, deviceID
        elif deviceType == 'ios':
            from com.qa.automation.appium.configs.iosConfig import appVersion, phoneVersion, buildVersion, deviceID
        else:
            raise

        self.appVersion = appVersion
        self.phoneVersion = phoneVersion
        self.buildVersion = buildVersion
        self.deviceID = deviceID

        self.reportPath = ''
        self.startTime = ''
        self.endTime = ''
        self.resultTraffic = ''

        self.coldBootFile     = 'ColdBootTime_performance.txt'
        self.warmBootFile     = 'WarmBootTime_performance.txt'
        self.trafficUsageFile = 'Traffic_performance.txt'
        self.cpuUsageFile     = 'Cpu_performance.txt'
        self.drawInfoFile     = 'Fps_performance.txt'
        self.fpsInfoFile      = 'Fps_performance.txt'
        self.memoryUsageFile  = 'Mem_peformance.txt'
        self.rxRateFile       = 'Rx_performance.txt'
        self.txRateFile       = 'Tx_performance.txt'

        self.coldBootData     = []
        self.warmBootData     = []
        self.trafficUsageData = []
        self.cpuUsageData     = []
        self.drawInfoData     = []
        self.fpsInfoData      = []
        self.memoryUsageData  = []
        self.rxRateData       = []
        self.txRateData       = []

        self.imageDict = {
            'cpu'    : 'cpuPerf.png',
            'cold'   : 'coldBootPerf.png',
            'warm'   : 'warmBootPerf.png',
            'traffic': 'trafficUsagePerf.png',
            'draw'   : 'overDrawPerf.png',
            'fps'    : 'fpsPerf.png',
            'memory' : 'memoryUsagePerf.png',
            'rx'     : 'rxRatePerf.png',
            'tx'     : 'txRatePerf.png'
        }

        self.titleDict = {
            'cpu'    : u'CPU 性能(%)',
            'cold'   : u'冷启动性能(ms)',
            'warm'   : u'热启动性能(ms)',
            'traffic': u'流量使用',
            'draw'   : u'Draw 性能',
            'fps'    : u'Fps 性能',
            'memory' : u'内存性能(Mb)',
            'rx'     : u'上行速率',
            'tx'     : u'下行速率'
        }


    def handle(self, startTime, endTime, reportPath):
        self.reportPath = reportPath
        self.startTime = startTime
        self.endTime = endTime
        try:
            self.cpuHandle()
            self.memoryHandle()
            self.txHandle()
            self.rxHandle()
            self.coldBootHandle()
            self.warmBootHandle()
            self.fpsHandle()
            self.drawHandle()
            self.trafficHandle()

            return self.generateReport()

        except Exception as e:
            print(str(e))

    def cpuHandle(self):
        filePath = os.path.join(self.reportPath, self.cpuUsageFile)
        try:
            pngX = []
            pngY = []
            if os.path.exists(filePath):
                i = 1
                performaceData = self.dataHandle(filePath)
                for line in performaceData:
                    value = str(line).split(':')
                    if (len(value) == 2):
                        pngX.append(i)
                        pngY.append(float(value[1]))
                        i = i + 1

                self.drawChart(pngX, pngY, 'cpu')
        except Exception as e:
            print(str(e))

    def memoryHandle(self):
        filePath = os.path.join(self.reportPath, self.memoryUsageFile)
        try:
            pngX = []
            pngY = []
            if os.path.exists(filePath):
                i = 1
                performaceData = self.dataHandle(filePath)
                for line in performaceData:
                    value = str(line).split(':')
                    if (len(value) == 2):
                        pngX.append(i)
                        pngY.append(float(value[1]))
                        i = i + 1

                self.drawChart(pngX, pngY, 'memory')
        except Exception as e:
            print(str(e))

    def coldBootHandle(self):
        filePath = os.path.join(self.reportPath, self.coldBootFile)
        try:
            pngX = []
            pngY = []
            if os.path.exists(filePath):
                i = 1
                performaceData = self.dataHandle(filePath)
                for line in performaceData:
                    value = str(line).split(':')
                    if (len(value) == 2):
                        pngX.append(i)
                        pngY.append(float(value[1]))
                        i = i + 1

                self.drawChart(pngX, pngY, 'cold')
        except Exception as e:
            print(str(e))

    def warmBootHandle(self):
        filePath = os.path.join(self.reportPath, self.warmBootFile)
        try:
            pngX = []
            pngY = []
            if os.path.exists(filePath):
                i = 1
                performaceData = self.dataHandle(filePath)
                for line in performaceData:
                    value = str(line).split(':')
                    if (len(value) == 2):
                        pngX.append(i)
                        pngY.append(float(value[1]))
                        i = i + 1

                self.drawChart(pngX, pngY, 'warm')
        except Exception as e:
            print(str(e))

    def fpsHandle(self):
        filePath = os.path.join(self.reportPath, self.fpsInfoFile)
        try:
            pngX = []
            pngY = []
            if os.path.exists(filePath):
                i = 1
                performaceData = self.dataHandle(filePath)
                for line in performaceData:
                    value = str(line).split(' ')
                    if (len(value) == 3):
                        pngX.append(value[0])
                        pngY.append(float(value[2]))
                        i = i + 1

                self.drawChart(pngX, pngY, 'fps')
        except Exception as e:
            print(str(e))

    def drawHandle(self):
        filePath = os.path.join(self.reportPath, self.drawInfoFile)
        try:
            pngX = []
            pngY = []
            if os.path.exists(filePath):
                i = 1
                performaceData = self.dataHandle(filePath)
                for line in performaceData:
                    value = str(line).split(' ')
                    if (len(value) == 3):
                        pngX.append(value[0])
                        pngY.append(float(value[1]))
                        i = i + 1

                self.drawChart(pngX, pngY, 'draw')
        except Exception as e:
            print(str(e))

    def rxHandle(self):
        filePath = os.path.join(self.reportPath, self.rxRateFile)
        try:
            pngX = []
            pngY = []
            if os.path.exists(filePath):
                i = 1
                performaceData = self.dataHandle(filePath)
                for line in performaceData:
                    value = str(line).split(':')
                    if (len(value) == 2):
                        pngX.append(i)
                        pngY.append(float(value[1]))
                        i = i + 1

                self.drawChart(pngX, pngY, 'rx')
        except Exception as e:
            print(str(e))

    def txHandle(self):
        filePath = os.path.join(self.reportPath, self.txRateFile)
        try:
            pngX = []
            pngY = []
            if os.path.exists(filePath):
                i = 1
                performaceData = self.dataHandle(filePath)
                for line in performaceData:
                    value = str(line).split(':')
                    if (len(value) == 2):
                        pngX.append(i)
                        pngY.append(float(value[1]))
                        i = i + 1

                self.drawChart(pngX, pngY, 'tx')
        except Exception as e:
            print(str(e))

    def trafficHandle(self):
        filePath = os.path.join(self.reportPath, self.trafficUsageFile)
        try:
            if os.path.exists(filePath):
                htmlContent = ''
                performaceData = self.dataHandle(filePath)
                for line in performaceData:
                    value = str(line).split(':')
                    if (len(value) > 1):
                        htmlContent = "<tr><td>%s</td><td>%s</td></tr>" % (str(value[0]) + 's', str(value[1]) + 'Mb')
                    self.resultTraffic = htmlContent
        except Exception as e:
            print(str(e))

    def dataHandle(self, filePath):
        performanceData = []
        dataFile = open(filePath, mode='r', encoding='utf-8')
        try:
            allLines = dataFile.readlines()
            for line in allLines:
                performanceData.append(line)
        except Exception as e:
            raise
        finally:
            dataFile.close()

        return performanceData

    def drawChart(self, x, y, type):
        if type == 'cold' or type == 'warm':
            def autolabel(rects):
                for rect in rects:
                    height = rect.get_height()
                    pl.text(rect.get_x() + rect.get_width(), height, "%sms" % int(height))

            pl.figure(figsize=[6, 2.5])
            rect = pl.bar(left=tuple(x), height=tuple(y), align="center", width = 0.35, color='#46a3ff')
            pl.title(self.titleDict[type])
            pl.grid(True)
            pl.xticks(tuple(x))
            autolabel(rect)
            pngFile = os.path.join(self.reportPath, self.imageDict[type])
            pl.savefig(pngFile)
            pl.close()
        elif type == 'fps' or type == 'draw':
            def autolabel(rects):
                for rect in rects:
                    height = rect.get_height()
                    pl.text(rect.get_x() + rect.get_width(), height, "%s" % float(height))

            pl.figure(figsize=[6, 2.5])
            rect = pl.bar(left=(0, 1, 2, 3), height=tuple(y), align="center", width=0.35, color='#46a3ff')
            pl.title(self.titleDict[type])
            pl.grid(True)
            pl.xticks((0, 1, 2, 3), tuple(x))
            autolabel(rect)
            pngFile = os.path.join(self.reportPath, self.imageDict[type])
            pl.savefig(pngFile)
            pl.close()
        else:
            pl.figure(figsize=[6, 2.5])
            pl.plot(x, y, color='#46a3ff', linewidth=1)
            pl.title(self.titleDict[type])
            pl.grid(True)
            pl.xlim(0, x[-1])

            pngFile = os.path.join(self.reportPath, self.imageDict[type])
            pl.savefig(pngFile)
            pl.close()

    def generateReport(self):
        try:
            templateHtml = self.loadHtmlTemplate()
            startTime = self.startTime
            endTime = self.endTime
            trafficResult = self.resultTraffic

            templateHtml = templateHtml % (self.phoneVersion, self.deviceID, self.buildVersion, self.appVersion, startTime, endTime, trafficResult)

            return templateHtml
        except Exception as e:
            print(str(e))

    def loadHtmlTemplate(self):
        resourcesDirectory = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/resources/"
        file = os.path.join(resourcesDirectory, 'templateMailPerformance.html')
        templateFile = open(file, encoding='utf-8')
        try:
            contents = templateFile.read()
        except Exception as e:
            raise
        finally:
            templateFile.close()
        return str(contents)


def sendPerformanceMail(startTime, endTime, reportPath, deviceType):
    fromAddress = constants.Email.mailAddress
    toAddress = constants.Email.performanceMaillAddress
    smtpServer = constants.Email.smtpServer
    smtpUser = constants.Email.username
    smtpPassword = constants.Email.password
    smtpPort = constants.Email.smtpPort

    msgRoot = MIMEMultipart('related')

    if deviceType == 'android':
        msgRoot['Subject'] = Header(constants.PERFORMANCE_HEADR_NAME % (deviceType.capitalize(), time.strftime('%Y-%m-%d')), "utf-8")
    elif deviceType == 'ios':
        msgRoot['Subject'] = Header(constants.PERFORMANCE_HEADR_NAME % ('IOS', time.strftime('%Y-%m-%d')), "utf-8")
    else:
        raise
    msgRoot['From'] = (r"%s <" + fromAddress + ">") % Header(constants.SYSTEM_NAME, "utf-8")
    msgRoot['To'] = ';'.join(toAddress)

    msgAlternative = MIMEMultipart('alternative')
    msgRoot.attach(msgAlternative)

    mailBodyContents = PeformanceDraw(deviceType).handle(startTime, endTime, reportPath)
    msgAlternative.attach(MIMEText(mailBodyContents, 'html', 'utf-8'))

    attachmentFile = 'test_performance_result.xlsx'

    attachmetPath = os.path.join(reportPath, attachmentFile)
    if os.path.exists(attachmetPath):
        attach = MIMEApplication(open(attachmetPath, 'rb').read())
        attach.add_header('Content-Disposition', 'attachment', filename=attachmentFile)
        msgRoot.attach(attach)

    # 指定图片为当前目录
    i = 1
    for png in ['cpuPerf.png', 'memoryUsagePerf.png', 'rxRatePerf.png', 'txRatePerf.png', 'coldBootPerf.png',
                'warmBootPerf.png', 'fpsPerf.png', 'overDrawPerf.png']:
        pngPath = os.path.join(reportPath, png)
        if os.path.exists(pngPath):
            fp = open(pngPath, 'rb')
            msgImage = MIMEImage(fp.read())
            fp.close()

            # 定义图片 ID，在 HTML 文本中引用
            msgImage.add_header('Content-ID', '<image%s>' % i)
            msgRoot.attach(msgImage)
            i += 1

    s = smtplib.SMTP(smtpServer, smtpPort)
    s.ehlo()
    s.starttls()
    s.login(smtpUser, smtpPassword)
    s.sendmail(fromAddress, toAddress, msgRoot.as_string())
    s.quit()


if __name__ == "__main__":
    reportPath = '/Users/songbo/workspace/autotest/report/ffan/20161020/1'
    sendPerformanceMail('2016/10/20 01:01:05', '2016/10/20 02:49:28', reportPath, 'android')