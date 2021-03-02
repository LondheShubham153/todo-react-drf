from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Task
# Create your views here.

@api_view(['GET'])
def api_details(request):
    api_endpoints = {
        "api_version" : "v1",
        "get all tasks" : "/task-list/",
        "Create task" : "/task-create/",
        "Read task" : "/task/<int:pk>/",
        "Update task" : "/task-update/<int:pk>/",
        "Delete task" : "/task-delete/<int:pk>/",
    }
    return Response(api_endpoints)

@api_view(['GET'])
def get_all_tasks(request):
    tasks = Task.objects.all()
    task_list= []

    for task in tasks:
        result = {
            "pk":task.pk,
            "title":task.title,
            "completed":task.completed
        }
        task_list.append(result)
    
    return Response(task_list)

@api_view(['GET'])
def get_task(request,pk):
    try:
        task = Task.objects.get(pk=pk)
    except:
        return Response({"message":"Task does not exist"},status=404)

    result = {
        "pk":task.pk,
        "title":task.title,
        "completed":task.completed
    }
    return Response(result)

@api_view(['POST'])
def create_task(request):
    title = request.data['title']

    task = Task.objects.create(title=title)
    task.save()
    return Response({"message":"Task inserted successfully"})

@api_view(['PUT'])
def update_task(request,pk):
    title = request.data['title']
    completed = request.data['completed']

    task = Task.objects.get(pk=pk)
    task.title = title
    task.completed = completed
    task.save()
    return Response({"message":"Task updated successfully"})

@api_view(['DELETE'])
def delete_task(request,pk):
    task = Task.objects.filter(pk=pk).delete()
    return Response({"message":"Task deleted successfully"})

