from django.db import models


# model for mode
# used to identify if automatic or manual
class Mode(models.Model):
    name = models.CharField(max_length=50)

# model for state
# used to identify if light is on or off
class State(models.Model):
    name = models.CharField(max_length=50)
    

    