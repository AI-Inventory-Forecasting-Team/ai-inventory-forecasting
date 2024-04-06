from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    author_username = serializers.SerializerMethodField() # 댓글에 대한 유저의 이름을 보여주기 위해 추가


    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'author_username', 'content', 'created_at', 'updated_at']
        read_only_fields = ['author', 'created_at', 'updated_at']

    def get_author_username(self, obj):
        '''
        get_author_username 함수가 serializers.SerializerMethodField()의 반환값이 되어author_username 에 삽입
        Django REST Framework는 해당 필드에 대한 값을 얻기 위해 get_<field_name> 형식의 메서드를 호출
        '''
        return obj.author.username  # 댓글 작성자의 사용자 이름 반환

    def create(self, validated_data):
        validated_data['author'] = self.context['request'].user
        return super().create(validated_data)