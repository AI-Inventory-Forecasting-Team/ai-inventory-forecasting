from django.shortcuts import get_object_or_404
from rest_framework import generics
from .models import Post, Comment
from .serializers import CommentSerializer

class CommentList(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class PostCommentList(generics.ListCreateAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        queryset = Comment.objects.all()
        post_pk = self.kwargs.get('post_pk')
        if post_pk is not None:
            queryset = queryset.filter(post_id=post_pk)
        return queryset

    def perform_create(self, serializer):
        post_pk = self.kwargs.get('post_pk')
        post = get_object_or_404(Post, pk=post_pk)
        serializer.save(post=post)