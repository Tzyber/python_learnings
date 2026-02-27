from abc import ABC, abstractmethod

class SmartDevice(ABC):
    def __init__(self, seriennummer):
        self.__seriennummer = seriennummer
        self._status = False

    def get_status(self):
        print("Status von :", self.__seriennummer, ":", self._status)
        return self._status


    def get_seriennummer(self):
        return self.__seriennummer

    @abstractmethod
    def ein_notfall(self):
        pass

    @abstractmethod
    def simulate_activity(self):
        pass


class SmartHomeHub:
    def __init__(self):
        self._devices = []

    def add_device(self, device):
        self._devices.append(device)

    def remove_device(self, device):
        if device in self._devices:
            self._devices.remove(device)
            print("Gerät mit Seriennummer", device.get_seriennummer(), "wurde entfernt.")

    def activate_all_devices(self):
        for device in self._devices:
            device.simulate_activity()

    def trigger_emergency(self):
        for device in self._devices:
            device.ein_notfall()

class Smartlight(SmartDevice):
    def ein_notfall(self):
        self._status = False
        print("Notfall! schalte alle Lichter aus. Seriennummer:", self.get_seriennummer())

    def simulate_activity(self):
        self._status = True
        print("Schalte alle Lichter ein mit der Seriennummer:", self.get_seriennummer())

class SmartThermostat(SmartDevice):
    def __init__(self, seriennummer, temperatur):
        SmartDevice.__init__(self,seriennummer)
        self.__temperatur = temperatur

    def get_temperatur(self):
        print("Aktuelle Temperatur:", self.__temperatur, "Grad")

    def set_temperatur(self, temperaturwert):
        if temperaturwert > 30:
            print("Temperatur zu hoch! Bitte wählen Sie einen Wert unter 30 Grad.")
            self.__temperatur = 30
        else:
            self.__temperatur = temperaturwert

    def ein_notfall(self):
        self._status = False
        print("Notfall! schalte die Heizung aus. Seriennummer:", self.get_seriennummer())
        self.set_temperatur(0)

    def simulate_activity(self):
        self._status = True
        print("Schalte die Heizung ein mit der Seriennummer:", self.get_seriennummer())
        self.set_temperatur(18)



# Beispielverwendung
smarthome = SmartHomeHub()
licht1 = Smartlight("Licht001")
thermostat1 = SmartThermostat("Thermo001", 22)
smarthome.add_device(licht1)
smarthome.add_device(thermostat1)
smarthome.activate_all_devices()
smarthome.trigger_emergency()
licht1.get_status()
thermostat1.get_status()
smarthome.remove_device(licht1)
