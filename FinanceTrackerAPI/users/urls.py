from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenBlacklistView,
    TokenRefreshView,
    TokenVerifyView
)
from .views import CustomUserViewSet


urlpatterns = [
    path('register/', CustomUserViewSet.as_view({'post':'create'}), name='auth_register'),
    path('login/', TokenObtainPairView.as_view(), name='auth_login'),
    path('logout/', TokenBlacklistView.as_view(), name='auth_logout'),

    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify')
]