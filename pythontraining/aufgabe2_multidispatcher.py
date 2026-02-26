from multipledispatch import dispatch


class SpielAktion:
    """
    Eine Klasse, die Interaktionen in einem Spiel basierend auf den Typen der Beteiligten verwaltet.
    """

    @dispatch(str, str)
    def interagiere(self, a, b):
        """
        Interaktion zwischen zwei benannten Spielern (String, String).
        """
        print("Interaktion zwischen zwei Spielern:", a, "und", b)

    @dispatch(int, int)
    def interagiere(self, a, b):
        """
        Berechnet den Gesamtschaden aus zwei Schadenswerten (Int, Int).
        """
        print("Schaden erlitten in höhe von:", a + b)

    @dispatch(str, int)
    def interagiere(self, a, b):
        """
        Zeigt den Punktestand eines Spielers an (String, Int).
        """
        print("Der Spieler", a, "hat", b, "Punkte erreicht!")

    @dispatch(list, list)
    def interagiere(self, a, b):
        """
        Kombiniert zwei Inventarlisten (List, List).
        """
        print("Inventar aktualisiert. Neue Gegenstände:", a + b)


aktion = SpielAktion()
aktion.interagiere("Alice", "Bob")
aktion.interagiere(20, 30)
aktion.interagiere("Charlie", 150)
aktion.interagiere(["Schwert", "Schild"], ["Heiltrank", "Rüstung"])




# Aufgabe 2: Multidispatch in einem Spielkontext
# Installieren Sie die Bibliothek multipledispatch und implementieren Sie eine Klasse
# SpielAktion.
# Die Klasse soll eine Methode interagiere(a, b) besitzen, die abhängig von den Typen beider
# Parameter unterschiedliche Spielaktionen ausführt.
# Definieren Sie beispielsweise folgende Kombinationen: - str, str: Zwei Spielernamen treten gegeneinander an. Geben Sie eine passende
# Textmeldung zurück. - int, int: Zwei Schadenswerte werden addiert und als Gesamtschaden zurückgegeben. - str, int: Ein Spielername und eine Punktzahl. Geben Sie eine formatierte Ergebnisnachricht
# zurück. - list, list: Zwei Inventarlisten werden zu einer neuen Liste zusammengeführt.

#Der Vorteil von Multidispatch ist, dass du sauberen und erweiterbaren Code schreibst,
# da Python automatisch die passende Logik basierend auf den Datentypen aller übergebenen Argumente auswählt,
# anstatt dass du riesige, unübersichtliche if-isinstance-Ketten bauen musst.