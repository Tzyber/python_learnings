'''2. Lösung: Dependency Injection über den Konstruktor
Nun wird die Abhängigkeit von außen übergeben. Die Klasse kennt nur noch das erwartete Verhalten (write-Methode), nicht jedoch die konkrete Implementierung.
'''


class FileWriter:
    def write(self, text):
        print(f"Schreibe in Datei: {text}")


class ConsoleWriter:
    def write(self, text):
        print(f"Konsolenausgabe: {text}")


class ReportService:
    def __init__(self, writer):  # Abhängigkeit wird injiziert
        self.writer = writer

    def create_report(self, content):
        self.writer.write(content)


file_writer = FileWriter()
console_writer = ConsoleWriter()

service1 = ReportService(file_writer) # Funktioniert mit mehreren Datentyen
service2 = ReportService(console_writer)

service1.create_report("Umsatzbericht 2026")
service2.create_report("Testbericht")


#Vorteil: Die Klasse ReportService ist nun flexibel und kann mit unterschiedlichen Implementierungen verwendet werden, ohne selbst geändert zu werden.
