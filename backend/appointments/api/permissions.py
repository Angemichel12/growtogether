from rest_framework.permissions import BasePermission


class IsPatient(BasePermission):
    """custom Permission class for Patient"""

    def has_permission(self, request, view):
        return bool(request.user and request.user.get(user_type='W').exists())
