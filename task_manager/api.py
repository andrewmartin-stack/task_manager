from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    http_method_names = ['get', 'post', 'patch', 'put', 'delete']
    queryset = Task.objects.all()
    serializer_class = TaskSerializer