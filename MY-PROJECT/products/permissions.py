from rest_framework.permissions import BasePermission

class IsAdminUser(BasePermission):
    """
    Custom permission to only allow admin users to manage products.
    """
    def has_permission(self, request, view):
        # Check if the user is authenticated and has the is_admin flag
        return request.user.is_authenticated and request.user.is_admin