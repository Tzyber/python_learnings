# ============================================================
# Getter und Setter in Python
# ============================================================
# Getter = eine Methode, die einen privaten Wert zurückgibt
# Setter = eine Methode, die einen privaten Wert setzt (mit Prüfung)
# Damit schützt man Daten vor falschen Eingaben von außen.
# ============================================================


class BankKonto:
    """
    Repräsentiert ein Bankkonto mit sicherem Zugriff auf Attribute durch Getter und Setter.
    """

    def __init__(self, inhaber, kontostand):
        """
        Erstellt ein neues Bankkonto.

        Args:
            inhaber (str): Name des Kontoinhabers.
            kontostand (float): Startguthaben.
        """
        self.__inhaber = inhaber        # private → von außen nicht direkt änderbar
        self.__kontostand = kontostand  # private → von außen nicht direkt änderbar

    # --- GETTER ---
    # Gibt den Kontostand zurück (nur lesen, nicht direkt ändern)
    @property
    def kontostand(self):
        """
        Gibt den aktuellen Kontostand zurück.
        """
        return self.__kontostand

    # Gibt den Inhaber zurück
    @property
    def inhaber(self):
        """
        Gibt den Namen des Kontoinhabers zurück.
        """
        return self.__inhaber

    # --- SETTER ---
    # Setzt einen neuen Kontostand, aber NUR wenn der Wert positiv ist
    @kontostand.setter
    def kontostand(self, neuer_betrag):
        """
        Setzt einen neuen Kontostand. Erlaubt keine negativen Werte.
        """
        if neuer_betrag < 0:
            print("Fehler: Kontostand darf nicht negativ sein!")
        else:
            self.__kontostand = neuer_betrag
            print(f"Kontostand wurde auf {self.__kontostand} € gesetzt.")

    # Setzt einen neuen Inhaber, aber NUR wenn der Name nicht leer ist
    @inhaber.setter
    def inhaber(self, neuer_name):
        """
        Ändert den Namen des Inhabers. Leere Namen sind nicht erlaubt.
        """
        if neuer_name == "":
            print("Fehler: Name darf nicht leer sein!")
        else:
            self.__inhaber = neuer_name
            print(f"Inhaber wurde auf '{self.__inhaber}' geändert.")


# ============================================================
# Verwendung:
# ============================================================
konto = BankKonto("Max Mustermann", 1000)

# Getter aufrufen (Werte lesen)
print("Inhaber:", konto.inhaber)       # → Max Mustermann
print("Kontostand:", konto.kontostand) # → 1000

print("-" * 30)

# Setter aufrufen (Werte setzen mit Prüfung)
konto.kontostand = 1500    # → OK
konto.kontostand = -200    # → Fehler! Negativ nicht erlaubt
konto.inhaber = "Erika"    # → OK
konto.inhaber = ""         # → Fehler! Leerer Name nicht erlaubt

print("-" * 30)

# Ergebnis nach den Änderungen:
print("Inhaber:", konto.inhaber)
print("Kontostand:", konto.kontostand)


# ============================================================
# Warum NICHT direkt auf private Attribute zugreifen?
# ============================================================
# konto.__kontostand = -99999  # ← Das würde Python blockieren (Name Mangling)
# Mit Getter/Setter kann man Regeln durchsetzen, bevor ein Wert geändert wird!
# ============================================================

