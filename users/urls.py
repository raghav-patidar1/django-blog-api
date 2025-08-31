from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

from . import views

app_name = 'users'

urlpatterns = [
    path('', views.UserCreateAPIView.as_view(), name='user-list-create'),
    path('me/', views.UserMeAPIView.as_view(), name='user-me'),
    path(
        'token/',
        TokenObtainPairView.as_view(),
        name='token_obtain_pair'
    ),
    path(
        'token/refresh/',
        TokenRefreshView.as_view(),
        name='token_refresh'
    ),
]
