from handle.register_handle import RegisteHandle


class RegisterBusiness(object):
    # 执行操作
    def __init__(self, driver):
        self.register_h = RegisteHandle(driver)

    def user_base(self, email, name, password, code):
        self.register_h.send_user_email(email)
        self.register_h.send_user_name(name)
        self.register_h.send_user_password(password)
        self.register_h.send_user_code(code)
        self.register_h.click_register_button()

    def register_function(self, email, username, password, code, assertCode, assertText):
        self.user_base(email, username, password, code)
        if self.register_h.get_user_text(assertCode, assertText):
            # print("邮箱校验不成功,case运行成功")
            return assertText
        else:
            return None

    def register_success(self, email, name, password, file_name):
        self.user_base(email, name, password, file_name)
        if self.register_h.get_register_text():
            print("登录失败，case运行成功")
            return True
        else:
            False

    # 邮箱错误
    def login_email_error(self, email, name, password, file_name):
        self.user_base(email, name, password, file_name)
        if self.register_h.get_user_text("user_email_error", "请输入有效的电子邮件地址"):
            print("邮箱校验不成功,case运行成功")
            return False
        else:
            return True

    # 用户错误
    def login_username_error(self, email, name, password, file_name):
        self.user_base(email, name, password, file_name)
        if self.register_h.get_user_text("user_name_error", "字符长度必须大于等于4，一个中文字算2个字符"):
            print("校验用户名校验不成功")
            return False
        else:
            return True

    # 密码错误

    def login_password_error(self, email, name, password, file_name):
        self.user_base(email, name, password, file_name)
        if self.register_h.get_user_text("user_password_error", "最少需要输入 5 个字符"):
            print("密码校验不成功")
            return False
        else:
            return True

    # 验证码错误

    def login_code_error(self, email, name, password, file_name):
        self.user_base(email, name, password, file_name)
        if self.register_h.get_user_text("code_text_error", "验证码错误"):
            print("验证码校验不成功")
            return False
        else:
            return True
