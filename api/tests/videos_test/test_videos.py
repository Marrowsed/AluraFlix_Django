from unittest import TestCase

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from api.models import Video, Category

import pytest

client = APIClient()


class VideoTests(TestCase):
    @pytest.mark.django_db
    def setUp(self):
        self.csrf_client = APIClient(enforce_csrf_checks=True)
        self.category = Category.objects.get(
            title='LIVRE')
        c = Category.objects.get(id=self.category.id)
        self.video = Video.objects.get(id=735)

    @pytest.mark.django_db
    def generate_token_header(self):
        token_url = "/api/token/"
        token_data = {
            'username': 'tester',
            'password': 'api_tester'
        }
        reponse_token = self.csrf_client.post(token_url, token_data)
        token = reponse_token.data
        return token

    # Success Tests
    @pytest.mark.django_db
    def test_post_video(self):
        token = self.generate_token_header()
        url = reverse('video-view')
        data = {'title': 'My First Video', 'description': 'The First Video of Database !',
                'url': 'https://www.google.com.br', "category": f"{self.category.id}"}
        header = f"Bearer {token['access']}"
        response = self.csrf_client.post(url, data=data, HTTP_AUTHORIZATION=header)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    @pytest.mark.django_db
    def test_get_video(self):
        token = self.generate_token_header()
        url = reverse('video-view')
        header = f"Bearer {token['access']}"
        response = self.csrf_client.get(url, HTTP_AUTHORIZATION=header, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    @pytest.mark.django_db
    def test_get_video_id(self):
        token = self.generate_token_header()
        url = f"/api/videos/{self.video.id}/"
        header = f"Bearer {token['access']}"
        response = self.csrf_client.get(url, HTTP_AUTHORIZATION=header)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    @pytest.mark.django_db
    def test_patch_video(self):
        token = self.generate_token_header()
        url = f"/api/videos/{self.video.id}/"
        data = {
            'title': 'My Video !',
        }
        header = f"Bearer {token['access']}"
        response = self.csrf_client.patch(url, data=data, HTTP_AUTHORIZATION=header)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    @pytest.mark.django_db
    def test_put_video(self):
        token = self.generate_token_header()
        url = f"/api/videos/{self.video.id}/"
        data = {
            'title': 'My Video is Back !',
            'description': 'Now with a PUT !',
            'url': 'https://www.google.com',
            "category": f"{self.category.id}"
        }
        header = f"Bearer {token['access']}"
        response = self.csrf_client.put(url, data=data, HTTP_AUTHORIZATION=header)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    @pytest.mark.django_db
    def test_delete_video(self):
        token = self.generate_token_header()
        url = f"/api/videos/{self.video.id}/"
        header = f"Bearer {token['access']}"
        response = self.csrf_client.delete(url, HTTP_AUTHORIZATION=header)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    # Fail Tests
    @pytest.mark.django_db
    def test_fail_get_no_token(self):
        url = f"/api/videos/{self.video.id + 10}/"
        response = self.csrf_client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    @pytest.mark.django_db
    def test_fail_get_video_wrong_id(self):
        token = self.generate_token_header()
        url = f"/api/videos/{self.video.id + 10}/"
        header = f"Bearer {token['access']}"
        response = self.csrf_client.get(url, HTTP_AUTHORIZATION=header)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    @pytest.mark.django_db
    def test_fail_post_video_no_category(self):
        token = self.generate_token_header()
        url = reverse('video-view')
        data = {'title': 'My First Video', 'description': 'The First Video of Database !',
                'url': 'mysite.com'}
        header = f"Bearer {token['access']}"
        response = self.csrf_client.post(url, data=data, HTTP_AUTHORIZATION=header)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    @pytest.mark.django_db
    def test_fail_post_video_wrong_url(self):
        token = self.generate_token_header()
        url = reverse('video-view')
        data = {'title': 'My First Video', 'description': 'The First Video of Database !',
                'url': 'mysite.com'}
        header = f"Bearer {token['access']}"
        response = self.csrf_client.post(url, data=data, HTTP_AUTHORIZATION=header)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    @pytest.mark.django_db
    def test_fail_post_video_with_blank(self):
        token = self.generate_token_header()
        url = reverse('video-view')
        data = {'title': '', 'description': 'The First Video of Database !',
                'url': 'https://www.youtube.com'}
        header = f"Bearer {token['access']}"
        response = self.csrf_client.post(url, data=data, HTTP_AUTHORIZATION=header)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    @pytest.mark.django_db
    def test_fail_put_video_wrong_url(self):
        token = self.generate_token_header()
        url = f"/api/videos/{self.video.id}/"
        data = {'title': 'My First Video', 'description': 'The First Video of Database !',
                'url': 'mysite.com'}
        header = f"Bearer {token['access']}"
        response = self.csrf_client.put(url, data=data, HTTP_AUTHORIZATION=header)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    @pytest.mark.django_db
    def test_fail_put_blank(self):
        token = self.generate_token_header()
        url = f"/api/videos/{self.video.id}/"
        data = {'title': 'My First Video', 'description': '',
                'url': 'https://www.github.com/marrowsed'}
        header = f"Bearer {token['access']}"
        response = self.csrf_client.put(url, data=data, HTTP_AUTHORIZATION=header)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    @pytest.mark.django_db
    def test_fail_patch_video_wrong_url(self):
        token = self.generate_token_header()
        url = f"/api/videos/{self.video.id}/"
        data = {'url': 'mysite.com'}
        header = f"Bearer {token['access']}"
        response = self.csrf_client.patch(url, data=data, HTTP_AUTHORIZATION=header)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    @pytest.mark.django_db
    def test_fail_delete_video_do_not_exist(self):
        token = self.generate_token_header()
        url = f"/api/videos/{self.video.id}/"
        header = f"Bearer {token['access']}"
        response = self.csrf_client.delete(url, HTTP_AUTHORIZATION=header)
        url2 = f"/api/videos/{self.video.id}/"
        response2 = self.csrf_client.delete(url2, HTTP_AUTHORIZATION=header)
        self.assertEqual(response2.status_code, status.HTTP_404_NOT_FOUND)
