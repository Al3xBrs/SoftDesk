from Users.models import Contributor, AnyUser
from Projects.models import Project, Issue, Comment

from rest_framework import serializers


class ProjectSerializer(serializers):
    class Meta:
        model = Project
        fields = ["name", "date_created", "date_upated"]


class IssueSerializer(serializers):
    class Meta:
        model = Issue
        fields = ["name"]


class CommentSerializer(serializers):
    class Meta:
        model = Comment
        fields = ["name"]


class ContributorSerializer(serializers):
    class Meta:
        model = Contributor
        fields = ["username"]


class UserSerializer(serializers):
    class Meta:
        model = AnyUser
        fields = ["username", "email", "age"]
