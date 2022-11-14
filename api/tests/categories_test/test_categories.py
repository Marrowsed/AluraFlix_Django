from unittest import TestCase

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from api.models import Category, Video

import pytest

client = APIClient()


class VideoTests(TestCase):
    @pytest.mark.django_db
    def setUp(self):
        self.csrf_client = APIClient(enforce_csrf_checks=True)
        self.category = Category.objects.get(
            title='LIVRE')
        c = Category.objects.get(id=self.category.id)
        self.video = Video.objects.get(id=740)


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
    def test_post_category(self):
        token = self.generate_token_header()
        header = f"Bearer {token['access']}"
        url = reverse('category-view')
        data = {'title': 'DRAMA', 'color': 'red'}
        response = self.csrf_client.post(url, HTTP_AUTHORIZATION=header, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    @pytest.mark.django_db
    def test_get_category(self):
        token = self.generate_token_header()
        header = f"Bearer {token['access']}"
        url = reverse('category-view')
        response = self.csrf_client.get(url, HTTP_AUTHORIZATION=header)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    @pytest.mark.django_db
    def test_get_category_id(self):
        token = self.generate_token_header()
        header = f"Bearer {token['access']}"
        url = f"/api/categories/{self.category.id}/"
        response = self.csrf_client.get(url, HTTP_AUTHORIZATION=header)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    @pytest.mark.django_db
    def test_patch_category(self):
        token = self.generate_token_header()
        url = f"/api/categories/{self.category.id}/"
        data = {
            'title': 'HORROR',
        }
        header = f"Bearer {token['access']}"
        response = self.csrf_client.patch(url, HTTP_AUTHORIZATION=header, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    @pytest.mark.django_db
    def test_put_category(self):
        token = self.generate_token_header()
        url = f"/api/categories/{self.category.id}/"
        data = {
            'title': 'NODE.JS',
            'color': 'black'
        }
        header = f"Bearer {token['access']}"
        response = self.csrf_client.put(url, HTTP_AUTHORIZATION=header, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    @pytest.mark.django_db
    def test_delete_category(self):
        token = self.generate_token_header()
        header = f"Bearer {token['access']}"
        url = f"/api/categories/{self.category.id}/"
        response = self.csrf_client.delete(url, HTTP_AUTHORIZATION=header)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    @pytest.mark.django_db
    def test_get_category_video(self):
        token = self.generate_token_header()
        header = f"Bearer {token['access']}"
        url = f"/api/categories/{self.category.id}/videos/"
        response = self.csrf_client.get(url, HTTP_AUTHORIZATION=header)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    #Fail Tests
    @pytest.mark.django_db
    def test_fail_get_category_wrong_id(self):
        token = self.generate_token_header()
        header = f"Bearer {token['access']}"
        url = f"/api/categories/{self.category.id + 10}/"
        response = self.csrf_client.get(url, HTTP_AUTHORIZATION=header)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    @pytest.mark.django_db
    def test_fail_post_category_no_title(self):
        token = self.generate_token_header()
        header = f"Bearer {token['access']}"
        url = reverse('category-view')
        data = {'title': '', 'color': 'white'}
        response = self.csrf_client.post(url, HTTP_AUTHORIZATION=header, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    @pytest.mark.django_db
    def test_fail_delete_category_do_not_exist(self):
        token = self.generate_token_header()
        header = f"Bearer {token['access']}"
        url = f"/api/categories/{self.category.id}/"
        response = self.csrf_client.delete(url, HTTP_AUTHORIZATION=header)
        url2 = f"/api/categories/{self.category.id}/"
        response2 = self.csrf_client.delete(url2, HTTP_AUTHORIZATION=header)
        self.assertEqual(response2.status_code, status.HTTP_404_NOT_FOUND)

    @pytest.mark.django_db
    def test_fail_get_category_no_video(self):
        token = self.generate_token_header()
        header = f"Bearer {token['access']}"
        url = reverse('category-view')
        data = {'title': 'HORROR', 'color': 'red'}
        response = self.csrf_client.post(url, HTTP_AUTHORIZATION=header, data=data, format='json')
        url2 = f"/api/categories/2/videos/"
        response2 = self.csrf_client.get(url2, HTTP_AUTHORIZATION=header)
        self.assertEqual(response2.status_code, status.HTTP_404_NOT_FOUND)