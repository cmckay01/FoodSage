from mfrc522 import SimpleMFRC522
import RPi.GPIO as GPIO

GPIO.setwarnings(False)

def read_rfid():
    reader = SimpleMFRC522()
    id, text = reader.read()
    text = text.strip()  # Remove extra spaces
    if not text:
        text = input("Please provide a name for the item: ")
        reader.write(text)
        print("Data writing is complete")
    return id, text

def change_name():
    reader = SimpleMFRC522()
    print("Please place the RFID tag near sensor for reading")
    id, old_text = reader.read()
    old_text = old_text.strip()  # Remove extra spaces
    new_text = input("Please provide a new name for the item: ")
    print("Please place the RFID tag near sensor for writing")
    reader.write(new_text)
    print("Data writing is complete")
    print(f"Changed name from '{old_text}' to '{new_text}'")
    return old_text, new_text.strip()  # Remove extra spaces







