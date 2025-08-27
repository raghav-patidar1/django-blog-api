from rest_framework import routers

from . import views

router = routers.SimpleRouter()
router.register(r'categories', views.CategoryViewSet, basename='category')
router.register(r'posts', views.PostViewSet, basename='post')
urlpatterns = router.urls
