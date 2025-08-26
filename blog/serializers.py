from rest_framework import serializers

from .models import Category, Post


class CategorySerializer(serializers.ModelSerializer):
    """
    Serializer for blog category objects.
    """
    class Meta:
        model = Category
        fields = ('id', 'title', 'slug')


class PostSerializer(serializers.ModelSerializer):
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

    def get_published_date(self, obj):
        return obj.created_at.date()

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
