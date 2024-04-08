from django.test import TestCase
from .filters import PostFilter
from .factories import PostFactory, CustomUserFactory

class PostFilterTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # 테스트 데이터 생성
        hong_user = CustomUserFactory(username="홍길동")
        PostFactory(author=hong_user, title="홍길동의 게시물", category__name="기타")
        PostFactory(title="Django 테스트", category__name="프로그래밍")  
        PostFactory(title="Django 고급", category__name="여행")  # "프로그래밍" 카테고리로 두 번째 게시물 추가
        PostFactory(title="요리 레시피", category__name="요리")  

    def test_filter_by_title(self):
        # 제목으로 필터링
        filter_result = PostFilter({'title': 'Django'}).qs
        self.assertEqual(filter_result.count(), 2)
        self.assertEqual(filter_result.first().title, "Django 테스트")

    def test_filter_by_author(self):
        # 작가로 필터링
        filter_result = PostFilter({'author': '홍길동'}).qs
        self.assertEqual(filter_result.count(), 1)
        # 수정된 부분: `CustomUser` 인스턴스의 `username` 속성과 문자열 비교
        self.assertEqual(filter_result.first().author.username, "홍길동")


    def test_filter_by_category(self):
        # 카테고리로 필터링
        filter_result = PostFilter({'category': '프로그래밍'}).qs
        self.assertEqual(filter_result.count(), 1)
        self.assertTrue(all(post.category.name == "프로그래밍" for post in filter_result))


# python manage.py test posts