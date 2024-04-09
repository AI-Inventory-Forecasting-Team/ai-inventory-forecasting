from django.db import models
from config.settings import AUTH_USER_MODEL as User
from pathlib import Path
from PIL import Image
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class Category(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name
    

    class Meta:
        verbose_name_plural = "Categories"


class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    image = models.ImageField(upload_to="posts/images/%Y/%m/%d/", blank=True)
    file_upload = models.FileField(upload_to="posts/files/%Y/%m/%d", blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    category = models.ForeignKey(
        Category, blank=True, null=True, on_delete=models.SET_NULL
    )
    view_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.title}"

    def get_file_name(self):
        return self.file_upload.name

    def get_file_ext(self):
        return Path(self.get_file_name()).suffix[1:]
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # 모델 저장

        if self.image:  # 이미지 필드에 파일이 있는지 확인
            img = Image.open(self.image.path)  # 이미지 파일 열기

            # 이미지 사이즈가 800x600이 아닌 경우에만 조정
            if img.width != 800 or img.height != 600:
                new_size = (800, 600)
                img = img.resize(new_size, Image.Resampling.LANCZOS)  # 이미지 사이즈 조정
                img.save(self.image.path)  # 변경된 이미지 저장
    

class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('post', 'user')

    def __str__(self):
        return f'{self.user.username} likes {self.post.title}'
    

class ViewCount(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    viewed_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'content_type', 'object_id')