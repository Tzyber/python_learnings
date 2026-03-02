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


if __name__ == "__main__":
    sms = SMSSender()
    email = EmailSender()
    fax = FaxSender()

    NotificationService(sms).send_notification("hallo")
    NotificationService(email).send_notification("hallo")
    NotificationService(fax).send_notification("hallo")
