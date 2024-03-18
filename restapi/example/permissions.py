from rest_framework.permissions import *


class IsAuthorOrReadOnly(BasePermission):

    def has_object_permission(self, request, view, obj):
        return bool(request.method in SAFE_METHODS or
                    obj.author_id == request.user.id or
                    request.user.is_staff or
                    request.user.is_superuser)


class IsAdminOrStaffOrReadOnly(BasePermission):

    def has_permission(self, request, view):
        return bool(request.method in SAFE_METHODS or
                    request.user.is_staff or
                    request.user.is_superuser)

    def has_object_permission(self, request, view, obj):
        return bool(request.method in SAFE_METHODS or
                    obj.author_id == request.user.id or
                    request.user.is_staff or
                    request.user.is_superuser)


class IsUserOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(request.method in SAFE_METHODS or
                    obj.id == request.user.id or
                    request.user.is_staff or
                    request.user.is_superuser)
