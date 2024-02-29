from django.urls import path, include

from product.views import ProductListAccessPurchase, LessonList

urlpatterns = [
    path('access/purchase/', ProductListAccessPurchase.as_view(), name='products_access_purchase'),
    path('<int:product_id>/lessons', LessonList.as_view(), name='lessons_in_product'),

]