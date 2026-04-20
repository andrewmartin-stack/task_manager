from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .api import TaskViewSet
from .views import task_count

router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/task_count/', task_count, name='task_count')
]