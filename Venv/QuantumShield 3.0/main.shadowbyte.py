from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import logging
import uvicorn
import datetime

# ───────────────────────────────────────────────
# Systemstart-Protokoll
startup_time = datetime.datetime.now()

# Logging aktivieren
logging.basicConfig(
    filename="logs/shadowcore_log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("🔒 QuantumShield gestartet")


# ───────────────────────────────────────────────
# FastAPI Initialisierung
app = FastAPI(
    title="QuantumShield Core",
    description="ASGI-Modul für Sicherheit, Sprache und Schutz",
    version="3.0"
)

# ───────────────────────────────────────────────
# CORS-Konfiguration (für GUI oder externe Panels)
origins = [
    "http://localhost",
    "http://127.0.0.1:8000",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ───────────────────────────────────────────────
# HTTP-Endpunkte
@app.get("/")
def index():
    return {"message": "🔐 QuantumShield ist aktiv", "status": "bereit"}

@app.get("/status")
def status():
    return {
        "system": "QuantumShield",
        "status": "online",
        "start": startup_time.isoformat(),
        "version": "3.0"
    }

# ───────────────────────────────────────────────
# WebSocket-Verbindung (z. B. für LEX oder GUI-Panel)
clients = []

@app.websocket("/ws/lex")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    clients.append(websocket)
    logging.info("🔌 Neue LEX-Verbindung akzeptiert")

    try:
        while True:
            data = await websocket.receive_text()
            logging.info(f"📨 Von LEX empfangen: {data}")
            # Echo zur Rückmeldung
            await websocket.send_text(f"LEX bestätigt: {data}")
    except WebSocketDisconnect:
        clients.remove(websocket)
        logging.warning("🔌 LEX-Verbindung getrennt")


# ───────────────────────────────────────────────
# Interne Fehlerbehandlung
@app.exception_handler(Exception)
async def all_exception_handler(request, exc):
    logging.error(f"❌ Fehler: {exc}")
    return JSONResponse(
        status_code=500,
        content={"message": "Interner Systemfehler", "error": str(exc)},
    )


# ───────────────────────────────────────────────
# Direkter Start (optional)
if __name__ == "__main__":
    uvicorn.run("main_shadowbyte:app", host="127.0.0.1", port=8000, reload=True)
