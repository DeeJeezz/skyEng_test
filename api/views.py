from typing import List

from rest_framework import generics
from rest_framework.permissions import BasePermission

from api import models, serializers, permissions


class ResumeList(generics.ListAPIView):
    queryset = models.Resume.objects.all()
    serializer_class = serializers.ResumeSerializer


class ResumeDetail(generics.RetrieveUpdateAPIView):
    queryset = models.Resume.objects.all()
    serializer_class = serializers.ResumeSerializer
    permission_classes: List[BasePermission] = [permissions.IsOwnerOrReadOnly]
