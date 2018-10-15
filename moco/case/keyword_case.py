import sys

sys.path.append('C:\\Users\\Administrator\\PycharmProjects\\moco')
from keywordselenium.actionMethod import ActionMethod
from util.excel_util import ExcelUtil


class KeywordCase(object):

    def run_main(self):
        self.action_metnod = ActionMethod()
        handle_excel = ExcelUtil(r"C:\Users\Administrator\PycharmProjects\moco\case\key_word.xls")
        # 拿到行数
        case_lines = handle_excel.get_lines()
        # 循环行数，执行每一行case
        if case_lines:
            for i in range(1, case_lines):
                is_run = handle_excel.get_col_value(i, 3)
                # print(is_run)
                # 是否执行
                if is_run == 'yes':
                    # 拿到执行方法
                    method = handle_excel.get_col_value(i, 4)
                    # 拿到输入数据
                    send_value = handle_excel.get_col_value(i, 5)
                    # 拿到操作元素
                    handle_value = handle_excel.get_col_value(i, 6)
                    # 获取预期结果的方法
                    except_result_method = handle_excel.get_col_value(i, 7)
                    # 获取预期结果的值
                    except_result = handle_excel.get_col_value(i, 8)
                    self.run_method(method, send_value, handle_value)
                    # 判断预期结果是否为空
                    if except_result != '':
                        except_value = self.get_except_result_value(except_result)
                        if except_value[0] == 'text':

                            result = self.run_method(except_result_method)
                            if except_value[1] in result:
                                handle_excel.write_value(i, 'pass')
                            else:
                                handle_excel.write_value(i, 'fail')
                        elif except_value[0] == 'element':
                            result = self.run_method(except_result_method, except_value[1])
                            if result:
                                handle_excel.write_value(i, 'pass')
                            else:
                                handle_excel.write_value(i, 'fail')
                        else:
                            return None
                    else:
                        print("预期结果为空")

    # 获取预期结果
    def get_except_result_value(self, data):
        return data.split("=")

    # 运行的方法、输入数据和操作元素连在一起
    def run_method(self, method, send_value='', handle_value=''):
        method_value = getattr(self.action_metnod, method)
        # 是否有输入数据
        if send_value == '' and handle_value != '':
            # 执行方法（输入数据，操作元素）
            result = method_value(handle_value)
        # 如果没有输入数据
        elif send_value != '' and handle_value == '':
            # 执行方法（操作元素）
            result = method_value(send_value)
        elif send_value != '' and handle_value != '':
            result = method_value(send_value, handle_value)
        else:
            result = method_value()
        return result


if __name__ == '__main__':
    key = KeywordCase()
    key.run_main()
