from django.shortcuts import render
from django.http import HttpResponse
from .models import Todo

# Create your views here.

def list_todos(request):
    todos = Todo.objects.all()
    todos = [
        {
            "id": todo.id,
            "title": todo.title,
            "description": todo.description,
            "created_at": todo.created_at,
            "due_date": todo.due_date,
            "completed": todo.completed
        }
        for todo in todos
    ]
    return HttpResponse([todos])

def todo_detail(request):
    return HttpResponse("Todo Details")

def todo_create(request):
    return HttpResponse("Todo Create")

def todo_update(request):
    return HttpResponse("Todo Update")

def todo_delete(request):
    return HttpResponse("Todo Delete")