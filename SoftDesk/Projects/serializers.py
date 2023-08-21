from Projects.models import Project, Issue, Comment, Contribution
from Users.models import AnyUser
from rest_framework.serializers import ModelSerializer, StringRelatedField, ChoiceField


class ContributionSerializer(ModelSerializer):
    class Meta:
        model = Contribution
        fields = [
            "user",
            "project",
        ]


class ProjectSerializer(ModelSerializer):
    author = StringRelatedField(
        source="author.username",
    )
    contributions = ContributionSerializer(many=True, read_only=True)

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
    status = ChoiceField(
        choices=Issue.status_choices,
        source="get_status_display",
    )
    priority = ChoiceField(
        choices=Issue.priority_choices,
        source="get_priority_display",
    )
    tag = ChoiceField(
        choices=Issue.tag_choices,
        source="get_tag_display",
    )

    class Meta:
        model = Issue
        fields = "__all__"
        read_only_fields = (
            "author",
            "date_created",
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
