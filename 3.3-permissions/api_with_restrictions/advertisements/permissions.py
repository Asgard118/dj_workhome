from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Пользователь может редактировать или удалять свои объявления,
    но не может редактировать или удалять объявления других пользователей.
    """

    def has_object_permission(self, request, obj):
        # Разрешено для чтения всем
        if request.method in permissions.SAFE_METHODS:
            return True

        # Разрешено только для владельца объявления
        return obj.creator == request.user
