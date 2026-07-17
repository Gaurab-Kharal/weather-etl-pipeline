import pandas as pd
weather_forecast = pd.read_csv("/home/sage_gaurab/chained/data_projects/weather-etl-pipeline/data/raw/berlin_raw.csv")
print(weather_forecast.sample(5))
print(weather_forecast.dtypes)
weather_forecast["time"] = pd.to_datetime(weather_forecast["time"])
print(weather_forecast.dtypes)
weather_forecast.to_csv("/home/sage_gaurab/chained/data_projects/weather-etl-pipeline/data/processed/berlin_processed.csv")

# checking if time column retains it datatype
berlin_processed = pd.read_csv("/home/sage_gaurab/chained/data_projects/weather-etl-pipeline/data/processed/berlin_processed.csv")
print(berlin_processed.shape)
print(berlin_processed.sample(3))
print(berlin_processed.dtypes)