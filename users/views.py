from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from .serializers import UserAccountSerializer


class UserCreateAPIView(CreateAPIView):
    """
    API view to signup.
    """
    serializer_class = UserAccountSerializer


class UserMeAPIView(RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update, or delete a self account.
    """
    serializer_class = UserAccountSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
