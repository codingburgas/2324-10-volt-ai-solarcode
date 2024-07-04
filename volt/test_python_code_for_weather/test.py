import openmeteo_requests

import requests_cache
import pandas as pd
from retry_requests import retry
import time

df = pd.read_csv("volt\docs\power_consumption_data.csv")

responses = {}

for idx, row in df.iterrows():
    print(row['Coordinates'])
    latitude = float(row['Coordinates'].split(",")[0])
    longtitude = float(row['Coordinates'].split(",")[1])

    # Setup the Open-Meteo API client with cache and retry on error
    cache_session = requests_cache.CachedSession('.cache', expire_after = -1)
    retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
    openmeteo = openmeteo_requests.Client(session = retry_session)

    # Make sure all required weather variables are listed here
    # The order of variables in hourly or daily is important to assign them correctly below
    url = "https://archive-api.open-meteo.com/v1/archive"
    params = {
    	"latitude": latitude,
    	"longitude": longtitude,
    	"start_date": "2021-01-01",
    	"end_date": "2024-01-01",
    	"hourly": ["temperature_2m", "precipitation", "cloud_cover", "terrestrial_radiation", "sunshine_duration"]
    }
    responses[row['City']] = openmeteo.weather_api(url, params=params)
    time.sleep(5)
    #responses = openmeteo.weather_api(url, params=params)

print(responses)

# Process first location. Add a for-loop for multiple locations or weather models


for city, response in responses.items():
    response = response[0]


    print(f"Coordinates {response.Latitude()}°N {response.Longitude()}°E")
    print(f"Elevation {response.Elevation()} m asl")
    print(f"Timezone {response.Timezone()} {response.TimezoneAbbreviation()}")
    print(f"Timezone difference to GMT+0 {response.UtcOffsetSeconds()} s")
    # Process hourly data. The order of variables needs to be the same as requested.
    hourly = response.Hourly()
    hourly_temperature_2m = hourly.Variables(0).ValuesAsNumpy()
    hourly_precipitation = hourly.Variables(1).ValuesAsNumpy()
    hourly_cloud_cover = hourly.Variables(2).ValuesAsNumpy()
    hourly_terrestrial_radiation = hourly.Variables(3).ValuesAsNumpy()
    hourly_sunshine_duration = hourly.Variables(4).ValuesAsNumpy()
    hourly_data = {"date": pd.date_range(
    	start = pd.to_datetime(hourly.Time(), unit = "s", utc = True),
    	end = pd.to_datetime(hourly.TimeEnd(), unit = "s", utc = True),
    	freq = pd.Timedelta(seconds = hourly.Interval()),
    	inclusive = "left"
    )}
    hourly_data["temperature_2m"] = hourly_temperature_2m
    hourly_data["precipitation"] = hourly_precipitation
    hourly_data["cloud_cover"] = hourly_cloud_cover
    hourly_data["terrestrial_radiation"] = hourly_terrestrial_radiation
    hourly_data["sunshine_duration"] = hourly_sunshine_duration
    hourly_dataframe = pd.DataFrame(data = hourly_data)
    print(hourly_dataframe)