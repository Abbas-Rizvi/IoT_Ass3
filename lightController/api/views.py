from django.shortcuts import render
from api.models import Mode, State 
from api.serializers import ModeSerializer, StateSerializer
from rest_framework import viewsets


# Create your views here.
class ModeViewSet(viewsets.ModelViewSet): 
    queryset = Mode.objects.all() 
    serializer_class = ModeSerializer


class StateViewSet(viewsets.ModelViewSet): 
    queryset = State.objects.all() 
    serializer_class = StateSerializer