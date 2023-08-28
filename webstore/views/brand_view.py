from rest_framework.views import APIView
from webstore.permissions import AdminPermission


class BrandView(APIView):
    permission_classes = [AdminPermission]
    
    def get(self, request, *args, **kwargs):
        pass
    
    def post(self, request, *args, **kwargs):
        pass
    
    def put(self, request, *args, **kwargs):
        pass
    
    def delete(self, request, *args, **kwargs):
        pass
    