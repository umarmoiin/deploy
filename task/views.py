from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse

from .models import *
from .forms import *

# Create your views here.
def index(request):
    tasks = Task.objects.all()

    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/")

    context = {'tasks':tasks, 'form':form} #dictionary 

    #return HttpResponse("hello world")
    return render(request, 'tasks/list.html', context) 

def updateTask(request, pk):
    task = Task.objects.get(id=pk)

    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect("/")
    
    context = {'form':form, 'task':task}

    return render(request, 'tasks/update_task.html', context)

def deleteTask(request, pk):
    item = Task.objects.get(id=pk)
    
    if request.method == 'POST':
        item.delete()
        return redirect('/')

    context = {'item':item}
    return render(request, 'tasks/delete.html', context)

def searchbar(request):
   if request.method == 'GET':
    search = request.GET.get('search_bar')
    post = Task.objects.all().filter(title__contains=search)
    return render(request, 'tasks/searchbar.html', {'post': post})



