'''
Created on Aug 31, 2016

@author: chencheng
'''

import os
import xlsxwriter


class PerformanceHandle:
    def __init__(self):
        self.dataList = dict()

        self.dataList['cpu'] = ''
        self.dataList['memory'] = ''
        self.dataList['coldBoot'] = ''
        self.dataList['warmBoot'] = ''
        self.dataList['fps'] = ''
        self.dataList['rx'] = ''
        self.dataList['tx'] = ''

        self.excelList = dict()
        self.excelList['cpu'] = []
        self.excelList['memory'] = []
        self.excelList['coldBoot'] = []
        self.excelList['warmBoot'] = []
        self.excelList['fps'] = []
        self.excelList['rx'] = []
        self.excelList['tx'] = []

        self.columnNum = 2

        self.numBootEn = dict()
        self.numBootEn[1] = '1st'
        self.numBootEn[2] = '2nd'
        self.numBootEn[3] = '3rd'
        self.numBootEn[4] = '4th'
        self.numBootEn[5] = '5th'
        self.numBootEn[6] = '6th'
        self.numBootEn[7] = '7th'
        self.numBootEn[8] = '8th'
        self.numBootEn[9] = '9th'
        self.numBootEn[10] = '10th'

        self.startTime = ''
        self.endTime = ''

        self.fileNameCpu = 'Cpu_performance.txt'
        self.fileNameMemory = 'Mem_peformance.txt'
        self.fileNameFps = 'Fps_performance.txt'
        self.fileNameRx = 'Rx_performance.txt'
        self.fileNameTx = 'Tx_performance.txt'
        self.fileNameColdBootTime = 'ColdBootTime_performance.txt'
        self.fileNameWarmBootTime = 'WarmBootTime_performance.txt'

    def Handle(self, startTime, endTime, reportPath=''):
        try:
            self.startTime = startTime
            self.endTime = endTime
            cpuFilePath = os.path.join(reportPath, self.fileNameCpu)
            memoryFilePath = os.path.join(reportPath, self.fileNameMemory)
            coldBootFilePath = os.path.join(reportPath, self.fileNameColdBootTime)
            warmBootFilePath = os.path.join(reportPath, self.fileNameWarmBootTime)
            fpsFilePath = os.path.join(reportPath, self.fileNameFps)
            rxFilePath = os.path.join(reportPath, self.fileNameRx)
            txFilePath = os.path.join(reportPath, self.fileNameTx)

            if(os.path.exists(cpuFilePath)):
                self.cpuHandle(cpuFilePath)

            if (os.path.exists(memoryFilePath)):
                self.memoryHandle(memoryFilePath)

            if (os.path.exists(coldBootFilePath)):
                self.coldBootHandle(coldBootFilePath)

            if (os.path.exists(warmBootFilePath)):
                self.warmBootHandle(warmBootFilePath)

            if (os.path.exists(fpsFilePath)):
                self.fpsHandle(fpsFilePath)

            if (os.path.exists(rxFilePath)):
                self.rxHandle(rxFilePath)

            if (os.path.exists(txFilePath)):
                self.txHandle(txFilePath)

            self.createHtmlReport(reportPath)
            self.createExcelReport(reportPath)

            # self.removePerformanceFile(cpuFilePath)
            # self.removePerformanceFile(memoryFilePath)
            # self.removePerformanceFile(coldBootFilePath)
            # self.removePerformanceFile(warmBootFilePath)
            # self.removePerformanceFile(fpsFilePath)
            # self.removePerformanceFile(rxFilePath)
            # self.removePerformanceFile(txFilePath)

        except Exception as e:
            print(str(e))

    def cpuHandle(self, filePath):
        try:
            htmlContent = ''
            totalNum = 0
            listValues = []
            excelValues = []
            if(filePath != ''):
                freq = 0
                i = 1
                performaceData = self.dataHandle(filePath)
                for line in performaceData:
                    value = str(line).split(':')
                    if (len(value) == 2):
                        if((i % self.columnNum) == 1):
                            rowContent = (
                            "<tr class='passClass'><td>%s</td><td>%s</td>" % (value[0].replace('_', ':'), value[1]))
                        else:
                            rowContent = (
                                "<td>%s</td><td>%s</td></tr>" % (value[0].replace('_', ':'), value[1]))
                        htmlContent = htmlContent + rowContent

                        totalNum = totalNum + float(value[1])

                        listValues.append(float(value[1]))
                        self.excelList['cpu'].append(line)
                        freq = freq + 10
                        i = i + 1

                average = totalNum / (i - 1)
                if((i-1) % 2 == 1):
                    htmlContent = htmlContent + "<td></td><td></td></tr>"
                maxValue = max(listValues)
                minValue = min(listValues)
                avgRowContent = ("<tr id='total_row'><td>average/max/min</td><td colspan='3'>%s/%s/%s</td></tr>" % (
                average, maxValue, minValue))
                htmlContent = htmlContent + avgRowContent
                self.dataList['cpu'] = htmlContent
        except Exception as e:
            print(str(e))

    def memoryHandle(self, filePath):
        try:
            htmlContent = ''
            totalNum = 0
            listValues = []
            if (filePath != ''):
                freq = 0
                i = 1
                performaceData = self.dataHandle(filePath)
                for line in performaceData:
                    value = str(line).split(':')
                    if (len(value) > 1):
                        if ((i % self.columnNum) == 1):
                            rowContent = (
                                "<tr class='passClass'><td>%s</td><td>%s</td>" % (value[0].replace('_', ':'), value[1]))
                        else:
                            rowContent = (
                                "<td>%s</td><td>%s</td></tr>" % (value[0].replace('_', ':'), value[1]))
                        listValues.append(float(value[1]))
                        htmlContent = htmlContent + rowContent
                        totalNum = totalNum + float(value[1])
                        self.excelList['memory'].append(line)
                        freq = freq + 10
                        i = i + 1

                average = totalNum / (i - 1)
                if ((i - 1) % 2 == 1):
                    htmlContent = htmlContent + "<td></td><td></td></tr>"
                maxValue = max(listValues)
                minValue = min(listValues)
                avgRowContent = ("<tr id='total_row'><td>average/max/min</td><td colspan='3'>%s/%s/%s</td></tr>" % (
                average, maxValue, minValue))
                htmlContent = htmlContent + avgRowContent
                self.dataList['memory'] = htmlContent
        except Exception as e:
            print(str(e))

    def coldBootHandle(self, filePath):
        try:
            htmlContent = ""
            totalNum = 0
            listValue = []
            if (filePath != ''):
                i = 1
                performaceData = self.dataHandle(filePath)
                for line in performaceData:
                    value = str(line).split(':')
                    if(len(value) > 1):
                        rowContent = (
                        "<tr class='passClass'><td>%s</td><td>%s</td></tr>" % (self.numBootEn[i], value[1]))
                        htmlContent = htmlContent + rowContent
                        totalNum = totalNum + float(value[1])
                        listValue.append(float(value[1]))
                        self.excelList['coldBoot'].append(line)
                        i = i + 1
                average = totalNum/10
                maxValue = max(listValue)
                minValue = min(listValue)
                avgRowContent = (
                "<tr id='total_row'><td>average/max/min</td><td>%s/%s/%s</td></tr>" % (average, maxValue, minValue))
                htmlContent = htmlContent + avgRowContent
                self.dataList['coldBoot'] = htmlContent
        except Exception as e:
            print(str(e))

    def warmBootHandle(self, filePath):
        try:
            htmlContent = ""
            totalNum = 0
            listValue = []
            if (filePath != ''):
                i = 1
                performaceData = self.dataHandle(filePath)
                for line in performaceData:
                    value = str(line).split(':')
                    if(len(value) > 1):
                        rowContent = (
                        "<tr class='passClass'><td>%s</td><td>%s</td></tr>" % (self.numBootEn[i], value[1]))
                        htmlContent = htmlContent + rowContent
                        totalNum = totalNum + float(value[1])
                        listValue.append(float(value[1]))
                        self.excelList['warmBoot'].append(line)
                        i = i + 1
                average = totalNum/10
                maxValue = max(listValue)
                minValue = min(listValue)
                avgRowContent = (
                "<tr id='total_row'><td>average/max/min</td><td>%s/%s/%s</td></tr>" % (average, maxValue, minValue))
                htmlContent = htmlContent + avgRowContent
                self.dataList['warmBoot'] = htmlContent
        except Exception as e:
            print(str(e))

    def fpsHandle(self, filePath):
        try:
            htmlContent = ""
            if (filePath != ''):
                performaceData = self.dataHandle(filePath)
                for line in performaceData:
                    value = str(line).split(' ')
                    if(len(value) > 1):
                        rowContent = (
                        "<tr class='passClass'><td>%s</td><td>%s</td><td>%s</td></tr>" % (value[0], value[1], value[2]))
                        htmlContent = htmlContent + rowContent
                        self.excelList['fps'].append(line)
                self.dataList['fps'] = htmlContent
        except Exception as e:
            print(str(e))

    def rxHandle(self, filePath):
        try:
            htmlContent = ''
            totalNum = 0
            listValue = []
            if (filePath != ''):
                freq = 0
                i = 1
                performaceData = self.dataHandle(filePath)
                for line in performaceData:
                    value = str(line).split(':')
                    if (len(value) > 1):
                        if ((i % self.columnNum) == 1):
                            rowContent = (
                                "<tr class='passClass'><td>%s</td><td>%s</td>" % (value[0].replace('_', ':'), value[1]))
                        else:
                            rowContent = (
                                "<td>%s</td><td>%s</td></tr>" % (value[0].replace('_', ':'), value[1]))
                        htmlContent = htmlContent + rowContent
                        totalNum = totalNum + float(value[1])
                        listValue.append(float(value[1]))
                        self.excelList['rx'].append(line)
                        freq = freq + 10
                        i = i + 1

                average = totalNum / (i - 1)
                maxValue = max(listValue)
                minValue = min(listValue)
                if ((i - 1) % 2 == 1):
                    htmlContent = htmlContent + "<td></td><td></td></tr>"
                avgRowContent = ("<tr id='total_row'><td>average/max/min</td><td colspan='3'>%s/%s/%s</td></tr>" % (
                average, maxValue, minValue))
                htmlContent = htmlContent + avgRowContent
                self.dataList['rx'] = htmlContent
        except Exception as e:
            print(str(e))

    def txHandle(self, filePath):
        try:
            htmlContent = ''
            totalNum = 0
            listValue = []
            if (filePath != ''):
                freq = 0
                i = 1
                performaceData = self.dataHandle(filePath)
                for line in performaceData:
                    value = str(line).split(':')
                    if (len(value) > 1):
                        if ((i % self.columnNum) == 1):
                            rowContent = (
                                "<tr class='passClass'><td>%s</td><td>%s</td>" % (value[0].replace('_', ':'), value[1]))
                        else:
                            rowContent = (
                                "<td>%s</td><td>%s</td></tr>" % (value[0].replace('_', ':'), value[1]))
                        htmlContent = htmlContent + rowContent
                        totalNum = totalNum + float(value[1])
                        listValue.append(float(value[1]))
                        self.excelList['tx'].append(line)
                        freq = freq + 10
                        i = i + 1

                average = totalNum / (i - 1)
                maxValue = max(listValue)
                minValue = min(listValue)
                if ((i - 1) % 2 == 1):
                    htmlContent = htmlContent + "<td></td><td></td></tr>"
                avgRowContent = ("<tr id='total_row'><td>average/max/min</td><td colspan='3'>%s/%s/%s</td></tr>" % (
                average, maxValue, minValue))
                htmlContent = htmlContent + avgRowContent
                self.dataList['tx'] = htmlContent
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

    def createHtmlReport(self, reportPath):
        report = os.path.join(reportPath, 'test_performance_result.html')
        resultFile = open(report, 'w+')
        try:
            templateHtml = self.loadHtmlTemplate()
            cpuData = self.dataList['cpu']
            memoryData = self.dataList['memory']
            fpsData = self.dataList['fps']
            coldBootData = self.dataList['coldBoot']
            warmBootData = self.dataList['warmBoot']
            upstreamData = self.dataList['tx']
            downstreamData = self.dataList['rx']

            templateHtml = templateHtml % (
            self.startTime, self.endTime, cpuData, memoryData, fpsData, coldBootData, warmBootData, upstreamData, downstreamData)

            resultFile.write(templateHtml)
        except Exception as e:
            print(str(e))
        finally:
            resultFile.close()


    def createExcelReport(self, reportPath):
        report = os.path.join(reportPath, 'test_performance_result.xlsx')
        workbook = xlsxwriter.Workbook(report)
        try:
            # 生成CPU perf sheet
            self.generateExcelReport('CPU Performance', workbook, 'cpu', 'time', 'usage(%)')

            # 生成memory perf sheet
            self.generateExcelReport('Memory Performance', workbook, 'memory', 'time', 'usage(Mb)')

            # 生成Fps perf sheet
            self.generateExcelReport('Fps Performance', workbook, 'fps', 'Tab', 'draw', 'fps')

            # 生成cold boot time perf sheet
            self.generateExcelReport('Cold Boot Time Performance', workbook, 'coldBoot', 'times', 'boot times(ms)')

            # 生成warm boot time perf sheet
            self.generateExcelReport('Warm Boot Time Performance', workbook, 'warmBoot', 'times', 'boot times(ms)')

            # 生成rx perf sheet
            self.generateExcelReport('Upstream Rate Performance', workbook, 'rx', 'date time', 'usage(KBps)')

            # 生成tx perf sheet
            self.generateExcelReport('Downstream Rate Performance', workbook, 'tx', 'date time', 'usage(KBps)')
        except Exception as e:
            print(str(e))
        finally:
            workbook.close()

    def generateExcelReport(self, title, workbook, key, *args):
        worksheet = workbook.add_worksheet(title)
        if len(args) == 2 and 'Boot' not in key:
            worksheet.write(0, 0, args[0])
            worksheet.write(0, 1, args[1])
            row = 1
            for line in self.excelList[key]:
                value = str(line).split(':')
                worksheet.write(row, 0, value[0])
                worksheet.write(row, 1, float(value[1]))
                row = row + 1
            chart = workbook.add_chart({'type': 'line'})
            chart.add_series({'categories' : '=%s!$A$2:$A$%s' % (title, row),
                              'values' : '=%s!$B$2:$B$%s' % (title, row),
                              'name'   : args[1]})
            chart.set_title({
                'name': title,
            })
            worksheet.insert_chart('D3', chart, {'x_scale': 2.5, 'y_scale': 2.5})

        elif len(args) == 2 and 'Boot' in key:
            worksheet.write(0, 0, args[0])
            worksheet.write(0, 1, args[1])
            row = 1
            for line in self.excelList[key]:
                value = str(line).split(':')
                worksheet.write(row, 0, self.numBootEn[row])
                worksheet.write(row, 1, float(value[1]))
                row = row + 1
            chart = workbook.add_chart({'type': 'column'})
            chart.add_series({'categories' : '=%s!$A$2:$A$11' % title,
                              'values': '=%s!$B$2:$B$11' % title,
                              'name': args[1]})
            chart.set_title({
                'name': title,
            })
            worksheet.insert_chart('D3', chart)
        else:
            worksheet.write(0, 0, args[0])
            worksheet.write(0, 1, args[1])
            worksheet.write(0, 2, args[2])
            row = 1
            for line in self.excelList[key]:
                value = str(line).split(' ')
                worksheet.write(row, 0, value[0])
                worksheet.write(row, 1, float(value[1]))
                worksheet.write(row, 2, float(value[2]))
                row = row + 1
            chart = workbook.add_chart({'type': 'column'})
            chart.add_series({'categories' : '=%s!$A$2:$A$%s' % (title, row),
                              'values': '=%s!$B$2:$B$%s' % (title, row),
                              'name': args[1]})
            chart.set_title({
                'name': title,
            })
            worksheet.insert_chart('E3', chart)
            chart = workbook.add_chart({'type': 'column'})
            chart.add_series({'categories' : '=%s!$A$2:$A$%s' % (title, row),
                              'values': '=%s!$B$2:$B$%s' % (title, row),
                              'name': args[2]})
            chart.set_title({
                'name': title,
            })
            worksheet.insert_chart('E20', chart)

    def loadHtmlTemplate(self):
        resourcesDirectory = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(
            os.path.dirname(os.path.abspath(__file__)))))) + "/resources/"
        file = os.path.join(resourcesDirectory, 'templatePerformance.html')
        templateFile = open(file)
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
    # filePath = dict()
    # filePath['cpu']='/Users/auto/Desktop/performance_data/Cpu_performance.txt'
    # filePath['memory']='/Users/auto/Desktop/performance_data/Mem_peformance.txt'
    # filePath['coldboottime']='/Users/auto/Desktop/performance_data/ColdBootTime_com.wanda.app.wanhui_20160831110613.txt'
    # filePath['warmboottime']='/Users/auto/Desktop/performance_data/WarmBootTime_com.wanda.app.wanhui_20160831110613.txt'
    # filePath['fps']=''
    # filePath['rx']='/Users/auto/Desktop/performance_data/Rx_performance.txt'
    # filePath['tx']='/Users/auto/Desktop/performance_data/Tx_performance.txt'
    performance = PerformanceHandle()
    performance.Handle('2016/09/26 09:16:35', '2016/09/26 10:35:53', '/Users/songbo/workspace/autotest/report/ffan/20160926/13')
    # performance.removePerformanceFile('/Users/auto/Desktop/performance_data/Mem_com.wanda.app.wanhui_20160831173118.txt')