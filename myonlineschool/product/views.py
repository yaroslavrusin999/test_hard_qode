from rest_framework import generics
from django.db.models import Subquery, Count

from product.permissions import ReadOnlyProductPermission
from product.models import Product


# Create your views here.


class ProductListAccessPurchase(generics.ListAPIView):
    permission_classes = [ReadOnlyProductPermission]

    def get_queryset(self):
        subquery = Subquery(self.request.
                            Student.study_groups.
                            select_related('product').
                            values_list("product_id", flat=True))
        products = (Product.objects.
                    exclude(id__in=subquery).
                    prefetch_related('lessons').
                    annotate(count_lessons=Count('lesson_id')))
