from django.shortcuts import render
import json
import urllib.request
import urllib.parse
from datetime import datetime
# Create your views here.
def index(request):
    if request.method=='POST':
        city=request.POST['city']
        #http://api.openweathermap.org/data/2.5/weather?q=las%20vegas&units=imperial&appid=2292c4f0b253ca08693910338321d445
        source=urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+urllib.parse.quote(city)+'&appid=2292c4f0b253ca08693910338321d445').read()
        datalist=json.loads(source)
        sr=datetime.fromtimestamp(datalist['sys']['sunrise'])
        ss=datetime.fromtimestamp(datalist['sys']['sunset'])
        data={
        "coun_code":str(datalist['sys']['country']),
        "name":str(datalist['name']),
        "coord":str(datalist['coord']['lon'])+' '+str(datalist['coord']['lat']),
        "temp":str(datalist['main']['temp'])+'K',
        "pres":str(datalist['main']['pressure']),
        "humid":str(datalist['main']['humidity']),
        "description":str(datalist ['weather'][0]['description']),
        "sunr":str(sr),
        "suns":str(ss),
        }
        print(data)
    else:
        data={}
    return render(request, "weather.html",data)
def about(request):
    return render(request,"about.html")
