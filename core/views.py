from django.shortcuts import render
from core.models import Habit, Record
from core.forms import NewHabitForm


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

def habit_tracker(request):
    all_habits = Habit.objects.filter(user=request.user)
    form = NewHabitForm(request.POST)
    context = {"all_habits": all_habits, "form": form} 
    return render(request, 'habit_tracker.html', context=context)