from rest_framework.pagination import PageNumberPagination


class PostPagination(PageNumberPagination):
    """
    Pagination for blog posts.
    """
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 20


class CommentPagination(PageNumberPagination):
    """
    Pagination for comments on a blog post.
    """
    page_size = 25
    page_size_query_param = 'page_size'
    max_page_size = 50
