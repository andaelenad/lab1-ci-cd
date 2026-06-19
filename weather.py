import requests


def get_coordinates(city):
    url = "https://geocoding-api.open-meteo.com/v1/search"
    params = {"name": city, "count": 1, "language": "en", "format": "json"}
    resp = requests.get(url, params=params)
    resp.raise_for_status()
    data = resp.json()
    if not data.get("results"):
        print(f"City '{city}' not found.")
        return None
    result = data["results"][0]
    return result["latitude"], result["longitude"], result.get("name", city)


def get_weather(lat, lon):
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lon,
        "current": [
            "temperature_2m",
            "relative_humidity_2m",
            "apparent_temperature",
            "weather_code",
            "wind_speed_10m",
        ],
        "timezone": "auto",
    }
    resp = requests.get(url, params=params)
    resp.raise_for_status()
    return resp.json()


def weather_description(code):
    descriptions = {
        0: "Clear sky",
        1: "Mainly clear",
        2: "Partly cloudy",
        3: "Overcast",
        45: "Foggy",
        48: "Depositing rime fog",
        51: "Light drizzle",
        53: "Moderate drizzle",
        55: "Dense drizzle",
        61: "Slight rain",
        63: "Moderate rain",
        65: "Heavy rain",
        71: "Slight snow",
        73: "Moderate snow",
        75: "Heavy snow",
        80: "Slight rain showers",
        81: "Moderate rain showers",
        82: "Violent rain showers",
        95: "Thunderstorm",
    }
    return descriptions.get(code, f"Unknown ({code})")


def main():
    city = input("Enter city name: ").strip()
    coords = get_coordinates(city)
    if not coords:
        return

    lat, lon, name = coords
    data = get_weather(lat, lon)
    current = data["current"]

    print(f"\nWeather in {name}")
    print(f"{'-' * 30}")
    print(f"Temperature:      {current['temperature_2m']}{data['current_units']['temperature_2m']}")
    print(f"Feels like:       {current['apparent_temperature']}{data['current_units']['apparent_temperature']}")
    print(f"Humidity:         {current['relative_humidity_2m']}{data['current_units']['relative_humidity_2m']}")
    print(f"Wind speed:       {current['wind_speed_10m']}{data['current_units']['wind_speed_10m']}")
    print(f"Condition:        {weather_description(current['weather_code'])}")


if __name__ == "__main__":
    main()
