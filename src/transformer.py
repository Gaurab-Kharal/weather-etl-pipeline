# importing essential libraries 

import pandas as pd
import os 
from config import raw_data_path, processed_data_path

# just checking quality of data

def transformed_df(df):
    df["time"] = pd.to_datetime(df["time"])
    df["date"] = df["time"].dt.date
    df["day"] = df["time"].dt.day

    return df 


class WeatherTransformer:
    def __init__(self):

        try : 
            self.df = transformed_df( pd.read_csv(os.path.join(raw_data_path,"cities_forecast.csv")) )

        except FileNotFoundError:
            print("cities_forecast.csv does not exist")
            self.df = None 
            
    def data_quality_check(self):

        try:
            df = self.df

            print(f"\n\nSample Data : \n\n{df.sample(5)} \n{'---'*50}")
            print(f"\n\nData Description : \n\n{df.describe()} \n{'---'*50}")
            print(f"\n\nNull Counts/Column : \n\n{df.isna().sum()} \n{'---'*50}")
            print(f"\n\nColumn Datatypes : \n\n{df.dtypes} \n{'---'*50}")
        
        except:
            print(f"DataFrame does not exist")



    def data_aggregation(self):

        try:

            df = self.df

            return (
                df.groupby(["city", "date"]).agg(
                avg_relative_humidity_2m_per_city = ('relative_humidity_2m', 'mean')
            ).sort_values(["city", "date"])
            
            )
        except:
            print("DataFrame does not exist")
    
    def save_processed(self):

        try:
            df = self.df
            df.to_csv(os.path.join(processed_data_path, "cities_forecast.csv"), index = False)
            print(f"\n\nSample data of processed data saved at : {os.path.join(processed_data_path, 'cities_forecast.csv')} \n\n{df.sample(5)}")
        except:
            print("DataFrame does not exist")

if __name__ == "__main__":
    data_inspection = WeatherTransformer()
    # data_inspection.data_quality_check()
    print(data_inspection.data_aggregation())
    data_inspection.save_processed()