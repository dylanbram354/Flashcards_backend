from django.db import models


# Create your models here.

class Collection(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=150)


class Flashcard(models.Model):
    word = models.CharField(max_length=100)
    definition = models.CharField(max_length=500)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
