from django.urls import path
from django.urls.conf import include
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostDeleteView,
    PostUpdateView,
    LikeView,
)

urlpatterns = [
    path("list/", PostListView.as_view(), name="post_list"), # 게시물 리스트
    path("create/", PostCreateView.as_view(), name="post_create"), # 게시물 생성
    path("<int:pk>/", PostDetailView.as_view(), name="post_detail"), # 게시물 상세보기
    path("<int:pk>/delete/", PostDeleteView.as_view(), name="post_delete"), # 게시물 삭제
    path("<int:pk>/update/", PostUpdateView.as_view(), name="post_update"), # 게시물 수정
    path('<int:post_id>/comments/', include('comments.urls')), # 댓글 리스트, 생성
    path("<int:pk>/like/", LikeView.as_view(), name="like"),
]