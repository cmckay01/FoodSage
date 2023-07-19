import sqlite3
import json

def connect_db():
    conn = sqlite3.connect('pantry.db')
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS inventory (
            item TEXT PRIMARY KEY,
            quantity INTEGER
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS recipes (
            name TEXT PRIMARY KEY,
            ingredients TEXT
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

def add_recipe(conn, name, ingredients):
    cursor = conn.cursor()
    ingredients_json = json.dumps(ingredients)
    cursor.execute("INSERT INTO recipes VALUES (?, ?)", (name, ingredients_json))
    conn.commit()

def get_possible_recipes(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM inventory")
    inventory = {row[0]: row[1] for row in cursor.fetchall()}
    cursor.execute("SELECT * FROM recipes")
    recipes = cursor.fetchall()
    possible_recipes = []
    for name, ingredients_json in recipes:
        ingredients = json.loads(ingredients_json)
        if all(item in inventory and inventory[item] >= quantity for item, quantity in ingredients.items()):
            possible_recipes.append(name)
    return possible_recipes

def change_item_name(conn, old_name, new_name):
    print(f"Updating item name in inventory from '{old_name}' to '{new_name}'")
    cursor = conn.cursor()
    cursor.execute("UPDATE inventory SET item = ? WHERE item = ?", (new_name, old_name))
    conn.commit()

