import jwt

class Token:
    def __init__(self):
        self.SECRET = "zvezd04ka"
    def produce(self, payload):
        token = jwt.encode(payload, self.SECRET, algorithm="HS256")
        return token
    def verify(self, token):
        payload = jwt.decode(token, self.SECRET, algorithms=["HS256"])
        return payload
        