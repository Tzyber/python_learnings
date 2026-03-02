import unittest
from unittest.mock import MagicMock
from Benarichtigungssystem_Mit_DI import NotificationService, NotificationSender


class TestNotificationService(unittest.TestCase):


    def test_send_notification(self):
        mock_sender = MagicMock(spec=NotificationSender)
        service = NotificationService(mock_sender)
        service.send_notification("Testnachricht")
        mock_sender.send_notification.assert_called_once()

if __name__ == "__main__":
    unittest.main()