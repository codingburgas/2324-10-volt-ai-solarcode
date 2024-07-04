""" Convert data to yearly data for all cities"""

import pandas as pd

hourly_data = pd.read_csv("models/data/cities_data_hourly.csv")

# Assuming hourly_data contains data for multiple locations
locations = hourly_data['city'].unique()
all_yearly_data = []

for location in locations:
    location_data = hourly_data[hourly_data['city'] == location]

    # set the date column as the index
    # TypeError: Only valid with DatetimeIndex, TimedeltaIndex or PeriodIndex, but got an instance of 'Index'
    location_data.index = pd.to_datetime(location_data.index)

    # Resample and aggregate data as shown above
    daily_data = location_data.resample('D').agg({
        'terrestrial_radiation': 'sum',
        'cloud_cover': 'mean',
        'temperature_2m': 'mean',
        'precipitation': 'sum',
        'sunshine_duration': 'sum'
    }).reset_index()

    yearly_data = daily_data.resample('YE', on='index').agg({
        'terrestrial_radiation': 'mean',
        'cloud_cover': 'mean',
        'temperature_2m': 'mean',
        'precipitation': 'sum',
        'sunshine_duration': 'sum'
    }).reset_index(drop=True)

    yearly_data['location'] = location
    all_yearly_data.append(yearly_data)

# Combine all yearly data into a single DataFrame
final_yearly_data = pd.concat(all_yearly_data, ignore_index=True)

print(final_yearly_data)

final_yearly_data.to_csv("models/data/cities_data_yearly.csv", index = False)