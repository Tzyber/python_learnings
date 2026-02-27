from abc import ABC, abstractmethod


class Fahrzeug(ABC):
    @abstractmethod
    def bewegen(self):
        print("ich kann mmich anscheinend bewegen")
        pass

class Fahrrad(Fahrzeug):
    def bewegen(self):
        print("das Fahrrad fährt auf zwei rädern los")

class Boot(Fahrzeug):
    def bewegen(self):
        print("Das Boot fährt über das Wasser")

def alle_fahrzeuge_bewegen(fahrzeuge):
    for fahrzeug in fahrzeuge:
        fahrzeug.bewegen()

alle_fahrzeuge = [Fahrrad(), Boot()]
alle_fahrzeuge_bewegen(alle_fahrzeuge)