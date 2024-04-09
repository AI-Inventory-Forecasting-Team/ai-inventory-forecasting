from django.urls import path
from django.urls.conf import include
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostDeleteView,
    PostUpdateView,
    CategoryListView,
    LikeCreateView,
    LikeDestroyView,
)

urlpatterns = [
    path("list/", PostListView.as_view(), name="post_list"), # 게시물 리스트
    path('categories/', CategoryListView.as_view(), name='category-list-create'), # 카테고리 리스트
    path("create/", PostCreateView.as_view(), name="post_create"), # 게시물 생성
    path("<int:pk>/", PostDetailView.as_view(), name="post_detail"), # 게시물 상세보기
    path("<int:pk>/delete/", PostDeleteView.as_view(), name="post_delete"), # 게시물 삭제
    path("<int:pk>/update/", PostUpdateView.as_view(), name="post_update"), # 게시물 수정
    path("<int:pk>/like/", LikeCreateView.as_view(), name="like-create"), # 좋아요 생성
    path("<int:pk>/unlike/", LikeDestroyView.as_view(), name="like-delete"), # 좋아요 삭제
    path('<int:post_id>/comments/', include('comments.urls')), # 댓글 리스트, 생성
]