from rest_framework import permissions

class IsAdmin(permissions.BasePermission):
    """
    Permite el acceso solo a administradores.
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_staff

class IsUser(permissions.BasePermission):
    """
    Permite el acceso solo a usuarios normales.
    """
    def has_permission(self, request, view):
        return request.user and not request.user.is_staff