from rest_framework import generics
from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied
from .models import Comment
from .serializers import CommentSerializer

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
        # Filters comments by post_id passed in the URL
        return self.queryset.filter(post_id=self.kwargs['post_id'])

class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Filters comments to those authored by the requesting user
        return Comment.objects.filter(author=self.request.user)

    def perform_update(self, serializer):
        # Checks if the user is the author of the comment before updating
        comment = self.get_object()
        if comment.author != self.request.user:
            raise PermissionDenied("You do not have permission to edit this comment.")
        serializer.save()

    def perform_destroy(self, instance):
        # Checks if the user is the author of the comment before deleting
        if instance.author != self.request.user:
            raise PermissionDenied("You do not have permission to delete this comment.")
        instance.delete()