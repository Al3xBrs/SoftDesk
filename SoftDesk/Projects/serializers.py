from Users.models import Contributor, AnyUser
from Projects.models import Project, Issue, Comment

from rest_framework.serializers import ModelSerializer


class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = [
            "name",
            "date_created",
            "description",
            "type",
            "author",
            "contributors",
        ]


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


class ContributorSerializer(ModelSerializer):
    class Meta:
        model = Contributor
        fields = [
            "username",
            "email",
        ]


class UserSerializer(ModelSerializer):
    class Meta:
        model = AnyUser
        fields = [
            "username",
            "email",
            "date_of_birth",
        ]
