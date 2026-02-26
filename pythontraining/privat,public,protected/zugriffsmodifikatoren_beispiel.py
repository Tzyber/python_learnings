# ============================================================
# Public, Protected und Private – einfaches Beispiel
# ============================================================
# In Python gibt es 3 Stufen, wie "öffentlich" ein Attribut ist:
#
#   self.name → public (kein Unterstrich)
#   self._name → protected (ein Unterstrich)
#   self.__name → private (zwei Unterstriche)
# ============================================================


class Schueler:
    """
    Beispielklasse zur Demonstration von Zugriffsmodifikatoren in Python.
    """

    def __init__(self, name, klasse, zeugnis_note):
        """
        Initialisiert den Schüler.

        Args:
            name (public): Öffentlich zugänglich.
            klasse (protected): Sollte nur intern oder von Unterklassen genutzt werden (`_`).
            zeugnis_note (private): Nur innerhalb dieser Klasse sichtbar (`__`).
        """
        # PUBLIC: jeder darf das lesen und ändern
        self.name = name

        # PROTECTED: nur für diese Klasse und Unterklassen gedacht
        self._klasse = klasse

        # PRIVATE: nur innerhalb dieser Klasse sichtbar
        self.__zeugnis_note = zeugnis_note

    # Eine öffentliche Methode, die alle privaten Infos sicher ausgibt
    def info_ausgeben(self):
        """
        Gibt alle Informationen inkl. der privaten Note aus.
        """
        print(f"Name:   {self.name}")
        print(f"Klasse: {self._klasse}")
        print(f"Note:   {self.__zeugnis_note}")

    # Private Methode – nur intern verwendbar
    def __note_bewerten(self):
        """
        Private Methode zur Bewertung der Note.
        """
        if self.__zeugnis_note > 2:
            return "Sehr gut!"
        elif self.__zeugnis_note <= 2:
            return "Gut!"
        else:
            return "Muss besser werden."

    # Öffentliche Methode, die die private Methode intern nutzt
    def bewertung_ausgeben(self):
        """
        Zeigt die textuelle Bewertung der Note an (nutzt intern die private Methode).
        """
        bewertung = self.__note_bewerten()  # private Methode intern aufrufen ← OK!
        print(f"Bewertung für {self.name}: {bewertung}")


# ============================================================
# Objekt erstellen
# ============================================================
schueler1 = Schueler("Anna Müller", "10B", 2)
schueler1.info_ausgeben()
print("-" * 30)
schueler1.bewertung_ausgeben()

print("-" * 30)

# ✅ PUBLIC → von außen lesen und ändern: ERLAUBT
print("Name (public):", schueler1.name)
schueler1.name = "Anna Schmidt"   # ändern ist erlaubt
print("Name geändert:", schueler1.name)

print("-" * 30)

# ⚠️ PROTECTED → technisch möglich, aber nicht empfohlen!
print("Klasse (protected):", schueler1._klasse)
# Man kann es ändern, sollte es aber NICHT von außen tun.
# Es ist eine Konvention: "Bitte nicht von außen anfassen!"

print("-" * 30)

# ❌ PRIVATE → von außen NICHT direkt zugreifbar
# Das hier würde einen AttributeError auslösen:
# print(schueler1.__zeugnis_note)   # ← FEHLER!

# Python versteckt private Attribute durch "Name Mangling":
# Der echte Name lautet intern: _Schueler__zeugnis_note
# Das zeigt: Python will, dass man es NICHT direkt nutzt.
print("Privates Attribut intern versteckt als: _Schueler__zeugnis_note")
print("Wert (so sollte man es NICHT machen):", schueler1._Schueler__zeugnis_note)

