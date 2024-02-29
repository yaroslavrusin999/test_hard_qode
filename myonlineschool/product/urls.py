from django.urls import path, include

from product.views import ProductListAccessPurchase, LessonList, buy_product

urlpatterns = [
    path('access/purchase/', ProductListAccessPurchase.as_view(), name='products_access_purchase'),
    path('<int:product_id>/lessons', LessonList.as_view(), name='lessons_in_product'),
    path('buy/<int:product_id>/', buy_product, name='buy_product'),

]