from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet
from Projects.models import Project, Issue, Comment
from Projects.serializers import (
    ProjectSerializer,
    IssueSerializer,
    CommentSerializer,
)


class ProjectViewset(ReadOnlyModelViewSet):
    serializer_class = ProjectSerializer

    def get_queryset(self):
        return Project.objects.all()


class IssueViewset(ReadOnlyModelViewSet):
    serializer_class = IssueSerializer

    def get_queryset(self):
        return Issue.objects.all()


class CommentViewset(ReadOnlyModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.all()
