from rest_framework import permissions
from .models import *


class IsAdministratorOrSUPEROrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        return bool(request.user and (hasattr(request.user, 'administrator') or request.user.is_superuser))


class IsSupervisorOrSUPEROrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        return bool(request.user and (hasattr(request.user, 'supervisor') or request.user.is_superuser))

class IsAdministratorOrSUPEROrClosed(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and (hasattr(request.user, 'administrator') or request.user.is_superuser))