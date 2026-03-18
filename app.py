from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import List
from datetime import datetime
import sqlite3
import os

app = FastAPI()

# Setup static files and templates
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Database setup
DATABASE = "iot_devices.db"

def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS devices (
        device_id TEXT PRIMARY KEY,
        name TEXT,
        status TEXT,
        battery_level INTEGER,
        last_updated TEXT
    )''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS alerts (
        alert_id TEXT PRIMARY KEY,
        device_id TEXT,
        message TEXT,
        timestamp TEXT,
        severity TEXT,
        FOREIGN KEY(device_id) REFERENCES devices(device_id)
    )''')
    # Seed data
    cursor.execute("INSERT OR IGNORE INTO devices VALUES ('device1', 'Temperature Sensor', 'active', 85, ?)" , (datetime.now().isoformat(),))
    cursor.execute("INSERT OR IGNORE INTO alerts VALUES ('alert1', 'device1', 'Battery low', ?, 'high')", (datetime.now().isoformat(),))
    conn.commit()
    conn.close()

init_db()

# Pydantic models
class Device(BaseModel):
    device_id: str
    name: str
    status: str
    battery_level: int
    last_updated: datetime

class Alert(BaseModel):
    alert_id: str
    device_id: str
    message: str
    timestamp: datetime
    severity: str

# API Endpoints
@app.get("/api/devices", response_model=List[Device])
async def get_devices():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM devices")
    devices = cursor.fetchall()
    conn.close()
    return [Device(device_id=row[0], name=row[1], status=row[2], battery_level=row[3], last_updated=datetime.fromisoformat(row[4])) for row in devices]

@app.post("/api/devices", response_model=Device)
async def add_device(device: Device):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO devices VALUES (?, ?, ?, ?, ?)", (device.device_id, device.name, device.status, device.battery_level, device.last_updated.isoformat()))
        conn.commit()
    except sqlite3.IntegrityError:
        raise HTTPException(status_code=400, detail="Device ID already exists")
    finally:
        conn.close()
    return device

@app.get("/api/alerts", response_model=List[Alert])
async def get_alerts():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM alerts")
    alerts = cursor.fetchall()
    conn.close()
    return [Alert(alert_id=row[0], device_id=row[1], message=row[2], timestamp=datetime.fromisoformat(row[3]), severity=row[4]) for row in alerts]

@app.put("/api/devices/{device_id}", response_model=Device)
async def update_device(device_id: str, device: Device):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("UPDATE devices SET name = ?, status = ?, battery_level = ?, last_updated = ? WHERE device_id = ?", 
                   (device.name, device.status, device.battery_level, device.last_updated.isoformat(), device_id))
    conn.commit()
    conn.close()
    return device

# HTML Endpoints
@app.get("/", response_class=HTMLResponse)
async def read_dashboard(request: Request):
    return templates.TemplateResponse("dashboard.html", {"request": request})

@app.get("/devices", response_class=HTMLResponse)
async def read_devices(request: Request):
    return templates.TemplateResponse("devices.html", {"request": request})

@app.get("/alerts", response_class=HTMLResponse)
async def read_alerts(request: Request):
    return templates.TemplateResponse("alerts.html", {"request": request})

@app.get("/settings", response_class=HTMLResponse)
async def read_settings(request: Request):
    return templates.TemplateResponse("settings.html", {"request": request})

@app.get("/analytics", response_class=HTMLResponse)
async def read_analytics(request: Request):
    return templates.TemplateResponse("analytics.html", {"request": request})
