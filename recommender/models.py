from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField()
    avg_rating = models.FloatField()
    num_ratings = models.IntegerField()
    url = models.URLField()

class CustomerSatisfaction(models.Model):
    yes_count = models.IntegerField(default=0)
    no_count = models.IntegerField(default=0)

    @classmethod
    def get_instance(cls):
        instance, created = cls.objects.get_or_create(pk=1)
        return instance