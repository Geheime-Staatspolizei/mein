from ..Record import Record
from ..Token import Token

class UserRecord(Record):
    def setPassword(self, password):
        self.password = password
        return self
    def setName(self, name):
        self.name = name
        return self
    def setTelephoneNumber(self, telephoneNumber):
        self.telephoneNumber = telephoneNumber
        return self
    def setEmail(self, email):
        self.email = email
        return self
    def setRole(self, role):
        self.role = role
        return self
    def getToken(self):
        token = Token().produce({
            "email": self.email,
            "password": self.password,
            "role": self.role,
        })
        return token
    def getStrModel(self):
        return f"INSERT INTO users VALUES ('{self.password}', '{self.name}', '{self.telephoneNumber}', '{self.email}', '{self.role}');"