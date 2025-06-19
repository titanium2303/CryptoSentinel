import sqlite3
from datetime import datetime

DB_NAME = "signals.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS signals (
            timestamp TEXT,
            action TEXT,
            confidence REAL
        )
    """)
    conn.commit()
    conn.close()

def save_signal(action, confidence):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("INSERT INTO signals (timestamp, action, confidence) VALUES (?, ?, ?)",
              (datetime.utcnow().isoformat(), action, confidence))
    conn.commit()
    conn.close()

def get_recent_signals(minutes=60):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("""
        SELECT * FROM signals
        WHERE timestamp >= datetime('now', ?)
    """, (f'-{minutes} minutes',))
    rows = c.fetchall()
    conn.close()
    return rows
