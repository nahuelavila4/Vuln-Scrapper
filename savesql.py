import sqlite3
import datetime

conn = sqlite3.connect("scraper.db")
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS vulnerabilities (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cve_id TEXT UNIQUE,
    descrip TEXT,
    date TEXT,
    last_update TEXT      
)
''')

def insert_vuln(cve, descrip, date):
    cursor.execute(f"SELECT * FROM vulnerabilities WHERE cve_id = ?", (cve,))
    result = cursor.fetchone()
    if result is None:
        try:
            cursor.execute('''
                INSERT INTO vulnerabilities(cve_id, descrip, date, last_update)
                VALUES (?, ?, ?, ?)     
            ''', (cve, descrip, date, datetime.datetime.now))
            print(f"Vulnerabilidad {cve} agregada a la base de datos")
            conn.commit()
        except Exception as e:
            print(f"Error: {e}")
    else:
        print("Las vulnerabilidades ya se encuentran en la base de datos")
    
