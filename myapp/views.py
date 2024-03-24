import requests
import datetime

from django.shortcuts import render

def index(request):
    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city = 'Rajshahi'
        
    appid = 'aa43e3e3877ee20eb2f6f1f24269fca1'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'q': city, 'appid': appid, 'units': 'metric'}
    r = requests.get(url=url, params=params)
    res = r.json()
    
    description = res['weather'][0]['description']
    icon = res['weather'][0]['icon']
    temp = res['main']['temp']
    wind_speed = res['wind']['speed']  # Fetching wind speed from the API response
    day = datetime.date.today()
    
    return render(request, 'weatherapp/index.html', {'description': description, 'icon': icon, 'temp': temp, 'wind_speed': wind_speed, 'day': day, 'city': city})
