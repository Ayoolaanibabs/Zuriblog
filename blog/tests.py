from .models import Post, Comment
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse



# Create your tests here.
class blog_tests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username = 'testuser',
            email = 'test@yahoo.com',
            password = 'password1'
        )

        self.post = Post.objects.create(
            title = 'Test title',
            body = 'Test body',
            author = self.user
        )

        self.comment = Comment.objects.create(
            post = Post.objects.create(
            title = 'Test title',
            body = 'Test body',
            author = self.user
        ),
            name = self.user,
            body = 'Test comment'
        )
    
    def test_string_representation(self):
        post = Post(title = 'a sample title')
        self.assertEqual(str(post), post.title)

    def test_post_content(self):
        self.assertEqual(f'{self.post.title}', 'Test title')
        self.assertEqual(f'{self.post.author}', 'testuser')
        self.assertEqual(f'{self.post.body}', 'Test body')

    def test_post_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_post_detail_page(self):
        response = self.client.get('/post/1/')
        no_response = self.client.get('/post/100000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'Test title')
        self.assertTemplateUsed(response, 'post_detail.html')

    def test_comment_content(self):
        self.assertEqual(f'{self.comment.post}', 'Test title')
        self.assertEqual(f'{self.comment.name}', 'testuser')
        self.assertEqual(f'{self.comment.body}', 'Test comment')
    