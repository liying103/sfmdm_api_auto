import xlrd3
from path import *
from utils.file_utils import fileutils


path = fileutils.local_file(excel_path)
excel = xlrd3.open_workbook(path)
sheet = excel.sheet_by_name('Sheet1')
# sheet.merged_cells 获取合并单元格的坐标
print(sheet.merged_cells)
# row_index:行；col_index：列
def get_merged_cell_value(row_index,col_index):
    cell_value = None
    for min_x,max_x,min_y,max_y in sheet.merged_cells:
        if min_x <= row_index and max_x >row_index:
            if min_y <= col_index and max_y>col_index:
               cell_value = sheet.cell_value(min_x,min_y)
               return cell_value
            else:
                cell_value = sheet.cell_value(row_index,col_index)
                return cell_value
        else:
            cell_value = sheet.cell_value(row_index, col_index)
            return cell_value
'''
for i in range(0,sheet.nrows):
    for j in  range(0,sheet.ncols):
        value = get_merged_cell_value(i,j)
        print(value,end=',')
    print('\n')'''
excel_list_date = []
row_head = sheet.row_values(0)  # 字典的key

# row_dict[row_head[0]]= sheet.cell_value(1,0)
# row_dict[row_head[1]]= sheet.cell_value(1,1)
# row_dict[row_head[2]]= sheet.cell_value(1,2)
# row_dict[row_head[3]]= sheet.cell_value(1,3)
# # print(row_dict)


for i in range(1,sheet.nrows):
    row_dict = {}
    for j in  range(0,sheet.ncols):
        row_dict[row_head[j]]= get_merged_cell_value(i,j)
    excel_list_date.append(row_dict)
print(excel_list_date)
    # excel_list_date.append(row_dict)


'''def get_excel_data_dict():
    row_head = sheet.row_values(0)
    excel_list_data =[]
    for row in range(1,sheet.nrows):
        row_dict = {}
        for item in range(sheet.ncols):
            row_dict[row_head[item]] = get_merged_cell_value(row, item)
        excel_list_data.append(row_dict)
    return excel_list_data
print(get_excel_data_dict())'''





