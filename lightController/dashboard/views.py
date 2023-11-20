from django.shortcuts import render
from dashboard.gpio import gpio_controller
import requests
import json


def dashboard(request):
    out = ''


    if request is None:
        # Handle the case where the request is None
       pass; 
    # For POST requests to page
    elif request.method == 'POST':

        # Check if the power on checkbox is selected
        # Update value
        if request.POST.get('state') == 'on':
            # if selected, turn on via put request
            values = {"name": "on"}
            r = requests.put('http://127.0.0.1:8000/api/state/1/', json=values)
            manual_state = True

        else:
            # if not selected, turn off via put request
            values = {"name": "off"}
            r = requests.put('http://127.0.0.1:8000/api/state/1/', json=values)
            manual_state = False

        # Check if the auto mode checkbox is selected
        # Update value
        if request.POST.get('mode') == 'auto':
            # if selected, turn on via put request
            values = {"name": "auto"}
            r = requests.put('http://127.0.0.1:8000/api/mode/1/', json=values)
            gpio_controller.auto_mode()

        else:
            # if not selected, turn off via put request
            values = {"name": "manual"}
            r = requests.put('http://127.0.0.1:8000/api/mode/1/', json=values)
            gpio_controller.toggle_mode()

            if manual_state:
                gpio_controller.turn_on_led()
            else:
                gpio_controller.turn_off_led()

    
    # get state of state variable, load as json and set currentState variable
    r = requests.get('http://127.0.0.1:8000/api/state/1/')
    result = r.text
    output = json.loads(result)
    currentstate = output['name']

    # get state of mode variable, load as json and set currentMode variable
    r = requests.get('http://127.0.0.1:8000/api/mode/1/')
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
