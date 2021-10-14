import uuid

from django.db import models


class Resume(models.Model):
    class StatusVariants(models.TextChoices):
        NOT_LOOKING = 'Not looking for a job'
        JUST_WATCHING = 'Just watching'
        LOOKING_FOR_JOB = 'Looking for a job'

    class EducationVariants(models.TextChoices):
        SECONDARY = 'Secondary'
        HIGHER = 'Higher'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    status = models.CharField(max_length=100, choices=StatusVariants.choices)
    grade = models.PositiveSmallIntegerField()
    specialty = models.CharField(max_length=255)
    salary = models.FloatField()
    education = models.CharField(max_length=25, choices=EducationVariants.choices)
    experience = models.TextField()
    portfolio = models.URLField()
    title = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    owner = models.ForeignKey('auth.User', related_name='resume_owner', on_delete=models.CASCADE)
