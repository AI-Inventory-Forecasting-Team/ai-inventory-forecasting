from django.urls import path
from .views import CommentList, CommentDetail, PostCommentList

urlpatterns = [
    path('comments/', CommentList.as_view(), name='comment-list'),
    path('comments/<int:pk>/', CommentDetail.as_view(), name='comment-detail'),
    path('posts/<int:post_pk>/comments/', PostCommentList.as_view(), name='post-comment-list'),
]