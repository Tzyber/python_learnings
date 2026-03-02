class DatabaseRepository:
    def get_data(self):
        return ["laptop", "smartphone", "tablet"]

class ProductController:
    def __init__(self):
        self.repository = DatabaseRepository()

    def get_products(self):
        products = self.repository.get_data()
        print(f"Produkte: {products}")


pr = ProductController()
pr.get_products()