class UserManager:
    """
    Verwaltet Benutzeraktionen. Diese Klasse koordiniert das Speichern, Loggen und Benachrichtigen,
    verletzt aber potenziell das Single Responsibility Principle, wenn sie zu viel Logik selbst enthält
    (hier delegiert sie aber sauber an andere Services).
    """

    def __init__(self, repository, logger, email_service):
        """
        Initialisiert den Manager mit den notwendigen Services.
        """
        self.repo = repository
        self.log = logger
        self.email = email_service

    def create_user(self, newuser, email):
        """
        Erstellt einen neuen Benutzer, speichert ihn, loggt die Aktion und sendet eine Willkommens-Mail.
        """
        user = User(newuser, email)
        self.repo.save_user(user)
        self.log.log(f"User: {newuser} created.")
        self.email.send_email(email, "Willkommen!")


class User:
    """
    Datenklasse für einen Benutzer.
    """

    def __init__(self, username, email):
        self.username = username
        self.email = email
        pass


class Repository:
    """
    Verantwortlich für die Datenspeicherung (z.B. Datenbank).
    """

    def save_user(self, user):
        """Speichert den Benutzer."""
        print("saving user:", user.username)
        pass


class Logger:
    """
    Verantwortlich für das Protokollieren von Ereignissen.
    """

    def log(self, message):
        """Schreibt eine Nachricht in das Log."""
        print(message)
        pass


class EmailService:
    """
    Verantwortlich für den E-Mail-Versand.
    """

    def send_email(self, email, message):
        """Sendet eine E-Mail an die angegebene Adresse."""
        print("Sende E-mail an:", email, message)
        pass


repo = Repository()
logger = Logger()
email_service = EmailService()
create_user = UserManager(repo, logger, email_service)
create_user.create_user("john_doe", "johndoe@gmx.com")