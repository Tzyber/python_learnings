# 📚 Python OOP & Design Patterns – Dokumentation

> **Ziel dieser Dokumentation:** Verstehen *warum* bestimmte Konzepte in Python eingesetzt werden, *was* sie bewirken und *wie* man sie korrekt anwendet – anhand der bereits erstellten Aufgaben und Beispiele.

---

## Inhaltsverzeichnis

1. [Klassen & Objekte – Grundlagen](#1-klassen--objekte--grundlagen)
2. [Zugriffsmodifikatoren – public, protected, private](#2-zugriffsmodifikatoren--public-protected-private)
3. [Getter & Setter mit `@property`](#3-getter--setter-mit-property)
4. [Methodenüberladung – `singledispatch` & `singledispatchmethod`](#4-methodenüberladung--singledispatch--singledispatchmethod)
5. [Multidispatch – mehrere Parameter überladen](#5-multidispatch--mehrere-parameter-überladen)
6. [SOLID-Prinzipien](#6-solid-prinzipien)
   - [SRP – Single Responsibility Principle](#61-srp--single-responsibility-principle)
   - [OCP – Open/Closed Principle](#62-ocp--openclosed-principle)
   - [LSP – Liskov Substitution Principle](#63-lsp--liskov-substitution-principle)
   - [ISP – Interface Segregation Principle](#64-isp--interface-segregation-principle)
   - [Adapter Pattern – Schnittstellen anpassen](#65-adapter-pattern--schnittstellen-anpassen)
   - [DIP – Dependency Inversion Principle](#66-dip--dependency-inversion-principle)
7. [Dependency Injection (DI)](#7-dependency-injection-di)
   - [DI ohne Abstraktion – das Problem](#71-di-ohne-abstraktion--das-problem)
   - [DI mit Konstruktor-Injektion – die Lösung](#72-di-mit-konstruktor-injektion--die-lösung)
   - [DI mit abstrakter Basisklasse](#73-di-mit-abstrakter-basisklasse)
   - [DI im Web-API-Kontext](#74-di-im-web-api-kontext)
   - [DI testen mit Mock-Objekten](#75-di-testen-mit-mock-objekten)
   - [Modulstruktur – main.py & Importe](#76-modulstruktur--mainpy--importe)
8. [Polymorphie](#8-polymorphie)
   - [Polymorphie durch Vererbung](#81-polymorphie-durch-vererbung)
   - [Polymorphie durch Duck Typing](#82-polymorphie-durch-duck-typing)
   - [Polymorphie mit gemeinsamen Schnittstellen](#83-polymorphie-mit-gemeinsamen-schnittstellen)
   - [Polymorphie im spielerischen Kontext](#84-polymorphie-im-spielerischen-kontext)
9. [Observer Pattern](#9-observer-pattern)
10. [Praxisprojekt – Modulares Smart Home](#10-praxisprojekt--modulares-smart-home)

---

## 1. Klassen & Objekte – Grundlagen

### 🔹 Warum?

Klassen helfen dabei, zusammengehörige Daten (Attribute) und Funktionen (Methoden) in einer einzigen Einheit zu bündeln. Ohne Klassen würde man mit vielen unstrukturierten Variablen und Funktionen arbeiten – bei größeren Projekten schnell unübersichtlich.

### 🔹 Wie?

Eine Klasse wird mit `class` definiert. Mit `__init__` werden beim Erstellen eines Objekts automatisch Werte zugewiesen. Mit `self` greift man auf die Attribute und Methoden des Objekts zu.

### 🔹 Beispiel

> Datei: `script.py`

```python
class Fahrzeug:
    def __init__(self, marke, geschwindigkeit):
        self.marke = marke
        self.geschwindigkeit = geschwindigkeit

    def beschleunigen(self, wert):
        self.geschwindigkeit += wert

    def ausgabe(self):
        print("Marke:", self.marke, "Geschwindigkeit:", self.geschwindigkeit, "km/h")

meinAuto = Fahrzeug("VW", 80)
meinAuto.ausgabe()          # → Marke: VW Geschwindigkeit: 80 km/h
meinAuto.beschleunigen(60)
meinAuto.ausgabe()          # → Marke: VW Geschwindigkeit: 140 km/h
```

### 🔹 Erklärung

| Begriff | Bedeutung |
|---|---|
| `class Fahrzeug` | Definiert den „Bauplan" für alle Fahrzeug-Objekte |
| `__init__` | Konstruktor – wird automatisch beim Erstellen aufgerufen |
| `self` | Verweis auf das aktuelle Objekt |
| `meinAuto = Fahrzeug(...)` | Erstellt eine konkrete Instanz (ein echtes Objekt) |
| `meinAuto.beschleunigen(60)` | Ruft eine Methode auf dem Objekt auf |

---

## 2. Zugriffsmodifikatoren – public, protected, private

### 🔹 Warum?

Nicht jede Information soll von überall im Programm verändert werden dürfen. Zugriffsmodifikatoren helfen dabei, Daten zu schützen und unbeabsichtigte Änderungen zu verhindern. Das ist ein Kernprinzip der objektorientierten Programmierung: **Kapselung** (Encapsulation).

### 🔹 Übersicht

| Schreibweise | Typ | Zugriff |
|---|---|---|
| `self.name` | **public** | Von überall erlaubt |
| `self._name` | **protected** | Konvention: nur innerhalb der Klasse & Unterklassen |
| `self.__name` | **private** | Nur innerhalb der eigenen Klasse |

> ⚠️ Python erzwingt diese Regeln nicht wie Java oder C#, aber die Konventionen sollten eingehalten werden!

### 🔹 Beispiel – Alle drei Stufen

> Datei: `privat,public,protected/zugriffsmodifikatoren_beispiel.py`

```python
class Schueler:
    def __init__(self, name, klasse, zeugnis_note):
        self.name = name              # PUBLIC   → jeder darf lesen/schreiben
        self._klasse = klasse         # PROTECTED → nur Klasse & Unterklassen
        self.__zeugnis_note = zeugnis_note  # PRIVATE → nur diese Klasse

    def info_ausgeben(self):
        print(f"Name:   {self.name}")
        print(f"Klasse: {self._klasse}")
        print(f"Note:   {self.__zeugnis_note}")

schueler1 = Schueler("Anna Müller", "10B", 2)

# ✅ PUBLIC – von außen lesen und ändern erlaubt
print(schueler1.name)       # → Anna Müller

# ⚠️ PROTECTED – technisch möglich, aber nicht empfohlen
print(schueler1._klasse)    # → 10B

# ❌ PRIVATE – direkter Zugriff schlägt fehl!
# print(schueler1.__zeugnis_note)  # AttributeError!

# Python verwendet intern "Name Mangling":
print(schueler1._Schueler__zeugnis_note)  # → 2 (so sollte man es NICHT nutzen!)
```

### 🔹 Beispiel – Mitarbeiter mit allen drei Typen

> Datei: `privat,public,protected/private,public,private1.py`

```python
class Mitarbeiter:
    def __init__(self, m_name, m_gehalt):
        self.name = m_name          # public
        self._abteilung = "Verkauf" # protected
        self.__gehalt = m_gehalt    # private

    def zeige_info(self):
        print(self.name, self._abteilung, self.__gehalt)

    def __berechne_bonus(self):     # private Methode
        return self.__gehalt * 0.1
```

### 🔹 Beispiel – Banktresor mit privaten Attributen

> Datei: `privat,public,protected/banktresor_mit_privaten_attributen.py`

```python
class banktresor:
    def __init__(self, pin, fuellstand):
        self.__pin = pin           # privat → PIN darf nie von außen gelesen werden
        self.__fuellstand = fuellstand

    def abheben(self, betrag, pin_eingabe):
        if pin_eingabe != self.__pin:
            print("Fehler: Falsche PIN! Zugriff verweigert.")
        elif betrag > self.__fuellstand:
            print("Fehler: Unzureichender Füllstand!")
        else:
            self.__fuellstand -= betrag
            print("Abhebung erfolgreich! Neuer Füllstand:", self.__fuellstand, "€")
```

**Warum hier `private`?** Die PIN darf niemals von außen gelesen oder geändert werden – das wäre ein Sicherheitsrisiko. Mit `__pin` verhindert Python den direkten Zugriff.

### 🔹 Beispiel – Fahrzeug mit geschütztem Status

> Datei: `privat,public,protected/Fahrzeug_mit_geschuetzten_Status.py`

```python
class Fahrzeug:
    def __init__(self, marke, geschwindigkeit, kilometerstand):
        self._marke = marke                      # PROTECTED → nur Klasse & Unterklassen
        self.__geschwindigkeit = geschwindigkeit  # PRIVATE → nur diese Klasse
        self.__kilometerstand = kilometerstand    # PRIVATE → nur diese Klasse

    def get_geschwindigkeit(self):
        return self.__geschwindigkeit

    def set_geschwindigkeit(self, neue_geschwindigkeit):
        if neue_geschwindigkeit >= 0:
            self.__geschwindigkeit = neue_geschwindigkeit
            print("Geschwindigkeit aktualisiert auf:", neue_geschwindigkeit, "km/h")
        else:
            print("Fehler! Ungültiger Geschwindigkeitseintrag!")

    def get_kilometerstand(self):
        return self.__kilometerstand

    def set_kilometerstand(self, neue_kilometerstand):
        if neue_kilometerstand >= 0 and neue_kilometerstand >= self.__kilometerstand:
            self.__kilometerstand = neue_kilometerstand
            print("Kilometerstand aktualisiert auf:", neue_kilometerstand)
        else:
            print("Fehler! Ungültiger Kilometerstand!")

auto = Fahrzeug("VW", 80, 50000)
auto.set_geschwindigkeit(-5)   # → Fehler
auto.set_geschwindigkeit(140)  # → OK
auto.set_kilometerstand(55000) # → OK
auto.set_kilometerstand(-100)  # → Fehler
```

**Warum hier protected & private kombinieren?** Die Marke (`_marke`) soll von Unterklassen (z. B. `Elektroauto`) lesbar sein, aber Geschwindigkeit und Kilometerstand werden über Getter/Setter mit Validierungslogik geschützt.

---

## 3. Getter & Setter mit `@property`

### 🔹 Warum?

Manchmal soll ein Attribut zwar gelesen, aber nicht direkt von außen gesetzt werden – oder es soll beim Setzen eine Validierung stattfinden. Statt klassischer `get_`/`set_`-Methoden empfiehlt Python den `@property`-Dekorator: **saubererer Code, gleiche Sicherheit**.

### 🔹 Wie?

- `@property` macht eine Methode zu einem **Getter** (lesbar wie ein Attribut).
- `@attributname.setter` definiert den **Setter** (mit Validierungslogik).

> **💡 Pro-Tipp:** In Python fängt man meist mit `public` Attributen an (`self.kontostand`). Wenn man später eine Validierung braucht, baut man **nachträglich** `@property` ein, ohne dass sich für den Rest des Codes etwas ändert (`konto.kontostand` bleibt gleich!). In Java müsste man den Code an allen Stellen umschreiben, wo `konto.kontostand` verwendet wurde, weil man plötzlich `getKontostand()` aufrufen muss.

### 🔹 Beispiel – BankKonto mit @property

> Datei: `getter_setter.py`

```python
class BankKonto:
    def __init__(self, inhaber, kontostand):
        self.__inhaber = inhaber
        self.__kontostand = kontostand

    @property
    def kontostand(self):           # GETTER – lesen erlaubt
        return self.__kontostand

    @kontostand.setter
    def kontostand(self, neuer_betrag):  # SETTER – mit Prüfung
        if neuer_betrag < 0:
            print("Fehler: Kontostand darf nicht negativ sein!")
        else:
            self.__kontostand = neuer_betrag
            print(f"Kontostand wurde auf {self.__kontostand} € gesetzt.")

konto = BankKonto("Max Mustermann", 1000)
print(konto.kontostand)   # → 1000  (wie Attribut-Zugriff, aber GETTER wird aufgerufen)
konto.kontostand = 1500   # → OK    (SETTER mit Prüfung)
konto.kontostand = -200   # → Fehler: Negativ nicht erlaubt
```

### 🔹 Vergleich: Klassischer Getter/Setter vs. @property

> Datei: `privat,public,protected/Benutzerkonto_mit_Zugriffsschutz.py`

```python
# Klassische Variante (ohne @property)
class Benutzerkonto:
    def __init__(self, benutzername, password):
        self.benutzername = benutzername  # public
        self.__password = password         # privat
        self.__kontostand = 2500           # privat

    def get_kontostand(self):              # klassischer Getter
        return self.__kontostand

    def set_kontostand(self, neuer_kontostand):  # klassischer Setter
        if neuer_kontostand >= 0:
            self.__kontostand = neuer_kontostand
        else:
            print("Fehler: Kontostand darf nicht negativ sein!")

konto = Benutzerkonto("Dominik", "krassespassword")
konto.set_kontostand(-250)   # → Fehler
print(konto.get_kontostand()) # → 2500
```

| Variante | Aufruf | Empfehlung |
|---|---|---|
| Klassisch (`get_`/`set_`) | `konto.get_kontostand()` | Veraltete Variante |
| `@property` | `konto.kontostand` | ✅ Pythonischer Stil |

---

## 4. Methodenüberladung – `singledispatch` & `singledispatchmethod`

### 🔹 Warum?

Python unterstützt keine klassische Methodenüberladung wie Java (gleicher Name, verschiedene Parameter). Stattdessen nutzen wir `functools.singledispatch` (für Funktionen) oder `functools.singledispatchmethod` (für Methoden in Klassen), um **basierend auf dem Typ des ersten Arguments** verschiedene Implementierungen zu verwenden.

### 🔹 Wie?

- Man dekoriert die Standardmethode mit `@singledispatchmethod`.
- Für jeden spezifischen Typ registriert man eine Variante mit `@methodenname.register`.

### 🔹 Beispiel – Rechner mit singledispatchmethod

> Datei: `scriptueberladen.py`

```python
from functools import singledispatchmethod

class Rechner:
    @singledispatchmethod
    def add(self, x):
        print("Standardfall:", x)     # wird aufgerufen, wenn kein Typ passt

    @add.register
    def _(self, x: int):
        print("int →", x + 10)        # int: addiert 10

    @add.register
    def _(self, x: str):
        print("str →", x + "!!!")     # str: hängt !!! an

rechner = Rechner()
rechner.add(3.14)   # → Standardfall: 3.14  (float ist nicht registriert)
rechner.add(5)      # → int → 15
rechner.add("Hallo")# → str → Hallo!!!
```

### 🔹 Beispiel – Klassen-Dispatcher (Aufgabe 1)

> Datei: `aufgabe1_dispatcher.py`

```python
from functools import singledispatchmethod

class verarbeiten:
    @singledispatchmethod
    def verarbeiten(self, x):
        print("Standard:", x)

    @verarbeiten.register
    def _(self, x: int):
        print("int → Quadrat:", x ** 2)

    @verarbeiten.register
    def _(self, x: float):
        print("float → Hälfte:", x / 2)

    @verarbeiten.register
    def _(self, x: str):
        print("str → Großbuchstaben:", x.upper())

v = verarbeiten()
v.verarbeiten(4)       # → int → Quadrat: 16
v.verarbeiten(3.14)    # → float → Hälfte: 1.57
v.verarbeiten("hallo") # → str → Großbuchstaben: HALLO
```

### 🔹 Wann `singledispatch` statt `singledispatchmethod`?

| Szenario | Werkzeug |
|---|---|
| Normale Funktion außerhalb einer Klasse | `@singledispatch` (aus `functools`) |
| Methode innerhalb einer Klasse | `@singledispatchmethod` (aus `functools`) |

---

## 5. Multidispatch – mehrere Parameter überladen

### 🔹 Warum?

`singledispatch` kann nur auf den Typ des **ersten** Arguments reagieren. `multipledispatch` ermöglicht es, auf die **Kombination mehrerer Argumenttypen** zu reagieren. Das ersetzt lange `if isinstance(...)`-Ketten und macht den Code übersichtlicher und erweiterbar.

### 🔹 Installation

```bash
pip install multipledispatch
```

### 🔹 Beispiel – Einfacher Rechner

> Datei: `multipleueberladen.py`

```python
from multipledispatch import dispatch

class calculator:
    @dispatch(int, int)
    def add(self, a, b):
        return a + b          # int + int → Addition

    @dispatch(float, float)
    def add(self, a, b):
        return a + b          # float + float → Addition

    @dispatch(str, str)
    def add(self, a, b):
        return a + b          # str + str → Verkettung

calc = calculator()
print(calc.add(3, 5))           # → 8
print(calc.add(3.14, 2.71))    # → 5.85
print(calc.add("Hello, ", "World!"))  # → Hello, World!
```

### 🔹 Beispiel – Spielkontext (Aufgabe 2)

> Datei: `aufgabe2_multidispatcher.py`

```python
from multipledispatch import dispatch

class SpielAktion:
    @dispatch(str, str)
    def interagiere(self, a, b):
        print("Interaktion zwischen:", a, "und", b)

    @dispatch(int, int)
    def interagiere(self, a, b):
        print("Gesamtschaden:", a + b)

    @dispatch(str, int)
    def interagiere(self, a, b):
        print(f"Spieler {a} hat {b} Punkte erreicht!")

    @dispatch(list, list)
    def interagiere(self, a, b):
        print("Inventar aktualisiert:", a + b)

aktion = SpielAktion()
aktion.interagiere("Alice", "Bob")          # → str, str
aktion.interagiere(20, 30)                  # → int, int → 50
aktion.interagiere("Charlie", 150)          # → str, int
aktion.interagiere(["Schwert"], ["Heiltrank"]) # → list, list
```

### 🔹 Beispiel – Lagerverwaltung (Hausaufgabe 1)

> Datei: `hausaufgabe1.py`

```python
from multipledispatch import dispatch

class Lagerverwaltung:
    @dispatch(str, int)
    def verarbeite(self, bestellung, menge):
        print("Bestätigung:", menge, "mal", bestellung, "bestellt")

    @dispatch(list, int)
    def verarbeite(self, bestellung, menge):
        for b in bestellung:
            print("Produkt:", b, "Menge:", menge)

    @dispatch(dict, int)
    def verarbeite(self, produkt, menge):
        for produkt, bestand in produkt.items():
            if bestand < menge:
                print("Warnung: Nur", bestand, "von", produkt, "verfügbar!")

lager = Lagerverwaltung()
lager.verarbeite("Buch", 10)
lager.verarbeite(["Buch", "Stift"], 10)
lager.verarbeite({"Buch": 8, "Stift": 11}, 10)
```

### 🔹 Beispiel – ZahlungsDispatcher (Hausaufgabe 2)

> Datei: `hausaufgaben2.py`

```python
from multipledispatch import dispatch

class ZahlungsDispatcher:
    def __init__(self):
        self.Kontostand = 250.00

    @dispatch()
    def zahlung(self):
        print("Kontostand:", self.Kontostand, "€")

    @dispatch(int)
    def zahlung(self, a, b=None):
        self.Kontostand += a
        print("Gebucht:", a, "€ | Neuer Stand:", self.Kontostand, "€")

    @dispatch(int, str)
    def zahlung(self, a, b=None):
        self.Kontostand -= a
        print("Bezahlt mit", b, ":", a, "€ | Neuer Stand:", self.Kontostand, "€")

zahlung = ZahlungsDispatcher()
zahlung.zahlung()          # → Kontostand anzeigen
zahlung.zahlung(100)       # → +100 €
zahlung.zahlung(110, "Kreditkarte")  # → -110 € mit Kreditkarte
```

### 🔹 Beispiel – Multidispatch vollständig in einer Klasse (Aufgabe 3)

> Datei: `aufgabe3_multidispatch_in_Klasse.py`

```python
from multipledispatch import dispatch

class MuldidispatchKlasse:
    @dispatch(int, int)
    def kombinieren(self, a, b):
        print("Die Summe der Zahlen ist:", a + b)    # int + int → Addition

    @dispatch(str, str)
    def kombinieren(self, a, b):
        print("Kombination lautet:", a, b)            # str + str → Verkettung

    @dispatch(list, list)
    def kombinieren(self, a, b):
        print("Die kombinierte Liste lautet:", a + b) # list + list → Zusammenführen

    @dispatch(int, float)
    def kombinieren(self, a, b):
        print("Ergebnis int × float:", a * b)         # int × float → Produkt

kombination = MuldidispatchKlasse()
kombination.kombinieren(5, 10)              # → 15
kombination.kombinieren("Hallo", "Welt")   # → Hallo Welt
kombination.kombinieren([1, 2], [3, 4])    # → [1, 2, 3, 4]
kombination.kombinieren(3, 2.5)            # → 7.5
```

**Warum eine eigene Klasse?** Das kapselt alle Dispatch-Varianten sauber in einem Objekt. So kann man mehrere Instanzen erstellen und die Logik wiederverwendbar gestalten – ideal für z. B. Berechnungsmodule.

### 🔹 Multidispatch vs. if-isinstance

```python
# ❌ Ohne Multidispatch – unübersichtlich und schwer erweiterbar
def interagiere(a, b):
    if isinstance(a, str) and isinstance(b, str):
        print("Zwei Spieler:", a, b)
    elif isinstance(a, int) and isinstance(b, int):
        print("Schaden:", a + b)
    # ... immer länger ...

# ✅ Mit Multidispatch – klar, lesbar, erweiterbar
@dispatch(str, str)
def interagiere(a, b): print("Zwei Spieler:", a, b)

@dispatch(int, int)
def interagiere(a, b): print("Schaden:", a + b)
```

---

## 6. SOLID-Prinzipien

SOLID ist ein Akronym für fünf Designprinzipien, die helfen, wartbaren, erweiterbaren und testbaren Code zu schreiben.

| Buchstabe | Prinzip | Bedeutung |
|---|---|---|
| **S** | Single Responsibility | Eine Klasse = eine Aufgabe |
| **O** | Open/Closed | Offen für Erweiterung, geschlossen für Änderung |
| **L** | Liskov Substitution | Unterklassen müssen die Elternklasse ersetzen können |
| **I** | Interface Segregation | Keine unnötigen Methoden in Interfaces |
| **D** | Dependency Inversion | Abhängig von Abstraktionen, nicht von konkreten Klassen |

---

### 6.1 SRP – Single Responsibility Principle

#### 🔹 Warum?

Eine Klasse soll **nur eine Aufgabe** haben. Wenn eine Klasse zu viel macht (z.B. speichern, loggen UND E-Mails senden), ist sie schwer zu testen, zu warten und zu ändern.

#### 🔹 Wie?

Man teilt die Verantwortlichkeiten auf mehrere spezialisierte Klassen auf. Ein Koordinator (`UserManager`) ruft diese dann auf.

#### 🔹 Beispiel

> Datei: `SRP_aufgabe/srp_aufgabe1.py`

```python
class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

class Repository:               # ← NUR zuständig für: Speichern
    def save_user(self, user):
        print("Speichere:", user.username)

class Logger:                   # ← NUR zuständig für: Loggen
    def log(self, message):
        print(message)

class EmailService:             # ← NUR zuständig für: E-Mails
    def send_email(self, email, message):
        print("Sende E-Mail an:", email)

class UserManager:              # ← Koordinator: delegiert die Arbeit
    def __init__(self, repository, logger, email_service):
        self.repo = repository
        self.log = logger
        self.email = email_service

    def create_user(self, name, email):
        user = User(name, email)
        self.repo.save_user(user)
        self.log.log(f"User {name} erstellt.")
        self.email.send_email(email, "Willkommen!")

# Verwendung:
manager = UserManager(Repository(), Logger(), EmailService())
manager.create_user("john_doe", "johndoe@gmx.com")
```

**Fazit:** Jede Klasse hat **genau eine Verantwortung**. Muss die Speicher-Logik geändert werden, ändert man nur `Repository` – nichts anderes.

---

### 6.2 OCP – Open/Closed Principle

#### 🔹 Warum?

Software soll **offen für Erweiterungen**, aber **geschlossen für Änderungen** sein. Das bedeutet: Neue Funktionalität wird durch neue Klassen hinzugefügt – bestehender Code bleibt unberührt.

#### 🔹 Wie?

Man definiert eine **abstrakte Basisklasse** (mit `ABC` und `@abstractmethod`). Neue Varianten werden als eigene Klassen implementiert, die die abstrakte Klasse erweitern.

#### 🔹 Beispiel – Rabattsystem

> Datei: `OCP_Aufgaben/ocp_aufgabe1.py`

```python
from abc import ABC, abstractmethod

class DiscountListe(ABC):               # abstrakte Basis-Klasse
    @abstractmethod
    def discount_anwenden(self, price):
        pass

class DiscountCalculator:
    def calculate_discount(self, price, discount: DiscountListe):
        return discount.discount_anwenden(price)

class StandardDiscount(DiscountListe): # 5%
    def discount_anwenden(self, price):
        return price * 0.05

class PremiumDiscount(DiscountListe):  # 10%
    def discount_anwenden(self, price):
        return price * 0.1

class VipDiscount(DiscountListe):      # 15%
    def discount_anwenden(self, price):
        return price * 0.15

class BlackFridayDiscount(DiscountListe): # 50% – NEU hinzugefügt, kein alter Code verändert!
    def discount_anwenden(self, price):
        return price * 0.5

calc = DiscountCalculator()
print(calc.calculate_discount(100, StandardDiscount()))   # → 5.0 €
print(calc.calculate_discount(100, PremiumDiscount()))    # → 10.0 €
print(calc.calculate_discount(100, BlackFridayDiscount())) # → 50.0 €
```

**Fazit:** Ein neuer Rabatttyp (z.B. `BlackFridayDiscount`) wird einfach als neue Klasse hinzugefügt. `DiscountCalculator` muss **nicht** verändert werden.

---

### 6.3 LSP – Liskov Substitution Principle

#### 🔹 Warum?

Wenn eine Klasse von einer anderen erbt, sollte sie sich auch so verhalten, wie man es erwartet. Eine Unterklasse muss **jederzeit** ihre Elternklasse ersetzen können, ohne dass das Programm abstürzt oder falsche Ergebnisse liefert.

#### 🔹 Das Problem (Beispiel)

```python
class Vogel:
    def fliegen(self):
        print("Ich fliege!")

class Pinguin(Vogel):
    def fliegen(self):
        raise Exception("Pinguine können nicht fliegen!")  # ❌ Verletzt LSP!
```

Wenn ich eine Liste von Vögeln durchgehe und `.fliegen()` aufrufe, stürzt das Programm beim Pinguin ab. Der Pinguin verhält sich nicht wie ein "normaler" Vogel.

#### 🔹 Die Lösung

Statt alles in eine `Vogel`-Klasse zu packen, teilt man die Fähigkeiten auf oder nutzt Komposition. Ein Pinguin *ist* ein Vogel, aber er *hat keine* Flugfähigkeit.

---

### 6.4 ISP – Interface Segregation Principle

#### 🔹 Warum?

Kein Client sollte gezwungen sein, Methoden zu implementieren, die er gar nicht braucht. Ein riesiges Interface ("Gott-Interface") ist schlecht, weil Änderungen daran alle Klassen betreffen. Besser sind viele kleine, spezifische Interfaces.

#### 🔹 Beispiel

**Schlecht:**
Ein Interface `MultifunktionsGeraet` mit `drucken()`, `scannen()`, `faxen()`.
Ein einfacher Drucker *muss* dann `scannen()` und `faxen()` implementieren (auch wenn er nur `pass` macht).

**Gut:**
Drei Interfaces: `Drucker`, `Scanner`, `Fax`.
- Das Kombigreät erbt von allen drei.
- Der einfache Drucker erbt nur von `Drucker`.

---

### 6.5 Adapter Pattern – Schnittstellen anpassen

#### 🔹 Warum?

Manchmal möchte man eine bestehende Klasse verwenden, deren Schnittstelle (Methodenname, Parameter) aber **nicht zur erwarteten Schnittstelle passt**. Statt die alte Klasse zu verändern (was gegen das OCP verstößt), erstellt man einen **Adapter** – eine Zwischenschicht, die die Schnittstelle übersetzt. Das Ergebnis: Alte und neue Klassen arbeiten zusammen, ohne dass man vorhandenen Code anfassen muss.

#### 🔹 Wie?

Der Adapter:
1. Nimmt das **inkompatible Objekt** im Konstruktor entgegen.
2. Stellt die **erwartete Schnittstelle** nach außen bereit.
3. Delegiert intern an das inkompatible Objekt – übersetzt also die Methode.

```
Aufrufer → erwartet: methode_X()
Adapter  → hat: methode_X() → ruft intern: methode_Y() auf
Ziel     → hat nur: methode_Y()
```

#### 🔹 Beispiel – Steckdosen-Adapter (Grundprinzip)

> Datei: `OCP_Aufgaben/Adapter Pattern.py`

```python
class EuropeanPlug:
    def round_pin_plug(self):
        return "Using European round pin plug"

class AmericanSocket:
    def flat_pin_socket(self):
        return "Using American flat pin socket"

class AmericanPlug:
    def flat_pin_plug(self):
        return "Using American flat pin plug"

class EuropeanSocket:
    def round_pin_socket(self):
        return "Using European round pin socket"

# Adapter: EUR-Stecker → US-Steckdose
class PlugAdapter_EUR_to_US:
    def __init__(self, use_european_plug, use_american_socket):
        self.european_plug = use_european_plug
        self.american_socket = use_american_socket

    def wired_connector(self):
        return self.european_plug.round_pin_plug() + " and " + self.american_socket.flat_pin_socket()

# Adapter: US-Stecker → EUR-Steckdose
class PlugAdapter_US_to_EUR:
    def __init__(self, use_american_plug, use_european_socket):
        self.american_plug = use_american_plug
        self.european_socket = use_european_socket

    def wired_connector(self):
        return self.american_plug.flat_pin_plug() + " and " + self.european_socket.round_pin_socket()

adapter1 = PlugAdapter_EUR_to_US(EuropeanPlug(), AmericanSocket())
print(adapter1.wired_connector())
# → Using European round pin plug and Using American flat pin socket

adapter2 = PlugAdapter_US_to_EUR(AmericanPlug(), EuropeanSocket())
print(adapter2.wired_connector())
# → Using American flat pin plug and Using European round pin socket
```

**Fazit:** Weder `EuropeanPlug` noch `AmericanSocket` wurden verändert. Der Adapter fungiert als Übersetzer zwischen den beiden inkompatiblen Schnittstellen.

---

#### 🔹 Beispiel – Audio-Adapter (Format-Konvertierung)

> Datei: `OCP_Aufgaben/audio_adapter.py`

```python
class AudioPlayer:
    def Mp3_Player(self, file):
        print(f"Playing MP3 file: {file}")

class WavPlayer:
    def Wav_Player(self, file):
        print(f"Playing WAV file: {file}")

class AudioAdapter:
    def __init__(self, audio_player):
        self.audio_player = audio_player

    def Play_Wav(self, file):
        print(f"--- Adapter-Log: Starte Konvertierung von '{file}' ---")
        print(f"--- Status: Transformiere MP3-Signal zu WAV-Signal... ---")
        mp3_format = file.replace(".wav", ".mp3")
        print(f"--- Adapter-Log: Konvertierung abgeschlossen. ---")
        self.audio_player.Mp3_Player(mp3_format)

adapter = AudioAdapter(AudioPlayer())
adapter.Play_Wav("hochzeit_aufnahme.wav")
# → Starte Konvertierung... → Playing MP3 file: hochzeit_aufnahme.mp3
```

**Szenario:** Ein neues System erwartet `Play_Wav()`, aber der vorhandene Player kennt nur `Mp3_Player()`. Der Adapter übersetzt intern das WAV-Format zu MP3 und delegiert an den bestehenden Player – **kein alter Code verändert**.

---

#### 🔹 Beispiel – Drucker-Adapter (altes API, neues Format)

> Datei: `OCP_Aufgaben/drucker_adapter.py`

```python
class Alter_Drucker:
    def print_text(self, text_string):       # erwartet: einfachen String
        print(f"Drucker druckt: {text_string}")

class PrintAdapter:
    def __init__(self, alter_drucker):
        self.alter_drucker = alter_drucker

    def print_document(self, doc_object):    # erwartet: Dictionary {"title", "content"}
        text = f"{doc_object['title']} - {doc_object['content']}"
        self.alter_drucker.print_text(text)  # wandelt Objekt → String um

adapter = PrintAdapter(Alter_Drucker())
mein_dokument = {"title": "Rechnung", "content": "Bitte zahlen Sie 50 Euro."}
adapter.print_document(mein_dokument)
# → Drucker druckt: Rechnung - Bitte zahlen Sie 50 Euro.
```

**Szenario:** Der alte Drucker kennt nur einfache Strings. Das neue System übergibt strukturierte Objekte (Dictionaries). Der `PrintAdapter` übersetzt das neue Format in das alte.

---

#### 🔹 Beispiel – Zahlungs-Adapter (altes System, neue API)

> Datei: `OCP_Aufgaben/payment.py`

```python
class OldPayment:
    def pay(self, amount):
        print(f"Zahlung von {amount} Euro mit altem System durchgeführt.")

class NewpaymentSystem:
    def make_payment(self, amount, currency):   # neue API: braucht auch Währung!
        print(f"Zahlung von {amount} {currency} mit neuem System durchgeführt.")

class PaymentAdapter:
    def __init__(self, new_payment_system, currency):
        self.new_payment_system = new_payment_system
        self.currency = currency

    def pay(self, amount):                       # alte Schnittstelle bleibt erhalten
        self.new_payment_system.make_payment(amount, self.currency)

adapter = PaymentAdapter(NewpaymentSystem(), "€")
adapter.pay(100)
# → Zahlung von 100 € mit neuem System durchgeführt.
```

**Szenario:** Der Rest des Systems ruft weiterhin `pay(amount)` auf (alte Schnittstelle). Das neue Zahlungssystem braucht aber auch eine Währungsangabe. Der `PaymentAdapter` fügt diese intern hinzu – alle bestehenden Aufrufe bleiben **unverändert**.

---

#### 🔹 Adapter Pattern – Zusammenfassung

| Begriff | Rolle |
|---|---|
| **Ziel (Target)** | Die Schnittstelle, die der Aufrufer erwartet |
| **Adaptee** | Die bestehende, inkompatible Klasse |
| **Adapter** | Übersetzt die Ziel-Schnittstelle zur Adaptee-Schnittstelle |

```
Aufrufer → ruft: pay(amount)
              ↓
        PaymentAdapter.pay(amount)        ← Adapter (übersetzt)
              ↓
        NewpaymentSystem.make_payment(amount, currency)   ← Adaptee
```

> 💡 **Verbindung zu OCP:** Der Adapter erlaubt es, neue oder inkompatible Klassen zu integrieren, **ohne bestehenden Code zu verändern** – das entspricht exakt dem Open/Closed Principle.

---

### 6.6 DIP – Dependency Inversion Principle

#### 🔹 Warum?

Klassen sollen nicht von **konkreten Implementierungen** abhängen, sondern von **Abstraktionen** (Interfaces/abstrakte Klassen). Dadurch ist der Code flexibel – man kann jederzeit eine Implementierung austauschen, ohne den Rest des Codes zu ändern.

#### 🔹 Wie?

Statt `NotificationService(SmsSender())` direkt zu verdrahten, übergibt man eine abstrakte `MessageSender`-Schnittstelle. Der Service weiß nur: *"Es gibt eine send_message-Methode"* – nicht, ob es SMS, E-Mail oder Push ist.

#### 🔹 Beispiel – Benachrichtigungssystem

> Datei: `DIP_Aufgaben/DIP_Aufgabe1.py`

```python
from abc import ABC, abstractmethod

class MessageSender(ABC):          # Abstraktion (das "Interface")
    @abstractmethod
    def send_message(self, message):
        pass

class SmsSender(MessageSender):    # Konkrete Implementierung 1
    def send_message(self, message):
        print("Sende SMS:", message)

class EmailSender(MessageSender):  # Konkrete Implementierung 2
    def send_message(self, message):
        print("Sende E-Mail:", message)

class PushNotificationSender(MessageSender):  # Konkrete Implementierung 3
    def send_message(self, message):
        print("Sende Push:", message)

class NotificationService:         # Hängt nur von der ABSTRAKTION ab!
    def __init__(self, sender: MessageSender):
        self.sender = sender

    def send_notification(self, message):
        self.sender.send_message(message)  # weiß nicht WAS, nur DASS gesendet wird

# Verwendung – einfach austauschen:
NotificationService(SmsSender()).send_notification("SMS kommt!")
NotificationService(EmailSender()).send_notification("Mail kommt!")
NotificationService(PushNotificationSender()).send_notification("Push kommt!")
```

**Fazit:** `NotificationService` muss **nie geändert** werden, egal ob man SMS, E-Mail oder WhatsApp als Sender hinzufügt – solange die neue Klasse `MessageSender` implementiert.

---

## 7. Dependency Injection (DI)

### 🔹 Warum?

**Dependency Injection (DI)** ist ein Entwurfsmuster, bei dem eine Klasse ihre Abhängigkeiten **nicht selbst erstellt**, sondern sie von außen **übergeben bekommt**. Das Ziel ist die **Entkopplung** von Klassen: Die Klasse weiß nur, *was* eine Abhängigkeit tun soll – nicht, *wer* es konkret macht. Das macht den Code **testbarer**, **flexibler** und leichter **wartbar**.

### 🔹 DI vs. kein DI – auf einen Blick

| Ohne DI | Mit DI |
|---|---|
| Klasse erstellt Abhängigkeit selbst (`self.x = KlasseX()`) | Abhängigkeit wird im Konstruktor übergeben |
| Fest an eine Implementierung gebunden | Flexibel austauschbar |
| Schlecht testbar | Leicht durch Mock-Objekte testbar |
| Verstößt gegen DIP | Entspricht dem Dependency Inversion Principle |

---

### 7.1 DI ohne Abstraktion – das Problem

#### 🔹 Beispiel

> Datei: `Dependency_injection/Beispiel DI.py`

```python
class FileWriter:
    def write(self, text):
        print(f"Schreibe in Datei: {text}")

class ReportService:
    def __init__(self):
        self.writer = FileWriter()  # Feste Abhängigkeit – nur FileWriter möglich!

    def create_report(self, content):
        self.writer.write(content)

service = ReportService()
service.create_report("Umsatzbericht 2026")
```

**Problem:** `ReportService` ist fest an `FileWriter` gebunden. Ein Wechsel zu Konsolen- oder Datenbankausgabe erfordert eine Änderung der Klasse selbst.

---

### 7.2 DI mit Konstruktor-Injektion – die Lösung

#### 🔹 Wie?

Die Abhängigkeit wird als Parameter an den Konstruktor übergeben. Die Klasse kennt nur die erwartete **Methode** (`write`), nicht die konkrete Klasse.

#### 🔹 Beispiel

> Datei: `Dependency_injection/Beispiel DI Lösung.py`

```python
class FileWriter:
    def write(self, text):
        print(f"Schreibe in Datei: {text}")

class ConsoleWriter:
    def write(self, text):
        print(f"Konsolenausgabe: {text}")

class ReportService:
    def __init__(self, writer):  # Abhängigkeit wird injiziert
        self.writer = writer

    def create_report(self, content):
        self.writer.write(content)

service1 = ReportService(FileWriter())
service2 = ReportService(ConsoleWriter())

service1.create_report("Umsatzbericht 2026")  # → Schreibe in Datei: ...
service2.create_report("Testbericht")          # → Konsolenausgabe: ...
```

**Vorteil:** `ReportService` muss nie geändert werden, egal welche Ausgabe verwendet wird.

---

### 7.3 DI mit abstrakter Basisklasse

Für noch mehr Sicherheit kombiniert man DI mit einer **abstrakten Basisklasse** (ABC). So wird erzwungen, dass jede injizierte Klasse die erwartete Methode tatsächlich implementiert.

#### 🔹 Beispiel – Benachrichtigungssystem ohne DI

> Datei: `Dependency_injection/Benarichtigungssystem_ohne_DI.py`

```python
class Emailsender:
    def send_email(self, msg):
        print("sending email with:", msg)

class NotificationSender:
    def __init__(self):
        self.email = Emailsender()  # Fest verdrahtet – kein Wechsel möglich!

    def notification(self, msg):
        self.email.send_email(msg)
```

#### 🔹 Beispiel – Benachrichtigungssystem mit DI & ABC

> Datei: `Dependency_injection/Benarichtigungssystem_Mit_DI.py`

```python
from abc import ABC, abstractmethod

class NotificationSender(ABC):
    @abstractmethod
    def send_notification(self, message):
        pass

class EmailSender(NotificationSender):
    def send_notification(self, message):
        print(f"📧 E-Mail: {message}")

class SMSSender(NotificationSender):
    def send_notification(self, message):
        print(f"📱 SMS: {message}")

class FaxSender(NotificationSender):
    def send_notification(self, message):
        print(f"📠 Fax: {message}")

class NotificationService:
    def __init__(self, sender: NotificationSender):
        self.sender = sender

    def send_notification(self, message):
        self.sender.send_notification(message)

NotificationService(SMSSender()).send_notification("hallo")    # → 📱 SMS: hallo
NotificationService(EmailSender()).send_notification("hallo")  # → 📧 E-Mail: hallo
NotificationService(FaxSender()).send_notification("hallo")    # → 📠 Fax: hallo
```

#### 🔹 Beispiel – Kaffeemaschine

> Datei: `Dependency_injection/Kaffeemaschiene.py` & `Kaffeemaschiene_dependencyinjection.py`

```python
# ❌ Ohne DI – fest verdrahtet
class Electricheater:
    def heat(self):
        print("heating water")

class CoffeeMachine:
    def __init__(self, electricity):
        self.electricity = electricity  # Nur Strom möglich!

    def make_coffee(self):
        self.electricity.heat()
        print("Making coffee")

# ✅ Mit DI & ABC – flexibel
from abc import ABC, abstractmethod

class Heater(ABC):
    @abstractmethod
    def heat(self):
        pass

class ElectricHeater(Heater):
    def heat(self):
        print("heating water with electricity")

class GasHeater(Heater):
    def heat(self):
        print("heating water with gas")

class CoffeMachine:
    def __init__(self, heater: Heater):
        self.heater = heater            # Beliebige Heizquelle injizierbar!

    def make_coffee(self):
        self.heater.heat()
        print("making coffee")

CoffeMachine(ElectricHeater()).make_coffee()  # → mit Strom
CoffeMachine(GasHeater()).make_coffee()       # → mit Gas
```

---

### 7.4 DI im Web-API-Kontext

DI ist besonders wertvoll, wenn man zwischen **Produktions-** und **Testdaten** wechseln möchte – z. B. in einer Web-API.

#### 🔹 Beispiel – ohne DI

> Datei: `Dependency_injection/Web_API_ohne_Di.py`

```python
class DatabaseRepository:
    def get_data(self):
        return ["laptop", "smartphone", "tablet"]

class ProductController:
    def __init__(self):
        self.repository = DatabaseRepository()  # Fest verdrahtet!

    def get_products(self):
        products = self.repository.get_data()
        print(f"Produkte: {products}")
```

#### 🔹 Beispiel – mit DI

> Datei: `Dependency_injection/Web_API_DI.py`

```python
from abc import ABC, abstractmethod

class ProductRepository(ABC):
    @abstractmethod
    def get_product(self):
        pass

class DatabaseRepository(ProductRepository):
    def get_product(self):
        return "Laptop (999€)"

class InMemoryRepository(ProductRepository):
    def get_product(self):
        return "Smartphone (499€)"           # Ideal für Tests!

class ProductController:
    def __init__(self, repository: ProductRepository):
        self.repository = repository

    def get_products(self):
        product = self.repository.get_product()
        print(f"Ergebnis der API: {product}")

# Produktion:
ProductController(DatabaseRepository()).get_products()   # → Laptop (999€)
# Test / Entwicklung:
ProductController(InMemoryRepository()).get_products()   # → Smartphone (499€)
```

**Vorteil:** Ohne eine echte Datenbank testen – einfach `InMemoryRepository` injizieren.

---

### 7.5 DI testen mit Mock-Objekten

Durch DI kann man Abhängigkeiten im Test durch **Mock-Objekte** ersetzen. Ein Mock simuliert das Verhalten einer Klasse, ohne echte Logik auszuführen.

#### 🔹 Beispiel – Unittest mit MagicMock

> Datei: `Dependency_injection/testing_notification.py`

```python
import unittest
from unittest.mock import MagicMock
from Benarichtigungssystem_Mit_DI import NotificationService, NotificationSender

class TestNotificationService(unittest.TestCase):
    def test_send_notification(self):
        mock_sender = MagicMock(spec=NotificationSender)   # Simulierter Sender
        service = NotificationService(mock_sender)
        service.send_notification("Testnachricht")
        mock_sender.send_notification.assert_called_once()  # Wurde die Methode aufgerufen?

if __name__ == "__main__":
    unittest.main()
```

**Erklärung:**
- `MagicMock(spec=NotificationSender)` erstellt ein Objekt, das sich wie `NotificationSender` verhält, aber nichts wirklich tut.
- `assert_called_once()` prüft, ob `send_notification` genau einmal aufgerufen wurde.
- **Kein echter E-Mail/SMS-Versand** im Test – schnell, zuverlässig, isoliert.

| Begriff | Bedeutung |
|---|---|
| `MagicMock` | Simuliertes Objekt für Tests |
| `spec=KlassenName` | Mock verhält sich wie diese Klasse |
| `assert_called_once()` | Prüft, ob die Methode exakt einmal aufgerufen wurde |

---

### 7.6 Modulstruktur – main.py & Importe

#### 🔹 Warum?

In größeren Projekten trennt man **Logik** (Funktionen, Klassen) von der **Ablaufsteuerung** (was beim Programmstart passiert). Die `main.py` enthält nur den Einstiegspunkt – sie importiert aus Modulen, schreibt aber keine wiederverwendbare Logik selbst.

#### 🔹 Beispiel

> Datei: `Dependency_injection/main.py` & `Dependency_injection/rechner/rechner.py`

```python
# rechner.py – NUR Logik, keine Ablaufsteuerung
def addieren(a, b):
    return a + b

def subtrahieren(a, b):
    return a - b
```

```python
# main.py – NUR Ablauf, importiert aus Modulen
import rechner.rechner as rechner

if __name__ == "__main__":   # Verhindert, dass der Code beim Import ausgeführt wird
    ergebnis = rechner.addieren(10, 5)
    print(f"Das Ergebnis ist: {ergebnis}")  # → 15
```

#### 🔹 Wichtige Regeln

| Regel | Bedeutung |
|---|---|
| Keine Ablauflogik in Modulen | Module nur für Funktionen/Klassen verwenden |
| `if __name__ == "__main__":` | Schützt Ablaufcode vor ungewollter Ausführung beim Import |
| Nie eine `main.py` importieren | `main.py` ist Einstiegspunkt, kein Modul |
| Importe nur in `main.py` oder Modulen | Nicht kreisförmig importieren |

---

## 8. Polymorphie

### 🔹 Warum?

**Polymorphie** (griech. „Vielgestaltigkeit") bedeutet, dass verschiedene Klassen eine **gleich benannte Methode** besitzen, die sich aber unterschiedlich verhält. So kann man Code schreiben, der mit beliebigen Objekten arbeitet – solange diese die erwartete Methode besitzen. Das Ergebnis: kürzerer, flexibler und leichter erweiterbarer Code.

### 🔹 Übersicht der Arten

| Art | Beschreibung |
|---|---|
| **Durch Vererbung** | Unterklassen überschreiben Methoden einer abstrakten Basisklasse |
| **Duck Typing** | Kein Erben nötig – jedes Objekt mit der richtigen Methode funktioniert |
| **Gemeinsame Schnittstellen** | Abstrakte Klasse gibt Methoden vor, die alle Unterklassen implementieren müssen |

---

### 8.1 Polymorphie durch Vererbung

#### 🔹 Warum?

Wenn mehrere Klassen eine gemeinsame Elternklasse haben, kann man alle Objekte gleich behandeln – obwohl jede Klasse das Verhalten individuell umsetzt. Man muss im Code nicht mehr prüfen, welche Klasse ein Objekt ist.

#### 🔹 Beispiel

> Datei: `polymorphie/polymorphie_durch_vererbung.py`

```python
from abc import ABC, abstractmethod

class Fahrzeug(ABC):
    @abstractmethod
    def bewegen(self):
        pass

class Fahrrad(Fahrzeug):
    def bewegen(self):
        print("Das Fahrrad fährt auf zwei Rädern los")

class Boot(Fahrzeug):
    def bewegen(self):
        print("Das Boot fährt über das Wasser")

def alle_fahrzeuge_bewegen(fahrzeuge):
    for fahrzeug in fahrzeuge:
        fahrzeug.bewegen()   # → jedes Objekt reagiert anders, Aufruf ist identisch

alle_fahrzeuge = [Fahrrad(), Boot()]
alle_fahrzeuge_bewegen(alle_fahrzeuge)
# → Das Fahrrad fährt auf zwei Rädern los
# → Das Boot fährt über das Wasser
```

**Fazit:** Die Funktion `alle_fahrzeuge_bewegen` muss **nicht wissen**, ob es ein Fahrrad oder ein Boot ist – sie ruft einfach `.bewegen()` auf. Das ist Polymorphie durch Vererbung.

---

### 8.2 Polymorphie durch Duck Typing

#### 🔹 Warum?

In Python gilt: **„If it walks like a duck and quacks like a duck, it's a duck."** Das bedeutet: Es ist egal, von welcher Klasse ein Objekt stammt – solange es die erwartete Methode hat, funktioniert es. Keine Vererbung nötig!

#### 🔹 Beispiel

> Datei: `polymorphie/polymorphie_durch_duck_typing.py`

> **💡 Pro-Tipp:** In statischen Sprachen (Java, C++) müssen Objekte oft ein gemeinsames Interface "unterschreiben" (implementieren), um zusammen genutzt zu werden. In Python reicht es, wenn sie *zufällig* die gleiche Methode haben – das nennt man **Duck Typing** ("Wenn es wie eine Ente läuft und quakt, ist es eine Ente"). Das macht den Code extrem flexibel, erfordert aber Sorgfalt (Runtime Error, wenn Methode fehlt!).

```python
class Email:
    def senden(self, nachricht):
        print("Email wird versendet:", nachricht)

class Sms:
    def senden(self, nachricht):
        print("SMS wird versendet:", nachricht)

class PushNotification:
    def senden(self, nachricht):
        print("Push Notification wird versendet:", nachricht)

class Whatsapp:
    def senden(self, nachricht):
        print("Whatsapp Nachricht wird versendet:", nachricht)

def benachrichtigung_versenden(dienst, nachricht):
    dienst.senden(nachricht)  # → funktioniert mit JEDER Klasse, die .senden() hat!

benachrichtigung_versenden(Sms(), "Hallo, das ist eine SMS!")
benachrichtigung_versenden(Email(), "Hallo per E-Mail!")
benachrichtigung_versenden(PushNotification(), "Push!")
```

**Fazit:** `Email`, `Sms`, `Whatsapp` erben von **nichts** – trotzdem funktioniert `benachrichtigung_versenden` mit allen, weil alle eine `.senden()`-Methode haben. Das ist Duck Typing.

| Polymorphie durch Vererbung | Duck Typing |
|---|---|
| Erbt von einer Basisklasse | Kein Erben nötig |
| `isinstance(x, Basisklasse)` wäre `True` | Kein gemeinsamer Typ |
| Klare Struktur, gut bei großen Projekten | Flexibel, pythonisch |

---

### 8.3 Polymorphie mit gemeinsamen Schnittstellen

#### 🔹 Warum?

Eine abstrakte Basisklasse definiert eine **verbindliche Schnittstelle** – jede Unterklasse **muss** alle abstrakten Methoden implementieren. Das garantiert, dass alle Objekte eine bestimmte Funktionalität besitzen, auch wenn sie sich unterschiedlich verhalten.

#### 🔹 Beispiel – Gehaltssystem

> Datei: `polymorphie/polymorhpie_mit_gemiensamen_Schnittstellen.py`

```python
from abc import ABC, abstractmethod

class Mitarbeiter(ABC):
    @abstractmethod
    def berechne_gehalt(self):
        pass

class Festangestellter(Mitarbeiter):
    def berechne_gehalt(self):
        return 3000                        # fixes Monatsgehalt

class Freelancer(Mitarbeiter):
    def __init__(self, stunden, stundenlohn):
        self.stunden = stunden
        self.stundenlohn = stundenlohn

    def berechne_gehalt(self):
        return self.stunden * self.stundenlohn  # variabel je nach Stunden

class Praktikant(Mitarbeiter):
    def berechne_gehalt(self):
        return 450                         # fixer Minijob-Betrag

def gesamt_gehalt(mitarbeiter_liste):
    gesamtsumme = 0
    for mitarbeiter in mitarbeiter_liste:
        gesamtsumme += mitarbeiter.berechne_gehalt()
    return gesamtsumme

mitarbeiter = [Festangestellter(), Freelancer(160, 20), Praktikant()]
print("Gesamtkosten:", gesamt_gehalt(mitarbeiter), "€")  # → 6650 €
```

**Fazit:** Die Funktion `gesamt_gehalt` muss nicht wissen, ob jemand Freelancer oder Festangestellter ist – sie ruft einfach `.berechne_gehalt()` auf. Die abstrakte Klasse **erzwingt**, dass diese Methode existiert.

---

### 8.4 Polymorphie im spielerischen Kontext

#### 🔹 Warum?

Polymorphie macht besonders Spaß bei Spielen: Verschiedene Charaktere oder Tiere reagieren unterschiedlich auf denselben Befehl. Man kann einfach neue Typen hinzufügen, ohne die Steuerlogik anzupassen.

#### 🔹 Beispiel – Zoo-Show

> Datei: `polymorphie/polymorphie_mit_spielerischen_Kontext.py`

```python
from abc import ABC, abstractmethod

class Tier(ABC):
    @abstractmethod
    def mache_laute(self):
        pass

class Hund(Tier):
    def mache_laute(self):
        print("Wuff! Wuff! Wuff!")

class Katze(Tier):
    def mache_laute(self):
        print("Miau! Miau! Miau!")

class Fuchs(Tier):
    def mache_laute(self):
        print("ring ring ring ring ring ring ring ring")

def zoo_show(tiere):
    print("Willkommen zur Zoo-Show!")
    for tier in tiere:
        tier.mache_laute()

show = [Hund(), Katze(), Fuchs()]
zoo_show(show)
# → Wuff! Wuff! Wuff!
# → Miau! Miau! Miau!
# → ring ring ring ...
```

**Fazit:** Um ein neues Tier hinzuzufügen (z. B. `Vogel`), erstellt man einfach eine neue Klasse – `zoo_show` bleibt **unverändert**. Das zeigt, wie Polymorphie und OCP (Open/Closed Principle) Hand in Hand gehen.

---

## 9. Observer Pattern

### 🔹 Warum?
Wenn sich der Zustand eines Objekts ändert (z.B. Wetterdaten, Spielstand), sollen alle davon abhängigen Objekte (Displays, Apps) automatisch benachrichtigt werden. Das Observer Pattern entkoppelt das beobachtbare Objekt (Subject) von den Beobachtern (Observers) – das Subject kennt seine Beobachter nicht persönlich, sondern nur über eine gemeinsame Schnittstelle.

### 🔹 Wie?
- **Subject** (Beobachtbares Objekt): Verwaltet eine Liste von Observern. Bietet Methoden zum An- und Abmelden (`attach`, `detach`) und Benachrichtigen (`notify`).
- **Observer** (Beobachter): Definiert eine Schnittstelle (`update`), die vom Subject aufgerufen wird.
- **ConcreteSubject & ConcreteObserver**: Implementieren die Logik.

```
       Subject                          Observer
    +----------------+             +----------------+
    | - observers [] | <---------> | + update()     |
    | + attach()     |             +----------------+
    | + detach()     |                     ^
    | + notify() ----|-----> ruft auf -----|
    +----------------+
```

### 🔹 Beispiel – Wetterstation
> Datei: `observer_Pattern/Oberserver.py`

```python
from abc import ABC, abstractmethod

# Subject (Wetterstation)
class WeatherStation:
    def __init__(self):
        self._observers = []
        self._temperature = 0

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self):
        for observer in self._observers:
            observer.update(self._temperature)

    def set_temperature(self, temperature):
        print(f"WeatherStation: Temp set to {temperature}")
        self._temperature = temperature
        self.notify_observers()

# Observer Interface
class Observer(ABC):
    @abstractmethod
    def update(self, temperature):
        pass

# Concrete Observer
class PhoneDisplay(Observer):
    def update(self, temperature):
        print(f"PhoneDisplay: Temp is {temperature}°C.")

station = WeatherStation()
phone = PhoneDisplay()
station.add_observer(phone)
station.set_temperature(25)
# → WeatherStation: Temp set to 25
# → PhoneDisplay: Temp is 25°C.
```
**Erläuterung:** Die Wetterstation benachrichtigt alle angemeldeten Beobachter über Temperaturänderungen, ohne zu wissen, wer oder was sie sind.

### 🔹 Beispiel – Fußball-Ticker
> Datei: `observer_Pattern/Fussball_Ticker.py`

```python
class Footballmatch:
    def __init__(self, home, away):
        self.home = home
        self.away = away
        self._observers = []
        self.score_home = 0
        self.score_away = 0

    def add_observer(self, observer):
        self._observers.append(observer)

    def notify_observers(self):
        score = f"{self.home} {self.score_home} - {self.score_away} {self.away}"
        for observer in self._observers:
            observer.update(score)

    def score(self, is_home_goal):
        if is_home_goal: self.score_home += 1
        else: self.score_away += 1
        self.notify_observers()

class MobileApp:
    def update(self, score):
        print(f"[App] Neuer Stand: {score}")

match = Footballmatch("Bayern", "BVB")
match.add_observer(MobileApp())
match.score(True)
# → [App] Neuer Stand: Bayern 1 - 0 BVB
```

**Szenario:** Ein Tor fällt – und sofort erhalten TV, Webportal und Apps die Info. Würde man das ohne Observer Pattern machen, müsste die `Footballmatch`-Klasse alle Apps direkt kennen. Das wäre schwer zu warten und unflexibel.

---

## 10. Praxisprojekt – Modulares Smart Home

### 🔹 Warum?

Das Smart-Home-Projekt kombiniert **alle gelernten Konzepte** in einem realistischen Szenario:
- Abstrakte Basisklasse (`SmartDevice`) → **gemeinsame Schnittstelle**
- `private` und `protected` Attribute → **Kapselung**
- Mehrere konkrete Unterklassen → **Polymorphie durch Vererbung**
- Ein Koordinator-Objekt (`SmartHomeHub`) → **SRP** (eine Klasse, eine Aufgabe)

### 🔹 Architektur

```
SmartDevice (ABC)          ← abstrakte Basisklasse
├── Smartlight             ← steuert Licht
└── SmartThermostat        ← steuert Temperatur

SmartHomeHub               ← verwaltet alle Geräte (Liste, hinzufügen, entfernen)
```

### 🔹 Beispiel

> Datei: `Modulare_smart_home.py`

```python
from abc import ABC, abstractmethod

class SmartDevice(ABC):
    def __init__(self, seriennummer):
        self.__seriennummer = seriennummer   # PRIVATE → von außen nicht änderbar
        self._status = False                 # PROTECTED → Unterklassen dürfen zugreifen

    def get_status(self):
        print("Status von:", self.__seriennummer, ":", self._status)

    def get_seriennummer(self):
        return self.__seriennummer

    @abstractmethod
    def ein_notfall(self):                   # jedes Gerät muss Notfall-Verhalten haben
        pass

    @abstractmethod
    def simulate_activity(self):             # jedes Gerät muss Aktivität simulieren können
        pass


class SmartHomeHub:
    def __init__(self):
        self._devices = []

    def add_device(self, device):
        self._devices.append(device)

    def remove_device(self, device):
        if device in self._devices:
            self._devices.remove(device)
            print("Gerät entfernt:", device.get_seriennummer())

    def activate_all_devices(self):
        for device in self._devices:
            device.simulate_activity()       # → Polymorphie! Jedes Gerät reagiert anders

    def trigger_emergency(self):
        for device in self._devices:
            device.ein_notfall()             # → Polymorphie! Jedes Gerät hat eigenen Notfallplan


class Smartlight(SmartDevice):
    def ein_notfall(self):
        self._status = False
        print("Notfall! Schalte alle Lichter aus. SN:", self.get_seriennummer())

    def simulate_activity(self):
        self._status = True
        print("Schalte Licht ein. SN:", self.get_seriennummer())


class SmartThermostat(SmartDevice):
    def __init__(self, seriennummer, temperatur):
        SmartDevice.__init__(self, seriennummer)
        self.__temperatur = temperatur       # PRIVATE → nur über set_temperatur veränderbar

    def set_temperatur(self, wert):
        self.__temperatur = min(wert, 30)   # max. 30 Grad erlaubt

    def ein_notfall(self):
        self._status = False
        self.set_temperatur(0)
        print("Notfall! Heizung aus. SN:", self.get_seriennummer())

    def simulate_activity(self):
        self._status = True
        self.set_temperatur(18)
        print("Heizung auf 18°C. SN:", self.get_seriennummer())


# Verwendung
smarthome = SmartHomeHub()
licht1 = Smartlight("Licht001")
thermostat1 = SmartThermostat("Thermo001", 22)

smarthome.add_device(licht1)
smarthome.add_device(thermostat1)
smarthome.activate_all_devices()   # → beide Geräte starten
smarthome.trigger_emergency()      # → beide Geräte reagieren auf Notfall
licht1.get_status()                # → False (nach Notfall ausgeschaltet)
smarthome.remove_device(licht1)    # → Licht wird entfernt
```

### 🔹 Konzepte auf einen Blick

| Konzept | Wo im Smart-Home verwendet |
|---|---|
| Abstrakte Klasse (`ABC`) | `SmartDevice` erzwingt `ein_notfall()` & `simulate_activity()` |
| `private` Attribut | `__seriennummer`, `__temperatur` – von außen nicht veränderbar |
| `protected` Attribut | `_status`, `_devices` – für Unterklassen & Hub zugänglich |
| Polymorphie | `activate_all_devices()` ruft auf jedem Gerät `simulate_activity()` auf |
| SRP | Hub verwaltet, Licht schaltet, Thermostat regelt Temperatur |
| Getter-Methode | `get_status()`, `get_seriennummer()` für kontrollierten Zugriff |

---

## 🔚 Zusammenfassung aller Konzepte

| Konzept | Warum? | Datei(en) |
|---|---|---|
| Klassen & Objekte | Daten und Logik bündeln | `script.py` |
| public / protected / private | Daten kapseln und schützen | `zugriffsmodifikatoren_beispiel.py`, `banktresor_mit_privaten_attributen.py`, `Fahrzeug_mit_geschuetzten_Status.py` |
| Getter & Setter (`@property`) | Kontrollierten Zugriff auf private Attribute | `getter_setter.py` |
| `singledispatchmethod` | Methodenüberladung nach Typ (1 Parameter) | `scriptueberladen.py`, `aufgabe1_dispatcher.py` |
| `multipledispatch` | Methodenüberladung nach mehreren Typen | `multipleueberladen.py`, `aufgabe2_multidispatcher.py`, `aufgabe3_multidispatch_in_Klasse.py`, `hausaufgabe1.py`, `hausaufgaben2.py` |
| SRP | Eine Klasse = eine Aufgabe | `srp_aufgabe1.py` |
| OCP | Erweiterbar ohne bestehenden Code zu ändern | `ocp_aufgabe1.py` |
| Adapter Pattern | Inkompatible Schnittstellen übersetzen ohne alten Code zu verändern | `Adapter Pattern.py`, `audio_adapter.py`, `drucker_adapter.py`, `payment.py` |
| DIP | Abhängig von Abstraktionen, nicht von konkreten Klassen | `DIP_Aufgabe1.py` |
| Dependency Injection (Grundprinzip) | Abhängigkeiten von außen übergeben statt selbst erstellen | `Beispiel DI.py`, `Beispiel DI Lösung.py` |
| DI mit ABC | Abstrakte Schnittstelle + Injektion für maximale Flexibilität | `Benarichtigungssystem_Mit_DI.py`, `Kaffeemaschiene_dependencyinjection.py` |
| DI im Web-API-Kontext | Produktions- und Testdaten-Repository austauschbar | `Web_API_DI.py`, `Web_API_ohne_Di.py` |
| DI testen mit Mocks | `unittest.mock.MagicMock` ersetzt echte Abhängigkeiten im Test | `testing_notification.py` |
| Modulstruktur & `main.py` | Logik von Ablauf trennen, `if __name__ == "__main__":` | `main.py`, `rechner/rechner.py` |
| Polymorphie durch Vererbung | Unterklassen überschreiben Basisklassen-Methoden | `polymorphie_durch_vererbung.py` |
| Duck Typing | Kein Erben nötig – gleiche Methode genügt | `polymorphie_durch_duck_typing.py` |
| Polymorphie mit Schnittstellen | Abstrakte Klasse erzwingt gemeinsame Methoden | `polymorhpie_mit_gemiensamen_Schnittstellen.py` |
| Polymorphie im Spielkontext | Erweiterbar ohne Steuerlogik zu ändern | `polymorphie_mit_spielerischen_Kontext.py` |
| Observer Pattern | Automatische Benachrichtigung bei Zustandsänderungen | `Oberserver.py`, `Fussball_Ticker.py` |
| Praxisprojekt Smart Home | Alle Konzepte kombiniert (ABC, Kapselung, Polymorphie, SRP) | `Modulare_smart_home.py` |

---

> 💡 **Tipp:** Gute objektorientierte Programme kombinieren alle diese Konzepte. SOLID-Prinzipien, Kapselung (private/protected), clevere Dispatch-Mechanismen und Polymorphie arbeiten zusammen, um Code verständlich, wartbar und sicher zu machen.

