from django.shortcuts import render

def home(request):
    return render(request, 'habitApp/habit_list.html')

