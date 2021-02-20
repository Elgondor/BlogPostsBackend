from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

class Post(models.Model):
    likes = models.IntegerField()
    popularity = models.FloatField()
    reads = models.IntegerField()
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)


class Author(models.Model):
    author = models.CharField(max_length=100)
