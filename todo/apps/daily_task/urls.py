from django.urls import path

from apps.daily_task.views import TaskView

urlpatterns = [
    path('tasks/', TaskView.as_view(), name='tasks'),
]
