from django.contrib import admin
from Users.models import AnyUser
from Projects.models import Project, Issue, Comment, Contribution

admin.site.register(AnyUser)
admin.site.register(Project)
admin.site.register(Issue)
admin.site.register(Comment)
admin.site.register(Contribution)
