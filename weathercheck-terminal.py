#! python3
# WeatherCheck.py - grabs weather for current location

import requests, time, wc_config

current_time = int(time.time())

lat_long_dict = {
    'latitude':wc_config.default_latitude,
    'longitude':wc_config.default_longitude}


res = requests.get('https://api.darksky.net/forecast/' + wc_config.api_key + \
    '/' + str(lat_long_dict.get('latitude')) + ',' + \
    str(lat_long_dict.get('longitude')) + ',' + str(current_time))

weather_data = res.json()
weather_data_current = weather_data.get('currently')
weather_data_minutely = weather_data.get('minutely')
weather_data_hourly = weather_data.get('hourly')
weather_data_daily = weather_data.get('daily')
weather_data_daily = weather_data_daily['data'][0]
summary_current = weather_data_minutely.get('summary')
temp_current = weather_data_current.get('temperature')

temp_high = weather_data_daily.get('temperatureHigh')
temp_low = weather_data_daily.get('temperatureLow')
wind_speed = weather_data_daily.get('windSpeed')
precip_chance = weather_data_daily.get('precipProbability')

print('Current Conditions: ' + summary_current)
print('Current Temp: ' + str(temp_current) + ' degrees')
print('High Temp: ' + str(temp_high) + ' degrees')
print('Low Temp: ' + str(temp_low) + ' degrees')
print('Average Wind Today: ' + str(wind_speed) + ' mph')
print('Chance of Rain: ' + str(precip_chance) + '%') 
