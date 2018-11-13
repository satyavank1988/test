 
import json
import requests
import os

API_KEY=os.environ["OPENWEATHER_API_KEY"]
CITY_NAME=os.environ["CITY_NAME"]
api_url="http://api.openweathermap.org/data/2.5/weather?q="+CITY_NAME+"&appid="+API_KEY

response = requests.get(api_url)

if response.status_code == 200:
#    print(json.loads(response.content.decode('utf-8')))
    items = json.loads(response.content.decode('utf-8'))
    for v in items.items():
        if "weather" in v:
            desc = v[1][0].get('description')
        if "main" in v:
            temp = str(v[1].get('temp'))
            humidity = str(v[1].get('humidity'))
    output = 'source=' + '"openweathermap", ' + 'city="' + CITY_NAME + '", ' + 'description="' + desc + '", ' + 'temp="' + temp + '", ' + 'humidity="' + humidity + '"'
    print(output)


else:
    print("Error in connection")






