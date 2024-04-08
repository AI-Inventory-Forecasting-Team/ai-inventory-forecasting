from django.urls import path
from .views import CommentListView, CommentCreateView, CommentDetailView, ReCommentCreateView, ReCommentListView, ReCommentDetailView

urlpatterns = [
    path('', CommentListView.as_view(), name='comment-list-for-post'),
    path('create/', CommentCreateView.as_view(), name='comment-create'),
    path('<int:pk>/', CommentDetailView.as_view(), name='comment-detail'),
    path('<int:comment_id>/replies/', ReCommentListView.as_view(), name='recomment-list-for-comment'),
    path('<int:comment_id>/replies/create/', ReCommentCreateView.as_view(), name='recomment-create'),
    path('replies/<int:pk>/', ReCommentDetailView.as_view(), name='recomment-detail'),
]