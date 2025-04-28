from django.urls import path

from .views import list_todos, todo_detail, todo_create, todo_update, todo_delete

urlpatterns = [
    path("", list_todos, name="list_todos"),
    path("todo_detail/", todo_detail, name="todo_detail"),
    path("todo_create/", todo_create, name="todo_create"),
    path("todo_update/", todo_update, name="todo_update"),
    path("todo_delete/", todo_delete, name="todo_delete"),
]
