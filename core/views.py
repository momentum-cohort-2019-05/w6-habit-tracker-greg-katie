from django.shortcuts import render
from core.models import Habit, Record


# Views for Habit Tracker.

def habit_list(request):
    habits = Habit.objects.all()
    return render(request, 'core/habit_detail.html', context={'habits': habits})


def record_list(request):
    records = Record.objects.all()
    return render(request, 'core/record_detail.html', context={'records': records})


def index(request):
    
    return render(request,'index.html')

def habit_detail(request, pk):
    habit = Habit.objects.get(pk=pk)
    records = Record.objects.filter(habit=habit)
    context = {"habit": habit, "records": records}
    return render(request, 'habit_detail.html', context=context)