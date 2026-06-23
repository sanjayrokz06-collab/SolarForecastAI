import requests
import pandas as pd


def get_weather():

    latitude = 9.9252
    longitude = 78.1198

    url = (
        "https://api.open-meteo.com/v1/forecast?"
        f"latitude={latitude}"
        f"&longitude={longitude}"
        "&hourly=temperature_2m,"
        "relative_humidity_2m,"
        "cloud_cover,"
        "windspeed_10m"
        "&forecast_days=2"
    )

    response = requests.get(url)

    data = response.json()

    df = pd.DataFrame({

        "temperature_2m":
            data["hourly"]["temperature_2m"],

        "relative_humidity_2m":
            data["hourly"]["relative_humidity_2m"],

        "windspeed_10m":
            data["hourly"]["windspeed_10m"],

        "cloud_cover":
            data["hourly"]["cloud_cover"]

    })

    return df.tail(24)