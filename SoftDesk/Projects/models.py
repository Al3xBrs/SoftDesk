from django.db import models
from Users.models import Contributor

class Issue(models.Model):
    
    name = models.CharField(max_length=50)

class Project(models.Model):

    name = models.CharField(max_length=50)
    contributors = models.ForeignKey(Contributor, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

