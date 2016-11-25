'''
Created on Aug 31, 2016

@author: chencheng
'''

import os

class MonkeyHandle:
    def __init__(self,):
        self.dataMonkey = ''
        self.resultMonkey = ''
        self.resultTraffic = ''

        self.startTime = ''
        self.endTime = ''

        self.fileNameMoneky = 'Android_monkey.log'
        self.fileNameTraffic = 'Traffic_performance.txt'
        self.monkeyTotalData = []

    def Handle(self, startTime, endTime, reportPath='/Users/auto/Desktop/performance_data/'):
        try:
            self.startTime = startTime
            self.endTime = endTime
            monkeyFilePath = os.path.join(reportPath, self.fileNameMoneky)
            trafficFilePath = os.path.join(reportPath, self.fileNameTraffic)

            if(os.path.exists(monkeyFilePath) and os.path.exists(trafficFilePath)):
                self.monkeyHandle(monkeyFilePath)
                self.trafficHandle(trafficFilePath)

            self.createHtmlReport(reportPath)

            # self.removePerformanceFile(monkeyFilePath)
        except Exception as e:
            print(str(e))

    def HandleForStability(self, fileName = '/Users/auto/Desktop/performance_data/log/logcat.log'):
        try:
            if(os.path.exists(fileName)):
                monkeyData = self.dataHandleForStability(fileName)
                if len(monkeyData) != 0:
                    self.monkeyTotalData.append(monkeyData)
#                 self.monkeyHandleForStability(fileName)

            #self.createHtmlReport(reportPath)

            # self.removePerformanceFile(monkeyFilePath)
        except Exception as e:
            print(str(e))

    def monkeyHandle(self, filePath):
        try:
            htmlContent = ''
            if filePath != '':
                number = 1
                monkeyData = self.dataHandle(filePath)
                crashLogs = ''
                exception = ''
                exception_list = {'空指针异常'      : 0,
                                  'debug异常'      : 0,
                                  '低内存异常'      : 0,
                                  '操作无响应异常'  : 0,
                                  '其他异常'        : 0}
                for line in monkeyData:
                    print(line)
                    crashLog = "<p>%s</p>" % line
                    crashLogs = crashLogs + crashLog
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
                        htmlContent = htmlContent + "<tr class='failClass'><td>%s</td><td><a href=\"javascript:showClassDetail('c%s',1)\">Detail</a></td></tr>" % (exception, number)
                        htmlContent = htmlContent + "<tr id='ft%s.1' class='none hiddenRow'><td class='errorCase'><div class='testcase'>异常信息</div></td><td colspan='5'>%s</td></tr>" % (number, crashLogs)
                        crashLogs = ''
                        number = number + 1

                if not htmlContent:
                    htmlContent = "<tr class='passClass'><td>无</td><td colspan='3'>Pass</td></tr>"
                self.dataMonkey = htmlContent

                avgRowContent = ''
                for key, value in exception_list.items():
                    avgRowContent = avgRowContent + "<tr id='result_row'><td>%s</td><td colspan='3'>%s</td></tr>" % (key, value)
                self.resultMonkey = avgRowContent
                print(self.resultMonkey)
        except Exception as e:
            print(str(e))

    def monkeyHandleForStability(self, startTime, endTime, reportPath='/Users/auto/Desktop/performance_data/'):
        try:
            self.startTime = startTime
            self.endTime = endTime
            htmlContent = ''
#             if filePath != '':
            number = 1
            monkeyData = self.monkeyTotalData
            crashLogs = ''
            exception = ''
            exception_list = {'空指针异常'      : 0,
                              'debug异常'      : 0,
                              '低内存异常'      : 0,
                              '操作无响应异常'  : 0,
                              '其他异常'        : 0}
            for line in monkeyData:
                crashLog = "<p>%s</p>" % line
                crashLogs = crashLogs + crashLog
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
                    htmlContent = htmlContent + "<tr class='failClass'><td>%s</td><td><a href=\"javascript:showClassDetail('c%s',1)\">Detail</a></td></tr>" % (exception, number)
                    htmlContent = htmlContent + "<tr id='ft%s.1' class='none hiddenRow'><td class='errorCase'><div class='testcase'>异常信息</div></td><td colspan='5'>%s</td></tr>" % (number, crashLogs)
                    crashLogs = ''
                    number = number + 1

            print(htmlContent)

            if not htmlContent:
                htmlContent = "<tr class='passClass'><td>无</td><td colspan='3'>Pass</td></tr>"
            self.dataMonkey = htmlContent
            print(self.dataMonkey)

            avgRowContent = ''
            for key, value in exception_list.items():
                avgRowContent = avgRowContent + "<tr id='result_row'><td>%s</td><td colspan='3'>%s</td></tr>" % (key, value)
            self.resultMonkey = avgRowContent
            self.createHtmlReportForStability(reportPath)

        except Exception as e:
            print(str(e))

    def trafficHandle(self, filePath):
        try:
            if (filePath != ''):
                performanceData = []
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

    def dataHandleForStability(self, filePath):
        monkeyData = []
#         inseartValue = False
        dataFile = open(filePath, mode='r', encoding='utf-8')
        try:
            allLines = dataFile.readlines()
            for line in allLines:
                if (line.find(': ANR ') != -1):
#                     inseartValue = True
#                     if line == '\n':
#                         continue
                    monkeyData.append(line)
#                     if line.startswith('**'):
#                         inseartValue = False
#                         monkeyData.append('\n')
        except Exception as e:
            raise
        finally:
            dataFile.close()


        print("MMMMMM")
        print(monkeyData)
        return monkeyData

    def createHtmlReport(self, reportPath):
        report = os.path.join(reportPath, 'test_monkey_result.html')
        resultFile = open(report, mode='w+', encoding='utf-8')
        try:
            templateHtml = self.loadHtmlTemplate()
            monkeyData = self.dataMonkey
            resultData = self.resultMonkey
            trafficData = self.resultTraffic

            templateHtml = templateHtml % (
            self.startTime, self.endTime, trafficData, resultData, monkeyData)

            resultFile.write(templateHtml)
        except Exception as e:
            print(str(e))
        finally:
            resultFile.close()

    def createHtmlReportForStability(self, reportPath):
        report = os.path.join(reportPath, 'test_stability_result.html')
        resultFile = open(report, mode='w+', encoding='utf-8')
        try:
            templateHtml = self.loadHtmlTemplateForStability()
            monkeyData = self.dataMonkey
            print("OOOOO")
            print(monkeyData)
            resultData = self.resultMonkey
            print("PPPPP")
            print(resultData)
            templateHtml = templateHtml % (
            self.startTime, self.endTime, resultData, monkeyData)

            resultFile.write(templateHtml)
        except Exception as e:
            print(str(e))
        finally:
            resultFile.close()

    def createExcelReport(self):
        pass

    def loadHtmlTemplate(self):
        resourcesDirectory = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(
            os.path.dirname(os.path.abspath(__file__)))))) + "/resources/"
        file = os.path.join(resourcesDirectory, 'templateMonkey.html')
        templateFile = open(file, encoding='utf-8')
        try:
            contents = templateFile.read()
        except Exception as e:
            raise
        finally:
            templateFile.close()
        return str(contents)

    def loadHtmlTemplateForStability(self):
        resourcesDirectory = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(
            os.path.dirname(os.path.abspath(__file__)))))) + "/resources/"
        file = os.path.join(resourcesDirectory, 'templateStability.html')
        templateFile = open(file, encoding='utf-8')
        try:
            contents = templateFile.read()
        except Exception as e:
            raise
        finally:
            templateFile.close()
        return str(contents)

    def removePerformanceFile(self, filePath):
        try:
            if(os.path.exists(filePath)):
                os.remove(filePath)
        except Exception as e:
            print(str(e))


if (__name__ == "__main__"):
    performance = MonkeyHandle()
    performance.Handle('2016/09/01 12:23', '2016/09/01 13:11', '/Users/songbo')
