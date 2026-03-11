
from abc import ABC, abstractmethod

# Definiere die Produktschnittstelle/abstrakte Klasse
class Fahrzeug(ABC):
    @abstractmethod
    def bremsen(self):
        pass

# Schritt 2: Definiere konkrete Produkte
class Auto(Fahrzeug):
    def __init__(self,f_id):

        if f_id == 1234:
            self.farbe = "rot"
            self.factory_id = f_id
        else:
            raise RuntimeError("Car nur über VehicleFactory mit Lizenzschlüssel - ansonsten Fälschung. Polizei ist benachrichtigt.")

    def bremsen(self):
         print("Vollbremsung")




# Definiere die Factory-Klasse
class FahrzeugFactory:
    @staticmethod
    #@classmethod würde auch gehen, dann müsste man cls in die Methode aufnehmen. aber cls wird nicht benötigt

    def produce_fahrzeug(vehicle_type, factory_id = 1234):
        if vehicle_type == 'car':
            return Auto(factory_id)
        else:
            raise ValueError(f"Fahrzeugtyp {vehicle_type} ist unbekannt")

# Verwende die Factory
if __name__ == "__main__":
    factory = FahrzeugFactory() # Bau der Fabrik

    #car = Auto(1234)

    # Erstelle ein Auto
    car = factory.produce_fahrzeug('car')

    print(car.farbe)
    car.bremsen()

    car1 = Auto() # direkt geht nicht mehr



