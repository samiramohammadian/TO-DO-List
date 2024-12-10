from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm

def task_list(request):
    tasks = Task.objects.all().order_by('-created_at')
    form = TaskForm()

    if request.method == "POST":
        if 'add_task' in request.POST:
            form = TaskForm(request.POST)
            if form.is_valid():
                form.save()
            return redirect('task_list')

        task_id = request.POST.get('task_id')
        task = get_object_or_404(Task, id=task_id)

        if 'complete_task' in request.POST:
            task.completed = not task.completed
            task.save()
            return redirect('task_list')

        if 'edit_task' in request.POST:
            # Render the edit form with the specific task pre-filled
            form = TaskForm(instance=task)
            return render(request, 'todo/task_edit.html', {'form': form, 'task_id': task.id})

        if 'update_task' in request.POST:
            # Handle the update form submission
            form = TaskForm(request.POST, instance=task)
            if form.is_valid():
                form.save()
                return redirect('task_list')

        if 'delete_task' in request.POST:
            task.delete()
            return redirect('task_list')

    return render(request, 'todo/task_list.html', {'tasks': tasks, 'form': form})
