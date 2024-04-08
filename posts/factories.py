from django.contrib.auth import get_user_model
from .models import Post, Category
import factory


CustomUser = get_user_model()

class CustomUserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = CustomUser

    username = factory.Sequence(lambda n: f'user{n}')
    email = factory.LazyAttribute(lambda obj: f'{obj.username}@example.com')


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = "기본 카테고리"


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    title = "테스트 제목"
    author = factory.SubFactory(CustomUserFactory)
    category = factory.SubFactory(CategoryFactory)  