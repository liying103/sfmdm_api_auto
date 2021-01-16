import xlrd3
from path import *
from utils.file_utils import fileutils

class ExcelUtils:
    def __init__(self,sheet_name="Sheet1"):
        self.path = fileutils.local_file(excel_path)
        self.xlrd = xlrd3.open_workbook(self.path)
        self.sheet = self.xlrd.sheet_by_name(sheet_name)

    def get_merged_cell_value(self,row_index,col_index):
        '''
        处理合并单元格
        :param row_index: 行数
        :param col_index: 列数
        :return: 对应单元格的值
        '''
        cell_value = None
        if self.sheet.merged_cells:
            for min_x,max_x,min_y,max_y in self.sheet.merged_cells:
                if min_x<= row_index and max_x>row_index:
                    if min_y <= col_index and max_y>col_index:
                        cell_value=self.sheet.cell_value(min_x,min_y)
                        return cell_value
                    else:
                        cell_value=self.sheet.cell_value(row_index,col_index)
                        return cell_value
                else:
                    cell_value=self.sheet.cell_value(row_index,col_index)
                    return cell_value
        else:
            cell_value = self.sheet.cell_value(row_index,col_index)
            return cell_value







    def get_rows(self):
        '''
        :return: excel行数
        '''
        return self.sheet.nrows

    def get_cols(self):
        '''
        :return: excel列数
        '''
        return self.sheet.ncols

    def get_data_list(self):
        '''
        获取excel中数据
        :return: [{excel中第0行的标题：每个标题对应的value},.....{excel中第0行的标题：每个标题对应的value}]
        '''
        excel_list_date = []
        row_head = self.sheet.row_values(0)  # 字典的key
        for rows in  range(1,self.sheet.nrows):
            dict_data = {}
            for cols in range(0,self.sheet.ncols):
                dict_data[row_head[cols]] = self.get_merged_cell_value(rows,cols)
            excel_list_date.append(dict_data)
        return excel_list_date

if __name__ == '__main__':
    value = ExcelUtils()
    # print(value.get_data_list())
    print(value.get_merged_cell_value(1,1))