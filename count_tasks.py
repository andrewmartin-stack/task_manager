from task_manager.models import Task

outstanding_tasks = Task.objects.count()
print(outstanding_tasks)