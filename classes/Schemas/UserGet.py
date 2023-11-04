from ..Record import Record

class UserGet(Record):
    def byEmail(self, email):
        self.str_model = f"SELECT * FROM users WHERE email = '{email}';"
        return self
    def byPhone(self, phone):
        self.str_model = f"SELECT * FROM users WHERE phone = '{phone}';"
        return self
    def getStrModel(self):
        return self.str_model