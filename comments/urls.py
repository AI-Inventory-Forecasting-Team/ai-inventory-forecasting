from django.urls import path
from .views import CommentListView, CommentCreateView, CommentDetailView

urlpatterns = [
    path('', CommentListView.as_view(), name='comment-list-for-post'),
    path('create/', CommentCreateView.as_view(), name='comment-create'),
    path('<int:pk>/', CommentDetailView.as_view(), name='comment-detail'),
]