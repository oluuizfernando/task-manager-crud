# from django.shortcuts import render
from django.views.generic import View
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
import datetime
from .models import Todo

# def todo_list(request):
#     todos = Todo.objects.all()
#     return render(request, "todos/todo_list.html", {"todos": todos})

class TodoListView(ListView):
    model = Todo

class TodoCreateView(CreateView):
    model = Todo
    fields = ["title", "deadline"]
    success_url = reverse_lazy("todo_list")

class TodoUpdateView(UpdateView):
    model = Todo
    fields = ["title", "deadline"]
    success_url = reverse_lazy("todo_list")

class TodoDeleteView(DeleteView):
    model = Todo
    success_url = reverse_lazy("todo_list")

class TodoFinishTaskView(View):
    def get(self, request, pk):
        todo = get_object_or_404(Todo, pk=pk)
        todo.mark_has_complete()
        return redirect("todo_list")