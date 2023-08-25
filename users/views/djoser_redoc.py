from djoser.views import UserViewSet as DjoserViewSet
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.decorators import action

class CustomUserViewset(DjoserViewSet):
    
    @swagger_auto_schema(
        method='get',
        operation_id = "Get user info",
        operation_description = "Returns current user information based on passed JWToken",
    )
    @swagger_auto_schema(
        method='put',
        operation_id = "Update user - full",
        operation_description = "Requires an email to update and any other required fields. Returns current user information based on passed JWToken. ",
    )
    @swagger_auto_schema(
        method='patch',
        operation_id = "Update user - partial",
        operation_description = "Requires any fields that exists in the user. Returns current user information based on passed JWToken",
    )
    @swagger_auto_schema(
        method='delete',
        operation_id = "Delete user",
        operation_description = "Returns 204_NO_CONTENT when successfull. Otherwise 400_BAD_REQUEST",
        request_body = openapi.Schema(
            type = openapi.TYPE_OBJECT,
            properties = {
                "current_password": openapi.Schema(type=openapi.TYPE_STRING)
            },
            description = "Pass current password to validate user deletion",
            required = ['current_password']
        ),
    )
    @action(["get", "put", "patch", "delete"], detail=False)
    def me(self, request, *args, **kwargs):
        return super().me(request, *args, **kwargs)