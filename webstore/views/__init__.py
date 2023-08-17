from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView

class HomeView(APIView):
    authentication_classes = []
    permission_classes = []
    
    def get(self, request, *args, **kwargs):
        return HttpResponse('Welcome to the website.')