import requests

# We need coordinates to get weather data
latitude = 28.21  # Pokhara latitude
longitude = 83.98  # Pokhara longitude

# Build the API URL with our parameters
url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m"

# Make the request
response = requests.get(url)
data = response.json()

print(data)
