from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from .models import Category, Post
from .permissions import IsAdminOrReadOnly, IsOwnerOrAdminDeleteOnly
from .serializers import CategorySerializer, PostSerializer


class CategoryViewSet(ModelViewSet):
    """
    ViewSet for creating, listing, updating, and deleting blog categories.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]


class PostViewSet(ModelViewSet):
    """
    ViewSet for creating, listing, updating, and deleting blog posts.
    """
    queryset = Post.objects.select_related('user', 'category')
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrAdminDeleteOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)
