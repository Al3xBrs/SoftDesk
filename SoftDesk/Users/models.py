from django.db import models

class Contributor(models.Model):

    name = models.CharField(max_length=20)