from rest_framework import status, exceptions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework_simplejwt.authentication import JWTAuthentication

from webstore.models import Category

class CategoryPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        else:
            if request.user.is_authenticated:
                return True
            else:
                return False

class CategoryViews(APIView):
    permission_classes = [CategoryPermission]
        
    def get(self, request, *args, **kwargs):
        try:
            categories = Category.objects.all()
        except:
            raise exceptions.NotFound
        
        context = {
            'detail': 'success',
            'categories': categories,
        }
        return Response(context, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        access_token = request.COOKIES.get('access')
        
        if access_token:
            request.data['token'] = access_token        
    
        context = {
            'detail': 'success',
        }
        return Response(context, status=status.HTTP_200_OK)