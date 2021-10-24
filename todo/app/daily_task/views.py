from drf_yasg.utils import swagger_auto_schema
from rest_framework import views
from app.daily_task.serializer import TaskSerializer


class HomePageView(views.APIView):
    #     # @swagger_auto_schema(query_serializer=SimpleScrappingQuerySerializer)
    #     # def get(self, *args, **kwargs):
    #     #     api_request_id = self.request.query_params.get('api_request_id')
    #     #     task_id = self.request.query_params.get('task_id')
    #     #     task = AsyncResult(task_id, app=app)
    #     #     if task.state == 'SUCCESS':
    #     #         products = Basicproduct.objects.filter(api_request_id=api_request_id)
    #     #         data = {
    #     #             'message': task.state,
    #     #             'products': products
    #     #         }
    #     #     else:
    #     #         data = {
    #     #             'message': task.state,
    #     #             'products': []
    #     #         }
    #     #
    #     #     serialized_products = SimpleScrappingListSerializer(data, context={'request': self.request})
    #     #     return Response(serialized_products.data)
    #     #
    #     # def get_risky_sellers_list(self, search_platform):
    #     #     try:
    #     #         black_list_sellers = RiskySeller.objects.get(user=self.request.user,
    #     #                                                      platform__name=search_platform).risky_sellers_list
    #     #     except RiskySeller.DoesNotExist:
    #     #         black_list_sellers = []
    #     #
    #     #     return black_list_sellers
    #

    @swagger_auto_schema(request_body=TaskSerializer)
    def post(self, request, *args, **kwargs):
        serialized_data = TaskSerializer(data=self.request.data)
        serialized_data.is_valid(raise_exception=True)
        task = serialized_data.validated_data
        task = create_task(task['task'], task['description'], task['date'])

        return JsonResponse(status=200,
                            data={'message': 'success', 'api_request_id': api_request_id, 'task_id': task.id})
