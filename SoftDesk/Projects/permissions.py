from rest_framework.permissions import BasePermission
from Projects.models import Contribution


class isContributorAuthenticated(BasePermission):
    def has_permission(self, request, view):
        user = request.user

        project_id = view.kwargs.get(
            "pk",
        )
        is_permitted = Contribution.objects.filter(
            user=user, project_id=project_id
        ).exists()
        return is_permitted
