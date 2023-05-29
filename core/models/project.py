from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    github_url = models.URLField()
    technologies = models.CharField(max_length=255)
    rating = models.IntegerField(default=0)
