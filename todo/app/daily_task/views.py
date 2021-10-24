from django.http import JsonResponse
from drf_yasg.utils import swagger_auto_schema
from rest_framework import views
from rest_framework.response import Response

from app.daily_task.models import create_task, get_task_list
from app.daily_task.serializer import TaskSerializer


class TaskView(views.APIView):
    @swagger_auto_schema(query_serializer=TaskSerializer)
    def get(self, *args, **kwargs):
        task_list = get_task_list()
        serialized_products = TaskSerializer(task_list, context={'request': self.request})
        return Response(serialized_products.data)

    @swagger_auto_schema(request_body=TaskSerializer)
    def post(self, request, *args, **kwargs):
        serialized_data = TaskSerializer(data=self.request.data)
        serialized_data.is_valid(raise_exception=True)
        task = serialized_data.validated_data
        task = create_task(task['task'], task['description'], task['date'])

        return JsonResponse(status=200, data={'message': 'successfully created.'})
