from abc import ABC, abstractmethod


class DiscountListe(ABC):
    """
    Abstrakte Basisklasse für Rabatt-Strategien (Open-Closed Principle).
    """
    @abstractmethod
    def discount_anwenden(self, price):
        """
        Wendet den Rabatt auf den Preis an.
        """
        pass

class DiscountCalculator:
    """
    Berechnet Rabatte unter Verwendung einer übergebenen Discount-Strategie.
    """
    def calculate_discount(self, price, discount: DiscountListe):
        """
        Berechnet den Rabattbetrag basierend auf dem Preis und der Strategie.
        """
        return discount.discount_anwenden(price)

class StandardDiscount(DiscountListe):
    """
    Standard-Rabatt: 5%.
    """
    def discount_anwenden(self, price):
        return price * 0.05

class PremiumDiscount(DiscountListe):
    """
    Premium-Rabatt: 10%.
    """
    def discount_anwenden(self, price):
        return price * 0.1

class VipDiscount(DiscountListe):
    """
    VIP-Rabatt: 15%.
    """
    def discount_anwenden(self, price):
        return price * 0.15

class BlackFridayDiscount(DiscountListe):
    """
    Black Friday Rabatt: 50%.
    """
    def discount_anwenden(self, price):
        return price * 0.5

discount_calculator = DiscountCalculator()
standard_discount = StandardDiscount()
premium_discount = PremiumDiscount()
vip_discount = VipDiscount()
black_friday = BlackFridayDiscount()

ergebnis = discount_calculator.calculate_discount(100, standard_discount)
print("Standard Discount:", ergebnis,"€ sparen!")
ergebnis = discount_calculator.calculate_discount(100, premium_discount)
print("Premium Discount:", ergebnis,"€ sparen!")
ergebnis = discount_calculator.calculate_discount(100, vip_discount)
print("VIP Discount:", ergebnis,"€ sparen!!")
ergebnis = discount_calculator.calculate_discount(100, black_friday)
print("Black Friday Discount:", ergebnis,"€ sparen!!!")
