class CommonUtile:
    # 字符串a是否存在b中
    def is_contain(self, str_one, str_two):
        flge = None
        if str_one in str_two:
            flge = True
        else:
            flge = False
        return flge

    # 判断str_one不包含str_two
    def is_not_contain(self, str_one, str_two):
        flge = None
        if str_one in str_two:
            flge = False
        else:
            flge = True
        return flge

    def contain(self, con, str_one, str_two):
        if con == "contain":
            self.is_contain(str_one, str_two)
        else:
            self.is_not_contain(str_one, str_two)
