class Fahrzeug:
    """
    Repräsentiert ein allgemeines Fahrzeug mit Marke und Geschwindigkeit.
    """
    # geschwindigkeit = 0 klassen variable

    def __init__(self, marke, geschwindigkeit):
        """
        Initialisiert ein neues Fahrzeug.

        Args:
            marke (str): Die Marke des Fahrzeugs (z.B. VW, BMW).
            geschwindigkeit (int): Die aktuelle Geschwindigkeit in km/h.
        """
        self.marke = marke
        self.geschwindigkeit = geschwindigkeit

    def beschleunigen(self, wert):
        """
        Erhöht die Geschwindigkeit des Fahrzeugs.

        Args:
            wert (int): Der Wert, um den die Geschwindigkeit erhöht wird.
        """
        self.geschwindigkeit += wert #objekt attribut


    def ausgabe(self):
        """
        Gibt die aktuellen Daten des Fahrzeugs auf der Konsole aus.
        """
        print("marke:", self.marke, "fährt", "Geschwindigkeit:", self.geschwindigkeit, "km/h")


meinAuto = Fahrzeug("VW", 80)
meinAuto.ausgabe()
meinAuto.beschleunigen(60)
meinAuto.ausgabe()
