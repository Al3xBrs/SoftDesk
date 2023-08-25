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

    class Meta:
        model = Issue
        fields = "__all__"
        read_only_fields = (
            "author",
            "date_created",
            "project",
        )


class CommentSerializer(ModelSerializer):
    author = StringRelatedField(
        source="author.username",
    )

    class Meta:
        model = Comment
        fields = "__all__"
        read_only_fields = (
            "author",
            "date_created",
            "issue",
        )


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
