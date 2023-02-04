from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
# Create your tests here.


class PostListTestCase(APITestCase):

    def test_post_list(self):
        url = 'post_list'
        response = self.client.get(reverse(url))
        # assertEqual is a method that compares the first argument to the second argument
        # if they are equal, the test passes
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [])
