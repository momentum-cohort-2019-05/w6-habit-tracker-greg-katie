from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse



# Models for our Habit Tracker.

class Habit(models.Model):
    name = models.CharField(max_length=500, help_text= "Please enter your habit here")
    objective = models.TextField(max_length=700, help_text= "Please enter the description of your habit here")
    target = models.IntegerField(help_text= "Please enter a desired target number for your habit")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    observers = models.ManyToManyField("Observer", blank=True)
    
    def get_absolute_url(self):
        return reverse('habit-detail', args=[str(self.id)])

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






