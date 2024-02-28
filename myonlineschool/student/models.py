from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class Student(AbstractUser):
    study_group = models.ForeignKey(
        'StudyGroup',
        on_delete=models.CASCADE,
        related_name='students')


class StudyGroup(models.Model):
    product = models.ForeignKey(
        'product.Product',
        on_delete=models.CASCADE,
        related_name='products')
    title = models.CharField(max_length=255)
