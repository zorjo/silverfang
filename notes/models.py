from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.search import SearchVectorField
# Create your models here.
class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title =models.CharField(max_length=100)
    content=models.TextField()
    search_vector = SearchVectorField(null=True, blank=True)
