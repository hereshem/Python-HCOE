from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    author = models.CharField(max_length=200)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    def __str__(self):
        return self.title + " ("+ self.author + ")"