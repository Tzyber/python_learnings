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
    dienst.senden(nachricht)

mail = Email()
sms = Sms()
push = PushNotification()
whatsapp = Whatsapp()

benachrichtigung_versenden(sms,"Hallo, das ist eine SMS Benachrichtigung!")