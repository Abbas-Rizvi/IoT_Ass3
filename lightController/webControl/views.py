from django.shortcuts import render

from webControl.models import Mode, State 
from rest_framework import viewsets
from webControl.serializers import ModeSerializer, StateSerializer

class ModeViewSet(viewsets.ModelViewSet): 
    queryset = Mode.objects.all() 
    serializer_class = ModeSerializer


class StateViewSet(viewsets.ModelViewSet): 
    queryset = State.objects.all() 
    serializer_class = StateSerializer
