from rest_framework.permissions import BasePermission

# Permission to allow any client 'GET' requests, but decline all others unless is_staff and is_authenticated
class AdminPermission(BasePermission):
    
    def has_permission(self, request, view):
        if request.method == 'GET' or (request.user.is_authenticated and request.user.is_staff):
            return True
        else:
            return False