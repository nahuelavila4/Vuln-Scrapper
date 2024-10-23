import sqlite3

conn = sqlite3.connect("vulnerabilities.db")
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS vulnerabilities (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cve_id TEXT,
    description TEXT,
    published_date TEXT
)
''')

def save_sql(id, descrip, date):
    print("Alo")





