class Electricheater:
    def heat(self):
        print("heating water")

class CoffeeMachine:
    def __init__(self, electricity):
        self.electricity = electricity

    def make_coffee(self):
        self.electricity.heat()
        print("Making coffee")


electricity = Electricheater()
coffee_machine = CoffeeMachine(electricity)
coffee_machine.make_coffee()
