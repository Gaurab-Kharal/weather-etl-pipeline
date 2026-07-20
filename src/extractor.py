# first definig class
import pandas as pd
import os 
from config import cities, base_url, raw_data_path
import requests 


CITIES = cities 
BASE_URL = base_url
class WeatherExtractor:
    def __init__(self, cities=CITIES, base_url=BASE_URL):
        self.cities = cities
        self.base_url = base_url

    def fetch_one_city(self):
        params = {
            'longitude' : 53, 
            'latitude' : 54

        }
    
        response = (requests.get(self.base_url, params)).json
        df = pd.DataFrame(response)

        df.to_csv(os.join_path(raw_data_path,"x.csv"))



    
    def fetch_all_cities():

        
        
