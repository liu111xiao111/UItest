
import os
import time
import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

from com.qa.automation.appium.configs import constants


class MonkeyHandle(object):
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

        self.startTime = ''
        self.endTime = ''

        self.resultMonkey = ''
        self.resultTraffic = ''

        self.fileNameMoneky = 'Android_monkey.log'
        self.fileNameTraffic = 'Traffic_performance.txt'

    def handle(self, startTime, endTime, reportPath):
        try:
            self.startTime = startTime
            self.endTime = endTime
            monkeyFilePath = os.path.join(reportPath, self.fileNameMoneky)
            trafficFilePath = os.path.join(reportPath, self.fileNameTraffic)
            if (os.path.exists(monkeyFilePath) and os.path.exists(trafficFilePath)):
                self.monkeyHandle(monkeyFilePath)
                self.trafficHandle(trafficFilePath)

            return self.generateReport()

        except Exception as e:
            print(str(e))

    def trafficHandle(self, filePath):
        try:
            if (filePath != ''):
                performanceData = []
                htmlContent = ''
                dataFile = open(filePath, mode='r', encoding='utf-8')
                allLines = dataFile.readlines()
                for line in allLines:
                    performanceData.append(line)
                for line in performanceData:
                    value = str(line).split(':')
                    if (len(value) > 1):
                        htmlContent = "<tr><td>%s</td><td>%s</td></tr>" % (str(value[0]) + 's', str(value[1]) + 'Mb')
                self.resultTraffic = htmlContent
        except Exception as e:
            print(str(e))
        finally:
            dataFile.close()

    def monkeyHandle(self, filePath):
        try:
            if os.path.exists(filePath):
                monkeyData = self.dataHandle(filePath)
                exception = ''
                exception_list = {'空指针异常': 0,
                                  'debug异常': 0,
                                  '低内存异常': 0,
                                  '操作无响应异常': 0,
                                  '其他异常': 0}
                for line in monkeyData:
                    if 'NullPointerException' in line:
                        exception = u'空指针异常'
                    elif 'IllegalStateException' in line:
                        exception = u'debug异常'
                    elif 'OutOfMemoryError' in line:
                        exception = u'低内存异常'
                    elif 'NOT RESPONDING' in line:
                        exception = u'操作无响应异常'
                    if line == '\n':
                        if exception == '':
                            exception = u'其他异常'
                        exception_list[exception] = exception_list[exception] + 1

                avgRowContent = ''
                for key, value in exception_list.items():
                    avgRowContent = avgRowContent + "<tr id='result_row'><td>%s</td><td colspan='3'>%s</td></tr>" % (
                    key, value)
                self.resultMonkey = avgRowContent
        except Exception as e:
            print(str(e))

    def dataHandle(self, filePath):
        monkeyData = []
        inseartValue = False
        dataFile = open(filePath, mode='r', encoding='utf-8')
        try:
            allLines = dataFile.readlines()
            for line in allLines:
                if line.startswith('// CRASH') or line.startswith('// NOT RESPONDING') or inseartValue == True:
                    inseartValue = True
                    if line == '\n':
                        continue
                    monkeyData.append(line)
                    if line.startswith('**'):
                        inseartValue = False
                        monkeyData.append('\n')
        except Exception as e:
            raise
        finally:
            dataFile.close()

        return monkeyData

    def generateReport(self):
        try:
            templateHtml = self.loadHtmlTemplate()
            startTime = self.startTime
            endTime = self.endTime
            trafficResult = self.resultTraffic
            resultMonkey = self.resultMonkey

            templateHtml = templateHtml % (self.phoneVersion, self.deviceID, self.buildVersion, self.appVersion, startTime, endTime, trafficResult, resultMonkey)

            return templateHtml
        except Exception as e:
            print(str(e))

    def loadHtmlTemplate(self):
        resourcesDirectory = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/resources/"
        file = os.path.join(resourcesDirectory, 'templateMailMonkey.html')
        templateFile = open(file, encoding='utf-8')
        try:
            contents = templateFile.read()
        except Exception as e:
            raise
        finally:
            templateFile.close()
        return str(contents)

def sendTestResultMail(startTime, endTime, reportPath, deviceType):
    fromAddress = constants.Email.mailAddress
    toAddress = constants.Email.monkeyMaillAddress
    smtpServer = constants.Email.smtpServer
    smtpUser = constants.Email.username
    smtpPassword = constants.Email.password
    smtpPort = constants.Email.smtpPort

    attachmentFiles = []

    if deviceType == 'android':
        logcatFile = 'Android_monkey_logcat.log'
        reportFile = 'test_monkey_result.html'
        attachmentFiles.append(logcatFile)
        attachmentFiles.append(reportFile)
    elif deviceType == 'ios':
        pass
        # file = 'test_monkey_result.html'
        # reportFile = os.path.join(reportPath, 'feifan_automation_test_report_ios.html')
    else:
        raise

    mailBodyContents = MonkeyHandle(deviceType).handle(startTime, endTime, reportPath)
    msg = MIMEMultipart('related')

    body = MIMEText(mailBodyContents, 'html', 'utf-8')
    msg.attach(body)

    for file in attachmentFiles:
        filePath = os.path.join(reportPath, file)
        if os.path.exists(filePath):
            attach = MIMEApplication(open(filePath, 'rb').read())
            attach.add_header('Content-Disposition', 'attachment', filename=file)
            msg.attach(attach)

    if deviceType == 'android':
        msg['Subject'] = Header(constants.MONKEY_HEADR_NAME % (deviceType.capitalize(), time.strftime('%Y-%m-%d')), "utf-8")
    elif deviceType == 'ios':
        msg['Subject'] = Header(constants.MONKEY_HEADR_NAME % ('IOS', time.strftime('%Y-%m-%d')), "utf-8")
    else:
        raise
    msg['From'] = (r"%s <" + fromAddress + ">") % Header(constants.SYSTEM_NAME, "utf-8")
    msg['To'] = ';'.join(toAddress)

    s = smtplib.SMTP(smtpServer, smtpPort)
    s.ehlo()
    s.starttls()
    s.login(smtpUser, smtpPassword)
    s.sendmail(fromAddress, toAddress, msg.as_string())
    s.quit()


if __name__ == "__main__":
    reportPath = '/Users/songbo/workspace/autotest/monkey/android_monkey_log'
    sendTestResultMail('2016/10/20 03:01:00', '2016/10/20 07:06:05', reportPath, 'android')
