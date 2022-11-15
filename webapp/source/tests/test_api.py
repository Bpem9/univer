from rest_framework import status
from rest_framework.test import APITestCase
import re

URLs = [
    'http://127.0.0.1:8000/api/v1/groups/',
    'http://127.0.0.1:8000/api/v1/courses/',
    'http://127.0.0.1:8000/api/v1/students/',
    'http://127.0.0.1:8000/api/v1/disciplines/',
    'http://127.0.0.1:8000/api/v1/supervisors/',
]

class UniversityDirectionTest(APITestCase):
    def test_status_200(self):
        for url in URLs:
            self.response = self.client.get(url)
            self.assertEqual(status.HTTP_200_OK, self.response.status_code)
            name = re.search(r'\w+/$', url).group(0)
            print('=' * 10, f'{name} - OK')