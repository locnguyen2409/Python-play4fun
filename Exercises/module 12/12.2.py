import requests

def get_weather():
    city = input("Enter municipality name: ")
    api_key = "YOUR_API_KEY_HERE"

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        description = data["weather"][0]["description"]
        temp_k = data["main"]["temp"]
        temp_c = temp_k - 273.15

        print(f"\nWeather in {city}:")
        print(f"Condition: {description}")
        print(f"Temperature: {temp_c:.2f} °C")
    else:
        print("Error: Could not find city or API issue.")


get_weather()
