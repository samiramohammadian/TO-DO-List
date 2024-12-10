from django.db import models
from django.db import models
from django.utils.timezone import now

class Task(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=now)

    def __str__(self):
        return self.title

# class Task(models.Model):
    # title = models.CharField(max_length=200)
    # completed = models.BooleanField(default=False)

    # def __str__(self):
    #     return self.title
