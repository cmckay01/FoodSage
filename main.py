from database.db_utils import connect_db, add_item, remove_item, show_inventory
from devices.rfid import read_rfid
from devices.barcode import read_barcode
from apis.upc import lookup_upc

def main():
    conn = connect_db()
    while True:
        print("1: Add item with RFID")
        print("2: Add item with barcode")
        print("3: Remove item")
        print("4: Show inventory")
        print("5: Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            id, item = read_rfid()
            quantity = int(input("Enter quantity: "))
            add_item(conn, item, quantity)
        elif choice == "2":
            barcode = read_barcode()
            item = lookup_upc(barcode)
            quantity = int(input("Enter quantity: "))
            add_item(conn, item, quantity)
        elif choice == "3":
            item = input("Enter item name: ")
            quantity = int(input("Enter quantity: "))
            remove_item(conn, item, quantity)
        elif choice == "4":
            inventory = show_inventory(conn)
            for row in inventory:
                print(f"Item: {row[0]}, Quantity: {row[1]}")
        elif choice == "5":
            break
    conn.close()


if __name__ == "__main__":
    main()