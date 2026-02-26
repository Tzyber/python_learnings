class Mitarbeiter:
    """
    Ein Mitarbeiter mit Attributen unterschiedlicher Sichtbarkeit (public, protected, private).
    """
    def __init__(self,m_name,m_gehalt):
        #public attribut
        self.name = m_name

        #protected attribut
        self._abteilung = "Verkauf"

        #private attribut
        self.__gehalt = m_gehalt

    def zeige_info(self):
        """
        Zeigt alle Informationen des Mitarbeiters an, auch die privaten (da wir innerhalb der Klasse sind).
        """
        print(self.name, self._abteilung, self.__gehalt)


    def __berechne_bonus(self):
        """
        Private Methode zur internen Bonusberechnung.
        Kann nicht direkt von außen aufgerufen werden.
        """
        bonus = self.__gehalt * 0.1
        return bonus


mitarbeiter1 = Mitarbeiter("Max Mustermann", 50000)
mitarbeiter1.zeige_info()