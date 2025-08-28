from drf_spectacular.utils import extend_schema_field
from rest_framework import serializers

from .mixins import CaseInsensitiveUniqueMixin
from .models import Category, Comment, Post


class CategorySerializer(
    CaseInsensitiveUniqueMixin,
    serializers.ModelSerializer
):
    """
    Serializer for blog category objects.
    """
    class Meta:
        model = Category
        fields = ('id', 'title', 'slug')


class PostSerializer(CaseInsensitiveUniqueMixin, serializers.ModelSerializer):
    """
    Serializer for blog posts, including author and category info.
    """
    author = serializers.CharField(source='user.username', read_only=True)
    category_title = serializers.CharField(
        source='category.title',
        read_only=True
    )
    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        write_only=True
    )
    published_date = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = (
            'id',
            'author',
            'category_title',
            'category',
            'title',
            'slug',
            'content',
            'image_url',
            'published_date',
        )

    @extend_schema_field(serializers.DateField())
    def get_published_date(self, obj):
        return obj.created_at.date()


class CommentSerializer(serializers.ModelSerializer):
    """
    Serializer for comments, including related user.
    """
    user = serializers.CharField(source='user.username', read_only=True)
    comment_date = serializers.SerializerMethodField()

    @extend_schema_field(serializers.DateField())
    def get_comment_date(self, obj):
        return obj.created_at.date()

    class Meta:
        model = Comment
        fields = ('id', 'user', 'comment_text', 'comment_date')
