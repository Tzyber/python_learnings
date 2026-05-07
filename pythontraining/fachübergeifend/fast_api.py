
from fastapi import FastAPI, HTTPException
import psycopg2
import psycopg2.extras
import os
from dotenv import load_dotenv
import uvicorn


load_dotenv()

app = FastAPI(
title = "Klinik",
description = "REST-API für die Klinik-Datenbank",
version = "1.0.0"
)

Verbindung = {
'host': os.getenv('DB_HOST', 'localhost'),
'dbname': os.getenv('DB_NAME', 'klinik'),
'user': os.getenv('DB_USER', 'postgres'),
'password': os.getenv('DB_PASSWORD', 'Awb2tz'),
}

@app.get("/")
def startseite():
    return {"status": "API läuft", "api" : "Klinik-API v1.0"}
    
@app.get("/aerzte")
def alle_arzte():
    '''gibt alle Ärzte zurück'''
    with psycopg2.connect(**Verbindung) as conn:
         with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
            cur.execute("select id, name, fachgebiet,email from personal.aerzte;")
            return cur.fetchall()


@app.get("/aerzte/{arzt_id}")
def arzt_detail(arzt_id: int):
    with psycopg2.connect(**Verbindung) as conn:
        with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
            cur.execute("select * from personal.aerzte where id = %s;", (arzt_id,))

            arzt = cur.fetchone()
        if not arzt:
            raise HTTPException(status_code=400, detail="Arzt nicht gefunden!")
        return arzt



@app.get("/statistik")
def statistik():
    """Gibt Klinik-Kennzahlen zurück."""
    with psycopg2.connect(**Verbindung) as conn:
        with conn.cursor() as cur:
            cur.execute("select count(*) from personal.aerzte;")
            aerzte = cur.fetchone()[0]
            cur.execute("select count(*) from patientendaten.patienten;")
            patienten = cur.fetchone()[0]
            cur.execute("select count(*) from patientendaten.diagnosen;")
            diagnosen = cur.fetchone()[0]
    return {
        "aerzte": aerzte,
        "patienten": patienten,
        "diagnosen": diagnosen,
    }

if __name__ == "__main__":
    uvicorn.run("fast_api:app", host="127.0.0.1", port=8000, reload=True)