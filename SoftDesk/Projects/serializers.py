from Projects.models import (
    Project,
    Issue,
    Comment,
    Contribution,
)
from Users.models import AnyUser
from rest_framework.serializers import (
    ModelSerializer,
    StringRelatedField,
    SlugRelatedField,
    ValidationError,
    SerializerMethodField,
)


class ContributionSerializer(ModelSerializer):
    user = StringRelatedField(
        source="user.name",
    )

    class Meta:
        model = Contribution
        fields = "__all__"
        read_only_fields = ("user",)


class ProjectSerializer(ModelSerializer):
    author = StringRelatedField(
        source="author.username",
    )

    class Meta:
        model = Project
        fields = "__all__"
        read_only_fields = (
            "author",
            "date_created",
            "date_updated",
        )


class IssueSerializer(ModelSerializer):
    author = StringRelatedField(
        source="author.username",
    )
    # project = SerializerMethodField()

    class Meta:
        model = Issue
        fields = "__all__"
        read_only_fields = (
            "author",
            "date_created",
        )

    # def get_project(self, instance):
    #     project = instance.project
    #     if project:
    #         return project.name
    #     return None

    def get_fields(self):
        fields = super().get_fields()
        contributions = Contribution.objects.filter(user=self.context["user"])
        users_contributors = [contribution.user for contribution in contributions]
        project_ids = [contribution.project.id for contribution in contributions]
        fields["project"].queryset = Project.objects.filter(id__in=project_ids)
        fields["affected_to"].queryset = users_contributors
        return fields


class CommentSerializer(ModelSerializer):
    author = StringRelatedField(
        source="author.username",
    )
    issue = SerializerMethodField()

    class Meta:
        model = Comment
        fields = "__all__"
        read_only_fields = (
            "author",
            "date_created",
        )

    def get_fields(self):
        fields = super().get_fields()
        contributions = Contribution.objects.filter(user=self.context["user"])
        project_ids = [contribution.project.id for contribution in contributions]
        fields["issue"].queryset = Issue.objects.filter(project__id__in=project_ids)
        return fields

    def get_issue(self, instance):
        issue = instance.issue
        if issue:
            return issue.name
        return None


class UserSerializer(ModelSerializer):
    projects_contribution = ContributionSerializer(
        many=True,
        source="contribution_set",
        read_only=True,
    )

    class Meta:
        model = AnyUser
        fields = [
            "username",
            "email",
            "date_of_birth",
        ]
