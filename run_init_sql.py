import sqlite3

# Read SQL commands from file
with open("init.sql", "r", encoding="utf-8") as file:
    sql_script = file.read()

# Connect to SQLite database (creates it if it doesn't exist)
conn = sqlite3.connect("library.db")
cursor = conn.cursor()

try:
    cursor.executescript(sql_script)
    print("Database initialized successfully!")
except Exception as e:
    print("Error:", e)

conn.commit()
conn.close()
