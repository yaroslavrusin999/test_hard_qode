from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class Student(AbstractUser):
    """Переопределенная модель пользователя"""
    pass


class StudyGroup(models.Model):
    """Модель для учебной группы"""
    product = models.ForeignKey(
        'product.Product',
        on_delete=models.CASCADE,
        related_name='products')
    students = models.ManyToManyField('Student', related_name='study_groups')
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title
