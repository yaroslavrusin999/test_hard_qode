from rest_framework import serializers

from product.models import Product, Lesson


class ProductAccessPurchaseSerializer(serializers.ModelSerializer):
    count_lessons = serializers.IntegerField(read_only=True)

    class Meta:
        model = Product
        fields = ['author', 'title', 'start_date', 'price', 'count_lessons']


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['title', 'description', 'link_to_video']
