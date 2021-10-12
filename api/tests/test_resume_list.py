from typing import List

from django.test import TestCase
from django.urls import reverse
from rest_framework import status, test

from api import models, serializers


class TestResumeList(TestCase):
    fixtures = ['resumes.json']

    def setUp(self) -> None:
        self.client = test.APIClient()
        self.url = reverse('resume_list')
        self.resumes: List[models.Resume] = models.Resume.objects.all()

    def test_get_list_of_resumes(self) -> None:
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        serializer = serializers.ResumeSerializer(self.resumes, many=True)
        self.assertEqual(response.data, serializer.data)
