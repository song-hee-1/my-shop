from rest_framework import permissions

from accounts.models import User


class IsNotAuthenticated(permissions.BasePermission):
    def has_permission(self, request, view):
        user: User = request.user
        if user is None or user.is_anonymous:
            return True
        return False
