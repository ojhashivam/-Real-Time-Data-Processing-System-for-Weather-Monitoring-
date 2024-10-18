import requests
from datetime import datetime
from alerts import AlertSystem
from db import store_daily_summary,fetch_data
from dotenv import load_dotenv
import os
load_dotenv()

API_KEY = os.getenv('API_KEY')

CITIES = ['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad']
weather_data = [] 

def get_weather_data(city):
    response = requests.get(f'http://api.openweathermap.org/data/2.5/find?q={city}&appid={API_KEY}')
    data = response.json()
    if response.status_code == 200:
        weather   = data['list'][0]['weather'][0]['main']
        data_list = data['list'][0]
        data_list = data_list['main']
        date    = datetime.now()
        temp  = data_list['temp'] - 273.15
        max_temp  = data_list['temp_max'] - 273.15
        min_temp = data_list['temp_min'] - 273.15
        dominant_condition = data_list['feels_like'] - 273.15
        return {'city':city ,
                'weather':weather , 
                'date':date ,
                'curr_temp':temp , 
                'max_temp':max_temp , 
                'min_temp':min_temp , 
                'feels_like':dominant_condition}


    else:
        print("Error Fetching Data")
        return None

def fetch_weather_data():
    global weather_data
    weather_data.clear()
    daily_summaries = []

    for city in CITIES:
        data = get_weather_data(city)
        if data:
            weather_data.append(data)

            daily_summaries.append({
                'city': data['city'],
                'weather':data['weather'] , 
                'date': data['date'],
                'avg_temp': data['curr_temp'],
                'max_temp': data['max_temp'],
                'min_temp': data['min_temp'],
                'dominant_condition': data['feels_like']
            })
    
    AlertSystem().check_thresholds(weather_data)
    for summary in daily_summaries:
        store_daily_summary(
            city=summary['city'],
            weather = summary['weather'],
            date=summary['date'],
            avg_temp=summary['avg_temp'],
            max_temp=summary['max_temp'],
            min_temp=summary['min_temp'],
            dominant_condition=summary['dominant_condition']
        )
        
    return fetch_data()

