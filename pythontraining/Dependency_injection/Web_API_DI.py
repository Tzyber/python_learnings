from abc import ABC, abstractmethod

class ProductRepository(ABC):
    @abstractmethod
    def get_product(self):
        pass

class DatabaseRepository(ProductRepository):
    def get_product(self):
        return "Laptop (999€)"

class InMemoryRepository(ProductRepository):
    def get_product(self):
        return "Smartphone (499€)"

class ProductController:
    def __init__(self, repository: ProductRepository):
        self.repository = repository

    def get_products(self):
        product = self.repository.get_product()
        print("---  Rufe Daten ab ---")
        print(f"Ergebnis der API: {product}")


api_db = ProductController(DatabaseRepository())
api_db.get_products()

print("-" * 30)

# 2. In-Memory-Modus (DI-Vorteil: Gleicher Controller, anderes Repo!)
api_test = ProductController(InMemoryRepository())
api_test.get_products()