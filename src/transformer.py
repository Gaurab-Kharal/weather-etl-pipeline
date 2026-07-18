import pandas as pd
import os 
from config import RAW_DATA_PATH, PROCESSED_DATA_PATH

# defining the real file path for processed and raw data
def transform_berlin():
    real_file_path_raw = os.path.join(RAW_DATA_PATH,"berlin_raw.csv")
    real_file_path_processed = os.path.join(PROCESSED_DATA_PATH, "berlin_processed.csv")

    # reading csv file to get the data

    weather_forecast = pd.read_csv(real_file_path_raw)

    if __name__ == "__main__":
        print(weather_forecast.sample(5))
        print(weather_forecast.dtypes)

    # converthing time column which is stored as obj/string in .csv file format to datatime 
    weather_forecast["time"] = pd.to_datetime(weather_forecast["time"])

    # loading the processed data to data/berlin_processed.csv
    weather_forecast.to_csv(real_file_path_processed, index = False)


if __name__ == "__main__":
    transform_berlin()