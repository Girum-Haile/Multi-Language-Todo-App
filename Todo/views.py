from django.shortcuts import render, redirect
from django.utils import timezone
from Todo.models import Todo
from .forms import TodoForm
from django.http import HttpResponseRedirect


def home(request):
    todo_items = Todo.objects.all().order_by("-added_date")

    return render(request, 'Todo/index.html', {
        "todo_items": todo_items
    })


def add_todo(request):
    current_date = timezone.now()
    content = request.POST["content"]
    created_obj = Todo.objects.create(added_date=current_date, text=content)
    length_of_todos = Todo.objects.all().count()
    return HttpResponseRedirect("/")


def delete_todo(request, todo_id):
    Todo.objects.get(id=todo_id).delete()
    return HttpResponseRedirect("/")


def edit(request, todo_id):
    if request.method == 'POST':
        item = Todo.objects.get(pk=todo_id)
        form = TodoForm(request.POST or None, instance=item)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        item = Todo.objects.get(pk=todo_id)
        return render(request, 'Todo/edit.html', {'item': item})
