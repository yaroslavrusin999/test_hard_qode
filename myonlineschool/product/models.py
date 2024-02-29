from django.db import models

from .validators import validate_positiv_price


# Create your models here.

class Product(models.Model):
    """Модель для продуктов"""
    author = models.CharField(max_length=50)
    title = models.CharField(max_length=255)
    start_date = models.DateTimeField()
    price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        validators=[validate_positiv_price])
    max_students = models.PositiveSmallIntegerField()
    min_students = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.title


class Lesson(models.Model):
    """
    Модель для уроков, содержит
    связь один ко многим с моделью продуктов
    """
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='lessons')
    title = models.CharField(max_length=255)
    description = models.TextField()
    link_to_video = models.URLField(max_length=200)

    def __str__(self):
        return self.title
