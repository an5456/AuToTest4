import xlrd
import xlwt
from xlutils.copy import copy


class ExcelUtil:
    def __init__(self, excel_path=None, index=None):
        if excel_path is None:
            self.excel_path = "C:/Users/Administrator/PycharmProjects/moco/case/test_data.xls"
        else:
            self.excel_path = excel_path
        if index is None:
            index = 0
            self.data = xlrd.open_workbook(self.excel_path)
            self.table = self.data.sheets()[index]

    def get_data(self):
        result = []
        row = self.get_lines()
        if row is not None:
            for i in range(self.get_lines()):
                # 获取每一行的每一列
                col = self.table.row_values(i)
                # 将每行的每一列放到result列表里面
                result.append(col)
            return result
        return None

    # 获取所有行数
    def get_lines(self):

        rows = self.table.nrows
        if rows >= 1:
            return rows
        else:
            None

    # 获取单元格的值
    def get_col_value(self, row, col):
        if self.get_lines() > row:
            data = self.table.cell(row, col).value
            return data
        else:
            return None

    # 写入数据
    def write_value(self, row, value):
        read_value = xlrd.open_workbook(self.excel_path)
        write_data = copy(read_value)
        write_data.get_sheet(0).write(row, 9, value)
        write_data.save(self.excel_path)


if __name__ == '__main__':
    exl = ExcelUtil("C:/Users/Administrator/PycharmProjects/moco/case/key_word.xls")
    print(exl.get_lines())
