from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1024)
    