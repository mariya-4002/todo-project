from django.http import JsonResponse
from .models import Todo

# Get all todos
def get_all_todos(request):
    todos = list(Todo.objects.values())
    return JsonResponse(todos, safe=False)

# Get single todo by id
def get_todo(request, id):
    try:
        todo = Todo.objects.get(id=id)
        return JsonResponse({
            "id": todo.id,
            "title": todo.title,
            "description": todo.description
        })
    except Todo.DoesNotExist:
        return JsonResponse({"error": "Todo not found"}, status=404)

# Create todo
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def add_todo(request):
    data = json.loads(request.body)
    todo = Todo.objects.create(
        title=data["title"],
        description=data["description"]
    )
    return JsonResponse({"message": "Todo added", "id": todo.id})

# Update todo
@csrf_exempt
def update_todo(request, id):
    data = json.loads(request.body)
    try:
        todo = Todo.objects.get(id=id)
        todo.title = data["title"]
        todo.description = data["description"]
        todo.save()
        return JsonResponse({"message": "Todo updated"})
    except Todo.DoesNotExist:
        return JsonResponse({"error": "Todo not found"}, status=404)

# Delete todo
@csrf_exempt
def delete_todo(request, id):
    try:
        todo = Todo.objects.get(id=id)
        todo.delete()
        return JsonResponse({"message": "Todo deleted"})
    except Todo.DoesNotExist:
        return JsonResponse({"error": "Todo not found"}, status=404)
