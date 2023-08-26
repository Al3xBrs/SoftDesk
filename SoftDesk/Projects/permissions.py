from rest_framework.permissions import (
    BasePermission,
    SAFE_METHODS,
)
from Projects.models import Contribution


class isContributorAuthenticated(BasePermission):
    def has_permission(self, request, view):
        user = request.user

        project_id = view.kwargs.get(
            "project_id",
        )
        is_permitted = Contribution.objects.filter(
            user=user, project_id=project_id
        ).exists()
        return is_permitted


class isAuthor(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True

        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        return obj.author == request.user
