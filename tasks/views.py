from django.shortcuts import render, redirect
from .models import *
from .forms import *


# Create your views here.
def TaskMenu(request):
    cat=Category.objects.all()

    context = {
        'cat': cat
    }
    return render(request, 'tasks/tasks_cat.html', context)





def addTask(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tasks')
    else:
        form = TaskForm()

    # Get all categories from the database
    categories = Category.objects.all()

    # Pass the categories to the form's field choices
    form.fields['category'].choices = [(category.id, category.name) for category in categories]

    context = {
        'form': form,
        'categories': categories
    }
    return render(request, 'tasks/addTask.html', context)



def showTask(request, id):
    task = Task.objects.get(id=id)
    context = {
        'task': task
    }
    return render(request, 'tasks/showTask.html', context)

def deleteTask(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    return redirect('tasks')

def Task_category(request, name):
    tasks = Task.objects.filter(category__name=name)
    context = {
        'tasks': tasks
    }
    return render(request, 'tasks/Taskmenu.html', context)

def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tasks')
    else:
        form = CategoryForm()

    context = {
        'form': form
    }
    return render(request, 'tasks/addCategory.html', context)