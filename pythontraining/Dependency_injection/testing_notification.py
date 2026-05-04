import unittest
from unittest.mock import MagicMock
from Benarichtigungssystem_Mit_DI import NotificationService, NotificationSender


class TestNotificationService(unittest.TestCase):

    def test_send_notification_with_status(self):
        mock_sender = MagicMock(NotificationSender)
        service = NotificationService(mock_sender)
        result = service.send_notification("Testnachricht")
        mock_sender.send_notification.assert_called_once_with("Testnachricht")
        self.assertEqual(result, "Erfolgreich versendet")

if __name__ == "__main__":
    unittest.main()