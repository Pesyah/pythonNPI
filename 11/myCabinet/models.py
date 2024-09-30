from django.db import models
from django.contrib.auth.models import User

class Selection_of_workouts(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    light_workouts = models.TextField() # HTML текст
    medium_workouts = models.TextField() # HTML текст
    hard_workouts = models.TextField() # HTML текст
    
    created_at = models.DateTimeField(auto_now_add=True)