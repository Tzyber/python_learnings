class Benutzerkonto:
    def __init__(self, benutzername, password):
        self.benutzername = benutzername # öffentliches Attribut
        self.__password = password # privates Attribut
        self.__kontostand = 2500 # privates Attribut


    def get_password(self):
        return self.__password

    def set_password(self, neues_passwort):
        if len(neues_passwort) >= 8:
            self.__password = neues_passwort
            print("Passwort wurde erfolgreich geändert.")
        else:
            print("Fehler: Das password steht nicht den Anforderungen (mindestens 8 Zeichen).")

    def get_kontostand(self):
        return self.__kontostand

    def set_kontostand(self, neuer_kontostand):
        if neuer_kontostand >= 0:
            self.__kontostand = neuer_kontostand
            print("Kontostand wurde erfolgreich aktualisiert.")
        else:
            print("fehler: Der Kontostand darf cniht getativ sein!")


konto = Benutzerkonto("Dominik", "krassespassword")
konto.set_kontostand(-250)

print("Das Konto von:", konto.benutzername,"Mit dem password:", konto.get_password(),"besitzt:", konto.get_kontostand(), "€")