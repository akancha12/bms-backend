from rest_framework import permissions
# from rest_framework.permissions import SAFE_METHODS
from django.contrib.auth import get_user_model

User = get_user_model()


class IsAdminOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        user = User.objects.filter(pk=request.user.id, is_staff=True)
        if user:
            return True
        return False
