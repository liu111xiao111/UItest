import os
import sys

import html.parser as html_parser

from com.qa.automation.appium.configs.androidConfig import caseList, appVersion, phoneVersion


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
        self.failed_case_detail = []
        self.error_case = []
        self.error_case_detail = []
        self.passed_case = []
        self.filterContent = ['Start Time:', 'Duration:', 'Status:']
        self.readStatus = False

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
        if(tag == 'pre' and not self.readStatus):
            self.readContent = 'failed_case_detail'
            self.readed = True

        if (tag == 'tr'):
            if (len(attrs) == 0):
                pass
            else:
                for (att, value) in attrs:
                    if (att == 'class' and value == 'errorClass'):
                        self.readContent = 'error_case'
                        self.readed = True
                        self.readStatus = True
        if (tag == 'pre' and self.readStatus):
            self.readContent = 'error_case_detail'
            self.readed = True

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
        if (tag == 'pre' and self.readContent == 'failed_case_detail'):
            self.readed = False
        if (tag == 'pre' and self.readContent == 'error_case_detail'):
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
        if (self.readed == True and self.readContent == 'failed_case_detail'):
            self.failed_case_detail.append(data)
            # print(self.failed_case_detail)
        if (self.readed == True and self.readContent == 'error_case'):
            if(len(str(data).strip()) > 1 and str(data).strip() != 'Detail'):
                self.error_case.append(data)
                # print(self.failed_case)
        if (self.readed == True and self.readContent == 'error_case_detail'):
            self.error_case_detail.append(data)
            # print(self.failed_case_detail)
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

    def getFailedCaseDetails(self):
        return self.failed_case_detail

    def getErrorCases(self):
        return self.error_case

    def getErrorCaseDetails(self):
        return self.error_case_detail

    def getPassedCases(self):
        return self.passed_case


class ReportHandle(object):
    def __init__(self):
        self.reportName = "feifan_automation_test_report.html"
        self.parser = TestResultParser()
        self.startTime = ''
        self.duration = ''
        self.resultStatus = ''
        self.htmlContents = ''

    def handle(self, reportPath):
        try:
            report = os.path.join(reportPath, self.reportName)
            htmlContents = self.parser.readHtmlContents(report)
            self.parser.feed(htmlContents)
            self.parser.close()

            reportSummary = self.parser.getTestSummary()

            self.startTime = reportSummary['start_time']
            self.duration = reportSummary['duration']
            self.resultStatus = "<tr id='result_row'><td class='totalClass'>%s</td><td class='passClass'>%s</td><td class='failClass'>%s</td><td class='errorClass'>%s</td></tr>"\
                                % (int(reportSummary['Pass'])+int(reportSummary['Failure'])+int(reportSummary['Error']), reportSummary['Pass'], reportSummary['Failure'], reportSummary['Error'])

            self.dataHandle()

            self.generateReport(reportPath)

        except Exception as e:
            print(str(e))

    def dataHandle(self):
        failedCases = self.parser.getFailedCases()
        failedCaseDetails = self.parser.getFailedCaseDetails()
        errorCases = self.parser.getErrorCases()
        errorCaseDetails = self.parser.getErrorCaseDetails()
        passedCases = self.parser.getPassedCases()
        htmlContent = ''

        for count in range(0, len(errorCases)):
            caseAutoName = errorCases[count].split('.')[-1]
            caseName = errorCases[count].split('.')[-2]
            htmlContent = htmlContent + "<tr class='errorClass'><td>%s</td><td>%s</td><td>Failed</td><td><a href=\"javascript:showClassDetail('c%s',1)\">Detail</a></td></tr>" % (caseList[caseAutoName], caseName, count+1)
            htmlContent = htmlContent + "<tr id='ft%s.1' class='none hiddenRow'><td class='errorCase'><div class='testcase'>失败信息</div></td><td colspan='3'><pre>%s</pre></td></tr>" % (count+1, errorCaseDetails[count])

        for count in range(0, len(failedCases)):
            caseAutoName = failedCases[count].split('.')[-1]
            caseName = failedCases[count].split('.')[-2]
            htmlContent = htmlContent + "<tr class='failClass'><td>%s</td><td>%s</td><td>Failed</td><td><a href=\"javascript:showClassDetail('c%s',1)\">Detail</a></td></tr>" % (caseList[caseAutoName], caseName, count+1)
            htmlContent = htmlContent + "<tr id='ft%s.1' class='none hiddenRow'><td class='failCase'><div class='testcase'>失败信息</div></td><td colspan='3'><pre>%s</pre></td></tr>" % (count+1, failedCaseDetails[count])

        for count in range(0, len(passedCases)):
            caseAutoName = passedCases[count].split('.')[-1]
            caseName = passedCases[count].split('.')[-2]
            htmlContent = htmlContent + "<tr class='passClass'><td>%s</td><td>%s</td><td>Passed</td><td></td></tr>" % (caseList[caseAutoName], caseName)

        self.htmlContents = htmlContent

    def generateReport(self, reportPath):
        report = os.path.join(reportPath, 'test_cases_report_android.html')
        resultFile = open(report, 'w+', encoding='utf-8')
        try:
            templateHtml = self.loadHtmlTemplate()
            startTime = self.startTime
            duration = self.duration
            resultStatus = self.resultStatus

            resultData = self.htmlContents

            templateHtml = templateHtml % (phoneVersion, appVersion, startTime, duration, resultStatus, resultData)

            resultFile.write(templateHtml)
        except Exception as e:
            print(str(e))
        finally:
            resultFile.close()


    def loadHtmlTemplate(self):
        resourcesDirectory = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(
            os.path.dirname(os.path.abspath(__file__)))))) + "/resources/"
        file = os.path.join(resourcesDirectory, 'templateReport.html')
        templateFile = open(file, encoding='utf-8')
        try:
            contents = templateFile.read()
        except Exception as e:
            raise
        finally:
            templateFile.close()
        return str(contents)

if __name__ == "__main__":
    ReportHandle().handle('/Users/songbo/workspace/autotest/report/ffan/20161010/4')
