from utils.file_utils import fileutils
from utils.excel_utils import ExcelUtils
from path import *


class DataAnalysis:
    def __init__(self):
        self.excel_path = fileutils.local_file(excel_path)
        self.excelutils = ExcelUtils()

    def convert_testcase_data_dict(self):
        '''
        :return:  excel数据按模块区分，并以字典的形式输出
        '''
        self.data = self.excelutils.get_data_list()
        testcase_dict = {}
        for data in self.data:
            if data['用例执行'] == '是':
                testcase_dict.setdefault(data['测试用例编号'],[]).append(data)
        return testcase_dict
    def convert_testcase_data_list(self):
        '''
        把onvert_testcase_data_dict测试用例数据转换成列表，并在每个元素中加key
        :return:[{'case_id':'','case_step':''},{},{}]
        '''
        excel_list = []
        for key,value  in self.convert_testcase_data_dict().items():
            excel_dict={}
            excel_dict['case_id'] = key
            excel_dict['case_step'] = value
            excel_list.append(excel_dict)
        return excel_list

if __name__ == '__main__':
    data = DataAnalysis()
    # for i,j in data.convert_testcase_data_dict().items():
    #     for a in  j:
    #         print(i,a)
    print(data.convert_testcase_data_list())