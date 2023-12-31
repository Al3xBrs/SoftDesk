from django.db import models
from Users.models import AnyUser

from uuid import uuid4


class Project(models.Model):
    name = models.CharField(
        max_length=50,
    )
    description = models.CharField(
        max_length=1200,
        blank=True,
        null=True,
    )
    type_choices = [
        ("BE", "Back-end"),
        ("FE", "Front-end"),
        ("IO", "IOS"),
        ("AN", "Android"),
    ]
    type = models.CharField(
        max_length=2,
        choices=type_choices,
    )
    author = models.ForeignKey(
        AnyUser,
        related_name="project_author",
        on_delete=models.CASCADE,
    )

    date_created = models.DateTimeField(
        auto_now_add=True,
    )
    date_updated = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return self.name


class Contribution(models.Model):
    user = models.OneToOneField(
        AnyUser,
        on_delete=models.CASCADE,
        related_name="contributor",
    )
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="project",
    )

    def __str__(self):
        return f"{self.user.username}"


class Issue(models.Model):
    """
    Project's issue. Can be a Bug, Task or Improvement.
    Status code :   OUVERT = open (issue created but no contributor affected)
                    EN_COURS = in progress (issue created AND contributor works on)
                    FERMÉ = closed (issue closed by the owner)

    """

    name = models.CharField(
        max_length=50,
    )

    author = models.ForeignKey(
        AnyUser,
        on_delete=models.CASCADE,
        related_name="issue_author",
    )

    affected_to = models.ForeignKey(
        Contribution,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="affected_AnyUser",
    )
    status_choices = [
        ("OP", "Open"),
        ("IP", "In Progress"),
        ("CL", "Closed"),
    ]
    status = models.CharField(
        max_length=2,
        choices=status_choices,
    )
    priority_choices = [
        ("HI", "High"),
        ("ME", "Medium"),
        ("LO", "Low"),
    ]
    priority = models.CharField(
        max_length=2,
        choices=priority_choices,
    )
    tag_choices = [
        ("BU", "Bug"),
        ("TA", "Task"),
        ("IM", "Improvement"),
    ]
    tag = models.CharField(
        max_length=2,
        choices=tag_choices,
    )

    description = models.CharField(
        max_length=1200,
        blank=True,
    )

    date_created = models.DateTimeField(
        auto_now_add=True,
    )

    project = models.ForeignKey(
        to=Project,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="project_issue",
    )

    def __str__(self):
        return f"Projet : {self.project.name} - Issue : {self.name}"


class Comment(models.Model):
    """
    Comment on the project's issue.
    Contributor automaticly add at the creation.
    """

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    comment = models.CharField(
        max_length=1000,
    )

    date_created = models.DateTimeField(
        auto_now_add=True,
    )
    author = models.ForeignKey(
        AnyUser,
        on_delete=models.CASCADE,
        related_name="comment_author",
    )

    issue = models.ForeignKey(
        to=Issue,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"Issue : {self.issue.name}"
