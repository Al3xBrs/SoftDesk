from rest_framework.permissions import BasePermission
from Projects.models import Contribution


class isContributorAuthenticated(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        print(request.data)
        # TODO:
        project = request.META["project_id"]
        is_permitted = Contribution.objects.filter(user=user).exists()
        return is_permitted
