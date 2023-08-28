from django.contrib import admin
from django.urls import path, include, re_path
from django.shortcuts import redirect
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from .views import index

schema_view = get_schema_view(
    openapi.Info(
        title='Ecommerce API',
        default_version='v1.0.0',
        description='Ecommerce API features a default product/category, user and basket models to accomodate any ecommerce website',
        terms_of_service='https://www.google.com/policies/terms/',
        contact=openapi.Contact(email='vladyslav.kovalovs@gmail.com'),
        license=openapi.License(name='MIT License'),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', index, name='index-view'),
    
    path('webstore/', include('webstore.urls'), name='webstore-page'),
    
    # Docs config
    # path('swagget<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    # path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('docs/', schema_view.with_ui('redoc', cache_timeout=0,), name='schema-redoc'),
    
    #Djoser & JWT Auth
    path("api/", include("djoser.urls")),
    path("api/", include("users.urls"), name='API-endpoint'),
    path('auth/', include('users.social.urls'), name='OAuth-endpoint'),
]