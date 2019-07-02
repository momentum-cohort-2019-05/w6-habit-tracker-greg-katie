from django.db import models
from datetime import date, time
from django.contrib.auth.models import User


# Models for our Habit Tracker.

class Habit(models.Model):
    name = models.CharField(max_length=200)
    objective = models.TextField(max_length=700)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name


class Record(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE)
    outcome = models.TextField(max_length=700)
    

    def __str__(self):
        return self.date

class Meta:
    ordering = ["-date"]

    


