from rest_framework import permissions


class ProductAccessPermission(permissions.BasePermission):
    """
    Разрешения для доступа к продуктам,
    к которым у студента есть доступ
    """
    message = 'Access product not allowed'

    def has_permission(self, request, view):
        product_id = (request.user.study_groups.
                      select_related('product').
                      filter(product__id=view.kwargs['product_id']).
                      values_list("product_id", flat=True))
        if product_id:
            return True
        else:
            return False


class ReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return False
