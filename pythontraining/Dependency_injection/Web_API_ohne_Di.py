class DatabaseRepository:
    def get_data(self):
        return ["laptop", "smartphone", "tablet"]

class ProductController:
    def __init__(self):
        self.repository = DatabaseRepository()

    def get_products(self):
        products = self.repository.get_data()
        print(f"Produkte: {products}")

# Ohne Dependency Injection: Der Controller ist fest an die Datenquelle gebunden
pr = ProductController()
pr.get_products()