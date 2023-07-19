from mfrc522 import SimpleMFRC522
import RPi.GPIO as GPIO

GPIO.setwarnings(False)

def read_rfid():
    reader = SimpleMFRC522()
    id, text = reader.read()
    if not text:
        text = input("Please provide a name for the item: ")
        reader.write(text)
    return id, text

def change_name():
    reader = SimpleMFRC522()
    id, text = reader.read()
    if text:
        text = input("Please provide a name for the item: ")
        reader.write(text)
    return id, text