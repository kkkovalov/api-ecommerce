from rest_framework import exceptions, status 
from rest_framework.views import APIView
from rest_framework.response import Response


from webstore.models import Brand
from webstore.serializers import BrandSerializer
from webstore.permissions import AdminPermission



class BrandView(APIView):
    permission_classes = [AdminPermission]
    
    def get(self, request, *args, **kwargs):
        try:
            brands = Brand.objects.all()
        except:
            raise exceptions.NotFound
        
        serializer = BrandSerializer(brands, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    def post(self, request, *args, **kwargs):
        pass
    
    def put(self, request, *args, **kwargs):
        pass
    
    def delete(self, request, *args, **kwargs):
        pass
    