from rest_framework import generics
from .models import Comment
from .serializers import CommentSerializer
from rest_framework import permissions

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
