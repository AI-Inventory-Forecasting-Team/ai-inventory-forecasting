from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    LikeView,
)

urlpatterns = [
    path("list/", PostListView.as_view(), name="post_list"), # 게시물 리스트
    path("create/", PostCreateView.as_view(), name="post_create"), # 게시물 생성
    path("<int:pk>/", PostDetailView.as_view(), name="post_detail"), # 게시물 상세보기
    # path("<int:pk>/comment/", CommentCreateView.as_view(), name="comment_create"),  # 댓글 생성
    # path("<int:pk>/comments/", CommentListView.as_view(), name="comment_list"),
    path("<int:pk>/like/", LikeView.as_view(), name="like"),
]