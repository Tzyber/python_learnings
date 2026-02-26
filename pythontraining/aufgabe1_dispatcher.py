from functools import singledispatchmethod


class verarbeiten:
    """
    Demonstriert die Verarbeitung verschiedener Datentypen mit `singledispatchmethod`.
    """
    @singledispatchmethod
    def verarbeiten(self, x):
        """
        Standard-Methode für unbekannte Datentypen.
        """
        print("standart", x)

    @verarbeiten.register
    def _(self, x: int):
        """
        Berechnet das Quadrat einer ganzen Zahl.
        """
        print("int", x ** 2)

    @verarbeiten.register
    def _(self, x: float):
        """
        Teilt eine Fließkommazahl durch 2.
        """
        print("float", x / 2)

    @verarbeiten.register
    def _(self, x: str):
        """
        Wandelt einen String in Großbuchstaben um.
        """
        print("str", x.upper())


verarbeiter = verarbeiten()
verarbeiter.verarbeiten(4)
verarbeiter.verarbeiten(3.14)
verarbeiter.verarbeiten("hallo")

# Aufgabe 1: Funktions-Dispatcher mit singledispatch
# Implementieren Sie eine Funktion verarbeite(x) unter Verwendung von
# functools.singledispatch.
# Die Funktion soll abhängig vom Typ des übergebenen Arguments unterschiedliche
# Operationen ausführen:
# - Bei int: Geben Sie das Quadrat der Zahl zurück.
# - Bei float: Geben Sie die Hälfte der Zahl zurück.
# - Bei str: Geben Sie den String in Großbuchstaben zurück.
# - Für alle anderen Typen soll eine Standardmeldung zurückgegeben werden.
# Testen Sie Ihre Implementierung mit mindestens vier unterschiedlichen Datentypen.
