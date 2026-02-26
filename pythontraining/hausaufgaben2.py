from multipledispatch import dispatch

class ZahlungsDispatcher:
    """
    Verwaltet Zahlungen und Kontostandänderungen mit verschiedenen Eingabeparametern.
    """
    def __init__(self):
        """
        Initialisiert das Konto mit einem Startguthaben von 250.00 €.
        """
        self.Kontostand = 250.00

    @dispatch()
    def zahlung(self):  #kontostand ausgabe
        """
        Zeigt den aktuellen Kontostand an.
        """
        print("Aktueller Kontostand beträgt:", self.Kontostand, "€")

    @dispatch(int)
    def zahlung(self, a,b=None): #Ein einzelner Betrag wird auf das Konto gebucht.
        """
        Bucht einen ganzzahligen Betrag auf das Konto.
        """
        self.Kontostand += a
        print("Buchung von:",a,"€", "wurden auf das Konto gebucht")
        print("Neuer Kontostand beträgt:", self.Kontostand, "€")

    @dispatch(float)
    def zahlung(self, a,b=None): #Ein Betrag in Dezimalform, auf das Konto buchen.
        """
        Bucht einen Dezimalbetrag auf das Konto.
        """
        self.Kontostand += a
        print("Buchung von:",a,"€", "wurden auf das Konto gebucht")
        print("Neuer Kontostand beträgt:", self.Kontostand, "€")

    @dispatch(int,str) # betrag und zahlungsmittel
    def zahlung(self, a,b=None): #Ein Betrag und ein Zahlungsmittel Ausgabe mit bestätigung
        """
        Bucht einen Betrag ab und gibt das verwendete Zahlungsmittel an.
        """
        self.Kontostand -= a
        print("Bestätigung!:","betrag von ",a,"€", "wurde mit", b, "beglichen")
        print("Neuer Kontostand beträgt:", self.Kontostand, "€")

    @dispatch(str, float)  #Ein Kundenname und Betrag, Ausgabe einer Zahlungsquittung
    def zahlung(self, a, b=None):
        """
        Bucht einen Betrag für einen bestimmten Kunden ab.
        """
        self.Kontostand -= b
        print("Bestätigung!:", "Betrag von", b, "€", "wurde von", a, "beglichen.")
        print("Neuer Kontostand beträgt:", self.Kontostand, "€")

zahlung = ZahlungsDispatcher()
print("-" * 30)
zahlung.zahlung()
print("-" * 30)
zahlung.zahlung(100)
print("-" * 30)
zahlung.zahlung(199.99)
print("-" * 30)
zahlung.zahlung(110,"Kreditkarte")
print("-" * 30)
zahlung.zahlung("Max Mustermann", 283.75)
print("-" * 30)
zahlung.zahlung()