from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from datetime import datetime

class AdditionTests(APITestCase):
    def test_add_numbers(self):
        url = reverse('add')
        data = {
            "batchid": "id0101",
            "payloada": [[1, 2], [3, 4]]
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['batchid'], 'id0101')
        self.assertEqual(response.data['response'], [3, 7])
        self.assertEqual(response.data['status'], 'complete')
        self.assertIn('started_at', response.data)
        self.assertIn('completed_at', response.data)

    def test_add_numbers_with_empty_list(self):
        url = reverse('add')
        data = {
            "batchid": "id0102",
            "payloada": []
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['batchid'], 'id0102')
        self.assertEqual(response.data['response'], [])
        self.assertEqual(response.data['status'], 'complete')
        self.assertIn('started_at', response.data)
        self.assertIn('completed_at', response.data)

    def test_add_numbers_with_invalid_data(self):
        url = reverse('add')
        data = {
            "batchid": "id0103",
            "payloada": [[1, "a"], [3, 4]]
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
