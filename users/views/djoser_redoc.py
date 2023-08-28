from djoser.views import UserViewSet as DjoserViewSet
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.decorators import action
from rest_framework import status

class CustomUserViewset(DjoserViewSet):

# ---------------------------------------------------------------------------------------------------------
    @swagger_auto_schema(
        operation_id = "List all users",
        operation_description = 'Use this endpoint to list users.',
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

# ---------------------------------------------------------------------------------------------------------
    @swagger_auto_schema(
        operation_id='Register new user',
        operation_description='Use this endpoint to register new users.',
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

# ---------------------------------------------------------------------------------------------------------
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

# ---------------------------------------------------------------------------------------------------------
    @swagger_auto_schema(
        method='get',
        operation_id = "Get current user",
        operation_description = "Use this endpoint to get current user information.",
    )
    @swagger_auto_schema(
        method='put',
        operation_id = "Update current user",
        operation_description = "Use this endpoint to update current user.",
    )
    @swagger_auto_schema(
        method='patch',
        operation_id = "Partially update current user",
        operation_description = "Use this endpoint to partially update the current user.",
    )
    @swagger_auto_schema(
        method='delete',
        operation_id = "Delete current user",
        operation_description = "Use this endpoint to delete the current user.",
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
        response = super().me(request, *args, **kwargs)
        if request.method == 'DELETE':
            response.delete_cookie('access')
            response.delete_cookie('refresh')
        return response
            
# ---------------------------------------------------------------------------------------------------------
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
    
# ---------------------------------------------------------------------------------------------------------
    @swagger_auto_schema(
        method = 'post',
        operation_id='Reset email confirmation',
        operation_description='Use this endpoint to confirm email reset.',
        request_body = openapi.Schema(
            type = openapi.TYPE_OBJECT,
            description = 'activation request body',
            properties = {
                "uid": openapi.Schema(type=openapi.TYPE_STRING, title="user identifier, usually two letters, first part of url"),
                "token": openapi.Schema(type=openapi.TYPE_STRING, title='token, second part of activation url'),
                'new_email': openapi.Schema(type=openapi.TYPE_STRING, title='new email'),
            },
            required = ['uid', 'token', 'new_email'],
        ),
        responses = {
            status.HTTP_204_NO_CONTENT: openapi.Response(
                description="OK. NO CONTENT."
            ),
            status.HTTP_400_BAD_REQUEST: openapi.Response(
                description='BAD REQUEST',
                schema = openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties = {
                        "uid": openapi.Schema(type=openapi.TYPE_STRING, title="user identifier, usually two letters, first part of url"),
                        "token": openapi.Schema(type=openapi.TYPE_STRING, title='token, second part of activation url'),
                        'new_email': openapi.Schema(type=openapi.TYPE_STRING, title='new email'),
                    },
                )
            )
        }
    )
    @action(methods=['post'], detail=False, url_path='reset_email_confirm')
    def reset_username_confirm(self, request, *args, **kwargs):
        return super().reset_username_confirm(request, *args, **kwargs)

# ---------------------------------------------------------------------------------------------------------
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
    
# ---------------------------------------------------------------------------------------------------------
    @swagger_auto_schema(
        operation_id = 'Reset password confirmation',
        operation_description = 'Use this endpoint to confirm password reset.',
        responses = {
            status.HTTP_204_NO_CONTENT: openapi.Response(
                description = 'OK. NO CONTENT.'
            ),
            status.HTTP_400_BAD_REQUEST: openapi.Response(
                description = "BAD REQUEST.",
            ),
        }
    )
    @action(methods=['post'], detail=False)
    def reset_password_confirm(self, request, *args, **kwargs):
        return super().reset_password_confirm(request, *args, **kwargs)

# ---------------------------------------------------------------------------------------------------------
    @swagger_auto_schema(
        method = 'post',
        operation_id = "Reset email",
        operation_description = 'Use this endpoint to reset users email. \n Client will receive a "reset_email/{uid}/{token}/" email by pressing it they should be redirected to your front-end page, which makes a "POST" request to confirm email reset.',
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
    @action(methods=['post'], detail=False, url_path='reset_email')
    def reset_username(self, request, *args, **kwargs):
        return super().reset_username(request, *args, **kwargs)

# ---------------------------------------------------------------------------------------------------------
    @swagger_auto_schema(
        operation_id='Set new email',
        operation_description = 'Use this endpoint to set new password for the user',
        responses = {
            status.HTTP_204_NO_CONTENT: openapi.Response(
                description = 'OK. NO CONTENT.'
            ),
            status.HTTP_400_BAD_REQUEST: openapi.Response(
                description = "BAD REQUEST.",
            ),
        }
    )
    @action(methods=['post'], detail=False, url_path='set_email')
    def set_username(self, request, *args, **kwargs):
        return super().set_username(request, *args, **kwargs)

# ---------------------------------------------------------------------------------------------------------
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

# ---------------------------------------------------------------------------------------------------------
    @swagger_auto_schema(
        operation_id="Get user by {id}",
        operation_description='Use this endpoint to return a specific user.',
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
# ---------------------------------------------------------------------------------------------------------
    @swagger_auto_schema(
        operation_id='Partial user update by {id}',
        operation_description='Use this endpoint to partially update a user.',
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

# ---------------------------------------------------------------------------------------------------------
    @swagger_auto_schema(
        operation_id='Update user by {id}',
        operation_description='Use this endpoint to update the user as a whole.',
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

# ---------------------------------------------------------------------------------------------------------
    @swagger_auto_schema(
        operation_id='Delete user by {id}',
        operation_description='Use this endpoint to delete a user.',
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)