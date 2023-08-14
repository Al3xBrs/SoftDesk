from rest_framework.permissions import BasePermission


class isContributorAuthenticated(BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.user
            and request.user.is_authenticated
            and request.user.is_contributor
        )
