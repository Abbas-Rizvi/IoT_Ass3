from django.shortcuts import render
from webControl.models import Mode, State 
from rest_framework import viewsets
from webControl.serializers import ModeSerializer, StateSerializer
import requests
import json

class ModeViewSet(viewsets.ModelViewSet): 
    queryset = Mode.objects.all() 
    serializer_class = ModeSerializer


class StateViewSet(viewsets.ModelViewSet): 
    queryset = State.objects.all() 
    serializer_class = StateSerializer


def dashboard(request):
    out = ''


    # For POST requests to page
    if request.method == 'POST':

        # Check if the power on checkbox is selected
        # Update value
        if request.POST.get('state') == 'on':
            # if selected, turn on via put request
            values = {"name": "on"}
            r = requests.put('http://127.0.0.1:8000/state/1/', json=values)

        else:
            # if not selected, turn off via put request
            values = {"name": "off"}
            r = requests.put('http://127.0.0.1:8000/state/1/', json=values)


        # Check if the auto mode checkbox is selected
        # Update value
        if request.POST.get('mode') == 'auto':
            # if selected, turn on via put request
            values = {"name": "auto"}
            r = requests.put('http://127.0.0.1:8000/mode/1/', json=values)

        else:
            # if not selected, turn off via put request
            values = {"name": "manual"}
            r = requests.put('http://127.0.0.1:8000/mode/1/', json=values)

    
    # get state of state variable, load as json and set currentState variable
    r = requests.get('http://127.0.0.1:8000/state/1/')
    result = r.text
    output = json.loads(result)
    currentstate = output['name']

    # get state of mode variable, load as json and set currentMode variable
    r = requests.get('http://127.0.0.1:8000/mode/1/')
    result = r.text
    output = json.loads(result)
    currentmode = output['name']


    # Context variables to be passed to page
    # used for default slider values
    context = {
        'currentMode': currentmode,
        'currentState': currentstate
    }

    # render page, using variables
    return render(request, 'dashboard.html', context)
