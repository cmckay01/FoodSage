import sqlite3

def connect_db():
    conn = sqlite3.connect('pantry.db')
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS inventory (
            item TEXT PRIMARY KEY,
            quantity INTEGER
        )
    """)
    conn.commit()
    return conn

def add_item(conn, item, quantity):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO inventory VALUES (?, ?) ON CONFLICT(item) DO UPDATE SET quantity = quantity + ?", (item, quantity, quantity))
    conn.commit()

def remove_item(conn, item, quantity):
    cursor = conn.cursor()
    cursor.execute("SELECT quantity FROM inventory WHERE item = ?", (item,))
    current_quantity = cursor.fetchone()[0]
    if current_quantity < quantity:
        print("Error: not enough of this item in inventory.")
    else:
        cursor.execute("UPDATE inventory SET quantity = quantity - ? WHERE item = ?", (quantity, item))
        conn.commit()
        
def show_inventory(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM inventory")
    rows = cursor.fetchall()
    return rows
