from django.conf import settings
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from djoser.social.views import ProviderAuthView

from drf_yasg.utils import swagger_auto_schema
