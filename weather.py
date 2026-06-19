import urllib.request
import json
import sys

def get_weather(city="Bucharest"):
    url = f"https://wttr.in/{city}?format=j1"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        response = urllib.request.urlopen(req)
        data = json.loads(response.read().decode('utf-8'))
        temp = data['current_condition'][0]['temp_C']
        desc = data['current_condition'][0]['weatherDesc'][0]['value']
        print(f"Vremea in {city}: {temp} C, {desc}")
    except Exception as e:
        print("Eroare la preluarea datelor:", e)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        get_weather(sys.argv[1])
    else:
        get_weather()
