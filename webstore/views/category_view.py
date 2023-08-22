from rest_framework import status, exceptions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, BasePermission

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from webstore.models import Category
from webstore.serializers import CategorySerializer

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
    
    @swagger_auto_schema(operation_description='Returns all categories from the database, no filter', operation_id='Get categories', responses={404: "Unable to fetch categories", 200: "OK"})
    def get(self, request, *args, **kwargs):
        """
        Get request will return all categories listed in the database. Names only. No body or parameters required.
        
        Request:
            None
        
        Response:
            status: 200 - OK
            detail: success
            categories: JSON object
        """
        try:
            categories = Category.objects.all()
        except:
            raise exceptions.NotFound
        
        serializer = CategorySerializer(categories, many=True)
        
        context = {
            'detail': 'success',
            'categories': serializer.data,
        }
        return Response(context, status=status.HTTP_200_OK)
    
    category_post_response_schema = {
        status.HTTP_200_OK: openapi.Response(
            description = "Category added to the database",
            schema = CategorySerializer(many=True),
            examples = {
                "application/json": {
                    "detail": "success",
                    "categories": ["list of categories"]
                }
            }
        ),
        status.HTTP_406_NOT_ACCEPTABLE: openapi.Response(
            description = 'denied'
        )
    }
    
    @swagger_auto_schema(operation_description='Returns a newly created category if successful, otherwise raises an error.', operation_id='Add category', request_body=CategorySerializer, responses=category_post_response_schema)
    def post(self, request, *args, **kwargs):
        """Add a new category to the database.

        Request:
            string: name
            string: description
        REQUEST_COOKIES:
            string: access

        Returns:
            _type_: _description_
        """
        try:
            request.data["name"]
            request.data["description"]
        except:
            return Response({'detail': 'Request body is missing information'}, status=status.HTTP_428_PRECONDITION_REQUIRED)
        serializer = CategorySerializer(data=request.data)
        
        serializer.is_valid(raise_exception=True)
        
        serializer.save()

        context = {
            'detail': 'success',
            'category': serializer.data
        }
        return Response(context, status=status.HTTP_200_OK)
    
    def put(self, request, *args, **kwargs):
        pass
    
    def delete(self, request, *args, **kwargs):
        pass