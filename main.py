from database.db_utils import *
from devices.barcode import *
from devices.rfid import *
from apis.upc import *

def main():
    conn = connect_db()
    while True:
        print("1: Add item manually")
        print("2: Add item with RFID")
        print("3: Add item with barcode")
        print("4: Remove item")
        print("5: Show inventory")
        print("6: Show possible recipes")
        print("7: Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            item = input("Enter item name: ")
            quantity = int(input("Enter quantity: "))
            add_item(conn, item, quantity)

        elif choice == "2":
            print("a: Scan RFID tag")
            print("b: Change item name")
            choice2 = input("Choose an option: ")
            if choice2 == "a":
                id, item = read_rfid()
                quantity = int(input("Enter quantity: "))
                add_item(conn, item, quantity)
            elif choice2 == "b":
                old_name, new_name = change_name()
                change_item_name(conn, old_name, new_name)

        elif choice == "3":
            barcode = read_barcode()
            item = lookup_upc(barcode)
            if item is None:
                print("Unrecognized barcode. Please enter the item details manually.")
                item = input("Enter item name: ")
            quantity = int(input("Enter quantity: "))
            add_item(conn, item, quantity)

        elif choice == "4":
            item = input("Enter item name: ")
            quantity = int(input("Enter quantity: "))
            remove_item(conn, item, quantity)

        elif choice == "5":
            inventory = show_inventory(conn)
            for row in inventory:
                print(f"Item: {row[0]}, Quantity: {row[1]}")

        elif choice == "6":
            possible_recipes = get_possible_recipes(conn)
            for recipe in possible_recipes:
                print(recipe)

        elif choice == "7":
            break

    conn.close()


if __name__ == "__main__":
    main()