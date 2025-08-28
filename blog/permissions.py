from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsAdminOrReadOnly(BasePermission):
    """
    - Read-only for everyone.
    - Only Admins can perform create, update and delete.
    """

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user and request.user.is_staff


class IsOwnerOrAdminDeleteOnly(BasePermission):
    """
    - Read-only for everyone.
    - Owner can perform update/delete.
    - Admins can only perform delete.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        if request.method == "DELETE":
            return obj.user == request.user or request.user.is_staff

        return obj.user == request.user


class IsOwnerOrReadOnly(BasePermission):
    """
    Allow only owner to perform create, update and delete an
    object.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.user == request.user
