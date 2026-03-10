class OldPayment:
    def pay(self, amount):
        print(f"Zahlung von {amount} Euro mit altem System durchgeführt.")


class NewpaymentSystem:
    def make_payment(self, amount, currency):
        print(f"Zahlung von {amount} {currency} mit neuem System durchgeführt.")

class PaymentAdapter:
    def __init__(self, new_payment_system, currency):
        self.new_payment_system = new_payment_system
        self.currency = currency

    def pay(self, amount):
        self.new_payment_system.make_payment(amount, self.currency)
        print(f"Zahlung von {amount}, {self.currency} mit Adapter durchgeführt.")


def main():
    # Beispielverwendung
    neues_system = NewpaymentSystem()
    adapter = PaymentAdapter(neues_system, "€")
    adapter.pay(100)

if __name__ == "__main__":
    main()