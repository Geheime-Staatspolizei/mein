from ..Record import Record

class ProductRecord(Record):
    def setTitle(self, title):
        self.title = title
        return self
    def setPrice(self, price):
        self.price = price
        return self
    def setTimestamp(self, timestamp):
        self.timestamp = timestamp
        return self
    def setDescription(self, description):
        self.description = description
        return self
    def setImageUrl(self, imageUrl):
        self.imageUrl = imageUrl
        return self
    def getStrModel(self):
        return f"INSERT INTO products VALUES ('{self.title}', '{self.description}', '{self.imageUrl}', '{self.price}', '{self.timestamp}');"