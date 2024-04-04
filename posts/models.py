from django.db import models
from config.settings import AUTH_USER_MODEL as User
from pathlib import Path


class Category(models.Model):
    name = models.CharField(max_length=30, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"/blog/category/{self.slug}/"

    def post_count(self):
        return self.post_set.count()

    class Meta:
        verbose_name_plural = "Categories"


class Tag(models.Model):
    name = models.CharField(max_length=30, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"/blog/tag/{self.slug}/"
    

class Post(models.Model):
    title = models.CharField(max_length=30)
    hook_text = models.CharField(max_length=100, blank=True)
    content = models.TextField()
    caption = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to="posts/images/%Y/%m/%d/", blank=True)

    thumbnail_image = models.ImageField(upload_to="posts/images/%Y/%m/%d/", blank=True)
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

    def get_absolute_url(self):
        return f"/blog/{self.pk}/"

    def get_file_name(self):
        return self.file_upload.name

    def get_file_ext(self):
        return Path(self.get_file_name()).suffix[1:]
    

class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('post', 'user')

    def __str__(self):
        return f'{self.user.username} likes {self.post.caption}'