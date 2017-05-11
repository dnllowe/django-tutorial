from django.db import models

# Create your models here.
class Question(models.Model):
  question = models.CharField(max_length = 200)
  date_published = models.DateTimeField()