from multipledispatch import dispatch


class Lagerverwaltung:
    """
    Verwaltet Bestellungen und Lagerbestände mit überladenen Methoden.
    """

    @dispatch(str,int)
    def verarbeite(self,bestellung,menge):
        """
        Verarbeitet eine einfache Bestellung eines einzelnen Produkts.

        Args:
            bestellung (str): Name des Produkts.
            menge (int): Anzahl der bestellten Einheiten.
        """
        print("Bestätigung", menge,"mal", bestellung, "wurde erfolgreich bestellt")

    @dispatch(list,int)
    def verarbeite(self,bestellung,menge):
        """
        Verarbeitet eine Liste von Produkten, von denen jeweils die gleiche Menge bestellt wird.
        """
        print("Bestellübersicht")
        for b in bestellung:
            print("Produkt:", b, "Menge:", menge)

    @dispatch(dict,int)
    def verarbeite(self,produkt,menge):
        """
        Prüft den Lagerbestand anhand eines Wörterbuchs (Produkt -> Bestand).
        Gibt eine Warnung aus, wenn der Bestand unter der angeforderten Menge liegt.
        """
        print("Prüfung des Lagerbestandes")
        warnung = False
        for produkt,bestand in produkt.items():
            if bestand < menge:
                print("Warnung: Es sind nur", bestand, "Einheiten von", produkt, "im Lager verfügbar.")
                warnung = True
        if not warnung:
            print("Alle Bestände sind noch reichlich gefüllt")

lager = Lagerverwaltung()
lager.verarbeite("Buch",10)
print("-" * 30)
lager.verarbeite(["Buch","Stift"],10)
print("-" * 30)
lager.verarbeite({"Buch":8,"Stift":11},10)