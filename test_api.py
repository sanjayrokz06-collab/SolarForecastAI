from weather_api import get_weather

df = get_weather()

print(df.head())

print()

print(df.tail())