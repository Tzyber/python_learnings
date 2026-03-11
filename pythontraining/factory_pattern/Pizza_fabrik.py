from abc import ABC, abstractmethod


class Pizza(ABC):
    @abstractmethod
    def zubereiten(self):
        pass

    @abstractmethod
    def backen(self):
        pass


class Margherita(Pizza):
    def zubereiten(self):
        print("Margherita Pizza wird zubereitet: Tomatensauce, Mozzarella, Basilikum")
    def backen(self):
        print("Margherita Pizza wird gebacken: 10 Minuten bei 220 Grad")

class Vegan(Pizza):
    def zubereiten(self):
        print("Vegane Pizza wird zubereitet: Tomatensauce, veganer Käse, Gemüse")

    def backen(self):
        print("Vegane Pizza wird gebacken: 12 Minuten bei 220 Grad")

class Salami(Pizza):
    def zubereiten(self):
        print("Salami Pizza wird zubereitet: Tomatensauce, Mozzarella, Salami")

    def backen(self):
        print("Salami Pizza wird gebacken: 15 Minuten bei 220 Grad")

class Hawaii(Pizza):
    def zubereiten(self):
        print("Hawaii Pizza wird zubereitet: Tomatensauce, Mozzarella, Schinken, Ananas")

    def backen(self):
        print("Hawaii Pizza wird gebacken: 12 Minuten bei 220 Grad")


class PizzaFactory:
    Moegliche_Pizzas = {}
    @classmethod
    def register_pizza(cls, pizza_type, pizza_class):
        cls.Moegliche_Pizzas[pizza_type] = pizza_class
        print("Pizza registriert: ", pizza_type)

    @classmethod
    def create_pizza(cls,pizza_type):
        pizza_class = cls.Moegliche_Pizzas.get(pizza_type)
        if pizza_class is None:
            raise ValueError(f"Pizza-Typ {pizza_type} ist unbekannt")
        return pizza_class()

if __name__ == "__main__":
    PizzaFactory.register_pizza("margherita", Margherita)
    PizzaFactory.register_pizza("salami", Salami)
    PizzaFactory.register_pizza("hawaii", Hawaii)
    PizzaFactory.register_pizza("vegan", Vegan)

    vegane_pizza = PizzaFactory.create_pizza("vegan")
    vegane_pizza.zubereiten()
    vegane_pizza.backen()

    hawaii_pizza = PizzaFactory.create_pizza("hawaii")
    hawaii_pizza.zubereiten()
    hawaii_pizza.backen()
