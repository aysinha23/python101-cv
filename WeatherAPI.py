import requests

# 1. The URL (The "Address" of the data)
# This is a public API for Cambridge, MA (lat 42.37, lon -71.10)
url = "https://api.open-meteo.com/v1/forecast?latitude=42.37&longitude=-71.10&current_weather=true"

# 2. The Request (The "Knock on the door")
response = requests.get(url)

# 3. The JSON (Turning the response into a Python Dictionary)
data = response.json()

# 4. Accessing the data (Just like your roadmap!)
current_temp = data["current_weather"]["temperature"]
wind_speed = data["current_weather"]["windspeed"]
wind_direction = data["current_weather"]["winddirection"]

print(f"🌡 Current Temp in Cambridge: {current_temp}°C")
print(f"💨 Wind Speed: {wind_speed} km/h")
print(f"🧭 Wind Direction: {wind_direction}")