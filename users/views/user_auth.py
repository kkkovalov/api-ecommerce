from django.conf import settings


from rest_framework import status, serializers
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from djoser.social.views import ProviderAuthView

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema


class TokenObtainPairResponseSerializer(serializers.Serializer):
    refresh = serializers.CharField()
    access = serializers.CharField()
    
    def create(self, validated_data):
        raise NotImplementedError()

    def update(self, instance, validated_data):
        raise NotImplementedError()


class CustomTokenObtainPairView(TokenObtainPairView):
    
    @swagger_auto_schema(
    operation_description  = "Login authentication method using JWToken",
    operation_id = "Login",
    responses= {
        status.HTTP_200_OK: openapi.Response(
            description = "OK",
            schema=TokenObtainPairResponseSerializer,
        ),
        status.HTTP_401_UNAUTHORIZED: openapi.Response(
            description = "Invalid credentials",
            schema = openapi.Schema(
                type = openapi.TYPE_OBJECT,
                properties = {
                    "detail": openapi.Schema(type=openapi.TYPE_STRING),
                },
                description = "No active account found with the given credentials",
            )
        )
        }
    )
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        
        if response.status_code >= 200:
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


class TokenRefreshResponseSerializer(serializers.Serializer):
    access = serializers.CharField()

    def create(self, validated_data):
        raise NotImplementedError()

    def update(self, instance, validated_data):
        raise NotImplementedError()


class CustomTokenRefreshView(TokenRefreshView):
    
    @swagger_auto_schema(
        operation_id = "Refresh JWT",
        operation_description = "Refresh Access JWToken using refresh token specified in either HTTP cookie or body.",
        responses = {
            status.HTTP_200_OK: openapi.Response(
                description = "OK",
                schema=TokenRefreshResponseSerializer,
            )
        }
    )
    def post(self, request, *args, **kwargs):        
        refresh_token = request.COOKIES.get('refresh')
        
        if refresh_token:
            request.data['refresh'] = refresh_token
            
        
        response = super().post(request, *args, **kwargs)
        
        if response.status_code >= 200:
            access_token = response.data.get('access')
            
            response.set_cookie(
                'access', access_token,
                max_age=settings.AUTH_COOKIE_ACCESS_MAX_AGE,
                path=settings.AUTH_COOKIE_PATH,
                secure = settings.AUTH_COOKIE_SECURE,
                httponly=settings.AUTH_COOKIE_HTTP_ONLY,
                samesite=settings.AUTH_COOKIE_SAMESITE,
            )
        
        return response
    
class CustomTokenVerifyView(TokenVerifyView):
    
    @swagger_auto_schema(
        operation_id = "Verify JWT",
        operation_description = "Verifies that current access token is valid",
        responses = {
            status.HTTP_200_OK: openapi.Response(
                description = "OK",
            )
        }
    )
    def post(self, request, *args, **kwargs):
        access_token = request.COOKIES.get('access')
        
        if access_token:
            request.data['token'] = access_token
        
        return super().post(request, *args, **kwargs)
    
    
class LogoutView(APIView):
    @swagger_auto_schema(
        operation_id = "Logout",
        operation_description = "Logout user by deleting the HTTP response cookie.",
        responses = {
            status.HTTP_204_NO_CONTENT: openapi.Response(
                description = "OK. NO CONTENT.",
            )
        }
    )
    def post(self, request, *args, **kwargs):
        response = Response(status=status.HTTP_204_NO_CONTENT)
        response.delete_cookie('access')
        response.delete_cookie('refresh')
        
        return response
    

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