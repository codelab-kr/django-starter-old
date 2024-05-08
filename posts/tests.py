from django.test import TestCase

# from .forms import CreatePost
from .models import Post, User


class PostModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", email="testuser@mail.com", password="testpassword"
        )
        self.post = Post.objects.create(
            title="Test title", body="Test body", slug="test-post", author=self.user
        )

    def test_post_model_exists(self):
        posts = Post.objects.count()
        self.assertEqual(posts, 1)

    def test_post_content(self):
        self.assertEqual(f"{self.post.title}", "Test title")
        self.assertEqual(f"{self.post.body}", "Test body")
        self.assertEqual(f"{self.post.slug}", "test-post")
        self.assertEqual(f"{self.post.author}", "testuser")
