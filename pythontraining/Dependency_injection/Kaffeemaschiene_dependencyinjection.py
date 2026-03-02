from abc import ABC, abstractmethod


class Heater(ABC):
    @abstractmethod
    def heat(self):
        pass

class ElectricHeater(Heater):
    def heat(self):
        print("heating water with electricity")

class GasHeater(Heater):
    def heat(self):
        print("heating water with gas")

class CoffeMachine:
    def __init__(self, heater: Heater):
        self.heater = heater

    def make_coffee(self):
        self.heater.heat()
        print("making coffee")

electric_heater = ElectricHeater()
gas_heater = GasHeater()

coffee_machine = CoffeMachine(electric_heater)
coffee_machine.make_coffee()
coffee_machine = CoffeMachine(gas_heater)
coffee_machine.make_coffee()