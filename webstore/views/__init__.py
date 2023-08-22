#package
from .category_view import CategoryViews

from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView

from drf_yasg.utils import swagger_auto_schema

class HomeView(APIView):
    authentication_classes = []
    permission_classes = []
    
    @swagger_auto_schema(operation_description='Welcome page for all views', operation_id='Welcome', request_body=None, )
    def get(self, request, *args, **kwargs):
        return HttpResponse('Welcome to the website.')