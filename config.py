
# Base URL for fetching forecast data from api.open-meteo.com
base_url = "https://api.open-meteo.com/v1/forecast"

# raw and processed data reletive path 
raw_data_path = "data/raw"
processed_data_path = "data/processed"

# cities dictionary with values latitude and longitude  
cities_lon_lat = {
    "Kathmandu" : {"latitude" : 27.70, "longitude" : 85.32},
    "Pokhara" : {"latitude" : 28.27, "longitude" : 83.97},
    "Bharatpur" : {"latitude" : 27.68, "longitude" : 83.44},
    "Biratnagar" : {"latitude" : 26.46, "longitude" : 87.27}
}