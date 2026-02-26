class banktresor:
    def __init__(self, pin,fuellstand):
        self.__pin = pin # privates Attribut
        self.__fuellstand = fuellstand # privates Attribut

    def einzahlen(self,betrag):
        if betrag > 0:
            self.__fuellstand += betrag
            print("Einzahlung von:", betrag, "€", "erfolgreich! Neuer Füllstand beträgt:", self.__fuellstand, "€")
        else:
            print("Fehler: Der Einzahlungsbetrag muss positiv sein!")

    def abheben(self,betrag,pin_eingabe):
        if pin_eingabe != self.__pin:
            print("Fehler: Falsche PIN! Zugriff verweigert.")
        elif betrag > self.__fuellstand:
            print("Fehler: Unzureichender Füllstand! Abhebung von", betrag,"€", "nicht möglich. Aktueller Kontostand beträgt:", self.__fuellstand, "€")
        elif betrag <= 0:
            print("Fehler: Der Abhebungsbetrag muss positiv sein!")
        else:
            self.__fuellstand -= betrag
            print("Abhebung von:", betrag, "€", "erfolgreich! Neuer Füllstand beträgt:", self.__fuellstand, "€")



    def get_fuellstand(self):
        return self.__fuellstand

tresor = banktresor("1234", 1000)
tresor.einzahlen(500)
tresor.abheben(200, "1234")
tresor.abheben(200, "1235")