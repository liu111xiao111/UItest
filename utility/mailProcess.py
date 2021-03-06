import os
import time
import smtplib
import html.parser as html_parser
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

from configs import constants


DEVICE_TYPE = 'LGE LG-D802'
SYSTEM_VERSION = '4.4.2'
APP_VERSION = '4.10.1.0'
START_TIME = '2016-12-07 01:06:01'
DURATION_TIME = '0:59:43.798332'
TOTAL_TEST_CASES = '0'
PASS_TEST_CASES = '0'
FAIL_TEST_CASES = '0'
ERROR_TEST_CASES = '0'


class TestResultParser(html_parser.HTMLParser):
    def __init__(self):
        html_parser.HTMLParser.__init__(self)

        self.readed = False
        self.readContent = None

        self.report_name = None
        self.test_summary = {
            'start_time': None,
            'duration': None,
            'Pass': 0,
            'Failure': 0,
            'Error' : 0
        }
        self.failed_case = []
        self.error_case = []
        self.passed_case = []
        self.filterContent = ['Start Time:', 'Duration:', 'Status:']

    def handle_starttag(self, tag, attrs):
        if(tag == 'h1'):
            self.readContent = 'report_name'
            self.readed = True
        if(tag == 'p'):
            if(len(attrs) == 0):
                pass
            else:
                for(att, value) in attrs:
                    if(att == 'class' and value == 'attribute'):
                        self.readContent = 'report_summary'
                        self.readed = True
        if(tag == 'tr'):
            if(len(attrs) == 0):
                pass
            else:
                for(att, value) in attrs:
                    if(att == 'class' and value == 'failClass'):
                        self.readContent = 'failed_case'
                        self.readed = True
                        self.readStatus = False
        if (tag == 'tr'):
            if (len(attrs) == 0):
                pass
            else:
                for (att, value) in attrs:
                    if (att == 'class' and value == 'errorClass'):
                        self.readContent = 'error_case'
                        self.readed = True
                        self.readStatus = True
        if (tag == 'tr'):
            if (len(attrs) == 0):
                pass
            else:
                for (att, value) in attrs:
                    if (att == 'class' and value == 'passClass'):
                        self.readContent = 'passed_case'
                        self.readed = True


    def handle_endtag(self, tag):
        if(tag == 'h1' and self.readContent == 'report_name'):
            self.readed = False
        if (tag == 'p' and self.readContent == 'report_summary'):
            self.readed = False
        if (tag == 'tr' and self.readContent == 'failed_case'):
            self.readed = False
        if (tag == 'tr' and self.readContent == 'error_case'):
            self.readed = False
        if (tag == 'tr' and self.readContent == 'passed_case'):
            self.readed = False

    def handle_data(self, data):
        if(self.readed == True and self.readContent == 'report_name'):
            self.report_name = data
            # print('report_name: ' + self.report_name)
        if(self.readed == True and self.readContent == 'report_summary'):
            if(data not in self.filterContent):
                if(self.test_summary['start_time'] == None):
                    self.test_summary['start_time'] = data
                elif(self.test_summary['duration'] == None):
                    self.test_summary['duration'] = data
                elif (self.test_summary['Pass'] == 0):
                    data = str(data).split(' ')
                    if len(data) == 3:
                        self.test_summary[data[1]] = data[2]
                    elif len(data) == 5:
                        self.test_summary[data[1]] = data[2]
                        self.test_summary[data[3]] = data[4]
                    elif len(data) == 7:
                        self.test_summary[data[1]] = data[2]
                        self.test_summary[data[3]] = data[4]
                        self.test_summary[data[5]] = data[6]
                else:
                    pass
                # print('test_summary:' + str(self.test_summary))
        if (self.readed == True and self.readContent == 'failed_case'):
            if(len(str(data).strip()) > 1 and str(data).strip() != 'Detail'):
                self.failed_case.append(data)
                # print(self.failed_case)
        if (self.readed == True and self.readContent == 'error_case'):
            if(len(str(data).strip()) > 1 and str(data).strip() != 'Detail'):
                self.error_case.append(data)
                # print(self.failed_case)
        if (self.readed == True and self.readContent == 'passed_case'):
            if(len(str(data).strip()) > 1 and str(data).strip() != 'Detail'):
                self.passed_case.append(data)
                # print(self.passed_case)

    def readHtmlContents(self, filePath):
        resultFile = open(filePath, encoding='utf-8')
        try:
            resultContents = resultFile.read()
        except Exception as e:
            print(str(e))
        finally:
            resultFile.close()
        return str(resultContents)

    def getReportName(self):
        return self.report_name

    def getTestSummary(self):
        return self.test_summary

    def getFailedCases(self):
        return self.failed_case

    def getErrorCases(self):
        return self.error_case

    def getPassedCases(self):
        return self.passed_case


class ReportHandle(object):
    def __init__(self, deviceType):

        if deviceType == 'android':
            from configs.androidConfig import caseList, appVersion, phoneVersion, buildVersion, deviceID
        elif deviceType == 'ios':
            from configs.iosConfig import caseList, appVersion, phoneVersion, buildVersion, deviceID
        else:
            raise

        self.caseList = caseList
        self.appVersion = appVersion
        self.phoneVersion = phoneVersion
        self.buildVersion = buildVersion
        self.deviceID = deviceID

        self.reportName = ""
        self.parser = TestResultParser()
        self.startTime = ''
        self.duration = ''
        self.resultStatus = ''
        self.htmlContents = ''

    def handle(self, reportFile):
        try:
            htmlContents = self.parser.readHtmlContents(reportFile)
            self.parser.feed(htmlContents)
            self.parser.close()

            reportSummary = self.parser.getTestSummary()

            self.startTime = reportSummary['start_time']
            self.duration = reportSummary['duration']
            self.resultStatus = "<tr id='result_row'><td class='totalClass'>%s</td><td class='passClass'>%s</td><td class='failClass'>%s</td><td class='errorClass'>%s</td></tr>"\
                                % (int(reportSummary['Pass'])+int(reportSummary['Failure'])+int(reportSummary['Error']), reportSummary['Pass'], reportSummary['Failure'], reportSummary['Error'])


            global DEVICE_TYPE
            DEVICE_TYPE = self.phoneVersion
            global SYSTEM_VERSION
            SYSTEM_VERSION = self.buildVersion
            global APP_VERSION
            APP_VERSION = self.appVersion
            global START_TIME
            START_TIME = reportSummary['start_time']
            global DURATION_TIME
            DURATION_TIME = reportSummary['duration']
            global TOTAL_TEST_CASES
            TOTAL_TEST_CASES = str(int(reportSummary['Pass']) + int(reportSummary['Failure']) + int(reportSummary['Error']))
            global PASS_TEST_CASES
            PASS_TEST_CASES = reportSummary['Pass']
            global FAIL_TEST_CASES
            FAIL_TEST_CASES = reportSummary['Failure']
            global ERROR_TEST_CASES
            ERROR_TEST_CASES = reportSummary['Error']

            self.dataHandle()

            return self.generateReport()

        except Exception as e:
            print(str(e))

    def dataHandle(self):
        failedCases = self.parser.getFailedCases()
        errorCases = self.parser.getErrorCases()
        passedCases = self.parser.getPassedCases()
        htmlContent = ''

        for count in range(0, len(errorCases)):
            caseAutoName = errorCases[count].split('.')[-1]
            caseName = errorCases[count].split('.')[-2]
            htmlContent = htmlContent + "<tr class='errorClass'><td>%s</td><td>%s</td><td>%s</td><td>Error</td></tr>" % (self.caseList[caseAutoName][1], self.caseList[caseAutoName][0], caseName)

        for count in range(0, len(failedCases)):
            caseAutoName = failedCases[count].split('.')[-1]
            caseName = failedCases[count].split('.')[-2]
            htmlContent = htmlContent + "<tr class='failClass'><td>%s</td><td>%s</td><td>%s</td><td>Failed</td></tr>" % (self.caseList[caseAutoName][1], self.caseList[caseAutoName][0], caseName)

        for count in range(0, len(passedCases)):
            caseAutoName = passedCases[count].split('.')[-1]
            caseName = passedCases[count].split('.')[-2]
            htmlContent = htmlContent + "<tr class='passClass'><td>%s</td><td>%s</td><td>%s</td><td>Passed</td></tr>" % (self.caseList[caseAutoName][1], self.caseList[caseAutoName][0], caseName)

        self.htmlContents = htmlContent

    def generateReport(self):
        try:
            templateHtml = self.loadHtmlTemplate()
            startTime = self.startTime
            duration = self.duration
            resultStatus = self.resultStatus

            resultData = self.htmlContents

            templateHtml = templateHtml % (self.phoneVersion, self.deviceID, self.buildVersion, self.appVersion, startTime, duration, resultStatus, resultData)

            return templateHtml
        except Exception as e:
            print(str(e))

    def loadHtmlTemplate(self):
        resourcesDirectory = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/resources/"
        file = os.path.join(resourcesDirectory, 'templateMailReport.html')
        templateFile = open(file, encoding='utf-8')
        try:
            contents = templateFile.read()
        except Exception as e:
            raise
        finally:
            templateFile.close()
        return str(contents)

def sendTestResultMail(reportPath, deviceType):
    fromAddress = constants.Email.mailAddress
    toAddress = constants.Email.patrolMailAddress
    smtpServer = constants.Email.smtpServer
    smtpUser = constants.Email.username
    smtpPassword = constants.Email.password
    smtpPort = constants.Email.smtpPort

    if deviceType == 'android':
        file = 'test_cases_report_android.html'
        if (os.path.exists(os.path.join(reportPath, 'feifan_automation_test_report.html'))):
            reportFile = os.path.join(reportPath, 'feifan_automation_test_report.html')
        elif (os.path.exists(os.path.join(reportPath, 'shanghu_automation_test_report.html'))):
            reportFile = os.path.join(reportPath, 'shanghu_automation_test_report.html')
        else:
            raise
    elif deviceType == 'ios':
        file = 'test_cases_report_ios.html'
        if (os.path.exists(os.path.join(reportPath, 'feifan_automation_test_report_ios.html'))):
            reportFile = os.path.join(reportPath, 'feifan_automation_test_report_ios.html')
        elif (os.path.exists(os.path.join(reportPath, 'shanghu_automation_test_report_ios.html'))):
            reportFile = os.path.join(reportPath, 'shanghu_automation_test_report_ios.html')
        else:
            raise
    else:
        raise

    mailBodyContents = ReportHandle(deviceType).handle(reportFile)
    msg = MIMEMultipart()

    body = MIMEText(mailBodyContents, 'html', 'utf-8')
    msg.attach(body)

    part = MIMEBase('application', 'octet-stream')
    part.set_payload(open(os.path.join(reportPath, file), 'rb').read())
    encoders.encode_base64(part)
    part.add_header('content-disposition', 'attachment', filename=file)
    msg.attach(part)

    if deviceType == 'android':
        if (os.path.exists(os.path.join(reportPath, 'feifan_automation_test_report.html'))):
            msg['Subject'] = Header(constants.PATROL_HEADR_NAME % (deviceType.capitalize(), time.strftime('%Y-%m-%d')), "utf-8")
        else:
            msg['Subject'] = Header(constants.PATROL_SHANGHU_HEADR_NAME % (deviceType.capitalize(), time.strftime('%Y-%m-%d')), "utf-8")
    elif deviceType == 'ios':
        if (os.path.exists(os.path.join(reportPath, 'feifan_automation_test_report_ios.html'))):
            msg['Subject'] = Header(constants.PATROL_HEADR_NAME % ('IOS', time.strftime('%Y-%m-%d')), "utf-8")
        else:
            msg['Subject'] = Header(constants.PATROL_SHANGHU_HEADR_NAME % ('IOS', time.strftime('%Y-%m-%d')), "utf-8")

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
    reportPath = '/Users/uasd-qiaojx/Desktop/report/shanghu/20161206/8'
    sendTestResultMail(reportPath, 'android')
