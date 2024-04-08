from django.shortcuts import get_object_or_404

# Rest Framework Modules
from rest_framework import generics, views, status, response, permissions
from rest_framework.permissions import IsAuthenticated

# Models
from .serializers import PostSerializer, CategorySerializer
from .models import Post, Like, Category

# Filters
from .filters import PostFilter
from django_filters.rest_framework import DjangoFilterBackend


class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = PostFilter
    permission_classes = [permissions.IsAuthenticated]  # 인증된 사용자만 접근 가능


class PostDetailView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostCreateView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]  # 인증된 사용자만 접근 가능

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostDeleteView(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]  # 인증된 사용자만 접근 가능

    def delete(self, request, *args, **kwargs):
        post = self.get_object()
        if post.author != request.user:
            return response.Response({'message': '본인이 작성한 게시글만 삭제할 수 있습니다.'},status=status.HTTP_403_FORBIDDEN)
        return super().delete(request, *args, **kwargs)


class PostUpdateView(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]  # 인증된 사용자만 접근 가능

    def update(self, request, *args, **kwargs):
        post = self.get_object()
        if post.author != request.user:
            return response.Response({'message': '본인이 작성한 게시글만 수정할 수 있습니다.'},status=status.HTTP_403_FORBIDDEN)
        return super().update(request, *args, **kwargs)
    

class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]  # 인증된 사용자만 접근 가능

class LikeView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        like, created = Like.objects.get_or_create(post=post, user=request.user)

        # 좋아요를 검색한 후 좋아요가 없으면 생성(like 생성된 객체, created가 생성 여부 판단)
        # created == True : 좋아요가 클릭이 안되어 있어서 새로 생성했다.
        # created == False : 좋아요가 클릭이 되어서 생성하지 못했다.

        if not created:
            # 이미 좋아요가 존재하는 경우, 409 Conflict 반환
            return response.Response(status=status.HTTP_409_CONFLICT)

        # 좋아요가 생성되었으면 201 응답
        return response.Response(status=status.HTTP_201_CREATED)

    def delete(self, request, post_id):
        post = get_object_or_404(Post, id=post_id) # 게시물이 존재하지 않으면 404 에러
        like = get_object_or_404(Like, post=post, user=request.user) # 좋아요가 존재하지 않으면 404 에러
        like.delete()
        return response.Response(status=status.HTTP_204_NO_CONTENT) # 좋아요가 삭제되었으면 204 응답