from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Task
from django.shortcuts import redirect

# Create your views here.
def add_Task(request):
    task = request.POST['task']
    if task:
        Task.objects.create(task=task)
    return redirect('home')

def mark_as_done(request,pk):
    task = get_object_or_404(Task, pk=pk)
    task.iscompleted = True
    task.save()
    return redirect('home')

def mark_as_undone(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.iscompleted = False
    task.save()
    return redirect('home')

def delete_task(request, pk):
    task = get_object_or_404(Task , pk=pk)
    task.delete()
    return redirect('home')

def edit_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        new_task = request.POST['task']
        task.task = new_task
        task.save()
        return redirect('home')
    else:
        context = {
            'tasks': task,
        }
    return render(request, 'edit_task.html', context)
