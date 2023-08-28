from users.views import (
    CustomTokenObtainPairView,
    CustomTokenVerifyView,
    CustomTokenRefreshView,
    LogoutView,
    CustomUserViewset,
)
from django.urls import path, re_path, include

from django.contrib.auth import get_user_model
from rest_framework.routers import DefaultRouter

from djoser import views

router = DefaultRouter()
router.register("users", CustomUserViewset)
User = get_user_model()

urlpatterns = [
    # redoc documentation add
    path('jwt/create/', CustomTokenObtainPairView.as_view(), name='login-view'),
    path('jwt/refresh/', CustomTokenRefreshView.as_view()),
    path('jwt/verify/', CustomTokenVerifyView.as_view()),
    path('logout/', LogoutView.as_view()),
] + router.urls
