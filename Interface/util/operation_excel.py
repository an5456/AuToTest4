import xlrd
from xlutils.copy import copy

import openpyxl


class OperationExcel:
    def __init__(self, file_name=None, sheet_id=None):
        if file_name:
            self.file_name = file_name
            self.sheet_id = sheet_id
        else:
            self.file_name = '../dataconfig/interface.xlsx'
            self.sheet_id = 'Sheet'

            self.data = self.get_data()

    # 获取execl数据
    def get_data(self):
        # 获取execl
        data = xlrd.open_workbook(self.file_name)
        # 获取sheet
        tables = data.sheet_by_name(self.sheet_id)
        # tables = len(data.sheets())
        # tables1 = data.sheets()
        # for i in range(0, tables):
        #     return tables1[i]
        return tables


    # 获取行数
    def get_lines(self):
        lines = self.data
        return lines.nrows

    # 获取单元格数据
    def get_cell_value(self, row, col):
        return self.data.cell_value(row, col)

    # execl写入数据
    def write_data(self, row, col, value):
        read_data = xlrd.open_workbook(self.file_name)
        write_data = copy(read_data)
        sheet_data = write_data.get_sheet(0)
        sheet_data.write(row, col, value)
        write_data.save(self.file_name)

    # 根据运行的caseID，获取到该行的内容
    def get_rows_data(self, case_id):
        row_num = self.get_rows_num(case_id)  # 获取行号
        rows_data = self.get_rows_value(row_num)  # 获取行的内容
        return rows_data

    # 根据依赖的caseID，找到依赖caseID的行号
    def get_rows_num(self, case_id):
        num = 0
        cols_data = self.get_cols_data()
        for col_data in cols_data:
            if case_id in col_data:
                return num
            num = num + 1

    # 根据依赖caseID的行号，获取到该行的数据
    def get_rows_value(self, row):
        row_data = self.data.row_values(row)
        return row_data

    # 获取某一列的内容
    def get_cols_data(self, case_id=None):
        if case_id is not None:
            cols = self.data.col_values(case_id)
        else:
            cols = self.data.col_values(0)
        return cols


if __name__ == '__main__':
    operation = OperationExcel()
    # operation.get_data()
    #print(operation.get_rows_num("Imooc-11"))
    print(operation.get_rows_value(2))
    #print(operation.get_rows_data("Imooc-11"))
