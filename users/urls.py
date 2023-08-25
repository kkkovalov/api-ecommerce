from users.views import (
    CustomTokenObtainPairView,
    CustomTokenVerifyView,
    CustomTokenRefreshView,
    LogoutView,
    CustomProviderAuthView,
)
from django.urls import path, re_path

urlpatterns = [
    path('jwt/create/', CustomTokenObtainPairView.as_view(), name='login-view'),
    path('jwt/refresh/', CustomTokenRefreshView.as_view()),
    path('jwt/verify/', CustomTokenVerifyView.as_view()),
    path('logout/', LogoutView.as_view()),
    re_path(r'^o/(?P<provider>\S+)/$', CustomProviderAuthView.as_view(), name='Provider Auth'),
]
