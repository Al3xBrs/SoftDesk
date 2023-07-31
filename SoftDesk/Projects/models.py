from django.db import models
from Users.models import Contributor


class Comment(models.Model):
    comment = models.CharField(max_length=1000)


class Issue(models.Model):
    name = models.CharField(max_length=50)
    comments = models.ForeignKey(Comment, on_delete=models.CASCADE)


class Project(models.Model):
    name = models.CharField(max_length=50)
    contributors = models.ManyToManyField(
        Contributor, related_name="contributor_projects", symmetrical=False
    )
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
