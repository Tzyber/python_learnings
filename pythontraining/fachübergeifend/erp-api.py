# Das kleinste mögliche FastAPI Programm
import uvicorn
from fastapi import FastAPI

# FastAPI Objekt anlegen
# Das ist die Anwendung. Sie kennt alle Routen und verwaltet den Server
app = FastAPI(
    title= "Bit connect office IT GmbH - ERP",
    version= "1.3.0",
)

print(type(app))  # <class 'fastapi.applications.FastAPI'>
print(app.title)  # Bit connect office IT GmbH - ERP
print(app.version)  # 1.3.0
print(len(app.routes)) # 0
print(app.openapi()) # {'openapi': '3.0.2', 'info': {'title': 'Bit connect office IT GmbH - ERP', 'version': '1.3.0'}, 'paths': {}

print("zum starten des servers: uvicorn main:app --reload")

if __name__ == "__main__":
    # "erp-api:app" -> Datei heißt erp-api.py, das Objekt heißt app
    uvicorn.run("erp-api:app", host="127.0.0.1", port=8000, reload=True)