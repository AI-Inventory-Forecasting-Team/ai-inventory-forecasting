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

      
class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    객체의 소유자만이 객체를 수정하거나 삭제할 수 있게 하는 커스텀 권한.
    """

    def has_object_permission(self, request, view, obj):
        # 읽기 권한은 모든 요청에 허용됩니다.
        # 따라서 GET, HEAD, OPTIONS 요청은 항상 허용됩니다.
        if request.method in permissions.SAFE_METHODS:
            return True

        # 쓰기 권한은 객체의 소유자에게만 부여됩니다.
        return obj.author == request.user