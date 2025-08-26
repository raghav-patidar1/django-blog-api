from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path('', views.UserCreateAPIView.as_view(), name='user-create'),
    path('me/', views.UserMeAPIView.as_view(), name='user-me')
]
