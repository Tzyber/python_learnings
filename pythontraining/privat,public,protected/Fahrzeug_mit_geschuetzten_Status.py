class Fahrzeug:
    def __init__(self, marke,geschwindigkeit,Kilometerstand):
        self._marke = marke # geschütztes Attribut
        self.__geschwindigkeit = geschwindigkeit  # privates Attribut
        self.__kilometerstand = Kilometerstand # privates Attribut


    def get_geschwindigkeit(self):
        return self.__geschwindigkeit

    def set_geschwindigkeit(self, neue_geschwindigkeit):
        if neue_geschwindigkeit >= 0:
            self.__geschwindigkeit = neue_geschwindigkeit
            print("Geschwindigkeit wurde erfolgreich aktualisiert auf:", neue_geschwindigkeit, "km/h")
        else:
            print("Fehler!", neue_geschwindigkeit, "ist ein ungültiger Geschwindigkeits eintrag!" )


    def get_kilometerstand(self):
        return self.__kilometerstand

    def set_kilometerstand(self, neue_kilometerstand):
        if neue_kilometerstand >= 0 and neue_kilometerstand >= self.__kilometerstand:
            self.__kilometerstand = neue_kilometerstand
            print("Kilometerstand wurde erfolgreich auf:", neue_kilometerstand, "aktualisiert.")
        else:
            print("Fehler!:", neue_kilometerstand, "ist ein ungültiger Kilometer Eintrag!")


auto = Fahrzeug("VW", 80, 50000)
print("Die Marke des Fahrzeugs ist:", auto._marke)
print("Die Geschwindigkeit des Fahrzeugs ist:", auto.get_geschwindigkeit(), "km/h")
print("Der Kilometerstand des Fahrzeugs ist:", auto.get_kilometerstand(), "km")
auto.set_geschwindigkeit(-5)
auto.set_geschwindigkeit(140)
auto.set_kilometerstand(55000)
auto.set_kilometerstand(-55000)