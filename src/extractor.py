import requests as req
import pandas as pd 
import os 
from config import RAW_DATA_PATH, BASE_URL

raw_file_path = os.path.join(RAW_DATA_PATH,"berlin_raw.csv")

def fetch_forecast(latitude, longitude, city_name):
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "hourly": "temperature_2m"
    }

    # Here we are requesting for response form BASE_URL
    # params structural way to ask question

    response = req.get(BASE_URL, params)

    # Checking the status
    # looking for attribute status_code in obj response 
    # If is not 200 then it was unccessful 

    if response.status_code != 200:
        print(f"Fetching data unsuccessful \n{response}")
        return None
    
    # If response was successful convert 
    # Converting json resopnse to dictionary which python understand and is a python object

    data = response.json()

    # creating a dataframe out of dictionary 
    df = pd.DataFrame(data["hourly"])

    # defining extra column for city 
    df["city"] = city_name

    # returning the resulted DataFrame and existing the function
    return df


def fetch_load_data(latitude,logitude, city_name ):
    berlin_df = fetch_forecast(latitude, logitude, city_name)
    if berlin_df is not None:
        berlin_df.to_csv(raw_file_path, index=False)
        print(f"Data was loaded to {raw_file_path}")
        print(f"sample of loaded data \n\n{berlin_df.sample(5)}")
        

if __name__ == "__main__" : 
    fetch_load_data(52.52, 13.41, "Berlin")

