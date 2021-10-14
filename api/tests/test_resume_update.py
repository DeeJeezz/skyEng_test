import base64
from typing import List
from uuid import uuid4

from django.test import TestCase
from django.urls import reverse
from rest_framework import status, test

from api import models, serializers


class TestResumeUpdate(TestCase):
    fixtures = ['users.json', 'resumes.json']

    def setUp(self) -> None:
        self.client = test.APIClient()
        self.resumes: List[models.Resume] = models.Resume.objects.all()
        self.valid_single_resume_params: List[uuid4] = [resume.id for resume in self.resumes]
        self._basic_auth: bytes = 'admin:admin'.encode()
        self.admin_basic_auth_header: str = 'Basic %s' % base64.b64encode(self._basic_auth).decode()

    def test_get_valid_single_resume(self) -> None:
        for resume_id in self.valid_single_resume_params:
            with self.subTest(id=resume_id):
                url = reverse('resume_update', kwargs={'pk': resume_id})
                response = self.client.get(url, format='json')
                resume = models.Resume.objects.get(pk=resume_id)
                serializer = serializers.ResumeSerializer(resume)
                self.assertEqual(response.status_code, status.HTTP_200_OK)
                self.assertEqual(response.data, serializer.data)

    def test_get_invalid_single_resume(self) -> None:
        url = reverse('resume_update', kwargs={'pk': uuid4()})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_valid_patch_resume(self) -> None:
        url = reverse('resume_update', kwargs={'pk': self.valid_single_resume_params[0]})
        before_changes_response = self.client.get(url, format='json')
        updated_data: dict = before_changes_response.data.copy()
        updated_data.update({'salary': 3333})
        self.client.credentials(HTTP_AUTHORIZATION=self.admin_basic_auth_header)
        after_changes_response = self.client.patch(url, data=updated_data)
        self.assertEqual(after_changes_response.status_code, status.HTTP_200_OK)
        self.assertEqual(updated_data, after_changes_response.data)

    def test_permissions_to_deny_patch_request(self) -> None:
        url = reverse('resume_update', kwargs={'pk': self.valid_single_resume_params[0]})
        self.client.credentials()
        response = self.client.patch(url, data={}, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
