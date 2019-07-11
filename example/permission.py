from rest_framework.permissions import BasePermission


class SVIPPermission(BasePermission):
    message = "user_type must be 3"

    def has_permission(self, request, view):
        if request.user.user_type != 3:
            return False
        return True
