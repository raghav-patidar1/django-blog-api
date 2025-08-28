from django.urls import path
from rest_framework import routers

from . import views

router = routers.SimpleRouter()
router.register(r'categories', views.CategoryViewSet, basename='category')
router.register(r'posts', views.PostViewSet, basename='post')
urlpatterns = router.urls

urlpatterns += [
    path(
        'posts/<int:post_id>/comments/',
        views.CommentListCreateAPIView.as_view(),
        name='comment-list-create'
    ),
    path(
        'posts/<int:post_id>/comments/<int:comment_id>',
        views.CommentDetailAPIView.as_view(),
        name='comment-detail'
    ),
]
