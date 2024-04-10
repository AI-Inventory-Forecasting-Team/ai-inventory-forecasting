from django.http import Http404
from django.contrib.contenttypes.models import ContentType

# Rest Framework Modules
from rest_framework import generics, status, response, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

# Models
from .serializers import PostSerializer, CategorySerializer, LikeSerializer, BookmarkSerializer
from .models import Post, Like, Category, ViewCount, Bookmark

# Filters
from rest_framework.filters import SearchFilter


class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [SearchFilter]
    search_fields = ['title', 'category__name', 'author__username']
    permission_classes = [permissions.IsAuthenticated]  # 인증된 사용자만 접근 가능


class PostDetailView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        post = self.get_object()
        user = self.request.user

        if user.is_authenticated:
            content_type = ContentType.objects.get_for_model(post)
            viewed, created = ViewCount.objects.get_or_create(
                user=user,
                content_type=content_type,
                object_id=post.id,
            )
            if created:
                post.view_count += 1
                post.save(update_fields=['view_count'])
        return response


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


class LikeCreateView(generics.CreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        post_id = self.kwargs.get('pk')
        post = Post.objects.get(id=post_id)
        like_exists = Like.objects.filter(user=user, post=post).exists()

        if like_exists:
            # 이미 좋아요한 상태라면 기존 좋아요 삭제
            existing_like = Like.objects.get(user=user, post=post)
            existing_like.delete()
            like_count = post.likes.count()
            return Response({'like_count': like_count})
        else:
            # 새로운 좋아요 생성
            serializer.save(user=user, post=post)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        like_count = instance.post.likes.count()
        return Response({'like_count': like_count})


class LikeDestroyView(generics.DestroyAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        user = self.request.user
        post_id = self.kwargs.get('pk')
        post = Post.objects.get(id=post_id)
        like = Like.objects.filter(user=user, post=post).first()
        if like is None:
            raise Http404
        return like
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        like_count = instance.post.likes.count()
        return Response({'like_count': like_count})
    

class BookmarkCreateView(generics.CreateAPIView):
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class BookmarkListView(generics.ListAPIView):
    serializer_class = BookmarkSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Bookmark.objects.filter(user=self.request.user)
    

class BookmarkDestroyView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer
    lookup_field = 'id'

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_destroy(self, instance):
        if instance.user == self.request.user:
            instance.delete()