from django.db import models

# Create your models here.
class IOT(models.Model):
    light = models.BooleanField(default=False)
    fan = models.BooleanField(default=False)
    tv = models.BooleanField(default=False)
    others = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField()

    def __str__(self):
        return str(self.modified)