from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Task
from django.contrib import messages


# def home(request):
#     if request.user.is_authenticated:
#         return redirect('task_list') 
#     return redirect('login') 

@login_required
def index(request):
    
    if request.user.is_staff or request.user.is_superuser:
        return redirect('admin:todo_list')

    return render(request, 'list/todo_list.html')

@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'list/todo_list.html', {'tasks': tasks})

@login_required
def task_create(request):
    if request.method == 'POST':
        Task.objects.create(
            user=request.user,
            title=request.POST['title'],
            description=request.POST['description'],
            deadline=request.POST['deadline'],
        )
        messages.success(request, 'Task berhasil ditambahkan')
        return redirect('task_list')
    return render(request, 'list/list_form.html')

@login_required
def task_update(request, id):
    task = get_object_or_404(Task, id=id, user=request.user)

    if request.method == 'POST':
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.deadline = request.POST.get('deadline')

        
        status = request.POST.get('status')
        if status == 'done':
            task.completed = True
        else:
            task.completed = False

        task.save() 

        messages.success(request, 'Task berhasil diupdate')
        return redirect('task_list')

    return render(request, 'list/list_form.html', {'task': task})

@login_required
def task_toggle(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.completed = not task.completed  
    task.save()
    return redirect('task_list')

@login_required
def task_delete(request, id):
    task = get_object_or_404(Task, id=id, user=request.user)

    if request.method == 'POST':
        task.delete()
        messages.success(request, 'Task berhasil dihapus')
        return redirect('task_list')

    return render(request, 'list/list_delete.html', {'task': task})
