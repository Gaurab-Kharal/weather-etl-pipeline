# Importing essential libraries 
import pandas as pd
import os 
import requests 

from config import base_url, raw_data_path, cities_lon_lat


CITIES = cities_lon_lat 
BASE_URL = base_url

# Creating a blueprint WeatherExtractor class that defines 3 methods
#   - fetch_one_city : fetches forecast data of one city and returns df or None based on response
#   - fetch_all_cities : fetches forecast data of all cities in dictionary return df 
#   - fetch_and_save : fetches and saves the DataFrame of all cities in data/raw/
 
class WeatherExtractor:
    def __init__(self, cities=CITIES, url=BASE_URL):
        self.cities = cities
        self.url = url


    def fetch_one_city(self, city_name):

        lat = self.cities[city_name]["latitude"]
        lon = self.cities[city_name]["longitude"]

        params = {
                "latitude" : lat,
                "longitude" : lon,
                "hourly": "temperature_2m,relative_humidity_2m,precipitation,wind_speed_10m,surface_pressure"
            }

        response = requests.get(self.url, params)
        if response.status_code != 200:
            print(f"\n\nstatus code : {response.status_code} \nFetching Data Unsuccessful")
            return None
            
            
        dic = response.json()
        df = pd.DataFrame(dic['hourly'])
        df['city'] = city_name

        return df 
    
    def fetch_all_cities(self):

        all_cities_df = []

        for city in self.cities:
            df = self.fetch_one_city(city)
            if df is not None:
                all_cities_df.append(df)

        return pd.concat(all_cities_df) 
    
    def fetch_and_save(self):
    
        all_cities_df = self.fetch_all_cities()
        all_cities_df.to_csv(os.path.join(raw_data_path,"cities_forecast.csv"), index = False)
        print(f"\n\nSample of data that is being saved at : \n\n{os.path.join(raw_data_path,'cities_forecast.csv')} \n\n{all_cities_df.sample(3)}")    


if __name__ == "__main__":

    # Defining extract_data object 
    extract_data = WeatherExtractor()

    # Calling method that fetch forecast data for one city and return DataFrame
    print(extract_data.fetch_one_city("Kathmandu").sample(10))
    print("___" * 100)

    # Calling method that fecthes data for all cities concat it and return one big DataFrame
    print(extract_data.fetch_all_cities().sample(10))

    # Fetches forecast data for all cities and saves DataFrame to data/raw/
    extract_data.fetch_and_save()
    
        
