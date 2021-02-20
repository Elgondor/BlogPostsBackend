from django.test import TestCase
from .models import Tag, Post, Author
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse

class PostTest(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        # Create a author
        test_author = Author.objects.create(
            author='Brandon Vallejos Silva'
        )
        test_author.save()
        # Create a tag
        test_tag = Tag.objects.create(
            name='Science',
        )
        test_tag.save()
        # Create a post
        test_post = Post.objects.create(
            likes = 2,
            popularity = 12,
            reads = 20,
            author = test_author
        )
        test_post.tags.add(test_tag)
        test_post.save()

        Post.objects.create(
            likes = 1,
            popularity = 10,
            reads = 10,
            author = test_author
        )
        test_post.tags.add(
            Tag.objects.create(
                name='Tech',
            )
        )

    
    
    def test_post_content(self):
        post = Post.objects.get(id=1)
        likes = post.likes
        popularity = post.popularity
        reads = post.reads
        author = post.author
        tags = post.tags.get(pk = 1)
        self.assertEqual(likes, 2)
        self.assertEqual(popularity, 12)
        self.assertEqual(reads, 20)
        self.assertEqual(author.author, 'Brandon Vallejos Silva')
        self.assertEqual(tags.name, 'Science')


    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()

        # self.bucketlist_data = {'name': 'Go to Ibiza'}
        self.response = self.client.get(
            reverse('api:posts'),
            format="json"
        )

    def test_ListPosts(self):
        # get API response
        posts = Post.objects.get()
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.response.data, posts.data)
