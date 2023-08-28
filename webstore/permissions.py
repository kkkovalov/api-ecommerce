from rest_framework.permissions import BasePermission

class AdminPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        else:
            if request.user.is_authenticated and request.user.is_staff:
                return True
            else:
                return False