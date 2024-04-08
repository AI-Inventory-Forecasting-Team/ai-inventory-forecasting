from rest_framework import generics, permissions
from rest_framework.exceptions import PermissionDenied
from .models import Comment, ReComment
from .serializers import CommentSerializer, ReCommentSerializer


class CommentCreateView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentListView(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self):
        return self.queryset.filter(post_id=self.kwargs['post_id'])


class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Comment.objects.filter(author=self.request.user)


class ReCommentCreateView(generics.CreateAPIView):
    queryset = ReComment.objects.all()
    serializer_class = ReCommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class ReCommentListView(generics.ListAPIView):
    queryset = ReComment.objects.all()
    serializer_class = ReCommentSerializer

    def get_queryset(self):
        return self.queryset.filter(comment_id=self.kwargs['comment_id'])


class ReCommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ReComment.objects.all()
    serializer_class = ReCommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return ReComment.objects.filter(author=self.request.user)