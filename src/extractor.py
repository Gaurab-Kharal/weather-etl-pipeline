# first definig class
import pandas as pd
import os 
from config import base_url, raw_data_path, cities_lon_lat
import requests 


CITIES = cities_lon_lat 
BASE_URL = base_url

class WeatherExtractor:
    def __init__(self, cities=CITIES, url=BASE_URL):
        self.cities = cities
        self.url = url

    def fetch_cities_forecast(self):

        all_cities_df = []
        for city, coord in self.cities.items():
            lat = coord["latitude"]
            lon = coord["longitude"]

            params = {
                'latitude' : lat,
                'longitude' : lon,
                "hourly": "temperature_2m,relative_humidity_2m,precipitation,wind_speed_10m,surface_pressure"
            }
        
            response = requests.get(self.url, params)

            if response.status_code != 200:
                print(f"\n\nstatus code : {response.status_code} \nFetching Data Unsuccessful")
                continue

            dic = response.json()
            print("___"*100)

            df = pd.DataFrame(dic['hourly'])
            df["city"] = city
            all_cities_df.append(df)

            print(df)

        all_cities_df = pd.concat(all_cities_df)
        all_cities_df.to_csv(os.path.join(raw_data_path,"cities_forecast.csv"), index = False)
        


if __name__ == "__main__":
    extract_data = WeatherExtractor()
    extract_data.fetch_cities_forecast()
    print(extract_data)
        
