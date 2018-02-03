from datetime import datetime
from django.shortcuts import render

# Create your views here.
from .models import IOT


'''
import RPi.GPIO as GPIO
PIN_TV      = 2
PIN_LIGHT   = 3
PIN_FAN     = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_TV   , GPIO.OUT)
GPIO.setup(PIN_LIGHT, GPIO.OUT)
GPIO.setup(PIN_FAN  , GPIO.OUT)
GPIO.output(PIN_TV, GPIO.LOW)
GPIO.output(PIN_LIGHT, GPIO.LOW)
GPIO.output(PIN_FAN, GPIO.LOW)

'''

def home(request):
    if IOT.objects.count() > 0:
        data = IOT.objects.last()
        to_save = False
        if 'tv' in request.GET:
            data.tv = request.GET['tv'] == 'ON'
            to_save = True
            #GPIO.output(PIN_TV, GPIO.HIGH if data.tv else GPIO.LOW)
        if 'light' in request.GET:
            data.light = request.GET['light'] == 'ON'
            to_save = True
            # GPIO.output(PIN_LIGHT, GPIO.HIGH if data.tv else GPIO.LOW)
        if 'fan' in request.GET:
            data.fan = request.GET['fan'] == 'ON'
            to_save = True
            # GPIO.output(PIN_FAN, GPIO.HIGH if data.tv else GPIO.LOW)

        if to_save:
            data.modified = datetime.now()
            data.save()

        return render(request, 'home.html', {"data": data})
    else:
        return render(request, '404.html',{})