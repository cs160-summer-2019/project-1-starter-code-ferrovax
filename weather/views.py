from django.shortcuts import render
from django.http import HttpResponse

def forecast(request):
    return render(request, 'weather/forecast.html')

def forecast_alert(request):
    return render(request, 'weather/forecast-alert.html')

def forecast2(request):
    return render(request, 'weather/forecast2.html')

def comparison_alert(request):
    return render(request, 'weather/comparison-alert.html')

def index(request):
    return render(request, 'weather/index.html')