from django.contrib import admin
from django.urls import path

# from todos.views import todo_list
from todos.views import TodoListView
from todos.views import TodoCreateView
from todos.views import TodoUpdateView
from todos.views import TodoDeleteView
from todos.views import TodoFinishTaskView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", TodoListView.as_view(), name="todo_list"),
    path("create", TodoCreateView.as_view(), name="todo_create"),
    path("update/<int:pk>", TodoUpdateView.as_view(), name="todo_update"),
    path("delete/<int:pk>", TodoDeleteView.as_view(), name="todo_delete"),
    path("finish_task/<int:pk>", TodoFinishTaskView.as_view(), name="todo_finish_task")
    # path("", todo_list)
]
