#! python3
# WeatherCheck.py - grabs weather for current location

import requests, time, wc_config, ast

current_time = int(time.time())

data = requests.get('http://ipinfo.io')
loc_dict = ast.literal_eval(data.text)

lat_long_dict = {
    'latitude':loc_dict.get('loc').split(',')[0],
    'longitude':loc_dict.get('loc').split(',')[1].strip()}

city_state = loc_dict.get('city') + ', ' + loc_dict.get('region')

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

print('Current Conditions for ' + city_state + ':\n' + summary_current)
print('Current Temp: ' + str(temp_current) + ' degrees')
print('High Temp: ' + str(temp_high) + ' degrees')
print('Low Temp: ' + str(temp_low) + ' degrees')
print('Average Wind Today: ' + str(wind_speed) + ' mph')
print('Chance of Rain: ' + str(precip_chance) + '%') 
