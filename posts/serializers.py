from rest_framework import serializers
from .models import Post, Like, Category


class PostSerializer(serializers.ModelSerializer):
    author_username = serializers.SerializerMethodField()
    likesCount = serializers.IntegerField(source='likes.count', read_only=True)
    isLiked = serializers.SerializerMethodField()
    image = serializers.ImageField(use_url=True)
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    category_name = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 
                'image', 'file_upload', 
                'created_at', 'updated_at', 'author', 'category', 'category_name', 'view_count',
                'author_username', 'likesCount', 'isLiked']
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
        return super().create(validated_data)
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.image:
            representation['image'] = self.context['request'].build_absolute_uri(instance.image.url)
        return representation
    

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']