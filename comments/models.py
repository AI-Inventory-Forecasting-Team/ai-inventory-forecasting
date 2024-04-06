from django.db import models
from config.settings import AUTH_USER_MODEL as User
from posts.models import Post


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Comment by {self.author} on {self.content}"

    def get_avatar_url(self):
        if self.author.socialaccount_set.exists():
            return self.author.socialaccount_set.first().get_avatar_url()
        else:
            return "https://picsum.photos/seed/{ self.author.pk }/50/50"

    class Meta:
        ordering = ["-created_at"]


# class ReComment(models.Model):
#     comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
#     author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="작성자")
#     content = models.CharField(max_length=150, verbose_name="대댓글")
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.content