from django.conf import settings

from rest_framework import status
from djoser.social.views import ProviderAuthView

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema


class CustomProviderAuthView(ProviderAuthView):
    
    @swagger_auto_schema(
        operation_id = "OAuth - authentication",
        operation_description = "Using these endpoints you can authenticate with external tools. See https://djoser.readthedocs.io/en/latest/social_endpoints.html for more information.",
        manual_parameters = [
            openapi.Parameter(name='provider', required=True, type=openapi.TYPE_STRING, in_=openapi.IN_PATH, description="Only 'facebook' and 'google-ouath2' are supported'"),
            openapi.Parameter(name='redirect_uri', required=True, type=openapi.TYPE_STRING, in_=openapi.IN_QUERY, description="Redirect URL after client completes OAuth."),
            ],
        responses = {
            status.HTTP_200_OK: openapi.Response(
                description = "OK",
                schema = openapi.Schema(
                    type = openapi.TYPE_OBJECT,
                    properties = {
                        "authorization_url": openapi.Schema(type=openapi.TYPE_STRING, description="Redirect client to this url to authenticate."),
                    }
                )
            )
        }
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_id = "OAuth - login",
        operation_description = "OAuth login endpoint for registering with Facebook or Google. After client authenticates pass 'code' and 'state' values in body.",
        request_body = None,
        manual_parameters = [
            openapi.Parameter(
                name = 'state',
                required = True,
                in_ = openapi.IN_QUERY,
                type = openapi.TYPE_STRING,
            ),
            openapi.Parameter(
                name = 'code',
                required = True,
                in_ = openapi.IN_QUERY,
                type = openapi.TYPE_STRING,
            ),
        ],
        responses = {
            status.HTTP_201_CREATED: openapi.Response(
                description = "USER CREATED",
                schema = openapi.Schema(
                    type = openapi.TYPE_OBJECT,
                    properties = {
                        "access": openapi.Schema(type=openapi.TYPE_STRING, title='Access token'),
                        "refresh": openapi.Schema(type=openapi.TYPE_STRING, title='Refresh token'),
                        "user": openapi.Schema(type=openapi.TYPE_STRING, title='User email'),
                    }
                )
            )
        }
    )
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        
        if response.status_code >= 201:
            access_token = response.data.get('access')
            refresh_token = response.data.get('refresh')
            response.set_cookie(
                'access', access_token,
                max_age=settings.AUTH_COOKIE_ACCESS_MAX_AGE,
                path=settings.AUTH_COOKIE_PATH,
                secure = settings.AUTH_COOKIE_SECURE,
                httponly=settings.AUTH_COOKIE_HTTP_ONLY,
                samesite=settings.AUTH_COOKIE_SAMESITE,
            )
            
            response.set_cookie(
                'refresh',refresh_token,
                max_age=settings.AUTH_COOKIE_REFRESH_MAX_AGE,
                path=settings.AUTH_COOKIE_PATH,
                secure = settings.AUTH_COOKIE_SECURE,
                httponly=settings.AUTH_COOKIE_HTTP_ONLY,
                samesite=settings.AUTH_COOKIE_SAMESITE,
            )
            
        return response