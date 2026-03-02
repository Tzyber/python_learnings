from abc import ABC, abstractmethod



class Mitarbeiter(ABC):
    @abstractmethod
    def berechne_gehalt(self):
        pass

class Festangestellter(Mitarbeiter):
    def berechne_gehalt(self):
        return 3000

class Freelancer(Mitarbeiter):
    def __init__(self, stunden, stundenlohn):
        self.stunden = stunden
        self.stundenlohn = stundenlohn

    def berechne_gehalt(self):
        return self.stunden * self.stundenlohn

class Praktikant(Mitarbeiter):
    def berechne_gehalt(self):
        return 450


def gesamt_gehalt(mitarbeiter_liste):
    gesamtsumme = 0
    for mitarbeiter in mitarbeiter_liste:
        gesamtsumme += mitarbeiter.berechne_gehalt()
    return gesamtsumme

mitarbeiter = [
    #Festangestellter(),
    Freelancer(160, 20),
    #Praktikant()
]

print("Die Gesamtkosten belaufen sich auf:", gesamt_gehalt(mitarbeiter), "€")
