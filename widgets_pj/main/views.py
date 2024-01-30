from django.shortcuts import render
import requests
from .scripts.weather import kel2cel
from datetime import datetime

# Create your views here.

def index_page(request):
    return render(request, 'main/index.html')


def weather_page(request):
    context = {}
    city = 'Москва'
    # 'http://api.openweathermap.org/data/2.5/weather?q=Москва&lang=ru&APPID=7ddd7271a0b12d6ff030f828d4776330'
    if request.method == 'POST' and request.POST['city'] != '':
        city = request.POST['city']
    # print(request.headers)
    resp = requests.get('http://api.openweathermap.org/data/2.5/weather',
                            params={
                                'q': {city},
                                'lang': 'ru',
                                'APPID': '7ddd7271a0b12d6ff030f828d4776330'

                            }).json()
    print(resp)
    if 'message' in resp.keys():
        context.update({'error': resp['message']})
    else:
        context.update({
            'city': resp['name'],
            'temp': kel2cel(resp['main']['temp']),
            'feels_like': kel2cel(resp['main']['feels_like']),
            'temp_max': kel2cel(resp['main']['temp_max']),
            'temp_min': kel2cel(resp['main']['temp_min']),
            'weather_title': resp['weather'][0]['main'],
            'weather_description': resp['weather'][0]['description'],
            'weather_icon_link': f'https://openweathermap.org/img/wn/{resp['weather'][0]['icon']}@2x.png',
            'sunrise': datetime.fromtimestamp(resp['sys']['sunrise']),
            'sunset': datetime.fromtimestamp(resp['sys']['sunset']),
            'wind_speed': resp['wind']['speed']
        })
    
    return render(request, 'main/weather.html', context=context)



def exchange_page(request):
    return render(request, 'main/exchange.html')
