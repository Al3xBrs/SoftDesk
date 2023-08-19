from Users.models import AnyUser
from Projects.models import Project, Issue, Comment, Contribution

from rest_framework.serializers import ModelSerializer


class ContributionSerializer(ModelSerializer):
    class Meta:
        model = Contribution
        fields = [
            "username",
            "email",
        ]


class ProjectSerializer(ModelSerializer):
    contributions = ContributionSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = [
            "name",
            "date_created",
            "description",
            "type",
            "contributions",
        ]

    def create(self, validated_data):
        project = Project.objects.create(
            name=validated_data["name"],
            description=validated_data["description"],
            type=validated_data["type"],
            author=self.context["request"].user,
        )
        project.save()
        return project


class IssueSerializer(ModelSerializer):
    class Meta:
        model = Issue
        fields = [
            "name",
            "author",
            "affected_to",
            "status",
            "priority",
            "tag",
            "description",
            "date_created",
        ]


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            "comment",
            "author",
            "date_created",
        ]


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
