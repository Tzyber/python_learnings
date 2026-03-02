'''Musterimplementierung: Dependency Injection in Python
Dieses Beispiel dient als gemeinsame Grundlage zur Einführung in das Konzept der Dependency Injection (DI) in Python.
Ziel ist es, das Prinzip der Entkopplung von Klassen sowie die Verbesserung der Testbarkeit zu verdeutlichen.'''


#1. Problem: Feste Abhängigkeit (Ohne Dependency Injection)
#In der folgenden Implementierung erzeugt die Klasse ReportService ihre Abhängigkeit selbst. Dadurch ist sie fest an eine konkrete Implementierung gebunden.

class FileWriter:
    def write(self, text):
        print(f"Schreibe in Datei: {text}")



class ReportService:
    def __init__(self):
        self.writer = FileWriter()  # Feste Abhängigkeit, Konstruktoraufruf, gebaut für einen Datentypen FileWriter

    def create_report(self, content):
        self.writer.write(content)


service = ReportService()
service.create_report("Umsatzbericht 2026")


#Nachteil: Die Klasse ReportService kann nicht ohne Weiteres mit einer anderen Ausgabeform (z. B. Datenbank, Konsole, API) verwendet oder einfach getestet werden.
