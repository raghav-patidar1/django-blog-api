from django.contrib.auth import get_user_model
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated

from .serializers import UserAccountSerializer

User = get_user_model()


class UserCreateAPIView(ListCreateAPIView):
    """
    API view to signup and list users (admin only).
    """
    queryset = User.objects.all()
    serializer_class = UserAccountSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            return [AllowAny()]
        else:
            return [IsAdminUser()]


class UserMeAPIView(RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update, or delete a self account.
    """
    serializer_class = UserAccountSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
