from django.http import JsonResponse
from .models import Task

def task_count(request):
    count = Task.objects.count()
    return JsonResponse({"outstanding_tasks": count})