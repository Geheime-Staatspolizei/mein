from ..Record import Record

class ProductPaginate(Record):
    def paginate(self, limit, offset):
        self.str_model = f" SELECT * FROM products ORDER BY title LIMIT {limit} OFFSET {offset};"
        return self
    def getStrModel(self):
        return self.str_model