from django.shortcuts import get_object_or_404

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Todo
from .serializers import TodoSerializer 


# Create your views here.

# API Overview
@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List':'/todo-list/',
        'Detail View':'/todo-detail/<str:pk>/',
        'Create':'/todo-create/',
        'Update':'/todo-update/<str:pk>/',
        'Delete':'/todo-delete/<str:pk>/',
        } 
    return Response(api_urls)

# list todos
@api_view(['GET'])
def todo_list(request):
    todos = Todo.objects.all()
    serializer = TodoSerializer(todos, many=True)
    return Response(serializer.data)

# todo details 
@api_view(['GET'])
def todo_detail(request, pk):
    todos = get_object_or_404(Todo, id=pk)
    serializer = TodoSerializer(todos, many=False)
    return Response(serializer.data)

# todo create
@api_view(['POST'])
def todo_create(request):
    serializer = TodoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# todo update
@api_view(['POST'])
def todo_update(request, pk):
    todos = get_object_or_404(Todo, id=pk)
    serializer = TodoSerializer(todos, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# todo delete 
@api_view(['DELETE'])
def todo_delete(request, pk):
    todos = get_object_or_404(Todo, id=pk) 
    todos.delete()
    return Response({'message': 'Todo deleted successfully!'}, status=status.HTTP_200_OK)