from rest_framework import serializers

from product.models import Product


class ProductAccessPurchase(serializers.ModelSerializer):
    count_lessons = serializers.IntegerField(read_only=True)

    class Meta:
        model = Product
        fields = ['author', 'title', 'start_date', 'price']
