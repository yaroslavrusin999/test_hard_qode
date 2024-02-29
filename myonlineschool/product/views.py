from django.db.models import Subquery, Count, Avg, Max
from django.http import JsonResponse
from rest_framework import generics

from product.models import Product, Lesson
from product.permissions import ReadOnly, ProductAccessPermission
from product.serializers import ProductAccessPurchaseSerializer, LessonSerializer, ProductStatisticsSerializer
from product.service import distribute_to_study_group
from student.models import Student


# Create your views here.


class ProductListAccessPurchase(generics.ListAPIView):
    """
    Класс представления для отображения
    списка продуктов, доступных для покупки
    """
    permission_classes = [ReadOnly]
    serializer_class = ProductAccessPurchaseSerializer

    def get_queryset(self):
        subquery = Subquery(self.request.
                            user.study_groups.
                            select_related('product').
                            values_list("product_id", flat=True))
        products = (Product.objects.
                    exclude(id__in=subquery).
                    prefetch_related('lessons').
                    annotate(count_lessons=Count('lessons')))
        return products


class LessonList(generics.ListAPIView):
    """
    Класс представления для отображения списка
    уроков у конкретного продукта
    """
    permission_classes = [ReadOnly, ProductAccessPermission]
    serializer_class = LessonSerializer

    def get_queryset(self):
        lessons = (Lesson.objects.
                   select_related('product').
                   filter(product__id=self.kwargs['product_id']))
        return lessons


def buy_product(request, product_id):
    """Функция бля обработке получения доступа к продукту"""
    if request.method == 'GET':
        st = request.user
        pr = Product.objects.get(id=product_id)
        is_successful = distribute_to_study_group(st, pr)
        return JsonResponse({'is_successful': is_successful})


class ProductStatisticsList(generics.ListAPIView):
    """
    Класс представления для отображения
    статистики по продуктам
    """
    permission_classes = [ReadOnly]
    serializer_class = ProductStatisticsSerializer

    def get_queryset(self):
        count_all_students = Student.objects.all().count()
        products = (Product.objects.
                    prefetch_related('study_groups').
                    prefetch_related('study_groups__students').
                    annotate(count_students=Count('study_groups__students')))
        for pr in products:
            pr.product_purchase = (pr.count_students / count_all_students) * 100
            avg_count_students = pr.count_students / len(pr.study_groups.all())
            max_count_students = max([len(sg.students.all()) for sg in pr.study_groups.all()])
            pr.fullness_study_groups = (avg_count_students / max_count_students) * 100
        return products
