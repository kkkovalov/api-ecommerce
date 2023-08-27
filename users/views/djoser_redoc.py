from djoser.views import UserViewSet as DjoserViewSet
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.decorators import action
from rest_framework import status

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
    
    
    @swagger_auto_schema(
        method = "post",
        operation_id = "Activate user",
        operation_description = "Use this endpoint to activate users after registering.",
        request_body = openapi.Schema(
            type = openapi.TYPE_OBJECT,
            description = 'activation request body',
            properties = {
                "uid": openapi.Schema(type=openapi.TYPE_STRING, title="user identifier, usually two letters, first part of url"),
                "token": openapi.Schema(type=openapi.TYPE_STRING, title='token, second part of activation url')
            },
            required = ['uid', 'token'],
        ),
        responses = {
            status.HTTP_204_NO_CONTENT: openapi.Response(
                description = "OK. NO CONTENT."
            ),
            status.HTTP_403_FORBIDDEN: openapi.Response(
                description="USER IS ACTIVE.",
            ),
        }
    )
    @action(['post'], detail=False)
    def activation(self, request, *args, **kwargs):
        return super().activation(request, *args, **kwargs)
    
    @swagger_auto_schema(
        method = 'post',
        operation_id = "Resend activation email",
        operation_description = "Use this endpoint to resend activation email.",
        request_body = openapi.Schema(
            type = openapi.TYPE_OBJECT,
            description = 'email',
            properties = {
                "email": openapi.Schema(type=openapi.TYPE_STRING),
            },
            required = ['email']
        ),
        responses = {
            status.HTTP_204_NO_CONTENT: openapi.Response(
                description = "OK. NO CONTENT.",
            ),
            status.HTTP_400_BAD_REQUEST: openapi.Response(
                description = "USER IS ACTIVE."
            ),
        }
    )
    @action(methods=["post"], detail=False)
    def resend_activation(self, request, *args, **kwargs):
        return super().resend_activation(request, *args, **kwargs)
    
    @swagger_auto_schema(
        method = 'post',
        operation_id = "Reset email",
        operation_description = "Use this endpoint to reset users email.",
        reques_body = openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties = {
                'email': openapi.Schema(type=openapi.TYPE_STRING),
            }
        ),
        responses = {
            status.HTTP_204_NO_CONTENT: openapi.Response(
                description = 'OK. NO CONTENT.',
            ),
            status.HTTP_400_BAD_REQUEST: openapi.Response(
                description = "EMAIL IS NOT IN THE DATABASE.",
                schema = openapi.Schema(
                    type = openapi.TYPE_OBJECT,
                    properties = {
                        'email': openapi.Schema(type=openapi.TYPE_STRING),
                    },
                )
            )
        }
    )
    @action(methods=['post'], detail=False)
    def reset_username(self, request, *args, **kwargs):
        return super().reset_username(request, *args, **kwargs)

    
    @swagger_auto_schema(
        method = 'post',
        operation_id = 'Set new password',
        operation_description = "Use this endpoint to set new password for the user.",
        request_body = openapi.Schema(
            type = openapi.TYPE_OBJECT,
            properties = {
                "current_password": openapi.Schema(type = openapi.TYPE_STRING),
                "new_password": openapi.Schema(type = openapi.TYPE_STRING),
                "re_new_password": openapi.Schema(type = openapi.TYPE_STRING),
            },
            required = ['current_password', 're_new_password', 'new_password'],
        ),
        responses = {
            status.HTTP_204_NO_CONTENT: openapi.Response(
                description = 'OK. NO CONTENT.'
            ),
            status.HTTP_400_BAD_REQUEST: openapi.Response(
                description = "BAD REQUEST",
                schema = openapi.Schema(
                    type = openapi.TYPE_OBJECT,
                    properties = {
                        "current_password": openapi.Schema(type = openapi.TYPE_STRING),
                        "new_password": openapi.Schema(type = openapi.TYPE_STRING),
                        "re_new_password": openapi.Schema(type = openapi.TYPE_STRING),
                    }
                )
            )
        }
    )
    @action(methods=['post'], detail=False)
    def set_password(self, request, *args, **kwargs):
        return super().set_password(request, *args, **kwargs)    
    
    
    
    @swagger_auto_schema(
        method = 'post',
        operation_id = "Reset password",
        operation_description = "Use this endpoint to reset current password. Email will be sent to client's email.",
        request_body = openapi.Schema(
            type = openapi.TYPE_OBJECT,
            properties = {
                "email": openapi.Schema(type=openapi.TYPE_STRING)
            },
            required = ['email'],
        ),
        responses = {
            status.HTTP_204_NO_CONTENT: openapi.Response(
                description = "OK. NO CONTENT.",
            ),
            status.HTTP_400_BAD_REQUEST: openapi.Response(
                description = "BAD REQUEST.",
            ),
        }
    )
    @action(methods = ['post'], detail=False)
    def reset_password(self, request, *args, **kwargs):
        return super().reset_password(request, *args, **kwargs)