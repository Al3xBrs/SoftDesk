from django.test import TestCase
from django.urls import reverse_lazy


from rest_framework.test import APITestCase
from Projects.models import Project, Issue, Comment
from Users.models import AnyUser


class TestProject(APITestCase):
    url = reverse_lazy("project-list")

    def format_datetime(self, value):
        return value.strftime("%Y-%m-%dT%H:%M:%S.%fZ")

    def create_user(self):
        AnyUser.objects.create(
            email="test@test.fr",
            username="test",
            date_of_birth="2000-12-12",
            is_contributor=True,
            can_be_contacted=True,
            can_data_be_shared=True,
        )
        return AnyUser.objects.get(email="test@test.fr")

    def test_list(self):
        project = Project.objects.create(
            name="Project1",
            type="BE",
            author=self.create_user(),
        )
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

        expected = [
            {
                "id": project.id,
                "name": project.name,
                "date_created": self.format_datetime(project.date_created),
                "description": project.description,
                "type": project.type,
                "author": str(project.author.id),
                "contributors": [
                    str(contributor.id)
                    for contributor in project.contributors.all()
                ],
                "date_updated": self.format_datetime(project.date_updated),
            }
        ]

        self.assertEqual(response.json(), expected)
