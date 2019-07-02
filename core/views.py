from django.shortcuts import render
from core.models import Habit, Record


# Views for Habit Tracker.

def habit_list(request):
    habits = Habit.objects.all()
    return render(request, 'core/habit_index.html', context={'habits': habits})


def record_list(request):
    records = Record.objects.all()
    return render(request, 'core/record_detail.html', context={'records': records})


def index(request):
    
    return render(request,'index.html')

