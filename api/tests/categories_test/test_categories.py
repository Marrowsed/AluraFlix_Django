from unittest import TestCase

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from api.models import Category, Video

import pytest

client = APIClient()


class VideoTests(TestCase):

    def setUp(self):
        self.csrf_client = APIClient(enforce_csrf_checks=False)
        self.category = Category.objects.create(
            title='LIVRE',
            color="blue"
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
    def test_post_category(self):
        url = reverse('category-view')
        data = {'title': 'DRAMA', 'color': 'red'}
        response = self.csrf_client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    @pytest.mark.django_db
    def test_get_category(self):
        url = reverse('category-view')
        response = self.csrf_client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    @pytest.mark.django_db
    def test_get_category_id(self):
        url = f"/api/categories/{self.category.id}/"
        response = self.csrf_client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    @pytest.mark.django_db
    def test_patch_category(self):
        url = f"/api/categories/{self.category.id}/"
        data = {
            'title': 'HORROR',
        }
        response = self.csrf_client.patch(url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    @pytest.mark.django_db
    def test_put_category(self):
        url = f"/api/categories/{self.category.id}/"
        data = {
            'title': 'HORROR',
            'color': 'black'
        }
        response = self.csrf_client.put(url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    @pytest.mark.django_db
    def test_delete_category(self):
        url = f"/api/categories/{self.category.id}/"
        response = self.csrf_client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    @pytest.mark.django_db
    def test_get_category_video(self):
        url = f"/api/categories/{self.category.id}/videos/"
        response = self.csrf_client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    #Fail Tests
    @pytest.mark.django_db
    def test_fail_get_category_wrong_id(self):
        url = f"/api/categories/{self.category.id + 10}/"
        response = self.csrf_client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    @pytest.mark.django_db
    def test_fail_post_category_no_title(self):
        url = reverse('category-view')
        data = {'title': '', 'color': 'white'}
        response = self.csrf_client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    @pytest.mark.django_db
    def test_fail_delete_category_do_not_exist(self):
        url = f"/api/categories/{self.category.id}/"
        response = self.csrf_client.delete(url)
        url2 = f"/api/categories/{self.category.id}/"
        response2 = self.csrf_client.delete(url2)
        self.assertEqual(response2.status_code, status.HTTP_404_NOT_FOUND)

    @pytest.mark.django_db
    def test_fail_get_category_no_video(self):
        url = reverse('category-view')
        data = {'title': 'HORROR', 'color': 'red'}
        response = self.csrf_client.post(url, data, format='json')
        url2 = f"/api/categories/2/videos/"
        response2 = self.csrf_client.get(url2)
        self.assertEqual(response2.status_code, status.HTTP_404_NOT_FOUND)