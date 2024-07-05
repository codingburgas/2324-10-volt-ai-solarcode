"""
Get data from Open-meteo and store it locally.
"""

import openmeteo_requests

import requests_cache
import pandas as pd
from retry_requests import retry
import time


print("")
# read city location data
power_consumption_data = pd.read_csv('C:\Users\DDPeev21\2324-10-volt-ai-solarcode\volt\docs\power_consumption_data.csv')
cities_with_coordinates = power_consumption_data[['City', 'Coordinates']]


# Setup the Open-Meteo API client with cache and retry on error
cache_session = requests_cache.CachedSession('.cache', expire_after = -1)
retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
openmeteo = openmeteo_requests.Client(session = retry_session)

# Make sure all required weather variables are listed here
# The order of variables in hourly or daily is important to assign them correctly below
url = "https://archive-api.open-meteo.com/v1/archive"

responses = {}

for index, row in cities_with_coordinates.iterrows():
	params = {
		"latitude": float(row['Coordinates'].split(",")[0]),
		"longitude": float(row['Coordinates'].split(",")[1]),
		"start_date": "2021-01-01",
		"end_date": "2024-01-01",
		"hourly": ["temperature_2m", "precipitation", "cloud_cover", "sunshine_duration", "terrestrial_radiation"]
	}
	responses[row['City']] = openmeteo.weather_api(url, params=params)

	#responses.append(openmeteo.weather_api(url, params=params))
	# sleep for 10 seconds to not overwhelm the API calls e.g.
	# Minutely API request limit exceeded. Please try again in one minute.
	time.sleep(10)

print(responses)

hourly_dataframe = pd.DataFrame()
# Process first location. Add a for-loop for multiple locations or weather models
# response = responses[0][0]
for city, resp in responses.items():
	response = resp[0]
	print(f"Coordinates {response.Latitude()}°N {response.Longitude()}°E")
	print(f"Elevation {response.Elevation()} m asl")
	print(f"Timezone {response.Timezone()} {response.TimezoneAbbreviation()}")
	print(f"Timezone difference to GMT+0 {response.UtcOffsetSeconds()} s")

	# Process hourly data. The order of variables needs to be the same as requested.
	hourly = response.Hourly()
	hourly_temperature_2m = hourly.Variables(0).ValuesAsNumpy()
	hourly_precipitation = hourly.Variables(1).ValuesAsNumpy()
	hourly_cloud_cover = hourly.Variables(2).ValuesAsNumpy()
	hourly_sunshine_duration = hourly.Variables(3).ValuesAsNumpy()
	hourly_terrestrial_radiation = hourly.Variables(4).ValuesAsNumpy()

	print("stuff")
	hourly_data = {
		"date": pd.date_range(
		start = pd.to_datetime(hourly.Time(), unit = "s", utc = True),
		end = pd.to_datetime(hourly.TimeEnd(), unit = "s", utc = True),
		freq = pd.Timedelta(seconds = hourly.Interval()),
		inclusive = "left"
	)}

	hourly_data["temperature_2m"] = hourly_temperature_2m
	hourly_data["precipitation"] = hourly_precipitation
	hourly_data["cloud_cover"] = hourly_cloud_cover
	hourly_data["sunshine_duration"] = hourly_sunshine_duration
	hourly_data["terrestrial_radiation"] = hourly_terrestrial_radiation
	hourly_data["city"] = city

	df = pd.DataFrame(data = hourly_data)
	hourly_dataframe = pd.concat([hourly_dataframe, df], ignore_index=True)
print(hourly_dataframe)


hourly_dataframe.to_csv("data\cities_data_hourly.csv", index = False)

