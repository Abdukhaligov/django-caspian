from django.db import models


class News(models.Model):
    title = models.CharField(max_length=128)
    body = models.TextField()

    def __str__(self):
        return self.title


class Partner(models.Model):
    name = models.CharField(max_length=128)
    link = models.CharField(max_length=512, blank=True, null=True)
    vip = models.BooleanField(default=False)

    def __str__(self):
        return self.name

