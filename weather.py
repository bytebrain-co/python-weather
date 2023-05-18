import requests
import json

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }

    response = requests.get(base_url, params=params)
    weather_data = json.loads(response.text)

    if weather_data["cod"] == "404":
        print("City not found. Please check the city name.")
        return

    temperature = weather_data["main"]["temp"]
    weather_condition = weather_data["weather"][0]["description"]

    print(f"Weather in {city}:")
    print(f"Temperature: {temperature}°C")
    print(f"Condition: {weather_condition}")


if __name__ == '__main__':
    api_key = "YOUR_API_KEY"
    city = input("Enter city name: ")
    get_weather(api_key, city)
