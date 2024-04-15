from rest_framework import serializers
from .models import Comment, ReComment

class CommentSerializer(serializers.ModelSerializer):
    author_username = serializers.SerializerMethodField()
    replies = serializers.PrimaryKeyRelatedField(many=True, read_only=True)  # 댓글에 대한 답글을 직렬화 데이터에 포함시킵니다.

    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'author_username', 'content', 'created_at', 'updated_at', 'replies']
        read_only_fields = ['author', 'created_at', 'updated_at']

    def get_author_username(self, obj):
        return obj.author.username

class ReCommentSerializer(serializers.ModelSerializer):
    author_username = serializers.SerializerMethodField()

    class Meta:
        model = ReComment
        fields = ['id', 'comment', 'author', 'author_username', 'content', 'created_at', 'updated_at']
        read_only_fields = ['author', 'created_at', 'updated_at']

    def get_author_username(self, obj):
        return obj.author.username

    def create(self, validated_data):
        """
        제공된 유효한 데이터로 새 ReComment 인스턴스를 생성하고 반환합니다.
        """
        # 요청 사용자가 view의 perform_create 메소드에서 설정되고,
        # 댓글 ID가 유효한 데이터에 전달된다고 가정합니다.
        return ReComment.objects.create(**validated_data)