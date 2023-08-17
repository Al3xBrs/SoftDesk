from django.shortcuts import render
from Projects.permissions import isContributorAuthenticated
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from Projects.models import Project, Issue, Comment
from Projects.serializers import (
    ProjectSerializer,
    IssueSerializer,
    CommentSerializer,
)


class ProjectViewset(ReadOnlyModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = (isContributorAuthenticated,)
    filterset_fields = [
        "type",
        "author",
        "contributors",
    ]
    search_fields = [
        "name",
        "description",
    ]

    def get_queryset(self):
        return Project.objects.all()


class IssueViewset(ReadOnlyModelViewSet):
    serializer_class = IssueSerializer
    permission_classes = (isContributorAuthenticated,)
    filterset_fields = [
        "author",
        "affected_to",
        "status",
        "priority",
        "tag",
    ]
    search_fields = [
        "name",
        "description",
    ]

    def get_queryset(self):
        return Issue.objects.all()


class CommentViewset(ReadOnlyModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (isContributorAuthenticated,)
    filterset_fields = [
        "author",
    ]
    search_fields = [
        "comment",
    ]

    def get_queryset(self):
        return Comment.objects.all()
