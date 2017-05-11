from django.db import models

# Create your models here.

# Questions for Poll
class Question(models.Model):
  text = models.CharField(max_length = 200)
  date_published = models.DateTimeField()

# Choices for Poll
class Choice(models.Model):
  question = models.ForeignKey(Question, on_delete=models.CASCADE)
  text = models.CharField(max_length = 200)
  votes = models.IntegerField(default = 0)