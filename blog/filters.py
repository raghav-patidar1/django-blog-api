import django_filters

from .models import Post


class PostFilter(django_filters.FilterSet):
    """
    Custom filters for Post queryset.

    Supports:
    - Searching by matching substring on title and content.
    - Filtering by author (case-insensitive).
    - Year and month lookup on created_at.
    """
    title = django_filters.CharFilter(
        field_name="title",
        lookup_expr="icontains"
    )
    content = django_filters.CharFilter(
        field_name="content",
        lookup_expr="icontains"
    )
    year = django_filters.NumberFilter(
        field_name="created_at",
        lookup_expr="year"
    )
    month = django_filters.NumberFilter(
        field_name="created_at",
        lookup_expr="month"
    )
    author = django_filters.CharFilter(
        field_name='user__username',
        lookup_expr="icontains"
    )

    class Meta:
        model = Post
        fields = ['author', 'title', 'content']
