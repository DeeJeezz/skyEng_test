from typing import List

from django.urls import path

from api import views

urlpatterns: List[path] = [
    path('resume/', views.ResumeList.as_view(), name='resume_list'),
    path('resume/<uuid:pk>/', views.ResumeDetail.as_view(), name='resume_update'),
]
