from django.urls import path

from product.views import ProductListAccessPurchase, LessonList, buy_product, ProductStatisticsList

urlpatterns = [
    path('access/purchase/', ProductListAccessPurchase.as_view(), name='products_access_purchase'),
    path('<int:product_id>/lessons', LessonList.as_view(), name='lessons_in_product'),
    path('buy/<int:product_id>/', buy_product, name='buy_product'),
    path('statistics/', ProductStatisticsList.as_view(), name='statistics_products'),
]
