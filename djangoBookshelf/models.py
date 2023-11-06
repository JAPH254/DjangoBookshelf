from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=250, blank=False, null=False)
    author = models.CharField(max_length=250, blank=250, null=False)
    isbn = models.CharField(max_length=250, blank=250, null=False)
    summary = models.CharField(max_length=250, blank=True, null=False)
    genre = models.CharField(max_length=250, blank=False, null=False)
    publish_date = models.DateField()


def __str__(self):
    return self.title
