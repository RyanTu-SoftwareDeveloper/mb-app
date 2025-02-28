from django.test import TestCase
from django.urls import reverse # new
from .models import Post

class PostModelTest(TestCase):

    def setUp(self):
        Post.objects.create(text='just a test')

    def test_text_content(self):
        post=Post.objects.get(id=1)
        expected_object_name = f'{post.text}'
        self.assertEqual(expected_object_name, 'just a test')

class HomePageViewTest(TestCase): # new
    def setUp(self): #Each test starts with a fresh database (Django resets the database for each test)
        Post.objects.create(text='this is another test')

    def test_view_url_exists_at_proper_location(self): #Test 1: URL Exists
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_by_name(self): #Test 2: URL Using Reverse Name
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self): #Test 3: Correct Template Used
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'home.html')