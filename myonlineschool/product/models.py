from django.db import models

from .validators import validate_positiv_price


# Create your models here.

class Product(models.Model):
    author = models.CharField(max_length=50)
    title = models.CharField(max_length=255)
    start_date = models.DateTimeField()
    price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        validators=[validate_positiv_price])
    max_students = models.PositiveSmallIntegerField()
    min_students = models.PositiveSmallIntegerField()

    class Meta:
        permissions = [
            (
                'product_access',
                'Имеет ли студент доступ к продукту'
            )
        ]


class Lesson(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='lessons')
    title = models.CharField(max_length=255)
    description = models.TextField()
    link_to_video = models.URLField(max_length=200)