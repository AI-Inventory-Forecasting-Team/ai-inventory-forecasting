import django_filters
from .models import Post

class PostFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    author = django_filters.CharFilter(field_name='author__username', lookup_expr='icontains')  # author 필드 수정
    category = django_filters.CharFilter(field_name='category__name', lookup_expr='icontains')  # category 필드 수정

    class Meta:
        model = Post
        fields = ['title', 'author', 'category']
