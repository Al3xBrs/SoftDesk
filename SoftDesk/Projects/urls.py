from rest_framework import routers
from Projects.views import ProjectViewset, IssueViewset, CommentViewset

router = routers.DefaultRouter()
router.register("project", ProjectViewset, basename="project")
router.register("issue", IssueViewset, basename="issue")
router.register("comment", CommentViewset, basename="comment")
