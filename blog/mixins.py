from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.exceptions import ValidationError
from rest_framework.filters import OrderingFilter, SearchFilter

from .filters import PostFilter


class CaseInsensitiveUniqueMixin:
    """
    Mixin to enforce case-insensitive uniqueness
    on `title` and `slug` fields.
    """

    def validate(self, data):
        """
        - Prevent duplicates for `title` and `slug` (ignoring case).
        - Handle both create and update by excluding self.instance.
        """
        title = data.get("title")
        slug = data.get("slug")

        qs = self.Meta.model.objects.filter(
            Q(title__iexact=title) | Q(slug__iexact=slug)
        )

        # Exclude current instance during update, otherwise it
        # would always match itself and raise a false duplicate error
        if self.instance:
            qs = qs.exclude(id=self.instance.id)

        if qs.exists():
            if qs.filter(title__iexact=title).exists():
                raise ValidationError(
                    {
                        "title": (
                            f"{self.Meta.model.__name__}"
                            " with this title already exists."
                        )
                    }
                )
            if qs.filter(slug__iexact=slug).exists():
                raise ValidationError(
                    {
                        "slug": (
                            f"{self.Meta.model.__name__}"
                            " with this slug already exists."
                        )
                    }
                )
        return data


class PostFilterMixin:
    """
    Mixin for Post views providing filtering, search, and ordering.

    Includes:
    - Field-based filters from PostFilter.
    - Search on title and content.
    - Ordering by created_at and title.
    """
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = PostFilter
    search_fields = ['title', 'content']
    ordering_fields = ['created_at', 'title']
