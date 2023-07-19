import requests

def lookup_upc(barcode):
    response = requests.get(f"https://api.upcitemdb.com/prod/trial/lookup?upc={barcode}")
    data = response.json()
    return data['items'][0]['title']
