from bot.database.db import get_connection

def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS settings (
        id INTEGER PRIMARY KEY,
        cpu_threshold INTEGER NOT NULL,
        ram_threshold INTEGER NOT NULL
    )
    """)

    # ensure one row exists
    cursor.execute("SELECT COUNT(*) FROM settings")
    if cursor.fetchone()[0] == 0:
        cursor.execute(
            "INSERT INTO settings (cpu_threshold, ram_threshold) VALUES (?, ?)",
            (80, 80)
        )

    conn.commit()        
    conn.close()
    