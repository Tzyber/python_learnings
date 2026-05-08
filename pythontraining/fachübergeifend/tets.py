from fastapi import FastAPI
from fastapi.testclient import TestClient
app = FastAPI()

# erste Route: GET
# GET bedeutet: Daten abrufen, ohne sie zu verändern

@app.get("/")
def startseite():
    # Was dieser Funktion zurück gibt, schickt FastAPI an uns als JSON-Antwort
    # Ein Dictionary wird zu einem JSON-Objekt : {'key', 'value'}
    return {"message": "Willkommen bei der Bit connect Office IT GmbH!", 'status_code': 200, 'version': '1.3.0'}


@app.get("/stammdaten/personen")
def alle_personen():
    return [{'id': 1, 'name': 'Dominik', 'typ': 'kunde'}, {'id': 2, 'name': 'Tominik', 'typ': 'lieferant'}, {'id': 3, 'name': 'Lominik', 'typ': 'kunde'}]

# Testen der API mit dem TestClient
client = TestClient(app)
response = client.get("/stammdaten/personen")
print(response.status_code)  # 200
print(response.json())  # [{'id': 1, 'name': 'Dominik',