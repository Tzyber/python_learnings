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
   - [DIP – Dependency Inversion Principle](#63-dip--dependency-inversion-principle)

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

---

## 3. Getter & Setter mit `@property`

### 🔹 Warum?

Manchmal soll ein Attribut zwar gelesen, aber nicht direkt von außen gesetzt werden – oder es soll beim Setzen eine Validierung stattfinden. Statt klassischer `get_`/`set_`-Methoden empfiehlt Python den `@property`-Dekorator: **saubererer Code, gleiche Sicherheit**.

### 🔹 Wie?

- `@property` macht eine Methode zu einem **Getter** (lesbar wie ein Attribut).
- `@attributname.setter` definiert den **Setter** (mit Validierungslogik).

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

### 6.3 DIP – Dependency Inversion Principle

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

## 🔚 Zusammenfassung

| Konzept | Warum? | Datei(en) |
|---|---|---|
| Klassen & Objekte | Daten und Logik bündeln | `script.py` |
| public / protected / private | Daten kapseln und schützen | `zugriffsmodifikatoren_beispiel.py`, `banktresor_mit_privaten_attributen.py` |
| Getter & Setter (`@property`) | Kontrollierten Zugriff auf private Attribute | `getter_setter.py` |
| `singledispatchmethod` | Methodenüberladung nach Typ (1 Parameter) | `scriptueberladen.py`, `aufgabe1_dispatcher.py` |
| `multipledispatch` | Methodenüberladung nach mehreren Typen | `multipleueberladen.py`, `aufgabe2_multidispatcher.py`, `aufgabe3_multidispatch_in_Klasse.py`, `hausaufgabe1.py`, `hausaufgaben2.py` |
| SRP | Eine Klasse = eine Aufgabe | `srp_aufgabe1.py` |
| OCP | Erweiterbar ohne bestehenden Code zu ändern | `ocp_aufgabe1.py` |
| DIP | Abhängig von Abstraktionen, nicht von konkreten Klassen | `DIP_Aufgabe1.py` |

---

> 💡 **Tipp:** Gute objektorientierte Programme kombinieren alle diese Konzepte. SOLID-Prinzipien, Kapselung (private/protected) und clevere Dispatch-Mechanismen arbeiten zusammen, um Code verständlich, wartbar und sicher zu machen.

