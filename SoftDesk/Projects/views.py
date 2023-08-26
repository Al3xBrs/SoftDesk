from rest_framework.permissions import (
    IsAuthenticated,
)
from Projects.permissions import isAuthor, isContributorAuthenticated
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.decorators import (
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
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ProjectViewset(ReadOnlyModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = (IsAuthenticated,)
    filterset_fields = [
        "type",
        "author",
    ]
    search_fields = [
        "name",
        "description",
    ]
    fields = "__all__"

    def get_queryset(self):
        user = self.request.user
        user_contributions = Contribution.objects.filter(user=user)
        project_ids = [contribution.project.pk for contribution in user_contributions]

        return Project.objects.filter(id__in=project_ids)


class ProjectRegisterView(generics.CreateAPIView):
    queryset = Project.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ProjectSerializer

    def perform_create(self, serializer):
        project = serializer.save(author=self.request.user)
        contribution = Contribution.objects.create(
            user=self.request.user, project=project
        )
        contribution.save()


class ProjectDeleteView(generics.DestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [
        isAuthor,
    ]


class ProjectUpdateView(generics.UpdateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [
        isAuthor,
    ]


class IssueDeleteView(generics.DestroyAPIView):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    permission_classes = [
        isAuthor,
    ]


class IssueUpdateView(generics.UpdateAPIView):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    permission_classes = [
        isAuthor,
    ]


class CommentDeleteView(generics.DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [
        isAuthor,
    ]


class CommentUpdateView(generics.UpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [
        isAuthor,
    ]


class CommentRegisterView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        issue_id = self.kwargs.get("issue_id")
        issue = Issue.objects.get(pk=issue_id)
        serializer.save(
            author=self.request.user,
            issue=issue,
        )


class IssueRegisterView(generics.CreateAPIView):
    queryset = Issue.objects.all()
    permission_classes = (isContributorAuthenticated,)
    serializer_class = IssueSerializer

    def perform_create(self, serializer):
        project_id = self.kwargs.get("project_id")
        project = Project.objects.get(pk=project_id)

        serializer.save(
            author=self.request.user,
            project=project,
        )


class IssueViewset(ReadOnlyModelViewSet):
    serializer_class = IssueSerializer
    permission_classes = (IsAuthenticated,)
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

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["user"] = self.request.user
        return context

    def get_queryset(self):
        user = self.request.user
        user_contributions = Contribution.objects.filter(user=user)
        project_ids = [contribution.project.pk for contribution in user_contributions]

        return Issue.objects.filter(project__id__in=project_ids)


class CommentViewset(ReadOnlyModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticated,)
    filterset_fields = [
        "author",
    ]
    search_fields = [
        "comment",
    ]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["user"] = self.request.user
        return context

    def get_queryset(self):
        user = self.request.user
        user_contributions = Contribution.objects.filter(user=user)
        project_ids = [contribution.project.pk for contribution in user_contributions]

        issue_ids = Issue.objects.filter(project__id__in=project_ids)

        return Comment.objects.filter(issue__id__in=issue_ids)
