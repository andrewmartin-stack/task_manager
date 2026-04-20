import os
import django
from task_manager.models import Task

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'task_manager.settings')
django.setup()

outstanding_tasks = Task.objects.count()
print(outstanding_tasks)