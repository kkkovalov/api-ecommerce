from django.conf import settings


from rest_framework import status, serializers
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

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