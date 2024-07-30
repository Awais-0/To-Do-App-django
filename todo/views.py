from django.shortcuts import render
from todo_app.models import Task

def home(request):
    tasks = Task.objects.filter(iscompleted = False).order_by('-updated_at')
    completed_task = Task.objects.filter(iscompleted = True)
    context = {
        'tasks': tasks,
        'completed_tasks' : completed_task
    }
    return render(request, 'home.html', context)