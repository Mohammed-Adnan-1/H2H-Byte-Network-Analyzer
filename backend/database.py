import sqlite3

conn = sqlite3.connect("wifi_logs.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    latency REAL,
    packet_loss REAL,
    signal_dbm REAL,
    qoe TEXT
)
""")
conn.commit()

def insert_log(data, qoe):
    cursor.execute("""
    INSERT INTO logs (latency, packet_loss, signal_dbm, qoe)
    VALUES (?, ?, ?, ?)
    """, (data["latency"], data["packet_loss"], data["signal_dbm"], qoe))
    conn.commit()