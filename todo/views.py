from django.shortcuts import get_object_or_404

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status

from .models import Todo
from .serializers import TodoSerializer 

from rest_framework.permissions import IsAuthenticated


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
@permission_classes([IsAuthenticated])
def todo_list(request):
    # Filter todos by the logged-in user
    todos = Todo.objects.filter(author=request.user)  # This ensures only the user's todos are returned
    serializer = TodoSerializer(todos, many=True)
    return Response(serializer.data)

# todo details 
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def todo_detail(request, pk):
    todos = get_object_or_404(Todo, id=pk)

    if todos.author != request.user:
        return Response({
            'error': 'Not authorized to view this todo'
            }, status=status.HTTP_403_FORBIDDEN)
    
    serializer = TodoSerializer(todos, many=False)
    return Response(serializer.data)

# todo create
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def todo_create(request):
    # Add the logged-in user to the request data
    request.data['user'] = request.user.id  # Associate the user with the Todo

    serializer = TodoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(author=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# todo update
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def todo_update(request, pk):
    todos = get_object_or_404(Todo, id=pk, author=request.user)  # Ensure the todo belongs to the current user

    # Pass the instance (existing object) and the new data
    serializer = TodoSerializer(todos, data=request.data)
    
    if serializer.is_valid():
        serializer.save(author=request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# todo delete 
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def todo_delete(request, pk):
    todos = get_object_or_404(Todo, id=pk, author=request.user)  # Ensure the todo belongs to the current user
    todos.delete()
    return Response({'message': 'Todo deleted successfully!'}, status=status.HTTP_200_OK)