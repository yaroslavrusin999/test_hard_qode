from rest_framework import permissions


class ProductAccessPermission(permissions.BasePermission):
    """
    Разрешения для доступа к продуктам,
    к которым у студента есть доступ
    """
    message = 'Access product not allowed'

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return False

    def has_object_permission(self, request, view, obj):
        product_id = (request.Student.study_groups.
                      select_related('product').
                      filter(product__id=obj.pk).
                      values_list("product_id", flat=True))
        if product_id:
            return True
        else:
            return False


class ReadOnlyProductPermission(permissions.BasePermission):
    """Разрешение на просмотр доступных для покупки продуктов"""
    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS
