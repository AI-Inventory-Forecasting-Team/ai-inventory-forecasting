from rest_framework import serializers
from .models import Post, Like, Category
from django.core.files.base import ContentFile
import requests


class PostSerializer(serializers.ModelSerializer):
    author_username = serializers.SerializerMethodField()
    likesCount = serializers.IntegerField(source='likes.count', read_only=True)
    isLiked = serializers.SerializerMethodField()
    image = serializers.ImageField(use_url=True, required=False, allow_null=True)
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    category_name = serializers.SerializerMethodField(read_only=True)
    file_upload = serializers.FileField(required=False, allow_null=True)
    full_url = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 
                'image', 'file_upload', 
                'created_at', 'updated_at', 'author', 'category', 'category_name', 'view_count',
                'author_username', 'likesCount', 'isLiked', 'full_url']
        read_only_fields = ['author', 'created_at', 'updated_at', 'view_count', 'likesCount']

    def get_isLiked(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            # Like 모델을 사용하여 현재 사용자가 게시물에 좋아요를 눌렀는지 확인
            return Like.objects.filter(post=obj, user=user).exists()
        return False

    def get_author_username(self, obj):
        return obj.author.username  # 댓글 작성자의 사용자 이름 반환
    
    def get_category_name(self, obj):
        return obj.category.name if obj.category else None

    def create(self, validated_data):
        # 현재 요청을 보낸 사용자를 게시물의 저자로 설정
        validated_data['author'] = self.context['request'].user

        # 사용자가 이미지를 업로드하지 않았을 경우 기본 이미지 설정
        if 'image' not in validated_data:
            image_url = 'https://picsum.photos/800/600'
            response = requests.get(image_url)
            if response.status_code == 200:
                # 이미지 파일의 이름 설정
                file_name = 'default_image.jpg'
                validated_data['image'] = ContentFile(response.content, name=file_name)
        return super().create(validated_data)
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.image:
            representation['image'] = self.context['request'].build_absolute_uri(instance.image.url)
        return representation
    
    def get_full_url(self, obj):
        # request context를 사용하여 절대 URL 생성
        request = self.context.get('request')
        if request is None:
            return ''
        return request.build_absolute_uri(obj.get_absolute_url())
    

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['id', 'post', 'user']
        read_only_fields = ['user']
    
    def create(self, validated_data):
        user = self.context['request'].user
        post = validated_data['post']
        like, created = Like.objects.get_or_create(user=user, post=post)
        return like

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['like_count'] = instance.post.likes.count()
        return representation
    
    def destroy(self, instance):
        like_count = instance.post.likes.count()
        instance.delete()
        return {'like_count': like_count}