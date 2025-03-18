from django.shortcuts import render, redirect
from habitTrackerApiApp.models import Tracker, HabitLog
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now

@login_required
def home(request):
    habits = Tracker.objects.filter(user=request.user)

    # Filter by frequency
    frequency_filter = request.GET.get("frequency")
    if frequency_filter:
        habits = habits.filter(frequency=frequency_filter)

    return render(request, 'habitApp/habit_list.html', {'habits': habits})

@login_required
def mark_done(request):
    if request.method == "POST":
        habit_id = request.POST.get("habit_id")
        date_completed = request.POST.get("date_completed")

        if habit_id and date_completed:
            try:
                habit = Tracker.objects.get(id=habit_id, user=request.user)
                HabitLog.objects.create(tracker=habit, date_completed=date_completed, user=request.user)
                return redirect('home') 
            except Tracker.DoesNotExist:
                pass  # Handle error (habit not found)
    
    return redirect('home')
