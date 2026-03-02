class Emailsender:
    def send_email(self, msg):
        print("sending email with:", msg)

class NotificationSender:
    def __init__(self):
        self.email = Emailsender()

    def notification(self, msg):
        self.email.send_email(msg)