from multipledispatch import dispatch


class MuldidispatchKlasse:
    """
    Zeigt verschiedene Kombinationen von Datentypen und deren Verarbeitung mittels `multipledispatch`.
    """

    @dispatch(int, int)
    def kombinieren(self, a, b):
        """
        Rechnet die Summe zweier ganzer Zahlen aus.
        """
        print("Die Summe der Zahlen ist:", a + b)

    @dispatch(str, str)
    def kombinieren(self, a, b):
        """
        Verbindet zwei Textstücke.
        """
        print("Kombination lautet:", a, b)

    @dispatch(list, list)
    def kombinieren(self, a, b):
        """
        Führt zwei Listen zusammen.
        """
        print("Die kombinierte Liste lautet:", a + b)

    @dispatch(int, float)
    def kombinieren(self, a, b):
        """
        Multipliziert eine ganze Zahl mit einer Fließkommazahl.
        """
        print("Die Kombination aus int und float ist:", a * b)


kombination = MuldidispatchKlasse()
kombination.kombinieren(5, 10)
kombination.kombinieren("Hallo", "Welt")
kombination.kombinieren([1, 2], [3, 4])
kombination.kombinieren(3, 2.5)


# Aufgabe 3: Multidispatch in einer Klasse
# Installieren Sie die Bibliothek multipledispatch und implementieren Sie eine Klasse
# Rechner.
# Die Klasse soll eine Methode kombiniere(a, b) besitzen, die abhängig von den Typen beider
# Parameter unterschiedlich arbeitet:
# - int, int: Addieren Sie beide Werte. - str, str: Verbinden Sie beide Strings mit einem Leerzeichen.
# - list, list: Geben Sie eine neue Liste zurück, die beide Listen zusammenführt. - int, float: Geben Sie das Produkt zurück.