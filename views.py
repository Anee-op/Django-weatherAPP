from django.shortcuts import render
from django.http import HttpResponse
from . import views 
import json
import urllib.request 

def index(request):
    
    data = {
        'city_name': 'Enter City',
        'main_temperature': '--',
        'current_humidity': '-- %',
        'current_wind_speed': '-- m/s',
        'current_feels_like': '-- °C',
        'error_message': None # New key for error handling
    }

    if request.method == 'POST':
        city = request.POST.get('city')
        
        try:
           
            res = urllib.request.urlopen(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=d1f8edf35d55a4090476549bbcdb125f&units=metric")
            
           
            json_content = res.read().decode('utf-8') 
            
            
            json_data = json.loads(json_content)
            
           
            data = {
                'city_name': str(json_data['name']),
                'main_temperature': str(json_data['main']['temp']) + ' °C',
                'current_humidity': str(json_data['main']['humidity']) + ' %',
               
                'current_wind_speed': str(json_data['wind']['speed']) + ' m/s', 
                'current_feels_like': str(json_data['main']['feels_like']) + ' °C',
                'error_message': None 
            }
            
           
            return render(request, 'index.html', data)
            
        except urllib.error.HTTPError as e:
            data['error_message'] = f"Error: City '{city}' not found (Status Code: {e.code})."
            
        except Exception as e:
            data['error_message'] = f"An unexpected error occurred: {e}"
    return render(request, 'index.html', data)








    return render(request,'index.html')
