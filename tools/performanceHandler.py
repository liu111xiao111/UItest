'''
Created on Nov 17, 2016

@author: songbo
'''

import os
import datetime
import argparse
import xlsxwriter
# import pylab as pl

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

from tools.utility.constants import *

# pl.mpl.rcParams['font.sans-serif'] = ['SimHei']

class Parser(object):
    def __init__(self):
        self.xmlTypeDict = {
            TYPE_CPU         : 'cpuUsage',
            TYPE_MEMORY      : 'ramUsage',
            TYPE_TX          : 'netUpFlow',
            TYPE_RX          : 'netDownFlow',
            TYPE_TEMPERATURE : 'temperature',
            TYPE_TRAFFIC     : 'traffic'
        }

    def txtParser(self, txtPath, type):
        performanceData = list()
        dataFile = open(txtPath, mode='r', encoding='utf-8')
        try:
            allLines = dataFile.readlines()
            for line in allLines:
                performanceData.append(line)
        except Exception as e:
            raise FileExistsError(e)
        finally:
            dataFile.close()

        return self._getTxtData(performanceData, type)

    def _getTxtData(self, performanceData, type):
        dataList = list()
        try:
            if type == TYPE_FPS:
                for line in performanceData:
                    value = str(line).split(' ')
                    if(len(value) > 1):
                        dataList.append(value)
            else:
                for line in performanceData:
                    value = str(line).split(':')
                    if(len(value) > 1):
                        dataList.append(value[1])
        except Exception as e:
            print(str(e))
        finally:
            return dataList

    def xmlParser(self, xmlPath, type):
        doc = ET.parse(xmlPath)
        root = doc.getroot()

        nodes = root.findall('performance')

        dataList = []
        if type == TYPE_TRAFFIC:
            dataList_rx = []
            dataList_tx = []
            for child in nodes:
                data_rx = self._getXmlData(child, self.xmlTypeDict[TYPE_RX])
                data_tx = self._getXmlData(child, self.xmlTypeDict[TYPE_RX])
                dataList_rx.append(float(data_rx))
                dataList_tx.append(float(data_tx))
            dataList.append(sum(dataList_rx) + sum(dataList_tx))
        else:
            for child in nodes:
                data = self._getXmlData(child, self.xmlTypeDict[type])
                dataList.append(data)
        return dataList

    def _getXmlData(self, node, type):
        data = node.find(type).text
        return data if data else ''


class DataHandler(object):
    def __init__(self):
        self.rsPath = ''
        self.testCase = ''
        self.type = ''
        self.parser = Parser()

    def handle(self, rsPath, testCase, type):
        self.rsPath = rsPath
        self.testCase = testCase
        self.type = type

        return self._getPerfData()

    def _getPerfData(self):
        if self.type == TYPE_TRAFFIC and (self.testCase == CASE_COLD_BOOT or self.testCase == CASE_WARM_BOOT):
            FFanTxtPath = os.path.join(os.path.join(os.path.join(self.rsPath, FFAN), CASE_FOLDER_LIST[self.testCase]),
                                       TRAFFIC_FILE)
            MTUANTxtPath = os.path.join(os.path.join(os.path.join(self.rsPath, MTUAN), CASE_FOLDER_LIST[self.testCase]),
                                        TRAFFIC_FILE)
            if os.path.exists(FFanTxtPath) and os.path.exists(MTUANTxtPath):
                ffanDate = self.parser.txtParser(FFanTxtPath, self.type)
                mtuanDate = self.parser.txtParser(MTUANTxtPath, self.type)
            else:
                raise FileExistsError('Can not find %s test performance results!!!' % self.testCase)
        else:
            if self.type == TYPE_COLD_BOOT or self.type == TYPE_WARM_BOOT:
                FFanTxtPath = os.path.join(os.path.join(os.path.join(self.rsPath, FFAN), CASE_FOLDER_LIST[self.testCase]),
                                           BOOTTIME_FILE)
                MTUANTxtPath = os.path.join(os.path.join(os.path.join(self.rsPath, MTUAN), CASE_FOLDER_LIST[self.testCase]),
                                           BOOTTIME_FILE)
                if os.path.exists(FFanTxtPath) and os.path.exists(MTUANTxtPath):
                    ffanDate = self.parser.txtParser(FFanTxtPath, self.type)
                    mtuanDate = self.parser.txtParser(MTUANTxtPath, self.type)
                else:
                    raise FileExistsError('Can not find %s test performance results!!!' % self.testCase)
            elif self.type == TYPE_FPS:
                FFanTxtPath = os.path.join(os.path.join(os.path.join(self.rsPath, FFAN), CASE_FOLDER_LIST[self.testCase]),
                                           FPS_FILE)
                MTuanTxtPath = os.path.join(os.path.join(os.path.join(self.rsPath, MTUAN), CASE_FOLDER_LIST[self.testCase]),
                                           FPS_FILE)
                if os.path.exists(FFanTxtPath) and os.path.exists(MTuanTxtPath):
                    ffanDate = self.parser.txtParser(FFanTxtPath, self.type)
                    mtuanDate = self.parser.txtParser(MTuanTxtPath, self.type)
                else:
                    raise FileExistsError('Can not find %s test performance results!!!' % self.testCase)
            else:
                FFanXmlPath = os.path.join(os.path.join(os.path.join(self.rsPath, FFAN), CASE_FOLDER_LIST[self.testCase]), PERF_FILE)
                MTuanXmlPath = os.path.join(os.path.join(os.path.join(self.rsPath, MTUAN), CASE_FOLDER_LIST[self.testCase]), PERF_FILE)
                if os.path.exists(FFanXmlPath) and os.path.exists(MTuanXmlPath):
                    ffanDate = self.parser.xmlParser(FFanXmlPath, self.type)
                    mtuanDate = self.parser.xmlParser(MTuanXmlPath, self.type)
                else:
                    raise FileExistsError('Can not find %s test performance results!!!' % self.testCase)

        return ffanDate, mtuanDate


# 性能数据处理装饰器
def dataHandle(type):
    def handler(func):
        def wrapper(cls, testCase):
            print('Process %s performance data!!!' % type)
            dataHandler = DataHandler()
            cls.dataList[FFAN], cls.dataList[MTUAN] = dataHandler.handle(rsPath=cls.rsPath,
                                                                         testCase=testCase,
                                                                         type=type)
            # cls.dataSuite[type] = cls.dataList
            # cls.dataCollection[testCase] = cls.dataSuite
            cls.dataLength = cls._dataLength(cls.dataList[FFAN], cls.dataList[MTUAN])
            func(cls, testCase)
        return wrapper
    return handler


class Handler(object):
    def __init__(self):
        self.rsPath = ''
        self.reportPath = ''
        self.workbook = ''
        self.dataLength = 0

        # 性能测试结果list
        self.dataList = dict()

        self.dataList[FFAN]  = ''
        self.dataList[MTUAN] = ''

    def handle(self, rsPath):
        self.rsPath = rsPath
        self._mkReportDir()
        try:
            for testCase in CASE_LIST:
                if os.path.exists(os.path.join(os.path.join(self.rsPath, FFAN), CASE_FOLDER_LIST[testCase])) and \
                        os.path.exists(os.path.join(os.path.join(self.rsPath, MTUAN), CASE_FOLDER_LIST[testCase])):
                    report = os.path.join(self.reportPath, EXCEL_REPORT_FILE % CASE_FOLDER_LIST[testCase])
                    self.workbook = xlsxwriter.Workbook(report)
                    if testCase == CASE_FPS:
                        self._fpsHandle(testCase)
                    else:
                        self._trafficHandle(testCase)
                        if testCase == CASE_WARM_BOOT:
                            self._warmBootHandle(testCase)
                        elif testCase == CASE_COLD_BOOT:
                            self._coldBootHandle(testCase)
                        else:
                            self._cpuHandle(testCase)
                            self._memoryHandle(testCase)
                            self._rxHandle(testCase)
                            self._txHandle(testCase)
                            self._temperatureHandle(testCase)
                else:
                    print('Missing %s test cases in result path.' % testCase)
        except Exception as e:
            print(e)
        finally:
            self.workbook.close()

    def _mkReportDir(self):
        '''
        创建报告目录, 包含excel报告, 性能测试结果图表图片
        '''
        self.reportPath = os.path.join(self.rsPath, 'report')
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

    @staticmethod
    def _dataLength(x, y):
        return len(x) if len(x) < len(y) else len(y)

    @dataHandle(TYPE_CPU)
    def _cpuHandle(self, testCase):
        # 生成CPU perf sheet
        self._createExcelReport(u'CPU 性能', self.workbook, TYPE_CPU, u'次数', u'cpu使用率(%)')

    @dataHandle(TYPE_MEMORY)
    def _memoryHandle(self, testCase):
        # 生成memory perf sheet
        self._createExcelReport(u'内存性能', self.workbook, TYPE_MEMORY, u'次数', u'内存(Mb)')

    @dataHandle(TYPE_RX)
    def _rxHandle(self, testCase):
        # 生成rx perf sheet
        self._createExcelReport(u'上行速率', self.workbook, TYPE_RX, u'次数', u'上行速率(KBps)')

    @dataHandle(TYPE_TX)
    def _txHandle(self, testCase):
        # 生成rx perf sheet
        self._createExcelReport(u'下行速率', self.workbook, TYPE_TX, u'次数', u'下行速率(KBps)')

    @dataHandle(TYPE_TEMPERATURE)
    def _temperatureHandle(self, testCase):
        # 生成rx perf sheet
        self._createExcelReport(u'电池温度', self.workbook, TYPE_TEMPERATURE, u'次数', u'电池温度(℃)')

    @dataHandle(TYPE_COLD_BOOT)
    def _coldBootHandle(self, testCase):
        # 生成冷启动性能excel
        self._createExcelReport(u'冷启动性能', self.workbook, TYPE_COLD_BOOT, u'次数', u'启动时间(ms)')

    @dataHandle(TYPE_WARM_BOOT)
    def _warmBootHandle(self, testCase):
        # 生成热启动性能excel
        self._createExcelReport(u'热启动性能', self.workbook, TYPE_WARM_BOOT, u'次数', u'启动时间(ms)')

    @dataHandle(TYPE_FPS)
    def _fpsHandle(self, testCase):
        self._createExcelReport(u'OverDraw和FPS 性能', self.workbook, TYPE_FPS, u'帧/秒', 'OverDraw', 'FPS')

    @dataHandle(TYPE_TRAFFIC)
    def _trafficHandle(self, testCase):
        self._createExcelReport(u'流量统计', self.workbook, TYPE_TRAFFIC, u'', u'流量统计(Kb)')

    def _createExcelReport(self, title, workbook, key, *args):
        worksheet = workbook.add_worksheet(title)

        format_title = workbook.add_format()  # 定义format_title格式对象
        format_title.set_border(1)  # 定义format_title对象单元格边框加粗(1像素)的格式
        format_title.set_bg_color('#cccccc')  # 定义format_title对象单元格背景颜色为
        # '#cccccc'的格式
        format_title.set_align('center')  # 定义format_title对象单元格居中对齐的格式
        format_title.set_bold()  # 定义format_title对象单元格内容加粗的格式

        format_ave = workbook.add_format()  # 定义format_ave格式对象
        format_ave.set_border(1)  # 定义format_ave对象单元格边框加粗(1像素)的格式

        if len(args) == 2 and key == TYPE_TRAFFIC:
            worksheet.write(1, 1, args[1], format_title)
            worksheet.write(2, 1, FFAN_APP, format_title)
            worksheet.write(3, 1, MTUAN_APP, format_title)
            worksheet.write(1, 2, '', format_title)
            worksheet.write(2, 2, float(self.dataList[FFAN][0]), format_ave)
            worksheet.write(3, 2, float(self.dataList[MTUAN][0]), format_ave)
            chart = workbook.add_chart({'type': 'column'})
            chart.add_series({'values': [title, 2, 2, 2, 2],
                              'name': [title, 2, 1]})
            chart.add_series({'values': [title, 3, 2, 3, 2],
                              'name': [title, 3, 1]})
            chart.set_title({'name': title})
            chart.set_y_axis({'name': args[1]})
            worksheet.insert_chart('F15', chart, {'x_scale': 2, 'y_scale': 1})
        elif len(args) == 2 and (key == TYPE_COLD_BOOT or key == TYPE_WARM_BOOT):
            worksheet.write(1, 1, args[1], format_title)
            worksheet.write(2, 1, FFAN_APP, format_title)
            worksheet.write(3, 1, MTUAN_APP, format_title)
            for row in range(0, 10):
                worksheet.write(1, row + 2, row+1, format_title)
                worksheet.write(2, row + 2, float(self.dataList[FFAN][row-1]), format_ave)
                worksheet.write(3, row + 2, float(self.dataList[MTUAN][row-1]), format_ave)

            dataFFanList = [float(data) for data in self.dataList[FFAN][:self.dataLength]]
            dataMTuanList = [float(data) for data in self.dataList[MTUAN][:self.dataLength]]

            maxFFanData = max(dataFFanList)
            maxMTuanData = max(dataMTuanList)
            minFFanData = min(dataFFanList)
            minMTuanData = min(dataMTuanList)
            averageFFanData = round(float(sum(dataFFanList) / self.dataLength), 2)
            averageMTuanData = round(float(sum(dataMTuanList) / self.dataLength), 2)
            worksheet.write(14, 1, u'统计', format_title)
            worksheet.write(14, 2, FFAN_APP, format_title)
            worksheet.write(14, 3, MTUAN_APP, format_title)
            worksheet.write(15, 1, u'最大值', format_title)
            worksheet.write(16, 1, u'最小值', format_title)
            worksheet.write(17, 1, u'平均值', format_title)
            worksheet.write(15, 2, maxFFanData, format_ave)
            worksheet.write(16, 2, minFFanData, format_ave)
            worksheet.write(17, 2, averageFFanData, format_ave)
            worksheet.write(15, 3, maxMTuanData, format_ave)
            worksheet.write(16, 3, minMTuanData, format_ave)
            worksheet.write(17, 3, averageMTuanData, format_ave)

            chart = workbook.add_chart({'type': 'column'})
            chart.add_series({'categories': [title, 1, 2, 1, row+2],
                              'values': [title, 2, 2, 2, row+2],
                              'name': [title, 2, 1]})
            chart.add_series({'categories': [title, 1, 2, 1, row+2],
                              'values': [title, 3, 2, 3, row+2],
                              'name': [title, 3, 1]})
            chart.set_title({'name': title})
            chart.set_y_axis({'name': args[1]})
            worksheet.insert_chart('F15', chart, {'x_scale': 2, 'y_scale': 1.5})
        elif len(args) == 2:
            worksheet.write(1, 1, args[1], format_title)
            worksheet.write(2, 1, FFAN_APP, format_title)
            worksheet.write(3, 1, MTUAN_APP, format_title)
            for row in range(1, self.dataLength):
                worksheet.write(1, row + 1, row, format_title)
                worksheet.write(2, row + 1, float(self.dataList[FFAN][row-1]), format_ave)
                worksheet.write(3, row + 1, float(self.dataList[MTUAN][row-1]), format_ave)

            dataFFanList = [float(data) for data in self.dataList[FFAN][:self.dataLength]]
            dataMTuanList = [float(data) for data in self.dataList[MTUAN][:self.dataLength]]

            maxFFanData = max(dataFFanList)
            maxMTuanData = max(dataMTuanList)
            minFFanData = min(dataFFanList)
            minMTuanData = min(dataMTuanList)
            averageFFanData = round(float(sum(dataFFanList) / self.dataLength), 2)
            averageMTuanData = round(float(sum(dataMTuanList) / self.dataLength), 2)
            worksheet.write(14, 1, u'统计', format_title)
            worksheet.write(14, 2, FFAN_APP, format_title)
            worksheet.write(14, 3, MTUAN_APP, format_title)
            worksheet.write(15, 1, u'最大值', format_title)
            worksheet.write(16, 1, u'最小值', format_title)
            worksheet.write(17, 1, u'平均值', format_title)
            worksheet.write(15, 2, maxFFanData, format_ave)
            worksheet.write(16, 2, minFFanData, format_ave)
            worksheet.write(17, 2, averageFFanData, format_ave)
            worksheet.write(15, 3, maxMTuanData, format_ave)
            worksheet.write(16, 3, minMTuanData, format_ave)
            worksheet.write(17, 3, averageMTuanData, format_ave)

            chart = workbook.add_chart({'type': 'line'})
            chart.add_series({'categories': [title, 1, 2, 1, row + 1],
                              'values': [title, 2, 2, 2, row + 1],
                              'name': [title, 2, 1]})
            chart.add_series({'categories': [title, 1, 2, 1, row + 1],
                              'values': [title, 3, 2, 3, row + 1],
                              'name': [title, 3, 1]})
            chart.set_title({'name': title})
            chart.set_x_axis({'name' : args[0]})
            chart.set_y_axis({'name': args[1]})
            worksheet.insert_chart('F15', chart, {'x_scale': 3.5, 'y_scale': 1.5})
        else:
            worksheet.write(1, 1, args[1], format_title)
            worksheet.write(2, 1, FFAN_APP, format_title)
            worksheet.write(3, 1, MTUAN_APP, format_title)
            worksheet.write(1, 7, args[2], format_title)
            worksheet.write(2, 7, FFAN_APP, format_title)
            worksheet.write(3, 7, MTUAN_APP, format_title)
            row = 1
            for data in self.dataList[FFAN]:
                if data[0] == 'Mine':
                    worksheet.write(1, 2, data[0], format_title)
                    worksheet.write(1, 8, data[0], format_title)
                    worksheet.write(2, 2, float(data[1]), format_ave)
                    worksheet.write(2, 8, float(data[2]), format_ave)
                elif data[0] == 'Dashboard':
                    worksheet.write(1, 3, data[0], format_title)
                    worksheet.write(1, 9, data[0], format_title)
                    worksheet.write(2, 3, float(data[1]), format_ave)
                    worksheet.write(2, 9, float(data[2]), format_ave)
                elif data[0] == 'BenefitsLife':
                    worksheet.write(1, 4, data[0], format_title)
                    worksheet.write(1, 10, data[0], format_title)
                    worksheet.write(2, 4, float(data[1]), format_ave)
                    worksheet.write(2, 10, float(data[2]), format_ave)
                else:
                    worksheet.write(1, 5, data[0], format_title)
                    worksheet.write(1, 11, data[0], format_title)
                    worksheet.write(2, 5, float(data[1]), format_ave)
                    worksheet.write(2, 11, float(data[2]), format_ave)
            for data in self.dataList[MTUAN]:
                if data[0] == 'Mine':
                    worksheet.write(3, 2, float(data[1]), format_ave)
                    worksheet.write(3, 8, float(data[2]), format_ave)
                elif data[0] == 'Dashboard':
                    worksheet.write(3, 3, float(data[1]), format_ave)
                    worksheet.write(3, 9, float(data[2]), format_ave)
            worksheet.write(3, 4, 0, format_ave)
            worksheet.write(3, 5, 0, format_ave)
            worksheet.write(3, 10, 0, format_ave)
            worksheet.write(3, 11, 0, format_ave)

            chart = workbook.add_chart({'type': 'column'})
            chart.add_series({'categories': [title, 1, 2, 1, 5],
                              'values': [title, 2, 2, 2, 5],
                              'name': [title, 2, 1]})
            chart.add_series({'categories': [title, 1, 2, 1, 5],
                              'values': [title, 3, 2, 3, 5],
                              'name': [title, 3, 1]})
            chart.set_title({'name': 'OverDraw 性能'})
            chart.set_y_axis({'name': args[0]})
            worksheet.insert_chart('B14', chart, {'x_scale': 1.5, 'y_scale': 1})
            chart = workbook.add_chart({'type': 'column'})
            chart.add_series({'categories': [title, 1, 8, 1, 11],
                              'values': [title, 2, 8, 2, 11],
                              'name': [title, 2, 7]})
            chart.add_series({'categories': [title, 1, 8, 1, 11],
                              'values': [title, 3, 8, 3, 11],
                              'name': [title, 3, 7]})
            chart.set_title({'name': 'FPS 性能'})
            chart.set_y_axis({'name': args[0]})
            worksheet.insert_chart('N14', chart, {'x_scale': 1.5, 'y_scale': 1})


class SendMail(object):
    def __init__(self):
        pass

    def mail(self):
        pass

def parse_command():
    '''
    解析日志路径命令行参数
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--log_path', action='store', default='.',
                        dest='log_path', help='Setup log path, default is current execution directory.')
    args = parser.parse_args()
    rsPath = os.path.abspath(args.log_path)
    return rsPath

if __name__ == "__main__":
    rspath = parse_command()
    handler = Handler()
    handler.handle('/Users/songbo/11')
