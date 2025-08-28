from django.shortcuts import get_object_or_404
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from .models import Category, Comment, Post
from .permissions import (
    IsAdminOrReadOnly,
    IsOwnerOrAdminDeleteOnly,
    IsOwnerOrReadOnly
)
from .serializers import (
    CategorySerializer,
    CommentSerializer,
    PostSerializer
)


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


class CommentListCreateAPIView(ListCreateAPIView):
    """
    API view to list all comments on a post or create a new comment.
    """
    queryset = Comment.objects.select_related('user')
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        """
        Filter comments associated with a given post id.
        """
        post_id = self.kwargs.get('post_id')
        return self.queryset.filter(post=post_id)

    def perform_create(self, serializer):
        post_id = self.kwargs.get('post_id')
        post = get_object_or_404(Post, id=post_id)
        return serializer.save(user=self.request.user, post=post)


class CommentDetailAPIView(RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update, or delete a specific comment.
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def get_object(self):
        """
        Retrieve and return a specific comment belonging to a given post.
        Look up the comment by its ID and the associated post ID from the URL,
        ensure it exists, and check object-level permissions before
        returning.
        """
        queryset = self.get_queryset()
        post_id = self.kwargs.get('post_id')
        comment_id = self.kwargs.get('comment_id')
        comment = get_object_or_404(queryset, id=comment_id, post=post_id)
        self.check_object_permissions(self.request, comment)
        return comment
