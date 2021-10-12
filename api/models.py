import uuid

from django.db import models


class Resume(models.Model):
    class StatusVariants(models.IntegerChoices):
        NOT_LOOKING = 0
        JUST_WATCHING = 1
        LOOKING_FOR_JOB = 2

    class EducationVariants(models.IntegerChoices):
        SECONDARY = 0
        HIGHER = 1

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    status = models.SmallIntegerField(choices=StatusVariants.choices)
    grade = models.PositiveSmallIntegerField()
    specialty = models.CharField(max_length=255)
    salary = models.FloatField()
    education = models.SmallIntegerField(choices=EducationVariants.choices)
    experience = models.TextField()
    portfolio = models.URLField()
    title = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    owner = models.ForeignKey('auth.User', related_name='resume_owner', on_delete=models.CASCADE)
