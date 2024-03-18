from rest_framework.permissions import *


class IsAuthorOrReadOnly(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return bool(obj.author_id == request.user.id or request.user.is_staff or request.user.is_superuser)


class IsAdminOrStaffOrReadOnly(BasePermission):

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return bool(request.user.is_staff or request.user.is_superuser)

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return bool(request.user.is_staff or request.user.is_superuser)


class IsUserOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return bool(obj.id == request.user.id or request.user.is_staff or request.user.is_superuser)
