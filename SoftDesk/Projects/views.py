from django.shortcuts import render
from rest_framework.permissions import (
    IsAuthenticated,
    AllowAny,
)
from Projects.permissions import isContributorAuthenticated
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.decorators import (
    api_view,
    permission_classes,
)
from rest_framework_simplejwt.views import generics
from Projects.models import (
    Project,
    Issue,
    Comment,
    Contribution,
)
from Projects.serializers import (
    ProjectSerializer,
    IssueSerializer,
    CommentSerializer,
    ContributionSerializer,
)


class ContributionRegisterView(generics.CreateAPIView):
    queryset = Contribution.objects.all()
    serializer_class = ContributionSerializer
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ProjectViewset(ReadOnlyModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = (isContributorAuthenticated,)
    filterset_fields = [
        "type",
        "author",
    ]
    search_fields = [
        "name",
        "description",
    ]

    def get_queryset(self):
        return Project.objects.all()


class ProjectRegisterView(generics.CreateAPIView):
    queryset = Project.objects.all()
    permission_classes = (isContributorAuthenticated,)
    serializer_class = ProjectSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentRegisterView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    permission_classes = (isContributorAuthenticated,)
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class IssueRegisterView(generics.CreateAPIView):
    queryset = Issue.objects.all()
    permission_classes = (isContributorAuthenticated,)
    serializer_class = IssueSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


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
