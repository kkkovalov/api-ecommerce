from rest_framework import status, exceptions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, BasePermission

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from webstore.models import Category
from webstore.serializers import CategorySerializer

from webstore.views.schema_responses import category_respones

class CategoryPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        else:
            if request.user.is_authenticated and request.user.is_staff:
                return True
            else:
                return False

class CategoryViews(APIView):
    permission_classes = [CategoryPermission]
    
    
    @swagger_auto_schema(
        operation_description='Returns all categories from the database, no filter',
        operation_id='Get categories',
        responses=category_respones.get_responses
    )
    def get(self, request, *args, **kwargs):
        """Returns all categories from the database in alphabetic order. No body or parameters required.
        
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

        return Response(serializer.data, status=status.HTTP_200_OK)
    
# ------------------------------------------------------------------------------------------------------------------------

    @swagger_auto_schema(
        operation_description='Returns a newly created category if successful, otherwise raises an error.',
        operation_id='Add category. STAFF ONLY.',
        request_body=CategorySerializer,
        responses=category_respones.post_responses
    )    
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
            return Response({'detail': 'Request body is missing information'}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = CategorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(serializer.data, status=status.HTTP_200_OK)

# ------------------------------------------------------------------------------------------------------------------------


class ExistingCategoryView(APIView):
    permission_classes = [CategoryPermission]
    
    @swagger_auto_schema(
        operation_description = 'Returns a category based on '
    )
    def get(self, request, *args, **kwargs):
        pass