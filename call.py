import requests

# API endpoint URL
url = "https://api.open-meteo.com/v1/forecast"

# Parameters (what you're asking for)
params = {
    "latitude": 48.85,  # pokhara
    "longitude": 2.35,
    "current": "temperature_2m",
}

# Make the request
response = requests.get(url, params=params)

# Get JSON data
data = response.json()

print(data)
# Extract the current temperature
current_temperature = data.get("current", {}).get("temperature_2m")
print(f"The current temperature in Pokhara is: {current_temperature}°C")


# Function to fetch weather data for given coordinates
def get_weather(latitude, longitude):
    url = "https://api.open-meteo.com/v1/forecast"

    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,wind_speed_10m",
    }

    response = requests.get(url, params=params)
    data = response.json()

    return {
        "temperature": data["current"]["temperature_2m"],
        "wind_speed": data["current"]["wind_speed_10m"],
    }


# Usage
weather = get_weather(27.7172, 85.3240)  # pokhara coordinates
print(f"Temperature: {weather['temperature']}°C")
print(f"Wind Speed: {weather['wind_speed']} km/h")
