'''
Wir haben eine Wetterstation, die den aktuellen Temperaturwert speichert.
Es gibt mehrere Displays (z.B. Handy, Web, Smartwatch), die diesen Wert anzeigen sollen.
Wenn sich die Temperatur ändert, sollten alle Displays automatisch aktualisiert werden.
'''

from abc import ABC, abstractmethod


# Subject (Wetterstation)
class WeatherStation:
    def __init__(self): # Konstruktor
        self._observers = [] # Registrierliste
        self._temperature = 0
        self.windstaerke = 0

    def add_observer(self, observer): #Anmeldung
        self._observers.append(observer)

    def remove_observer(self, observer): #Abmeldung
        self._observers.remove(observer)

    def notify_observers(self): #alle, die bei der Wettersation registriert sind, werden jetzt benachrichtigt, pushh
        for observer in self._observers:
            observer.update(self._temperature)

    # Wenn sich die Temperatur ändert, werden alle Observer benachrichtigt, quasi Sensorsimulation
    def set_temperature(self, temperature): # simuliert den Sensor
        print(f"WeatherStation: Setting temperature to {temperature}")
        self._temperature = temperature
        self.notify_observers()


# Observer Interface
class Observer(ABC): #Beobachter
    @abstractmethod
    def update(self, temperature):
        pass


# Concrete Observer: Handy Display
class PhoneDisplay(Observer): # Ein konkreter Beobachter
    def update(self, temperature):
        print(f"PhoneDisplay: The current temperature is {temperature}°C.")


# Concrete Observer: Web Display
class WebDisplay(Observer): # das ist ein anderer Beobachter
    def update(self, temperature):
        print(f"WebDisplay: The current temperature is {temperature}°C.")


# Client code
if __name__ == "__main__":
    # Wetterstation (Subject)
    weather_station = WeatherStation()

    # Displays (Observers)
    phone_display = PhoneDisplay()
    web_display = WebDisplay()

    # Beobachter registrieren
    weather_station.add_observer(phone_display)
    weather_station.add_observer(web_display)

    # Temperaturänderung
    weather_station.set_temperature(25)
    weather_station.set_temperature(30)

    # WebDisplay entfernen und Temperatur erneut ändern
    weather_station.remove_observer(web_display)
    weather_station.set_temperature(20)
