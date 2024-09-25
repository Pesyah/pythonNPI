from django.db import models

# Create your models here.
class Selection_of_workouts(models.Model):

    light_workouts = models.TextField() # HTML текст
    medium_workouts = models.TextField() # HTML текст
    hard_workouts = models.TextField() # HTML текст
    
    created_at = models.DateTimeField(auto_now_add=True)