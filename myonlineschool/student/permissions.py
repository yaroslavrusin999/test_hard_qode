from rest_framework import permissions


class ProductAccessPermission(permissions.BasePermission):
    message = 'Access product not allowed'

    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS

    def has_object_permission(self, request, view, obj):
        return request.Student.study_group.product.pk == obj.pk
