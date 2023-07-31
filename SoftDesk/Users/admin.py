from django.contrib import admin
from Users.models import AnyUser, Contributor
from Projects.models import Project, Issue, Comment

admin.site.register(AnyUser)
admin.site.register(Project)
admin.site.register(Issue)
admin.site.register(Comment)
admin.site.register(Contributor)
