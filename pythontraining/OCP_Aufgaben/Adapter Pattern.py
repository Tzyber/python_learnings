# Die bestehende Klasse, die die europäische Steckdose repräsentiert.
class EuropeanPlug:
    def round_pin_plug(self):
        return "Using European round pin plug"

# Die bestehende Klasse, die die amerikanische Steckdose repräsentiert.
class AmericanSocket:
    def flat_pin_socket(self):
        return "Using American flat pin socket"

class AmericanPlug:
    def flat_pin_plug(self):
        return "Using American flat pin plug"

# Die bestehende Klasse, die die amerikanische Steckdose repräsentiert.
class EuropeanSocket:
    def round_pin_socket(self):
        return "Using European round pin socket"



# Der Adapter, der die Schnittstelle von EuropeanPlug an die von AmericanSocket anpasst.
class PlugAdapter_EUR_to_US:
    def __init__(self, use_european_plug,use_american_socket):
        self.european_plug = use_european_plug
        self.american_socket = use_american_socket

    # Der Adapter bietet eine Methode, die zur amerikanischen Steckdose passt,
    # aber intern die Methode der europäischen Steckdose aufruft.
    def wired_connector(self):
        return self.european_plug.round_pin_plug() + " and " + self.american_socket.flat_pin_socket()


class PlugAdapter_US_to_EUR:
    def __init__(self, use_american_plug,use_european_socket):
        self.american_plug = use_american_plug
        self.european_socket = use_european_socket

    # Der Adapter bietet eine Methode, die zur amerikanischen Steckdose passt,
    # aber intern die Methode der europäischen Steckdose aufruft.
    def wired_connector(self):
        return self.american_plug.flat_pin_plug() + " and " + self.european_socket.round_pin_socket()



#1. Adapter
american_socket = AmericanSocket()
european_plug = EuropeanPlug()
adapter1 = PlugAdapter_EUR_to_US(european_plug, american_socket)
print(adapter1.wired_connector())


#2. Adapter
european_socket = EuropeanSocket()
american_plug = AmericanPlug()
adapter2 = PlugAdapter_US_to_EUR(american_plug, european_socket)
print(adapter2.wired_connector())