from django.urls import path

from .views import apiOverview, todo_list, todo_detail, todo_create, todo_update, todo_delete

urlpatterns = [
    path("api-overview/", apiOverview, name="api-overview"),
    path("todo-list/", todo_list, name="todo-list"),
    path("todo-detail/<str:pk>/", todo_detail, name="todo-detail"),
    path("todo-create/", todo_create, name="todo-create"),
    path("todo-update/<str:pk>/", todo_update, name="todo-update"),
    path("todo-delete/<str:pk>/", todo_delete, name="todo-delete"),
]
