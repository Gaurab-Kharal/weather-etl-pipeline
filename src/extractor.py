import requests as req
import pandas as pd 

BASE_URL = "https://api.open-meteo.com/v1/forecast"

def fetch_forecast(latitude, longitude, city_name):
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "hourly": "temperature_2m"
    }
    response = req.get(BASE_URL, params)

    if response.status_code != 200:
        print(f"Fetching data unsuccessful \n{response}")
        return None

    data = response.json()
    df = pd.DataFrame(data["hourly"])
    df["city"] = city_name
    return df

berlin_df = fetch_forecast(52.52, 13.41, "Berlin")

if berlin_df is not None:
    berlin_df.to_csv("/home/sage_gaurab/chained/data_projects/weather-etl-pipeline/data/raw/berlin_raw.csv", index=False)
    print(berlin_df.head(24))
