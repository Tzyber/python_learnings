from abc import ABC, abstractmethod


class MessageSender(ABC):
    """
    Abstrakte Basisklasse für alles, was Nachrichten senden kann.
    """
    @abstractmethod
    def send_message(self, message):
        """
        Sendet eine Nachricht. Muss von Unterklassen implementiert werden.
        """
        pass

class CheckSimCard(ABC):
    """
    Abstrakte Basisklasse für Geräte, die eine SIM-Karte prüfen können.
    """
    @abstractmethod
    def check_sim(self):
        """
        Prüft den Status der SIM-Karte.
        """
        pass

class SmsSender(MessageSender, CheckSimCard):
    """
    Klasse zum Senden von SMS. Implementiert MessageSender und CheckSimCard.
    """
    def send_message(self, message):
        """Sendet den Text als SMS."""
        print("Sende SMS:", message)

    def check_sim(self):
        """Prüft, ob die SIM-Karte bereit ist."""
        print("Sim Karte ist ok!")

class EmailSender(MessageSender):
    """
    Klasse zum Senden von E-Mails.
    """
    def send_message(self, message):
        """Sendet den Text als E-Mail."""
        print("Sende E-Mail:", message)

class PushNotificationSender(MessageSender):
    """
    Klasse zum Senden von Push-Benachrichtigungen.
    """
    def send_message(self, message):
        """Sendet den Text als Push-Nachricht."""
        print("Sende Push Notification:", message)


class NotificationService:
    """
    Ein Service, der Benachrichtigungen über einen beliebigen MessageSender verschickt.
    Folgt dem Dependency Inversion Principle (DIP).
    """
    def __init__(self, sender: MessageSender):
        """
        Initialisiert den Service mit einer konkreten Sender-Implementierung.
        """
        self.sender = sender

    def send_notification(self, message):
        """
        Verschickt die Nachricht über den konfigurierten Sender.
        """
        self.sender.send_message(message)

sms = SmsSender()
email = EmailSender()
push = PushNotificationSender()

service = NotificationService(sms)
sms.check_sim()
service.send_notification("mensch SMS ist ja toll")

service2 = NotificationService(email)
service2.send_notification("Das sollte Email sein")

service3 = NotificationService(push)
service3.send_notification("Neues Update verfügbar!")