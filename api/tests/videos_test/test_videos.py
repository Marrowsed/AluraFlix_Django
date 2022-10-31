from unittest import TestCase

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from api.models import Video, Category

import pytest

client = APIClient()


class VideoTests(TestCase):

    def setUp(self):
        self.csrf_client = APIClient(enforce_csrf_checks=False)
        self.category = Category.objects.create(
            title="LIVRE",
            color="white"
        )
        c = Category.objects.get(id=self.category.id)
        self.video = Video.objects.create(
            title='My First Video',
            description='My First Video in Youtube !',
            url='https://www.github.com/marrowsed',
            category=c
        )

    # Success Tests
    @pytest.mark.django_db
    def test_post_video(self):
        url = reverse('video-view')
        data = {'title': 'My First Video', 'description': 'The First Video of Database !',
                'url': 'https://www.google.com.br', "category": f"{self.category.id}"}
        response = self.csrf_client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    @pytest.mark.django_db
    def test_get_video(self):
        url = reverse('video-view')
        response = self.csrf_client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    @pytest.mark.django_db
    def test_get_video_id(self):
        url = f"/api/videos/{self.video.id}/"
        response = self.csrf_client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    @pytest.mark.django_db
    def test_patch_video(self):
        url = f"/api/videos/{self.video.id}/"
        data = {
            'title': 'My Video !',
        }
        response = self.csrf_client.patch(url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    @pytest.mark.django_db
    def test_put_video(self):
        url = f"/api/videos/{self.video.id}/"
        data = {
            'title': 'My Video is Back !',
            'description': 'Now with a PUT !',
            'url': 'https://www.google.com',
            "category": f"{self.category.id}"
        }
        response = self.csrf_client.put(url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    @pytest.mark.django_db
    def test_delete_video(self):
        url = f"/api/videos/{self.video.id}/"
        response = self.csrf_client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    #Fail Tests
    @pytest.mark.django_db
    def test_fail_get_video_wrong_id(self):
        url = f"/api/videos/{self.video.id + 10}/"
        response = self.csrf_client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    @pytest.mark.django_db
    def test_fail_post_video_no_category(self):
        url = reverse('video-view')
        data = {'title': 'My First Video', 'description': 'The First Video of Database !',
                'url': 'mysite.com'}
        response = self.csrf_client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    @pytest.mark.django_db
    def test_fail_post_video_wrong_url(self):
        url = reverse('video-view')
        data = {'title': 'My First Video', 'description': 'The First Video of Database !',
                'url': 'mysite.com'}
        response = self.csrf_client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    @pytest.mark.django_db
    def test_fail_post_video_with_blank(self):
        url = reverse('video-view')
        data = {'title': '', 'description': 'The First Video of Database !',
                'url': 'https://www.youtube.com'}
        response = self.csrf_client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    @pytest.mark.django_db
    def test_fail_put_video_wrong_url(self):
        url = f"/api/videos/{self.video.id}/"
        data = {'title': 'My First Video', 'description': 'The First Video of Database !',
                'url': 'mysite.com'}
        response = self.csrf_client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    @pytest.mark.django_db
    def test_fail_put_blank(self):
        url = f"/api/videos/{self.video.id}/"
        data = {'title': 'My First Video', 'description': '',
                'url': 'https://www.github.com/marrowsed'}
        response = self.csrf_client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    @pytest.mark.django_db
    def test_fail_patch_video_wrong_url(self):
        url = f"/api/videos/{self.video.id}/"
        data = {'url': 'mysite.com'}
        response = self.csrf_client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    @pytest.mark.django_db
    def test_fail_delete_video_do_not_exist(self):
        url = f"/api/videos/{self.video.id}/"
        response = self.csrf_client.delete(url)
        url2 = f"/api/videos/{self.video.id}/"
        response2 = self.csrf_client.delete(url2)
        self.assertEqual(response2.status_code, status.HTTP_404_NOT_FOUND)