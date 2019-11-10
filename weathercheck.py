#! python3
# WeatherCheck.py - grabs weather for current location

import requests, location, time, console, wc_config, webbrowser

current_time = int(time.time())

#tries to get the lat and long for the phone. If it fails, data for saved default lat and long is ised instead
try:
    lat_long_dict = location.get_location()
    latitude = lat_long_dict.get('latitude')
    longitude = lat_long_dict.get('longitude')
except:
    console.alert('Could not find GPS data')
    latitude = wc_config.default_latitude
    longitude = wc_config.default_longitude
    lat_long_dict = {'latitude':latitude, 'longitude':longitude}

location_dict_list = location.reverse_geocode(lat_long_dict)

location_dict = location_dict_list[0]

#get address of current location to display in the alert from lat and long
street = location_dict.get('Street')
city = location_dict.get('City')
state = location_dict.get('State')

alert_message = street + '\n' + city + ', ' + state + '\n\n'

res = requests.get('https://api.darksky.net/forecast/' + wc_config.api_key + '/' + str(latitude) + ',' + str(longitude) + ',' + str(current_time))

#parse json into way more data than necessary, but it might be handy later
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

alert_message = alert_message + \
'Current Conditions: ' + summary_current + '\n' + 'Current Temp: ' + str(temp_current) + ' degrees' + '\n' + 'High Temp: ' + str(temp_high) + ' degrees' + '\n' + 'Low Temp: ' + str(temp_low) + ' degrees'  + '\n' + 'Average Wind Today: ' + str(wind_speed) + ' mph'  + '\n' + 'Chance of Rain: ' + str(precip_chance)

close_option = console.alert('Weather Conditions', alert_message, 'Open Dark Sky', 'Close', hide_cancel_button=True)

if close_option == 1:
    #open dark sky app using URL scheme- could be mofified for any weather app
    webbrowser.open('darksky://')

