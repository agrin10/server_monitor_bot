from bot.database.db import get_connection

def get_settings():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT cpu_threshold, ram_threshold FROM settings LIMIT 1")

    row = cursor.fetchone()
    conn.close()
    return row

def update_cpu(value):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE settings SET cpu_threshold = ?", (value,))

    conn.commit()
    conn.close()


def update_ram(value):
    conn = get_connection()
    cursor  = conn.cursor()
    cursor.execute("UPDATE settings SET ram_threshold = ?",(value,))

    conn.commit()
    conn.close()
